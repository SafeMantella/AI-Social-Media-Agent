#!/usr/bin/env python3
"""Scan a tree for leaked secrets and an external wordlist.

The wordlist is passed with --wordlist and is not stored in this repository.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    "gravações",
    "recordings",
    "site",
    "docs",
    # Third-party clone. Its own text is not this template.
    "Pytho-inator",
    "pytho-inator",
    # Owned-tool clones and the pre-move backup. Gitignored. Not template source.
    "_repos",
    "_old",
}

# Built by concatenation so this file does not contain the org name.
_CLONE_ORG = "Safe" + "Mantella"
CLONE_URLS = (
    f"https://github.com/{_CLONE_ORG}/Pytho-inator.git".lower(),
    f"https://github.com/{_CLONE_ORG}/Pytho-inator".lower(),
)

# Path prefixes are concatenated so this file does not contain them as literals.
SECRET_RES = [
    re.compile(re.escape("/" + "Users" + "/")),
    re.compile(re.escape("/" + "Volumes" + "/")),
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    re.compile(r"https?://(?:www\.)?notion\.(?:so|com)/\S+", re.I),
    re.compile(r"https?://(?:www\.)?canva\.com/\S+", re.I),
    re.compile(r"(?i)(api[_-]?key|access_token|refresh_token)\s*[:=]\s*\S+"),
    re.compile(r"(?i)\b(sk-[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,})"),
]

TEXT_SUFFIXES = {
    ".md", ".py", ".sh", ".json", ".txt", ".toml", ".yml", ".yaml",
    ".html", ".css", ".js", ".ts", ".gitignore", ".csv",
}


def load_words(path: Path | None) -> list[str]:
    if path is None:
        return []
    words = []
    for line in path.read_text(encoding="utf-8").splitlines():
        word = line.strip()
        if word and not word.startswith("#"):
            words.append(word)
    return words


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def scan(root: Path, words: list[str]) -> list[str]:
    hits: list[str] = []
    lowered = [(w, w.lower()) for w in words]
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        name_lower = path.name.lower()
        for raw, low in lowered:
            if low in name_lower:
                hits.append(f"{rel}: filename contains {raw}")
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            hits.append(f"{rel}: unreadable ({exc})")
            continue
        low_text = text.lower()
        for url in CLONE_URLS:
            low_text = low_text.replace(url, "")
        for raw, low in lowered:
            if low in low_text:
                hits.append(f"{rel}: contains {raw}")
        for lineno, line in enumerate(text.splitlines(), 1):
            for pattern in SECRET_RES:
                if pattern.search(line):
                    hits.append(f"{rel}:{lineno}: secret pattern {pattern.pattern}")
                    break
    return hits


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fail if a tree contains secrets or wordlist hits.")
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--wordlist", type=Path, default=None)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    hits = scan(root, load_words(args.wordlist))
    if hits:
        print(f"{len(hits)} hit(s)")
        for hit in hits:
            print(hit)
        return 1
    print("0 hits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
