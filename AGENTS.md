# How to work in this project

This folder is a social-media system for one creator. The brand is empty until onboarding fills it. The language pass may rename creator-facing folders. Their jobs stay.

## First open

Read `memory/config.md`.

Stop and follow `onboarding/interview.md` when any of these is true:

- `memory/config.md` is missing
- `status` is not `ready`
- a required key is missing, empty, or not an allowed value. `writes_scripts` and `claude_in_chrome` are not among those keys when `status` is already `ready`
- any brand file below still contains `FILL VIA ONBOARDING`
- `dm_automation` is `yes` and `memory/dm-automation.md` does not contain a trigger word and both messages
- `existing_content` is `yes` and `referencia/perfil-atual/RESUMO.md` is missing
- `existing_content` is `yes` and `memory/edicao-observada.md` has no `decision: keep` or `decision: change`
- `content_language` is set and `files_language` is empty or not the same value

Do no other work until `status` is `ready`. If the creator opens the folder and sends any first message while the stop applies, say in one line that `/onboarding` starts the setup and begin it. The command and this section say the same thing. Ask one question at a time. The one exception is the tool-switch table in `onboarding/interview.md`. Question 1 is the language. From question 2, ask and write in `content_language`. Write each answer immediately. If the conversation stops, resume at the first unanswered required question. If `content_language` is set and `files_language` does not match, resume at `.claude/commands/aplicar-idioma.md` instead of renaming folders in the middle of the interview.

One setup step is allowed during that stop. If `ferramentas/Pytho-inator/pytho-inator` is missing, clone `https://github.com/SafeMantella/Pytho-inator.git` into `ferramentas/Pytho-inator` and make the wrapper executable. Do not edit the clone. Do not run it until `status` is `ready`.

On every open, including during that stop, read `memory/revisao-armazenamento.md`. The storage review is due when `last_review` is empty or older than `due_days`, and `defer_until` is empty or already past. When you give the warning, write `asked_on` as today. If `asked_on` is already today, do not ask again today. When it is due, warn before any other question and ask to run the review. A later with a date writes `defer_until`. Neither a later nor the warning moves a file or counts as a review. A yes follows `.claude/commands/revisar-armazenamento.md`. Nothing is moved, trashed, or deleted until the creator approves those paths.

At the start of every new session, including during that stop, read `memory/toolkit-updates.md`. It only records the date each part of the toolkit was last checked: `toolkit` (this template) and each tool repository. An item is due when its date is empty or older than `due_days`. When any item is due, say which ones in one line and ask to run `/update-toolkit`. Ask once per session. If the storage review is also due, ask that one first and this one in the next turn. When every date is empty and `status` is not `ready`, say nothing: setup has just cloned the tools. A no or a later ends the question for this session and changes nothing. A yes follows `.claude/commands/update-toolkit.md`. A filled brand file stays as this copy wrote it. Nothing is pushed.

On every open, including during that stop, read `memory/evolucao-template.md`. Skip this check when `memory/evolucao-template.local.md` contains `role: upstream`. If `started` is empty, write today's date and do not warn. The evolution report is due when `last_report` is empty and `started` is older than `due_days`, or when `last_report` is older than `due_days`, and `defer_until` is empty or already past. If the storage review or the toolkit update is also due and has not been asked this session, ask the earlier one and do not ask this one in the same turn. Storage comes first, then the toolkit update. When you give the warning, write `asked_on` as today. If `asked_on` is already today, do not ask again today. A later with a date writes `defer_until`. Neither a later nor the warning publishes anything or counts as a report. A yes follows `.claude/commands/reportar-evolucao.md`. Nothing is pushed, and no issue or pull request is opened, until the creator approves the exact text.

Allowed values:

- `status`: `empty` or `ready`
- `storage`: `notion` or `md`
- `carousel`: `claude`, `hyperframes`, or `md`. A copy that already uses Canva may keep `canva`, but onboarding no longer offers it
- `transcription`: `whisper` or `elevenlabs`
- `last30days`, `instagram_research`, `grok_image`, `dm_automation`, `behind_the_scenes`, `face`, `existing_content`: `yes` or `no`
- `reddit`: `no`, `manual`, or `auto`
- `content_language`: the language name the creator gave. This is the language of the system and of published content
- `files_language`: the same language name, written only after `onboarding/language_paths.py check` prints `ok`
- `brand_name`: non-empty
- `claude_in_chrome`: `yes` or `no`. `yes` only after the extension answered a test from the agent. Empty does not reopen onboarding when `status` is already `ready`. Offer it once at the next task that needs a logged-in browser, and write the key. A new onboarding asks it as question 1a
- `writes_scripts`: `yes` or `no`. Empty does not reopen onboarding when `status` is already `ready`. Ask once before the next script, and write the key. A new onboarding asks it before the readback.

