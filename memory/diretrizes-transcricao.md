# Transcription

Read this before step 1 of the video pipeline.

`transcription` in `memory/config.md` chooses the engine.

- `whisper`: local, no API bill. Prefer the more accurate local engine over a fast one that drops words without warning. When two local engines are installed, diff them. A gap in time is not the check. A difference in words is the check.
- `elevenlabs`: one engine, billed by the provider. The secret stays in `ELEVENLABS_API_KEY` in the environment. Check timings. Say that a second engine was not run.

Write `transcripts/master.json` with word timings the caption step can read. Correct names in that file. Show the cues to the creator before rendering captions.

The skill `.claude/skills/transcricao-confiavel/SKILL.md` is the procedure. The tool is `ferramentas/transcrever/`.
