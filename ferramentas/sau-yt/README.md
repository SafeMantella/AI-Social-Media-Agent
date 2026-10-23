# sau-yt

Upload a video through YouTube Studio with a persistent browser profile, the same pattern as `reddit-answers`.

```bash
ferramentas/sau-yt/sau-yt login
ferramentas/sau-yt/sau-yt upload --file v.mp4 --title T [--visibility private|unlisted|public]
```

The profile lives in `.profile/` and is gitignored. The wrapper uses `ferramentas/scrapling/.venv`. The last stdout line is the video URL. Nothing is published public unless the creator asked for that visibility.
