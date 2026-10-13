---
description: Record this session's technical decisions as the next case in the behind-the-scenes series. Runs only when behind_the_scenes is yes.
---

# Record a behind-the-scenes case

Read this file and follow it. It is a workflow.

Read `memory/config.md` first. If `behind_the_scenes` is not `yes`, stop. Say the workflow is off. Do not write a case.

The series is build-in-public about building this agent and this system — the work in this project folder, not the finished post that goes out on a platform. Each case is raw material the creator can later record as an episode.

If the request includes a note about what changed, use it as the summary of the session, as well as the conversation. If the session has no real work yet and the note is empty, ask what to record. Do not invent a case.

## What to do

1. **Find the series page or file.**
   - `storage: notion` — the series page linked from `estrategia/02-arquitetura-notion.md`. Fetch it. If that file has no link yet, ask the creator which page to update. Do not invent a URL and do not create a new database.
   - `storage: md` — `conteudo/bastidores/serie.md`. Create it only when the first real case is written, with two headings: `## Cases already recorded` and `## Candidates for the next entry`.

2. **Read the current text** of `## Cases already recorded` (to know the next number) and `## Candidates for the next entry` (so a candidate that just became a case is not duplicated, and a candidate that is not ready yet is not dropped).

3. **Gather what changed in the agent or the system this session.** Not every task qualifies. A qualifying change is a decision that changed direction, a real obstacle (a tool that did not do what it claimed, a limit that was discovered), a correction about how the agent should have done something, or a new piece of architecture (memory, skill, workflow, automation). Routine execution with nothing reusable does not qualify.

4. **If nothing qualifies,** say so. Do not force an entry so that the series has something new.

5. **Write the new entry** under `## Cases already recorded`, next number, in the same shape as the entries already there: `**N. "short title, stated as the problem or the insight"**`, then **one narrative paragraph** in the third person (the creator did X, the agent did Y, the result was Z). Inside the paragraph, no extra markdown except a little bold on key terms. No bullets. No headings inside the case.
   - Notion: `notion-update-page` with `command: "update_content"` and an `old_str` / `new_str` anchored on the end of the last existing entry plus the start of `## Candidates for the next entry`. Do not use `replace_content`. That would erase the earlier cases.
   - Markdown: insert in the same place in the file. Do not rewrite the earlier cases.

6. **Update `## Candidates for the next entry` only when it helps.** Remove the item that just became a case. Add a future hook that came up in the session but is not ready to be a full case.

7. Confirm in one or two sentences what was recorded, and where.
