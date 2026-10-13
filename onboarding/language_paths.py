#!/usr/bin/env python3
"""Rename creator-facing folders into the language of memory/config.md, then check.

`apply` renames and rewrites path references.
`check` fails while a markdown file still points at an old path.
The script does not translate prose. It does not set files_language.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# template path, English path, Portuguese path. Longer paths stay above their parents.
ROWS: list[tuple[str, str, str]] = [
    ("conteudo/ideias", "content/ideas", "conteudo/ideias"),
    ("conteudo/roteiros", "content/scripts", "conteudo/roteiros"),
    ("conteudo/carrosseis", "content/carousels", "conteudo/carrosseis"),
    ("conteudo/legendas", "content/captions", "conteudo/legendas"),
    ("referencia/pesquisas", "reference/research", "referencia/pesquisas"),
    ("referencia/perfil-atual", "reference/current-profile", "referencia/perfil-atual"),
    ("onboarding/interview.md", "onboarding/interview.md", "onboarding/entrevista.md"),
    ("estrategia", "strategy", "estrategia"),
    ("conteudo", "content", "conteudo"),
    ("referencia", "reference", "referencia"),
    ("gravações", "recordings", "gravações"),
    ("memory", "memory", "memoria"),
    ("freebies", "freebies", "iscas"),
]

SKIP_DIRS = {
    ".git",
    "venv",
    ".venv",
    "node_modules",
    "site-packages",
    "__pycache__",
    "gravações",
    "recordings",
    # Third-party clones. Rewriting them dirties an upstream repo.
    "Pytho-inator",
    "pytho-inator",
    "last30days-skill",
    "fontastic-text-image-generator",
}
SKIP_FILES = {"language_paths.py", "test_language_paths.py"}
TEXT_SUFFIXES = {
    ".md", ".py", ".sh", ".json", ".txt", ".toml", ".yml", ".yaml",
    ".html", ".css", ".js", ".ts", ".csv",
}


def normalize(name: str) -> str:
    folded = name.strip().lower().replace("ê", "e").replace("ú", "u").replace("á", "a")
    if folded in {"en", "english", "ingles"} or folded.startswith("english"):
        return "english"
    if folded.startswith("portug") or folded in {"pt", "pt-br", "ptbr"}:
        return "portuguese"
    return ""


def read_config_language(root: Path) -> str:
    for rel in ("memory/config.md", "memoria/config.md"):
        path = root / rel
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("content_language:"):
                return line.split(":", 1)[1].strip()
    return ""


def target_of(row: tuple[str, str, str], language: str) -> str:
    return row[1] if language == "english" else row[2]


def stale_names(language: str) -> list[str]:
    names: list[str] = []
    for row in ROWS:
        target = target_of(row, language)
        for name in row:
            if name != target and name not in names:
                names.append(name)
    names.sort(key=len, reverse=True)
    return names


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        if path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def replace_paths(text: str, language: str) -> str:
    for name in stale_names(language):
        target = ""
        for row in ROWS:
            if name in row:
                target = target_of(row, language)
                break
        if not target or target == name:
            continue
        text = text.replace(f"`{name}`", f"`{target}`")
        text = text.replace(f"{name}/", f"{target}/")
        if name.endswith(".md"):
            text = text.replace(name, target)
    return text


def apply_tree(root: Path, language: str) -> None:
    for name in stale_names(language):
        target = ""
        for row in ROWS:
            if name in row:
                target = target_of(row, language)
                break
        source = root / name
        dest = root / target
        if not source.exists():
            continue
        if dest.exists():
            raise SystemExit(f"both exist, not merging: {name} -> {target}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        source.rename(dest)
    for path in iter_text_files(root):
        original = path.read_text(encoding="utf-8", errors="ignore")
        updated = replace_paths(original, language)
        if updated != original:
            path.write_text(updated, encoding="utf-8")


def check_tree(root: Path, language: str) -> list[str]:
    hits: list[str] = []
    stale = [name for name in stale_names(language)]
    for path in iter_text_files(root):
        if path.suffix.lower() != ".md" and path.name != ".gitignore":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(root).as_posix()
        for name in stale:
            if f"{name}/" in text or f"`{name}`" in text or (name.endswith(".md") and name in text):
                hits.append(f"{rel}: still points at {name}")
    return hits


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("apply", "check"))
    parser.add_argument("--root", default=".", type=Path)
    parser.add_argument("--language", default="")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    raw = args.language or read_config_language(root)
    language = normalize(raw)
    if not language:
        print("language must be English or Portuguese for this command", file=sys.stderr)
        return 2
    if args.action == "apply":
        apply_tree(root, language)
        print("applied")
        return 0
    hits = check_tree(root, language)
    if hits:
        print(f"{len(hits)} hits")
        print("\n".join(hits))
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
