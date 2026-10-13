# Recent case studies and social discussion — `last30days`

Use the local tool **`last30days`** (`ferramentas/last30days-skill/`) to ground case studies (`referencia/estudos-de-caso/`), trend-response scripts, benchmarking of reference profiles, and market facts from the last 30 days.

Whether this collector runs is the `last30days` key in `memory/config.md`. API secrets stay in the environment. A browser session file is kept outside git. Do not commit either.

## How it works, and which sources it asks

It searches in parallel and weights results by real human engagement (upvotes, likes, comments, prediction markets with money volume) instead of by pages tuned for search engines:

- **Reddit:** top threads and comments with real upvote counts. No API secret. This public path is separate from Reddit Answers; that collector follows the `reddit` key (`no`, `manual`, or `auto`) in `memory/config.md`.
- **YouTube:** full transcripts of recent videos, looking for quotable lines (via `yt-dlp`, no API secret).
- **Hacker News and GitHub:** technical discussion, commit pace, issues, and pull requests (`--github-user`, `--github-repo`).
- **Polymarket:** probabilities and prediction markets with real volume.
- **Web grounding:** news and a general synthesis. Needs an API secret in the environment. This is the web source.
- **X:** included only with a session file kept outside git, or with an API secret in the environment for that provider. Secondary.
- **TikTok and Instagram:** **left off inside this tool.** They would require a paid scraper. See Status. Instagram discovery, when wanted, is `minet` and follows `instagram_research` in `memory/config.md`.

## Commands

The script is `ferramentas/last30days-skill/skills/last30days/scripts/last30days.py`. Do not run the skill's first-run wizard. Call the script directly.

1. **Quick scan of a topic or trend:**

   ```bash
   python3 "ferramentas/last30days-skill/skills/last30days/scripts/last30days.py" "<topic>" --quick --emit md --output "<path>.md"
   ```

2. **Deep pass for a new case study:**

   ```bash
   python3 "ferramentas/last30days-skill/skills/last30days/scripts/last30days.py" "<topic or creator>" --deep --emit md --output "<path>.md"
   ```

   **`--emit md` alone does not save a file** (confirmed by reading `last30days.py`). It only sets the stdout format. Persist with `--output <path>` (an exact file) or `--save-dir <folder>`.

3. **Named short-video profiles** (flags exist; those sources stay off under the decision in Status):

   ```bash
   python3 "ferramentas/last30days-skill/skills/last30days/scripts/last30days.py" "<topic>" --tiktok-creators "user1,user2" --ig-creators "user1"
   ```

4. **Compare competitors or tools:**

   ```bash
   python3 "ferramentas/last30days-skill/skills/last30days/scripts/last30days.py" "Brand A vs Brand B" --competitors-list "Brand A,Brand B,Brand C"
   ```

5. **Integrity check / source diagnosis:**

   ```bash
   python3 "ferramentas/last30days-skill/skills/last30days/scripts/last30days.py" --preflight
   ```

## Status — local sources only

