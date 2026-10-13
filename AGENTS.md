# How to work in this project

This folder is a social-media system for one creator. The layout stays. The brand is empty until onboarding fills it.

## First open

Read `memory/config.md`.

Stop and follow `onboarding/interview.md` when any of these is true:

- `memory/config.md` is missing
- `status` is not `ready`
- a required key is missing, empty, or not an allowed value
- any brand file below still contains `FILL VIA ONBOARDING`
- `dm_automation` is `yes` and `memory/dm-automation.md` does not contain a trigger word and both messages

Do no other work until `status` is `ready`. Ask one question at a time, in the language the creator is writing in. Write each answer immediately. If the conversation stops, resume at the first unanswered required question.

Allowed values:

- `status`: `empty` or `ready`
- `storage`: `notion` or `md`
- `carousel`: `canva` or `md`
- `transcription`: `whisper` or `elevenlabs`
- `last30days`, `instagram_research`, `grok_image`, `dm_automation`, `behind_the_scenes`, `face`: `yes` or `no`
- `reddit`: `no`, `manual`, or `auto`
- `content_language`: the language name the creator gave
- `brand_name`: non-empty

Brand files that must be filled:

- `estrategia/01-posicionamento-e-pilares.md`
- `estrategia/00-identidade-visual.md`
- `memory/visual_identity_standard.md`
- `memory/social_media_handles.md`
- `memory/estilo-de-escrita/guia-voz.md`

## After onboarding

Read `memory/project_social_media_status.md`, then the pipeline for the task.

System files are English. Talk to the creator in the language they are using. Write posts, scripts, captions, and hooks in `content_language`.

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

## Skills

- `.claude/skills/sistema-social-media/SKILL.md` — carousel and video SOP
- `.claude/skills/ferramentas-locais/SKILL.md` — local tools
- `.claude/skills/transcricao-confiavel/SKILL.md` — transcription

## Approval

The creator approves before anything is scheduled or published. Photos and screen recordings are real files the creator supplies.
