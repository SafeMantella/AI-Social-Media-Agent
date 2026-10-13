# token-saver

A `tool.call` hook on `Read`. The first time a raw read targets an image over 150 KB or a text over 30 KB, it refuses and points at `prep-frames` or `prep-texto`. Repeating the read is allowed. It ignores `memory/`, `AGENTS.md`, and `SKILL.md`.

Register once from the repo root:

```bash
claude plugin marketplace add ./ferramentas/token-saver --scope project
claude plugin install token-saver@social-tools --scope project
```

Check: `claude plugin validate ferramentas/token-saver && claude plugin test ferramentas/token-saver`.
