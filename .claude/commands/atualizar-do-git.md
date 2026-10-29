---
description: Pull the template main into this folder and adapt the system files. Keep filled brand files as they are.
---

# Update this folder from git

Read this file and follow it. It is a workflow. The creator runs it by asking, and `/update-toolkit` runs it as its step 3.

The template is `https://github.com/SafeMantella/AI-Social-Media-Agent.git`, branch `main`. A yes to the question that opened this command approves the pull and the adaptation below. It does not approve a push, an issue, or a pull request.

Do not `git push`. Do not `git reset --hard`. Do not `git clean`. Do not delete a file the creator filled.

## Link

If `.git` is missing, run `git init`, then `git add -A` and commit the current tree. `.gitignore` stays in force. Do not force-add a cookie, a session, an `.env`, or a media file.

If `upstream` is missing and `origin` is not the template, add `upstream` with the template URL. Leave an existing `origin` in place when it points somewhere else.

Use `upstream` when it exists. Use `origin` when that remote is the template. Fetch that remote. If the fetch fails, stop and say so. Do not invent an update.

## A copy that already ran the language command

Read `files_language` in `memory/config.md` and the rows in `onboarding/language_paths.py`. When the creator-facing folders are no longer the template's names, do not pull with `--allow-unrelated-histories`. That pull conflicts add/add on almost every system file and plants a second tree beside the translated one.

Do this instead:

1. Find the template commit this copy started from. It is the newest template commit whose system files match this copy once translated prose and the path renames are ignored. Same code, translated words.
2. Apply only the template's delta since that commit.
3. Write that delta onto the local paths, in `content_language`. Map each path through the rows in `onboarding/language_paths.py`. Do not create the template's folder names beside the translated ones.
4. When a conflict is a file the template did not change since that base commit, keep the local side.
5. If a bad pull already created a duplicate tree, remove only the duplicate template folders. Do not remove a folder that holds a local fill. If you cannot tell which tree is the duplicate, stop and ask.

A copy that still uses the template's folder names uses the pull below.

## Pull

When tracked files have uncommitted edits, commit them with `git add -u` before the pull. That commit records the current tree. It does not add untracked files.

Merge `main` from the remote into the current branch:

```bash
git pull <remote> main --no-rebase
```

On a folder that was a zip, the histories have no common ancestor. Use the same pull with `--allow-unrelated-histories`. If the pull fails, stop and show the error. Leave the conflict markers in place and say which files need a decision.

## What stays

These stay as this copy filled them. An empty `FILL VIA ONBOARDING` in the template does not come back over a local fill. In a conflict, keep the local side (`--ours` during a pull):

- `memory/config.md`
- `memory/visual_identity_standard.md`
- `memory/social_media_handles.md`
- `memory/estilo-de-escrita/`
- `memory/dm-automation.md`
- `memory/edicao-observada.md`
- `memory/ambiente-maquina.md`
- `estrategia/00-identidade-visual.md`
- `estrategia/01-posicionamento-e-pilares.md`
- `estrategia/02-arquitetura-notion.md`
- `estrategia/marca/`
- `conteudo/`
- `referencia/`
- `freebies/` other than its README
- `gravações/`, `books/`, `site/`
- `.env`, cookies, sessions, and credentials

Do not remove `venv`, `.venv`, tool clones, downloads, or gitignored media. A template file the client never edited can leave when `main` deleted it. A file they edited stays.

## What updates

The new `main` wins on system structure: `AGENTS.md`, `CLAUDE.md`, the READMEs, `.gitignore`, `.claude/`, `onboarding/`, `ferramentas/` outside the clones and the virtualenvs, pipeline notes in `memory/`, and the method guides `estrategia/03-templates-sops-calendario.md` through `estrategia/10-copywriting.md`.

When both sides changed the same system lines, take the new rule. Keep a local sentence that is an onboarding answer or a brand fact. Remove conflict markers before you finish. If a hunk is not clearly one or the other, stop and ask. Do not choose the empty template side.

## After

Tell the creator what came in, what you adapted, and what you kept. Then write today's date (`YYYY-MM-DD`) in the `toolkit` row of `memory/toolkit-updates.md`, including when `main` was already current.

A closed chat with no yes is not an update. Leave the date as it was.
