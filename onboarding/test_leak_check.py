#!/usr/bin/env python3
"""Plant a name and a home path. The checker must fail, then pass a clean dir."""

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECK = ROOT / "leak_check.py"


def run(folder: Path, wordlist: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECK), str(folder), "--wordlist", str(wordlist)],
        text=True,
        capture_output=True,
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        words = base / "words.txt"
        words.write_text("ExampleName\n", encoding="utf-8")

        dirty = base / "dirty"
        dirty.mkdir()
        (dirty / "note.md").write_text("hello ExampleName\n", encoding="utf-8")
        planted = run(dirty, words)
        if planted.returncode == 0:
            print(planted.stdout)
            print("FAIL: planted name was not caught")
            return 1

        secret = base / "secret"
        secret.mkdir()
        planted_home = "/" + "Users" + "/someone/file\n"
        (secret / "note.md").write_text("see " + planted_home, encoding="utf-8")
        secret_run = run(secret, words)
        if secret_run.returncode == 0:
            print(secret_run.stdout)
            print("FAIL: home path was not caught")
            return 1

        clean = base / "clean"
        clean.mkdir()
        (clean / "note.md").write_text("a generic note\n", encoding="utf-8")
        clean_run = run(clean, words)
        if clean_run.returncode != 0:
            print(clean_run.stdout)
            print(clean_run.stderr)
            print("FAIL: clean dir was flagged")
            return 1

        org = "Safe" + "Mantella"
        url_words = base / "url-words.txt"
        url_words.write_text(org + "\n", encoding="utf-8")
        allowed = base / "allowed"
        allowed.mkdir()
        (allowed / "note.md").write_text(
            "git clone https://github.com/" + org + "/Pytho-inator.git\n",
            encoding="utf-8",
        )
        allowed_run = run(allowed, url_words)
        if allowed_run.returncode != 0:
            print(allowed_run.stdout)
            print("FAIL: the clone URL was flagged")
            return 1
        extra = base / "extra"
        extra.mkdir()
        (extra / "note.md").write_text("see " + org + " elsewhere\n", encoding="utf-8")
        extra_run = run(extra, url_words)
        if extra_run.returncode == 0:
            print("FAIL: org name outside the clone URL was accepted")
            return 1

    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
