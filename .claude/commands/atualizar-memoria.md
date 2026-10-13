---
description: Scan this session for decisions, corrections, and patterns that are not saved yet, and update memory/ in this project plus the index that points at it.
---

# Update memory from this session

Read this file and follow it. It is a workflow.

The only project memory is `memory/` in this folder. Do not write project facts into a tool's private memory, and do not write them outside this folder. `memory/INDEX.md` is the full index. The project guide lists the files that should be read every session.

If the request includes a note about what changed, use that note as well as the session. Do not use the note instead of looking at the session.

## What to do

1. **Gather what changed.** Review the session for corrections about how something should have been done, new decisions (calendar, priority, architecture), technical patterns that worked and are worth repeating, confirmed preferences (a non-obvious choice the creator accepted), and new pointers to external systems. If the session has no real work yet and the request did not say what changed, ask the creator. Do not invent entries.

2. **Classify each candidate** as `user`, `feedback`, `project`, or `reference`. Do not save a code or architecture pattern that can be derived from the repo, git history, a one-off bug fix, or an ephemeral detail of work still in progress. If the creator asked to save something that falls under an exclusion, say so instead of saving it, and ask what was surprising or non-obvious. That is the part worth keeping.

3. **Check for a duplicate before creating a file.** Search `memory/*.md` for the same subject. Prefer **editing the existing file** over creating a second one.

4. **Update `memory/`.** Match the format already used there: a `# Title` and prose, no frontmatter, unless the file you are editing already has a different shape — then match that file. A fact that is specific to this project belongs only here.

5. **Update the index if a new file was created.** Add a short line to `memory/INDEX.md`, and to the project guide's memory list if that guide is supposed to name the file every session. Follow the existing pattern (file name plus one sentence). Do not rewrite a whole section to add one line.

6. **Report, short.** What was created, what was edited and why (not only "updated X"), and what was considered and dropped because it fell under an exclusion. Do not list a file that did not change.
