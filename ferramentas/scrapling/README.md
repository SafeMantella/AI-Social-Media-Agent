# Scrapling

Adaptive fetch for pages behind bot checks. Upstream: [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling), BSD-3. Call the wrapper `ferramentas/scrapling/scrapling`. The venv in this folder is gitignored.

`scrapling[fetchers]` wants a newer `curl_cffi` than `yt-dlp`. They do not share a Python. That is why this venv exists.

Use it to fetch articles, docs, and public pages for research. It does not discover Instagram or TikTok posts.

```bash
python3 -m venv ferramentas/scrapling/.venv
ferramentas/scrapling/.venv/bin/pip install "scrapling[fetchers]" markdownify
ferramentas/scrapling/.venv/bin/scrapling install
```

`markdownify` is required for markdown output.
