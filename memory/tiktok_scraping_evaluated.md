# TikTok scraping — evaluated, not free from a normal machine

Niche discovery on TikTok without a paid API was tested on three paths. All three are blocked. TikTok hard-blocks automated scraping from a residential IP that has no proxy.

| Tool | Result |
|---|---|
| `minet tiktok search-videos` | TikTok returns `200` with an empty body (`TiktokPublicAPIInvalidResponseError`). Search requires a device signature this client does not compute. |
| Scrapling (`fetch` / `stealthy-fetch`) | `get` returns an empty client-side shell ("Please wait..."). `fetch` triggers TikTok's own slider challenge. It is not a Cloudflare Turnstile, so the Cloudflare solver does not clear it. |
| **`davidteather/TikTok-Api`** (v7.3.3, tested and removed) | Installed in an isolated virtualenv (Playwright chromium and webkit). **Every mode** (`hashtag`, `trending`, `user`) raised `EmptyResponseException: TikTok returned an empty response. They are detecting you're a bot`. Headless chromium, headless webkit, and headful chromium (a visible window) all failed. A signed-in browser session did not help. The library itself says to consider a proxy. Without a residential proxy, it dies. |

## What is left for TikTok

- **Zeeschuimer + 4CAT** ([digitalmethodsinitiative/zeeschuimer](https://github.com/digitalmethodsinitiative/zeeschuimer)) is a browser extension. Scroll the TikTok feed or search normally and it writes ndjson to analyze later. **No detection**, because it is real browsing. Cost: it is manual, and 4CAT wants Docker (or the Zeehaven converter to CSV). It is the only free path that actually works. **Not adopted yet.** Adopt it if TikTok research becomes a priority.
- **A residential proxy** would unblock TikTok-Api, but it is paid, so it stays out while the project avoids paid APIs.
- **TikTok Research API** is free only for approved researchers, and it is region-locked.

## How to revive TikTok-Api (only with a proxy, or from another network)

```bash
uv venv --python 3.12 ferramentas/tiktok-api/.venv
uv pip install --python ferramentas/tiktok-api/.venv/bin/python TikTokApi
ferramentas/tiktok-api/.venv/bin/python -m playwright install chromium
```

The trial script was deleted with the trial. It read a session file kept outside git, opened one session, and walked hashtag, user, trending, and search results into a CSV (author, stats, music, challenges). Passing a proxy list into session creation is the missing piece. Keep that session file outside git.

## Other platforms

- **Instagram.** `minet` works (see `minet_niche_research_tool.md`): hashtag, user posts, the profile graph, and comments, via a session file kept outside git. The rate limit is aggressive. Run it only when `instagram_research` is enabled in `memory/config.md`.
- **"I have a video and I need a transcript"** on TikTok or Instagram is `ferramentas/instagram-transcript/` (yt-dlp plus the transcription mode in `memory/config.md`, `whisper` or `elevenlabs`). It does not do discovery.
- **last30days** leaves TikTok and Instagram discovery off (paid scraper, limited credits). See `last30days_case_study_research.md`.