1. **Web grounding is configured with an API secret in the environment.** It is the brain of the run: synthesis, query planning, and web grounding. A separate paid web-search secret is unnecessary while grounding works.
2. **X is best-effort.** The run may read a session file kept outside git from the installed browsers. X is secondary. If it misses, the rest of the run is still valid.
3. **TikTok / Instagram inside this tool: off. No paid scraper.** Same rule as the rest of the project: do not add a paid API. The vendor's free grant is **100 credits, one-time use**. The tool's own docs disagree: the code says 100, while older pages and a startup check have said 10,000 ([issue #367](https://github.com/mvanhorn/last30days-skill/issues/367)). Rechecked on the local checkout after that issue's fix: `hooks/scripts/check-config.sh` says "100 free credits", but `SKILL.md`, `AGENTS.md`, and `last30days.py doctor` can still announce "10,000 free calls". Trust the corrected hook, not the larger number. Local substitutes were fragile, so automatic discovery of those two platforms inside this tool is an accepted gap. "I already have this video; give me a transcript and comments" is `ferramentas/instagram-transcript/` (extended to the short-video host, with comments, using a session file kept outside git). Transcription mode is `transcription` in `memory/config.md` (`whisper` or `elevenlabs`).
4. **The transcription module inside `last30days` (`lib/transcribe.py`) is dead code.** The engine never calls it. Nothing to configure there. Transcription outside the skill follows `transcription` in `memory/config.md`.
5. **`curl_cffi` 0.13** is installed on the system Python. `yt-dlp` needs it for TLS impersonation on short-video hosts. The range that note recorded is `>=0.5.10,<0.14`. **Do not** upgrade to 0.14 or above. Scrapling's fetchers want a newer, incompatible release and therefore live in their own virtualenv (see `scrapling_scraping_tool.md`).

Discovery that runs locally with no secret: **Reddit, YouTube (`yt-dlp`), Hacker News, GitHub, Polymarket, plus web grounding** when the grounding secret is set.

**Per-source status, from `python3 last30days.py doctor` (re-run if time has passed):**

- **Working:** YouTube (search and transcript via `yt-dlp`), Hacker News, GitHub (`gh` CLI).
- **On but unstable:** Reddit (the public path hits HTTP 429 on heavy runs). X (session file kept outside git; the session is only confirmed during the run).
- **Down:** Polymarket, when `gamma-api.polymarket.com` does not resolve. That is DNS on the network, not a bug in the code, if the URL still matches the vendor docs. Low priority: the source is rarely the one that matters.
- **Off, and not worth the paid path:** TikTok, Instagram, and the other social connectors behind the vendor's free-credit setup. See point 3. The real grant is 100, not 10,000.

What remains unsolved is discovery of those short-video platforms inside this tool. See `memory/tiktok_scraping_evaluated.md`.

## When not to rely on it

- **Evergreen or academic topics** (a settled how-to, a principle, a paper) come back empty or off-topic, because there is no fresh social discussion under 30 days to capture. Go straight to web search plus the paper or the official doc. At most, use `last30days` to collect *hook language* that already appears in real posts. Never use it as the only basis. To pull articles or docs that sit behind a bot wall or client-rendered pages, use Scrapling (`memory/scrapling_scraping_tool.md`).
- **Transient degradation:** HTTP 429 from the grounding provider and from Reddit zeros the reranker and web grounding. The "Ranked Evidence Clusters" section comes back empty. If grounding is the only web path, it falls with them. When a run says "No candidates survived retrieval and ranking", try again later, or treat the tool as not covering that topic.
- **A real pattern:** a topic can return zero on-topic evidence on both a `--deep` run and a `--quick` run. The page then has to be grounded entirely with web search and primary documents.
- **Source mismatch, even on a fresh topic:** the mix (Reddit, Hacker News, GitHub, YouTube, Polymarket) leans toward technical communities. A creator-marketing question can finish with no technical error and still be mostly noise: unrelated repositories and threads, and "top voices" from places that have nothing to do with the question. If that happens, take the refresh from direct web search.
- **A non-English query can degrade search on X** (see `lib/bird_x.py`). The zero-result fallback shortens the query until it anchors on a "strongest term", but the low-signal word list only covers English. A common function word from another language can be left as the anchor and pull in noise. It is a third-party library with a formal change process. Do not patch it locally. Practical workaround: write the topic in English, or bilingual, when the result depends on X.
- **Redundancy rule:** if `last30days` does not return a usable signal within two tries — crash, "no candidates survived", or a result that is mostly off-topic — switch to direct web search. Do not insist on a third run.

## Why

Social and algorithm data goes stale in about 2–3 months. For a market read, a case study of a channel or a viral post, or a timely response, the last 30 days beats an outdated premise and supplies real counts (upvote volume, retention figures people actually cite). See the limits above. For a topic with no social footprint, direct web search is better.

## How to apply

- **Before a case study** in `referencia/estudos-de-caso/`, run `last30days` on the topic or the creator to capture recent consensus and discussion.
- **When judging ideas or hooks** for video, use the synthesis as script grounding, then check it against the limits above.
- **Updates:** the tool is a git sub-repository managed by `.claude/commands/atualizar-ferramentas.md`.
