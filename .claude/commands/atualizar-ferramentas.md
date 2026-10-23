---
description: Check the cloned tools under ferramentas/ against their remotes, and fast-forward the ones that are behind.
argument-hint: [optional tool name]
---

# Update cloned tools in `ferramentas/`

Read this file and follow it. It is a workflow.

Run `ferramentas/atualizar-ferramentas/atualizar-ferramentas` with the tool name when one was given. The script scans each git checkout directly under `ferramentas/` and each checkout in `ferramentas/_repos/`. It skips symlinks, so a tool that points into `_repos/` is pulled once. Read the last line (`resumo: ...`). One line per tool:

- `já estava atualizada` — current
- `atualizada` — fast-forwarded. The line names the commits. If it also says `dependência mudou, reinstalar`, tell the creator. Do not install.
- `bloqueada` — the clone has local changes. Do not touch it. The line lists the files.
- `erro` — no remote, no network, or the fast-forward failed.

The script does not install dependencies and does not edit a dirty clone. If no git folder was found, say that.
