# minet — Instagram discovery without a paid API

CLI for web mining from [médialab / Sciences Po](https://github.com/medialab/minet) (GPL-3, v4.2.1), in an **isolated virtualenv** (`ferramentas/minet/.venv/`, Python 3.12 via `uv`, gitignored). Call it through the wrapper `ferramentas/minet/minet`. Usage notes live in `ferramentas/minet/README.md`.

Run it only when `instagram_research` is enabled in `memory/config.md`. The signed-in browser session is a session file kept outside git. Do not commit that file.

## What actually works

Checked with a signed-in session file:

- **Instagram works.** `hashtag` and `user-posts` returned real data (caption, likes, comments, media, timestamp). `user-followers`, `user-following`, and `comments` should work on the same path. `user-infos` came back empty once; that was probably the rate limit.
- **TikTok `search-videos` is broken.** TikTok returns `200` with an empty body (`TiktokPublicAPIInvalidResponseError`). Search requires a device signature this client does not compute. It is not the session file. It is TikTok's bot wall. minet 4.2.1 does not fix it. TikTok in minet is only `search-videos` (no `hashtag` or `user-posts`).
- `tiktok search-commercials` and `scrape-commercials` need the TikTok Research API (a key and a secret). Ignore them.

**TikTok gap:** there is no free fix from a normal machine. minet, Scrapling, and `davidteather/TikTok-Api` (tested, then removed) are all blocked without a residential proxy. See `memory/tiktok_scraping_evaluated.md`. Only a manual browser capture works, and it is not adopted.

## Session file (manual step)

The built-in browser-session grabber does not read Chrome or Brave on this kind of machine (app-bound encryption). `yt-dlp` can.

1. Export a session file kept outside git from the browser where the creator is signed in, using yt-dlp's browser-session export, against a TikTok URL and an Instagram URL. yt-dlp may print errors; it still writes the file.
2. Confirm the file is a real Instagram session: the project helper that prints the session header should show a session id.
3. Run:

```bash
ferramentas/minet/minet instagram hashtag "<tag>" -c "<session header>" -l 50 -o out.csv
```

The session file is gitignored. Treat it like a password. It expires in days or weeks. A `401` that asks for login means export it again.

## Why an isolated virtualenv

minet 4.x needs a prerelease allowed (it depends on a pre-release Twitter library) and does not build on the system Python 3.13. Create the venv with Python 3.12 and install `minet==4.2.1` with prereleases allowed. **This does not touch the global Python** (unlike the Scrapling / `curl_cffi` incident on the same day).

## Why it is here

Real niche discovery on Instagram (search a hashtag, pull a profile's history, map a graph) without a paid API. It uses the creator's own signed-in session. Same rule as the rest of the project: do not add a paid dependency. It complements, and does not replace, `last30days` (discussion synthesis) and `instagram-transcript` (a transcript of one known video).

## How to apply

- Make sure the session file is fresh before a run (check the session id).
- **The rate limit is aggressive.** Space the searches out. Do not run a large batch. `user-infos` already failed after about five calls in two minutes.
- Output is CSV. Read it with the file reader, or filter it with `minet select` / `minet filter`. Count rows with a CSV parser. A multiline caption inflates a raw line count.
- If Instagram breaks later: upgrade `minet` inside `ferramentas/minet/.venv` with prereleases allowed.
- Use it for occasional research, not bulk collection (platform terms).
