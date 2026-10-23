# social-auto-upload

Browser upload for Instagram, YouTube, and TikTok. The clone is gitignored.

```bash
cd ferramentas
git clone https://github.com/dreammis/social-auto-upload.git
```

Python 3.12. `uv sync --python 3.12` inside the clone. Cookies stay in `ferramentas/social-auto-upload/cookies/` and are not committed. `conf.py` is local. Do not commit it.

- Instagram and YouTube go through `sau` inside the clone. Pass `--file` as an absolute path.
- YouTube through that clone posts now. It does not schedule. A headless check can report a valid cookie as expired. The Studio path that does schedule-free upload with a visible window is `ferramentas/sau-yt/`.
- TikTok is `ferramentas/sau-tiktok/`. On a Mac the caption clear is Meta+A. Without `--schedule` the post is public.
- `sau-yt` keeps its logged-in profile in `.profile/`, gitignored.

Nothing is published until the creator names the file and the visibility.
