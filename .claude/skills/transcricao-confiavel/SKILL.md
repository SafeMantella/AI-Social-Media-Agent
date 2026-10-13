---
name: transcricao-confiavel
description: Transcribe local video or audio without silently dropping speech. Choose the engine, cross-check two engines, apply the glossary, and check sync before captions. Use for any recording in this project, at the first step of a video edit, or when a transcript looks incomplete or wrong.
---

# Reliable transcription

Use this instead of `helpers/transcribe.py` from the `local-video-use` skill for any recording in this project. Why, the measurements, and what already failed: **`memory/diretrizes-transcricao.md`**. Read that before changing a parameter here.

This skill is the local whisper path. It applies when `transcription` in `memory/config.md` is `whisper`. If it is not, use the configured provider. Never write a secret into the repo.

Tool: `ferramentas/transcrever/` (an isolated environment for whisperx). Language follows `content_language`. Do not assume a language.

## Default flow (4 commands)

```bash
# 1. Transcribe (whisperx is the default; it is the engine that did not drop speech)
python3 ferramentas/transcrever/transcrever.py "<video>" -o "<edit>/transcripts/base.wx.json"

# 2. Apply the glossary (recurring names the model misspells)
python3 ferramentas/transcrever/glossario.py "<edit>/transcripts/base.wx.json" \
        -o "<edit>/transcripts/base.json"

# 3. Cross-check when the piece is going to be published
python3 ferramentas/transcrever/transcrever.py "<video>" -o /tmp/check.json --motor vad
python3 ferramentas/transcrever/comparar.py "<edit>/transcripts/base.json" /tmp/check.json \
        --rotulos "whisperx,vad"

# Shortcut for steps 1 and 3 in one command:
python3 ferramentas/transcrever/transcrever.py "<video>" -o base.json --verificar
```

## Hard rules

1. **Never use whisper.cpp `-dtw` for anything that must be complete.** It drops whole segments without warning. That was measured on more than one video. It is why this skill exists.
2. **A time-gap check is not protection.** The worst loss measured so far had continuous timestamps. The real protection is the diff between two engines (`comparar.py`).
3. **Every difference of 3 or more words that `comparar.py` lists has to be resolved** before a cue is generated. Re-transcribe that window alone. That is where the model is accurate. `<lang>` is the code for `content_language`.
   ```bash
   ffmpeg -nostdin -v error -y -ss <t-2> -t <dur+4> -i "<video>" -ar 16000 -ac 1 /tmp/j.wav
   whisper-cli -m "$WHISPER_CPP_MODEL" -l <lang> -nt /tmp/j.wav
   ```
4. **Check sync before accepting a render,** not only the text. `transcrever.py` already complains about an impossible timestamp. Also look at the real composite at 3 or 4 points spread across the video (a contact sheet), never only the log. When `face` in `memory/config.md` is `no`, skip face-coverage checks. Captions still go on.
5. **A wrong proper name becomes a glossary entry,** not a hand correction on one file — `ferramentas/transcrever/glossario.json`. That is what reduces the next round of edits.
6. **Show the cues to the creator before rendering** (the caption step of the video pipeline in `.claude/skills/sistema-social-media/SKILL.md`). Skip that only when they explicitly ask for the final render in the same message, and say that the check was skipped.

## Which engine

| Engine | Use when |
|---|---|
| `whisperx` (default) | the transcript will become captions — complete text and a trustworthy timestamp |
| `vad` | a fast draft, or the second engine in the cross-check |
| `janela` | last resort; the seam between windows drops words |

Rough time for 2 minutes of audio: whisperx about 3–5 minutes on CPU, vad about 40 seconds, janela about 2 minutes.

## Output shape

`{"words": [{"text", "start", "end"}, ...]}` — the same shape `pack_transcripts.py`, `render.py`, and the caption build already expect. Drop-in replacement for `transcribe.py` from `local-video-use`.
