---
description: Compare this copy with the template, draft a sanitized system report, and publish nothing until the creator approves the exact text.
---

# Report system evolution

Read this file and follow it. It is a workflow. The creator runs it by asking, and the agent asks for it when `memory/evolucao-template.md` says the report is due.

This copy is one creator's working system. The template is `https://github.com/SafeMantella/AI-Social-Media-Agent`. A report sends a lesson upstream. It does not send the brand.

Skip the whole workflow when `memory/evolucao-template.local.md` contains `role: upstream`. That file is the maintainer's checkout. Do not create it on a client copy.

## What a yes means

A yes to the question that opened this command approves the comparison and the draft. It does not approve sending.

Do not `git push`. Do not open an issue. Do not open a pull request. Do not copy a file from the template over this folder. Those wait for a later yes that names the exact text or the exact paths.

## Snapshot

Clone the template once, shallow, outside this folder:

```bash
rm -rf /tmp/ai-social-template-snapshot
git clone --depth 1 https://github.com/SafeMantella/AI-Social-Media-Agent.git /tmp/ai-social-template-snapshot
```

If the clone fails, stop and say so. Do not invent a diff. Delete `/tmp/ai-social-template-snapshot` before you finish, including when you stop early.

Compare the worktree on disk with that snapshot. A zip download and a git clone use the same comparison. Do not use `git diff` against `origin` as the source. Their commits mix brand files with system files.

Before a difference counts as a system change, map both sides through the rows in `onboarding/language_paths.py`. A renamed folder and translated prose are not a change. Compare a file with the file at its mapped path. A hunk that is only a translation is not upstream and not bring-in.

## Paths

Compare these when they exist on either side:

- `AGENTS.md`, `CLAUDE.md`, `README.md`, `README.pt-BR.md`, `.gitignore`
- `.claude/`
- `onboarding/`
- `ferramentas/`, except `venv`, `.venv`, `__pycache__`, `node_modules`, `downloads`, `transcripts`, `output`, `*.log`, cookie files, session files, `ferramentas/_repos/`, `ferramentas/_old/`, and the clones `Pytho-inator`, `last30days-skill`, and `fontastic-text-image-generator`
- template notes in `memory/` that are pipelines, feedback, or tool notes
- method guides `estrategia/03-templates-sops-calendario.md` through `estrategia/10-copywriting.md`

Do not read these into the report: `memory/config.md`, `memory/visual_identity_standard.md`, `memory/social_media_handles.md`, `memory/estilo-de-escrita/`, `memory/dm-automation.md`, `memory/edicao-observada.md`, `memory/ambiente-maquina.md`, `estrategia/00-identidade-visual.md`, `estrategia/01-posicionamento-e-pilares.md`, `estrategia/02-arquitetura-notion.md`, `estrategia/marca/`, `conteudo/`, `referencia/`, `freebies/` other than its README, `gravações/`, `books/`, `site/`, `.git/`, `.env`, and any file whose name contains `cookie`, `token`, `secret`, or `credential`.

A file that is only on the client under `.claude/`, `onboarding/`, or `ferramentas/` is a candidate when it is a system rule or a local tool. Leave it out when it is content, a brand asset, or a secret.

## Two lists

**Upstream.** Lines they added or changed that the template does not have. This is the only list that can become an issue.

**Bring in.** Lines the template has that this copy lacks, or that differ because the template moved on. Propose a copy of those paths onto this folder. Never propose a path in the do-not-read list. When both sides changed the same lines, do not copy. Show both and ask.

Ignore a hunk that only fills `FILL VIA ONBOARDING`, a config value, a handle, a bio, or a brand name.

## Draft

Write `memory/relato-evolucao.md`. It is gitignored. Show the same text in the chat.

The draft has three parts, in the creator's language:

1. **Upstream.** For each candidate: the path, what the system does differently, and the general rule in words. A short unified diff is allowed only when every line is safe under the redaction below.
2. **Bring in.** Paths to copy from the snapshot, and conflicts to leave for a decision.
3. **Leave local.** One line stating that brand, content, research, and credentials stayed out. Do not summarize them.

Redact before the creator sees the draft. Remove names, handles, bios, niches, audience, promises, captions, transcripts, profile URLs, emails, phone numbers, home-directory paths, and session paths. Remove any line that matches a key, a token, a cookie, a password, `api_key`, `secret`, `BEGIN PRIVATE`, `sk-`, or `xoxb-`. If a lesson only makes sense with those details, describe the mechanic and drop the example. If nothing generalizable remains, say so in one line.

Then stop. Ask which upstream items may be sent, and which bring-in paths may be copied.

## Send and apply

An upstream yes names the items, or explicitly approves the upstream section as shown. Anything unnamed stays. Rewrite the issue body from the approved items only. Show that body. A second yes sends.

The issue goes to `SafeMantella/AI-Social-Media-Agent`, not to a fork and not to their own remote. Title prefix: `[sistema]`. Use the issue form `sistema.md` when it exists. Prefer `gh issue create --repo SafeMantella/AI-Social-Media-Agent`. If `gh` is missing or not logged in, give the creator the title, the body, and this URL, and do not retry with another account:

`https://github.com/SafeMantella/AI-Social-Media-Agent/issues/new?template=sistema.md`

Do not open a pull request from this copy. The maintainer turns an accepted issue into a change on the template.

A bring-in yes names paths. Copy only those paths from the snapshot over this folder. Do not use `git merge` or `git pull`. If the destination has a local edit you did not show them, stop.

After they have answered, update `memory/evolucao-template.md`:

- `last_report`: today, `YYYY-MM-DD`, when they answered the draft, including when they kept everything local
- clear `asked_on` and `defer_until`
- append one log line: the date, how many items were approved, and the issue number if one was opened

Do not paste the report into that file. A closed chat with no answer is not a report. Leave `last_report` as it was.

Delete `/tmp/ai-social-template-snapshot`.
