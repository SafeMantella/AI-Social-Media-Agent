# How to work in this project

This folder is a social-media system for one creator. The brand is empty until onboarding fills it. The language pass may rename creator-facing folders. Their jobs stay.

## First open

Read `memory/config.md`.

Stop and follow `onboarding/interview.md` when any of these is true:

- `memory/config.md` is missing
- `status` is not `ready`
- a required key is missing, empty, or not an allowed value
- any brand file below still contains `FILL VIA ONBOARDING`
- `dm_automation` is `yes` and `memory/dm-automation.md` does not contain a trigger word and both messages
- `existing_content` is `yes` and `referencia/perfil-atual/RESUMO.md` is missing
- `existing_content` is `yes` and `memory/edicao-observada.md` has no `decision: keep` or `decision: change`
- `content_language` is set and `files_language` is empty or not the same value

Do no other work until `status` is `ready`. Ask one question at a time. Question 1 is the language. From question 2, ask and write in `content_language`. Write each answer immediately. If the conversation stops, resume at the first unanswered required question. If `content_language` is set and `files_language` does not match, resume at `.claude/commands/aplicar-idioma.md` instead of renaming folders in the middle of the interview.

One setup step is allowed during that stop. If `ferramentas/Pytho-inator/pytho-inator` is missing, clone `https://github.com/SafeMantella/Pytho-inator.git` into `ferramentas/Pytho-inator` and make the wrapper executable. Do not edit the clone. Do not run it until `status` is `ready`.

Allowed values:

- `status`: `empty` or `ready`
- `storage`: `notion` or `md`
- `carousel`: `canva` or `md`
- `transcription`: `whisper` or `elevenlabs`
- `last30days`, `instagram_research`, `grok_image`, `dm_automation`, `behind_the_scenes`, `face`, `existing_content`: `yes` or `no`
- `reddit`: `no`, `manual`, or `auto`
- `content_language`: the language name the creator gave. This is the language of the system and of published content
- `files_language`: the same language name, written only after `onboarding/language_paths.py check` prints `ok`
- `brand_name`: non-empty

Brand files that must be filled:

- `estrategia/01-posicionamento-e-pilares.md`
- `estrategia/00-identidade-visual.md`
- `memory/visual_identity_standard.md`
- `memory/social_media_handles.md`
- `memory/estilo-de-escrita/guia-voz.md`

## After onboarding

Read `memory/project_social_media_status.md`, then the pipeline for the task.

After `.claude/commands/aplicar-idioma.md`, the markdown files and the creator-facing folders are in `content_language`. Until that command, new notes and posts are already in that language and the folders still have their template names. Talk to the creator in `content_language`. Config keys and the marker `FILL VIA ONBOARDING` stay as written.

## Memory

The only project memory is `memory/` in this folder. Do not write project facts into a tool's private memory. When the creator corrects something that is a reusable preference, save it in `memory/` immediately and say so in one line. When it is unclear whether the correction is a one-off, ask.

## Posture

Be a critical growth and sales partner, not only an executor. Point out tensions. Research algorithm claims again when the source is older than two or three months. Read the strategy guide for the task. The pipelines still set the order of work.

## Pipelines

Read the file when the task arrives:

- Script or hook: `memory/feedback-notion-canonical-roteiro-hook.md`
- Carousel: `memory/feedback-carousel-pipeline.md`
- Video edit: `memory/feedback-video-editing-pipeline.md`
- Research: `memory/pipeline_pesquisa.md` and `.claude/commands/pesquisar.md`
- Transcription: `memory/diretrizes-transcricao.md` and `.claude/skills/transcricao-confiavel/SKILL.md`
- Before publish: `memory/checklist-revisao-pre-publicacao.md`

Order is fixed: interview the creator, research, write in the canonical store, wait for approval, then build.

`storage` and `carousel` in `memory/config.md` choose Notion or `conteudo/`, and Canva or markdown. If a login fails, stop and ask the creator to reconnect. Do not switch stores.

Research uses only the tools set to `yes`, `manual`, or `auto`. Record a gap in `referencia/pesquisas/<slug>/RESUMO.md` for every tool that is `no`.

Nothing is published, built in Canva, or rendered at full resolution without an explicit yes.

The creator cuts the video and returns `base.mp4`. The agent transcribes, checks, corrects, interviews, then builds overlays and captions. Visual punch-ins only when the creator asks. `face: no` skips face-coverage checks and cutaways whose job is to remove the face. Captions still go on.

## Workflows

Ask the agent to read the file and follow it:

- `.claude/commands/pesquisar.md`
- `.claude/commands/atualizar-memoria.md`
- `.claude/commands/atualizar-ferramentas.md`
- `.claude/commands/refinar-overlay.md`
- `.claude/commands/sugerir-conteudo.md`
- `.claude/commands/registrar-bastidores.md` only when `behind_the_scenes` is `yes`
- `.claude/commands/aplicar-idioma.md` once, after the onboarding readback, before `status: ready`
- `.claude/commands/map-automation-opportunities.md` once `status` is `ready`
- `.claude/commands/check-skills.md` once `status` is `ready`

## Skills

- `.claude/skills/sistema-social-media/SKILL.md` — carousel and video SOP
- `.claude/skills/ferramentas-locais/SKILL.md` — local tools
- `.claude/skills/transcricao-confiavel/SKILL.md` — transcription
- `.claude/skills/pytho-inator/SKILL.md` — map a repeated task to one local Python CLI. The folder is a symlink into the clone.

## Approval

The creator approves before anything is scheduled or published. Photos and screen recordings are real files the creator supplies.

## Automation

Run this only when `status` is `ready`.

When a task created or edited files, finish the task, then run `ferramentas/Pytho-inator/pytho-inator glance` on those files. Empty stdout means do not mention automation. A hit is one local Python CLI: at most three lines, and the last line of the CLI output is the finished task. Ask, in `content_language`, whether to build it. Do not build it and do not test it in that turn. A yes follows `ferramentas/Pytho-inator/skills/pytho-inator/SKILL.md`. Drop menus (`shape=fan-out`) and taste, approval, voice, strategy, or the interview (`judgment=keep`). If a Claude Code hook already printed the line, do not run glance again.
