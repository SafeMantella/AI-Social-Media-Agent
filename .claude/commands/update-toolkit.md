---
description: Check the toolkit and every tool repository for updates, apply what is behind, and record the dates in memory/toolkit-updates.md.
---

# Update the toolkit

Read this file and follow it. It is a workflow. The creator types `/update-toolkit`, or says yes to the session-start question from `AGENTS.md`.

A yes approves fetching and fast-forwarding. It does not approve a push, an issue, a pull request, or installing a changed dependency.

Do not `git push`, `git reset --hard`, or `git clean`. Never touch a filled brand file.

## 1. Read the registry

Read `memory/toolkit-updates.md`. Say which rows are empty or older than `due_days`. If the creator named one item, check only that one.

## 2. Tool repositories

Run `ferramentas/atualizar-ferramentas/atualizar-ferramentas`. It fetches every checkout in `ferramentas/_repos/` and every loose clone under `ferramentas/`, fast-forwards the ones that are behind, and writes the date of each successful check into the registry. Read the last line (`resumo: ...`).

- `bloqueada`: the clone has local edits. Do not touch it. List the files and ask.
- `erro`: no date is written. Say why.
- `dependência mudou, reinstalar`: tell the creator which tool and which manifest. Install only after a yes.

Then compare the folder with `memory/ferramentas-repos.md` and `README.md`. Each tool listed there must exist. If a clone or a symlink is missing, offer the clone command from `memory/ferramentas-repos.md`. Clone only after a yes.

## 3. The toolkit itself

Follow `.claude/commands/atualizar-do-git.md`. It pulls the template `main` and adapts the system files. When it finishes, write today's date in the `toolkit` row of `memory/toolkit-updates.md`, even when `main` was already current.

If the folder has no git remote for the template, say so and skip this step. Do not write a date for a step that did not run.

## 4. Report

Reply with one line per item: `current`, `updated (N commits)`, `blocked`, or `error`. Add what needs a decision from the creator. If any tool or the toolkit changed `AGENTS.md`, `.claude/`, or `onboarding/`, say the new rules apply from the next session.

Always run `ferramentas/manual-comandos/gerar` after an update. It rewrites `COMANDOS.md` and the tool catalog skill, and warns about a pointer to a missing tool folder. Report those warnings.
