---
description: Suggest content ideas from the work done this session. Show them in the chat only, until the creator picks what to save.
---

# Suggest content from this session

Read this file and follow it. It is a workflow.

Use it after a working session. The task does not have to be about social media (a bug fixed, a feature built, an architecture decision, a piece of hardware). The work itself is raw material. The goal here is an angle for the audience, on any pillar in `estrategia/01-posicionamento-e-pilares.md`, not a behind-the-scenes case. That series is `.claude/commands/registrar-bastidores.md`, and only when `behind_the_scenes` is `yes`.

**This step is suggestions only.** Do not create a page or a file while suggesting, even when an idea seems too obvious to leave out.

If the request includes a direction, use it as the starting point, as well as the session.

## What to do

1. **Gather what this conversation actually did** — decisions, an obstacle that was solved, code that was written, a correction, a tool that was used for the first time.

2. **Read the live options. Do not trust a hardcoded list.**
   - `storage: notion` — fetch the ideas database linked from `estrategia/02-arquitetura-notion.md` and read the current options for pillar, target platforms, origin, impact, and effort. If the link is missing, stop and ask. Do not invent a database.
   - `storage: md` — pillars come from `estrategia/01-posicionamento-e-pilares.md`. Platforms come from `memory/social_media_handles.md`.

3. **Apply the growth lens** (`memory/growth_sales_critical_lens.md`). The hook is specific, not vague. Authority, connection, and trust stay in balance. Do not propose another authority video when that is already most of the queue.

4. **Generate 3 to 6 suggestions.** Fewer is not a real choice. More is noise. Number each one:
   - **Name** — short, ready to become the title.
   - **Summary** — 1–3 sentences. The angle for the audience, not "post about what we did".
   - **Suggested pillar**
   - **Suggested platform or platforms**
   - **Suggested format** — a short video is the base format (`memory/content-format-cascade.md`). Suggest a text-only format only when a video does not make sense.
   - If one suggestion has a clearly stronger growth signal (a pain or curiosity hook, or a proof pillar the queue is missing), say which one and why. Do not inflate the others so they look equal.

5. **Show only that in the chat, and stop.**

## When the creator says what to save

They will name the numbers, the main platform (it may differ from the suggestion), and any change to the pillar or the summary. That may be in the same turn or later.

1. Create only the chosen ideas.
   - `storage: notion` — `notion-create-pages`, parent = the ideas database from `estrategia/02-arquitetura-notion.md`.
   - `storage: md` — one file per idea at `conteudo/ideias/<slug>.md`.
2. Fields:
   - **Name / summary** — as suggested, or as the creator adjusted.
   - **Pillar** — as suggested, or as adjusted.
   - **Platforms** — the ones the creator named (more than one is allowed).
   - **Origin** — work in progress (the idea came from real work, not a loose brainstorm), unless they explicitly name another origin.
   - **Status** — not started.
   - **Impact / effort** — fill only when the creator gives a clear signal, or when it is obvious from the scope (an idea that already has a finished script from another task is low effort). Do not invent a score.
3. Confirm which items were created, and where each one is.
