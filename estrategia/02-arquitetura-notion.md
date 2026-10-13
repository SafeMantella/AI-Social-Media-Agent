# Notion architecture

Used when `storage` in `memory/config.md` is `notion`. When `storage` is `md`, the canonical store is `conteudo/` and this file is only the map of what would exist in Notion.

## Databases

FILL VIA ONBOARDING

Onboarding writes the links. The expected databases are:

- Ideas — one backlog. A status field separates a raw idea from a script that is ready to record. An order field sorts the queue.
- Ready content — carousels, single images, and text posts. Video does not live here. The idea database is the calendar for short video.
- Analytics — performance by platform.

Each piece stores the visual element planned for each slide or beat.

## If there is no Notion

Ideas: `conteudo/ideias/<slug>.md`
Scripts: `conteudo/roteiros/<slug>.md`
Carousels: `conteudo/carrosseis/<slug>.md`
Captions: `conteudo/legendas/<slug>.md`
Research: `referencia/pesquisas/<slug>/`