Brand files that must be filled:

- `estrategia/01-posicionamento-e-pilares.md`
- `estrategia/00-identidade-visual.md`
- `memory/visual_identity_standard.md`
- `memory/social_media_handles.md`
- `memory/estilo-de-escrita/guia-voz.md`

## After onboarding

Read `memory/project_social_media_status.md`, then the pipeline for the task.

After `.claude/commands/aplicar-idioma.md`, the markdown files and the creator-facing folders are in `content_language`. Until that command, new notes and posts are already in that language and the folders still have their template names. Talk to the creator in `content_language`. Config keys and the marker `FILL VIA ONBOARDING` stay as written.

## Folder map

- `memory/` — config, rules, pipelines, brand notes. Index: `memory/INDEX.md`.
- `estrategia/` — strategy guides and the brand files.
- `conteudo/` — canonical pieces when `storage` is `md`.
- `referencia/` — research and the read of the creator's current profiles.
- `ferramentas/` — local tools. Owned ones are symlinks into `ferramentas/_repos/`.
- `.claude/commands/` and `.claude/skills/` — workflows and SOPs, the single source for every agent.
- `onboarding/` — the interview and its path and leak checks.
- `COMANDOS.md` — generated manual of commands and skills.

## Memory

The only project memory is `memory/` in this folder. Do not write project facts into a tool's private memory. When the creator corrects something that is a reusable preference, save it in `memory/` immediately and say so in one line. When it is unclear whether the correction is a one-off, ask.

## Posture

Never invent an opinion, a stance, or a taste for the creator. Draft what they said or what a source supports, and mark a gap where a stance is missing. A risky option (one that can limit or ban an account, or bills money) is never turned on by "yes to all" or "do as you prefer": the creator types the tool name after hearing the risk.

Be a critical growth and sales partner, not only an executor. Point out tensions. Research algorithm claims again when the source is older than two or three months. Read the strategy guide for the task. The pipelines still set the order of work.

## Pipelines

Read the file when the task arrives:

- Script or hook: `memory/feedback-notion-canonical-roteiro-hook.md`
- Carousel: `memory/feedback-carousel-pipeline.md` and `.claude/commands/carousel.md` (`/carousel`)
- Video edit: `memory/feedback-video-editing-pipeline.md`
- Research: `memory/pipeline_pesquisa.md` and `.claude/commands/pesquisar.md`
- Transcription: `memory/diretrizes-transcricao.md` and `.claude/skills/transcricao-confiavel/SKILL.md`
- Before publish: `memory/checklist-revisao-pre-publicacao.md`
- Any task: `memory/regras-execucao-robusta.md` (read the whole task first, keep the step order, evidence before "done")

Order is fixed: interview the creator, research, write in the canonical store, wait for approval, then build.

`storage` and `carousel` in `memory/config.md` choose Notion or `conteudo/`, and how a carousel is built: Claude's design tools, HyperFrames, or markdown only. If a login fails, stop and ask the creator to reconnect. Do not switch stores.

Research uses only the tools set to `yes`, `manual`, or `auto`. Record a gap in `referencia/pesquisas/<slug>/RESUMO.md` for every tool that is `no`.

Nothing is published, built as a carousel, or rendered at full resolution without an explicit yes.

The creator cuts the video and returns `base.mp4`. The agent transcribes, checks, corrects, interviews, then builds overlays and captions. Visual punch-ins only when the creator asks. `face: no` skips face-coverage checks and cutaways whose job is to remove the face. Captions still go on.

## Workflows

Ask the agent to read the file and follow it:

