# Automatic-cut evals

`ferramentas/evals/` checks a cut from transcript to preview. The last take of a repeated line is the one that stays. The tool may remove silence over 0.7s, retakes, and false starts inside an eval. The output is an EDL, a table, and a 960p preview. A full-resolution render and a publish still wait for a yes.

Set `WHISPER_CPP_MODEL` and `WHISPER_VAD_MODEL` in the environment. A case file lives with the piece, not in this template. `REVISAR` is the agent's call.
