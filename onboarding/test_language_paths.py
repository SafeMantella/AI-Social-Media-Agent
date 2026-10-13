#!/usr/bin/env python3
"""A mini tree renames cleanly, and a leftover old path still fails the check."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TOOL = ROOT / "language_paths.py"


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(TOOL), *args], text=True, capture_output=True)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        en = base / "en"
        write(en / "estrategia" / "01.md", "See `conteudo/ideias` and conteudo/roteiros/a.md\n")
        write(en / "memory" / "config.md", "content_language: English\nfiles_language:\n")
        write(en / "freebies" / "README.md", "ok\n")
        write(en / "gravações" / "README.md", "raw\n")
        write(en / "note.md", "Open referencia/perfil-atual/RESUMO.md\n")

        applied = run(["apply", "--root", str(en)])
        if applied.returncode != 0:
            print(applied.stderr)
            print("FAIL: english apply")
            return 1
        if not (en / "strategy" / "01.md").is_file():
            print("FAIL: strategy folder missing")
            return 1
        if (en / "estrategia").exists():
            print("FAIL: estrategia still exists")
            return 1
        body = (en / "strategy" / "01.md").read_text(encoding="utf-8")
        if "content/ideas" not in body or "content/scripts/a.md" not in body:
            print("FAIL: references were not rewritten")
            print(body)
            return 1
        note = (en / "note.md").read_text(encoding="utf-8")
        if "reference/current-profile/RESUMO.md" not in note:
            print("FAIL: profile path")
            print(note)
            return 1
        checked = run(["check", "--root", str(en), "--language", "English"])
        if checked.returncode != 0 or "ok" not in checked.stdout:
            print(checked.stdout)
            print("FAIL: english check")
            return 1
        again = run(["apply", "--root", str(en), "--language", "English"])
        if again.returncode != 0:
            print("FAIL: second apply")
            return 1

        dirty = base / "dirty"
        write(dirty / "note.md", "still estrategia/01.md\n")
        dirty_check = run(["check", "--root", str(dirty), "--language", "English"])
        if dirty_check.returncode == 0:
            print("FAIL: leftover path was accepted")
            return 1

        pt = base / "pt"
        write(pt / "memory" / "config.md", "content_language: Português\n")
        write(pt / "freebies" / "README.md", "see memory/config.md\n")
        write(pt / "onboarding" / "interview.md", "question\n")
        pt_apply = run(["apply", "--root", str(pt), "--language", "Português"])
        if pt_apply.returncode != 0:
            print(pt_apply.stderr)
            print("FAIL: portuguese apply")
            return 1
        if not (pt / "memoria" / "config.md").is_file() or not (pt / "iscas" / "README.md").is_file():
            print("FAIL: portuguese folders")
            return 1
        if not (pt / "onboarding" / "entrevista.md").is_file():
            print("FAIL: interview was not renamed")
            return 1
        iscas = (pt / "iscas" / "README.md").read_text(encoding="utf-8")
        if "memoria/config.md" not in iscas:
            print("FAIL: memory reference")
            print(iscas)
            return 1
        pt_check = run(["check", "--root", str(pt), "--language", "Português"])
        if pt_check.returncode != 0:
            print(pt_check.stdout)
            print("FAIL: portuguese check")
            return 1

    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
