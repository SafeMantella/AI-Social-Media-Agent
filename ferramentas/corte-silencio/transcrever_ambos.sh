#!/bin/zsh
# usage: transcrever_ambos.sh <edit-folder> <stem>...
# Set WHISPER_CPP_BIN, WHISPER_CPP_MODEL, and WHISPER_VAD_MODEL before running.
export WHISPER_CPP_BIN="${WHISPER_CPP_BIN:-$(command -v whisper-cli)}"
ed="$1"; shift
for s in "$@"; do
  python3 ferramentas/transcrever/transcrever.py "$ed/audio/$s-enhanced.mp3" -o "$ed/transcripts/$s.wx.json" > "$ed/transcripts/$s.wx.log" 2>&1
  python3 ferramentas/transcrever/transcrever.py "$ed/audio/$s-enhanced.mp3" -o "$ed/transcripts/$s.vad.json" --motor vad > "$ed/transcripts/$s.vad.log" 2>&1
done
touch "$ed/transcripts/done.flag"
