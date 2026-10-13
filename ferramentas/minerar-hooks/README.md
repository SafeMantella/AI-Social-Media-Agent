# minerar-hooks

Input: a CSV with hook text, views, and an optional source column. Column names are detected.

```bash
python3 minerar.py hooks.csv [--top 40] [--out dir]
```

Writes `hooks.mined.json` and a short summary. Rank is a percentile inside each source. Sources stay separate. Families follow `referencia/swipe-openers.md`.

`--selftest` checks the script. Rewriting the words is the agent's job. See `memory/pipeline_pesquisa.md`.

Origin: github.com/Ootto-AI/claude-content-skills (MIT), adapted.
