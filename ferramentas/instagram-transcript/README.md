# Instagram, TikTok, and YouTube transcripts

Downloads one known video, transcribes it locally, and can save the top comments. It does not discover what is popular. Research discovery is `memory/pipeline_pesquisa.md`.

```bash
python3 instagram_transcript.py "https://www.youtube.com/watch?v=XXXX" --comments

python3 instagram_transcript.py "https://www.instagram.com/reel/XXXX/" \
  --cookies-file /path/outside/the/repo/session.txt --comments
```

- `--model` whisper size. `medium` is the default balance for a short video.
- `--language` is the spoken language.
- `--comments` writes the top 15 by likes.
- Instagram and TikTok need a session file from a logged-in browser. Keep that file outside git. On macOS, reading the browser store directly prompts for the keychain on every call, so export once and pass `--cookies-file`.

The word in `--cookies-file` is the upstream flag name. The file itself is gitignored when it sits in this folder as `ig_cookies.txt`.
