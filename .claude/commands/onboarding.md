---
description: Start or resume the setup interview. This is the whole install: it clones what is missing, asks one question at a time, and fills the brand.
---

# Onboarding

Read this file and follow it. It is a workflow. The creator types `/onboarding` once, right after opening this folder in the agent. Typing it again resumes at the first unanswered question.

1. If `ferramentas/Pytho-inator/pytho-inator` is missing, clone `https://github.com/SafeMantella/Pytho-inator.git` into `ferramentas/Pytho-inator` and make the wrapper executable. Do not edit that clone. Do not run it during onboarding.
2. Read `AGENTS.md`, then `memory/config.md`.
3. If `status` is `ready`, say so in one line and do not interview again. Read `memory/project_social_media_status.md` and wait for a task. Stop here.
4. Otherwise follow `onboarding/interview.md` and do no other work. The rules that matter most:
   - Question 1 is the language of the whole system. After the answer, ask the rest in that language and write the answers in it.
   - Ask one question at a time. Write each answer into the file the interview names, immediately.
   - Do not rename folders in the middle of the interview. After the readback, follow `.claude/commands/aplicar-idioma.md` once.
   - Ask the creator's permission before installing anything on their machine, Claude in Chrome included.
   - If they already publish, ask for the links of three specific posts (question 4b) and finish the profile read before asking about niche, voice, or visuals. Propose only from what you actually opened.
   - Run the install check for every tool set to `yes`. A failed check does not finish onboarding.
   - Do not suggest an automation during onboarding.
   - Do not set `status: ready` until every required answer is written and every check has passed.
5. Do not publish, build a carousel, or render at full resolution without an explicit yes.
6. The session-start checks in `AGENTS.md` (storage review, toolkit update, evolution report) still apply during onboarding.

When onboarding ends, run `ferramentas/manual-comandos/gerar` so `COMANDOS.md` and the tool catalog match this machine, then tell the creator the three commands to start with: `/iniciar`, `/pesquisar`, and `/carousel`.
