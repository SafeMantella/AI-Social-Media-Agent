# transcrever

Local transcription. Procedure: `memory/diretrizes-transcricao.md` and `.claude/skills/transcricao-confiavel/SKILL.md`.

## Install

```bash
cd ferramentas/transcrever
python3 -m venv venv && ./venv/bin/pip install whisperx
```

Keep this venv separate from the Python that runs yt-dlp. The `vad` and `janela` engines do not use the venv. They call `whisper-cli`. Set `WHISPER_CPP_BIN`, `WHISPER_CPP_MODEL`, and `WHISPER_VAD_MODEL`. If those are missing, the script exits with code 2.

## Files

| File | Role |
|---|---|
| `transcrever.py` | Transcribe. `--motor whisperx\|vad\|janela`, `--verificar` |
| `comparar.py` | Diff two transcripts |
| `glossario.py` | Apply `glossario.json` |
| `leitura.py` | Write a short reading file (phrase and time) |
| `glossario.json` | Mishear to correct form. Empty until the creator adds terms |

## Notes

- whisperx runs on CPU here. MPS being available does not mean CTranslate2 will use it.
- The first run downloads the model into the Hugging Face cache.
- A torchcodec warning on stderr is harmless. It falls back to another decoder.
