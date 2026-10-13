# Research pipeline

One agent does the whole pass: frame the target, collect with the enabled tools, read the files that were produced, and write the summary. There is no required second agent.

Operational steps: `.claude/commands/pesquisar.md`.

## Frame

Slug, sub-targets, and the tier (quick or deep). Read the enabled keys in `memory/config.md` before collecting.

## Collect

Quick tier, each step only if that tool is enabled:

1. `last30days` when `last30days` is `yes`.
2. Web search.
3. YouTube search via `yt-dlp` when it is installed.
4. Instagram via the local minet tool when `instagram_research` is `yes`.
5. Reddit when `reddit` is `manual` or `auto`. Manual: give the creator the questions and wait for the paste. Auto: the local tool, read-only. See `memory/reddit_answers_tool.md`.
6. X via the Grok CLI only when the creator has already chosen to pay for that call. It is not a default key. Do not run it silently.

Deep tier adds a deeper last30days pass, broader autocomplete, and page fetches with the local scraping tool when it is installed.

A tool set to `no` is skipped. The gap is written in the summary. Do not pretend the source was checked.

## Write

`referencia/pesquisas/<slug>/RESUMO.md` with: pains and questions, what people are saying, top content, verified links, open angles, and the gaps. Read the raw files before citing a number. Do not trust a digest you have not opened.

TikTok has no free discovery path from this machine. Say so when the target is mostly TikTok. See `memory/tiktok_scraping_evaluated.md`.
