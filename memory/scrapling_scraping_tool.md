# Scrapling — local scraping that can pass a bot wall

Added as a pip package (`scrapling` 0.4.15) in an **isolated virtualenv** (`ferramentas/scrapling/.venv/`, gitignored). **Not** in global Python. Call the wrapper `ferramentas/scrapling/scrapling`. Usage notes are in `ferramentas/scrapling/README.md`.

## What it is

A web scraping framework ([D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling), BSD-3). Three fetch tiers, used in order: `get` (HTTP with impersonation), then `fetch` (Chromium, renders client-side pages), then `stealthy-fetch` (stealth, and it can clear a Cloudflare Turnstile). Output is markdown, text, HTML, or JSON based on the file extension (`.md` needs `markdownify`, which is installed in the venv).

## Why an isolated virtualenv (not a global install)

`scrapling[fetchers]` requires `curl_cffi>=0.16.1`. `yt-dlp` (used by `ferramentas/instagram-transcript/` and by `last30days`) requires `curl_cffi<0.16` for TLS impersonation on short-video hosts. They cannot share one environment. A global install moved `curl_cffi` to 0.16.3 and wiped yt-dlp's impersonation targets. Global was put back on `curl_cffi==0.13.0`. Scrapling stayed in its own venv. **Side effect that remains:** global `playwright` moved from 1.60 to 1.62 and `anyio` from 4.11 to 4.14. Nothing else depends on that Playwright, the bumps are forward, and the risk is low, so they were not reverted.

## When to use it

1. **Case-study research.** Pull pages that sit behind Cloudflare or another bot wall to ground `referencia/estudos-de-caso/`. This covers the hole in `last30days` on evergreen topics and on topics that are not a social conversation (see `last30days_case_study_research.md`, "when not to rely on it").
2. **Watch competitors and profiles.** Discovery of profiles, rankings, and lists. `instagram-transcript` explicitly does not do discovery.
3. **Feed `last30days`.** A collection layer for URLs and page content.

## Decisions

- **CLI now, MCP later.** Scrapling has an MCP server (`scrapling[ai]`, `scrapling-mcp`, 13 tools). It is not registered: this setup has no local MCP, 13 tools loaded every session cost context, and it overlaps the in-app browser. Revisit if the CLI falls short (a persistent browser session, dozens of URLs per session, on a repeating basis).
- Smoke test: all three tiers passed through the venv and the wrapper (`get` to example.com, `fetch -s` to quotes.toscrape.com/js, `stealthy-fetch --solve-cloudflare` to nowsecure.nl, where the challenge cleared).

## How to use it

```bash
ferramentas/scrapling/scrapling extract <get|fetch|stealthy-fetch> "<url>" output.md --ai-targeted [-s "<css>"]
```

**Always pass `--ai-targeted`** (it sanitizes HTML, which is the protection against prompt injection). Always start at `get`. Move up to `fetch` or `stealthy-fetch` only if the result is empty or a 403. Delete the temporary files after reading them. Full syntax, flags, and gotchas are in `ferramentas/scrapling/README.md`.

## Why this tool

Local tools are preferred over a paid API. Same rule as `transcription` in `memory/config.md` (`whisper` or `elevenlabs`) and as not using a paid scraper inside `last30days`. Scrapling is the local path for pages that plain HTTP cannot get (Cloudflare, client-rendered pages, other bot walls), with no per-request fee.

## How to apply

- Occasional research, not bulk collection (platform terms).
- Upgrade with `ferramentas/scrapling/.venv/bin/pip install --upgrade "scrapling[fetchers]" markdownify`. The command in `.claude/commands/atualizar-ferramentas.md` does not cover it (this folder is not a git repo).
- When changing global Python, remember the pin `curl_cffi<0.16`. Do not let anything raise that, or `instagram-transcript` breaks on short-video hosts.
