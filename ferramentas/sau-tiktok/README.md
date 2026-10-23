# sau-tiktok

Upload a video to TikTok through the cloned `social-auto-upload` tool. The clone is gitignored. Cookies stay in that clone and are not committed.

```bash
ferramentas/sau-tiktok/sau-tiktok login
ferramentas/sau-tiktok/sau-tiktok upload-video --file v.mp4 --title T
```

The wrapper uses `ferramentas/social-auto-upload/.venv`. On a Mac the caption field needs Meta+A, not Control+A. Without `--schedule` the post goes out public. Detail: `memory/social-auto-upload.md`.
