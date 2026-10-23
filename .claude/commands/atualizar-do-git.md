---
description: Once a week, pull the template main into this folder and adapt the system files. Keep filled brand files as they are.
---

# Update this folder from git

Read this file and follow it. It is a workflow. The creator runs it by asking, and the agent asks for it when `memory/atualizacao-git.md` says the update is due.

The template is `https://github.com/SafeMantella/AI-Social-Media-Agent.git`, branch `main`. A yes to the question that opened this command approves the pull and the adaptation below. It does not approve a push, an issue, or a pull request.

Do not `git push`. Do not `git reset --hard`. Do not `git clean`. Do not delete a file the creator filled.

## Link

If `.git` is missing, run `git init`, then `git add -A` and commit the current tree. `.gitignore` stays in force. Do not force-add a cookie, a session, an `.env`, or a media file.

If `upstream` is missing and `origin` is not the template, add `upstream` with the template URL. Leave an existing `origin` in place when it points somewhere else.

Use `upstream` when it exists. Use `origin` when that remote is the template. Fetch that remote. If the fetch fails, stop and say so. Do not invent an update.

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

Tell the creator what came in, what you adapted, and what you kept. Then update `memory/atualizacao-git.md`:

- `last_pull`: today, `YYYY-MM-DD`, including when `main` was already current
- clear `asked_on` and `defer_until`
- append one log line: the date, and either `already current` or the commit subjects that arrived

A closed chat with no yes is not an update. Leave `last_pull` as it was.
