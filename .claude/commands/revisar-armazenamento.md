---
description: Measure this folder, propose what to move or remove, and change nothing until the creator approves those paths.
---

# Review storage in this folder

Read this file and follow it. It is a workflow. The creator runs it by asking, and the agent asks for it when `memory/revisao-armazenamento.md` says the review is due.

The review is a proposal. A yes to start it approves the measurement only. A move, a trash, or a delete waits for a later yes that names those paths.

## What to measure

Stay inside this folder. Do not follow a symlink that leaves it. Do not upload the tree anywhere.

1. From the repo root, record `du -hd 1` for the top level. For any top-level folder over about 100MB, record `du -hd 2` inside it. Group caches. Do not list every file inside `venv`, `.venv`, `node_modules`, or `__pycache__`.
2. Note files over about 50MB: path and size.
3. Note the known heavy and regenerable groups when they exist: `venv` and `.venv`, `__pycache__`, `node_modules`, `*.log`, `ferramentas/instagram-transcript/downloads/`, `ferramentas/instagram-transcript/transcripts/`, `ferramentas/pdf-to-markdown/output/`, frame images under `referencia/perfil-atual/`, and model caches that sit inside this folder.
4. Note a file that sits outside the folder whose job it is. The jobs are in `memory/project_social_media_status.md`. A research note belongs in `referencia/pesquisas/`. A canonical piece belongs in `conteudo/` when storage is markdown. A recording belongs in `gravações/`. Do not invent a new tree. Do not rename the creator-facing folders. The language command owns that.

## What to propose

Sort the findings into four groups. Every line has the path, the size, why it is there, and one proposed action: `trash`, `move to <existing folder>`, or `leave`.

- **Regenerable.** Virtualenvs, package caches, logs, download folders, frame images, and tool output. The proposal may say trash. Name the install line from that tool's README when a trash would force a reinstall.
- **Misplaced.** A file in the wrong existing folder. The proposal may say move. The destination already exists and its job matches.
- **Media.** Any `.mp4`, `.mov`, or other recording. Report the size. The proposed action is `leave` unless the creator has already said that piece is finished and that a backup exists. Rendered video stays until then. Read `memory/feedback_video_editing_recording_patterns.md` and `memory/feedback-generated-video-in-project.md`. Do not propose deleting `master.mp4`, `base.mp4`, or an approved deliverable.
- **Leave unless asked.** `.git`, markdown in `memory/`, `estrategia/`, `conteudo/`, and `onboarding/`, the agent rules, the skills, the commands, and third-party clones under `ferramentas/`. Report a clone's size. Do not propose deleting it in this review.

Do not propose `git clean`. Do not propose `rm`.

Show the list in the chat. Then stop.

## What a yes means

- "Yes" to the question that opened this command means measure and propose. It does not approve a path.
- After the list, act only on paths the creator names, or on the whole list when they explicitly approve that list. A bare yes, when the list has more than one action, approves nothing. Ask which lines.
- Anything they do not name stays where it is.
- "Leave everything" is a finished review. Change no files. Write `last_review` as today.

## What to change

For an approved `trash`, put the path in the macOS Trash. Use the `trash` command when it exists. Otherwise ask Finder, one path at a time:

```bash
osascript -e 'tell application "Finder" to delete POSIX file "/absolute/path"'
```

If neither one works, stop and say so. Do not fall through to `rm`.

For an approved move, `mv` only into the destination already named in the proposal. The destination is an existing folder. Do not overwrite a file that is already there. Stop and ask.

After the creator has answered the list, update `memory/revisao-armazenamento.md`:

- `last_review`: today, `YYYY-MM-DD`
- clear `asked_on` and `defer_until`
- append one log entry: the date, the paths they approved, the paths they refused, and the size freed when a trash or a move happened

A closed chat with no answer to the list is not a review. Leave `last_review` as it was.