- `.claude/commands/onboarding.md` (`/onboarding`) starts or resumes the setup interview. The creator types it once after opening the folder
- `.claude/commands/ativar-ferramenta.md` (`/ativar-ferramenta <tool>`) turns on an optional integration after express onboarding
- `.claude/commands/learn-from-edit.md` (`/learn-from-edit`) when the creator pastes their own version of a draft
- `.claude/commands/iniciar.md` (`/iniciar`) at the start of a session, to recall what is pending
- `.claude/commands/pesquisar.md`
- `.claude/commands/atualizar-memoria.md`
- `.claude/commands/atualizar-ferramentas.md`
- `.claude/commands/comandos.md`
- `.claude/commands/revisar-video.md`
- `.claude/commands/edicao.md`
- `.claude/commands/avaliar-edicao.md`
- `.claude/commands/refinar-overlay.md`
- `.claude/commands/sugerir-conteudo.md`
- `.claude/commands/registrar-bastidores.md` only when `behind_the_scenes` is `yes`
- `.claude/commands/aplicar-idioma.md` once, after the onboarding readback, before `status: ready`
- `.claude/commands/map-automation-opportunities.md` once `status` is `ready`
- `.claude/commands/check-skills.md` once `status` is `ready`
- `.claude/commands/revisar-armazenamento.md` when the storage review is due, or when the creator asks
- `.claude/commands/update-toolkit.md` (`/update-toolkit`) when the session-start check says an item is due, or when the creator asks. It runs `.claude/commands/atualizar-ferramentas.md` and `.claude/commands/atualizar-do-git.md`
- `.claude/commands/reportar-evolucao.md` when the evolution report is due, or when the creator asks. Skip on the maintainer checkout

## Skills

- `.claude/skills/sistema-social-media/SKILL.md` — carousel and video SOP
- `.claude/skills/catalogo-ferramentas/SKILL.md` — generated list of every tool in `ferramentas/` and what it does. Read it before writing a script
- `.claude/skills/ferramentas-locais/SKILL.md` — syntax and gotchas of the local tools
- `.claude/skills/transcricao-confiavel/SKILL.md` — transcription
- `.claude/skills/pytho-inator/SKILL.md` — map a repeated task to one local Python CLI. The folder is a symlink into the clone.

## Owned tools

Before changing a tool under `ferramentas/`, read `memory/ferramentas-repos.md`. Eighteen owned tools are symlinks into gitignored clones at `ferramentas/_repos/`. Keep the paths `ferramentas/<tool>/...` in skills, commands, and memory. Every tool is one folder in `ferramentas/` with a one-line `README.md`. After adding, removing, or renaming one, run `ferramentas/manual-comandos/gerar`: it rewrites the tool catalog skill and warns about any agent file that points at a folder that does not exist. Edit and push inside `ferramentas/_repos/<repo>/`, as SafeMantella, with the GitHub noreply address already on that repository. Never commit `venv/`, `.profile/`, `.env`, cookies, or `__pycache__/`.

## Browser

Claude in Chrome (`claude_in_chrome` in `memory/config.md`) is how the agent reaches what sits behind the creator's login and has no API. It is vital to this toolkit, so offer it whenever it is off and a task needs it. Use the cheapest route that works: a connector, then a local script with its own profile, then Chrome reading text (`get_page_text`, `read_page`), and a screenshot last. Full policy: `memory/regras-execucao-robusta.md`. Install and test belong to onboarding question 1a. Never install or connect it without the creator's yes.

## Approval

The creator approves before anything is scheduled or published. Photos and screen recordings are real files the creator supplies.

## Automation

Pytho-inator is how this toolkit grows. Every new tool, script, or repeated task becomes one local Python CLI built through it, never an ad hoc script left in a piece folder. Run this only when `status` is `ready`.

Where the creator's repeated jobs are written down: `memory/ferramentas-existentes.md`, section "Repeated jobs". Read it when a hit appears or when the creator asks what to automate.

In Claude Code, the Pytho-inator mod runs `glance` after each turn that saved a file and prints the hit under the answer. Install it during onboarding with the creator's yes: `claude plugin marketplace add ./ferramentas/Pytho-inator --scope project`, then `claude plugin install pytho-inator@pytho-inator --scope project`. With the mod on, do not run `glance` again. Without it, run it as described below.

Building a hit, after a yes only: read `ferramentas/Pytho-inator/skills/pytho-inator/SKILL.md`, set the ponytail skill to `ultra` before the first line, use `uv` and never the system Python, prefer free open-source dependencies, and ask before any paid API and before the first test run. The finished CLI goes in `ferramentas/<name>/` with a README. When it belongs to one of the owned repositories, follow `memory/ferramentas-repos.md`. Then run `ferramentas/manual-comandos/gerar` if a command or skill changed.

When a task created or edited files, finish the task, then run `ferramentas/Pytho-inator/pytho-inator glance` on those files. Empty stdout means do not mention automation. A hit is one local Python CLI: at most three lines, and the last line of the CLI output is the finished task. Ask, in `content_language`, whether to build it. Do not build it and do not test it in that turn. A yes follows `ferramentas/Pytho-inator/skills/pytho-inator/SKILL.md`. Drop menus (`shape=fan-out`) and taste, approval, voice, strategy, or the interview (`judgment=keep`). If a Claude Code hook already printed the line, do not run glance again.
