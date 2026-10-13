# minet

Web mining CLI from [médialab / Sciences Po](https://github.com/medialab/minet) (GPL-3). Isolated venv, Python 3.12, gitignored. Call `ferramentas/minet/minet`.

Instagram commands need a browser session export kept outside git (`ferramentas/minet/cookies.txt` is gitignored). Set `instagram_research` to `yes` in onboarding only after that file exists.

| Command | Returns |
|---|---|
| `minet instagram hashtag "<tag>"` | Posts for a hashtag |
| `minet instagram user-posts "<user>"` | Posts of a profile |
| `minet instagram user-followers` / `user-following` | A profile's network |
| `minet instagram comments "<url>"` | Comments on a post |
| `minet instagram user-infos "<user>"` | Profile info. Empty results usually mean rate limit. Space the calls. |

TikTok search from this tool returns an empty body. There is no free TikTok discovery path here. See `memory/tiktok_scraping_evaluated.md`.

Without a session file it still does `fetch`, `scrape`, `extract`, `crawl`, `resolve`, and `url-parse`.

```bash
cd ferramentas/minet
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python minet
```
