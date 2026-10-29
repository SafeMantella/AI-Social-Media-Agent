# Parity with the Antigravity CLI (agy)

Optional. Only for a creator who also runs this folder in Antigravity (`agy`). Claude Code needs none of it.

## What already works with no setup

- `AGENTS.md` is the entry file, and `CLAUDE.md` is a symlink to it. `agy` reads `AGENTS.md` on open, so it gets the same rules, the same `memory/` pointer, and the same session-start checks.
- Commands live in `.claude/commands/` and skills in `.claude/skills/`. `AGENTS.md` names the files, so any agent reads them from there. Do not copy them into another folder.
- `/pesquisar` splits collection from synthesis for Claude. In `agy` the one agent does both and does not delegate to itself.

## What does not carry over

- Notion and Canva connectors are hosted on the Claude account. They are not local MCP entries, so there is nothing to copy. Register the endpoints in `agy` (`agy mcp add <name> <url>`) and authorize them again the first time. Ask the creator to do that login.
- Claude Code's automatic memory is not folded into `agy` on purpose. This folder keeps its own `memory/`.

## Optional migration helper

The `antigravity` plugin (third party: `antigravity-for-claude-code`) ships `agy-migrate`. Install it only if the creator asks. Run it with `--apply` only after showing the dry run. It registers global skills and trusted workspaces. A skill folder inside a project is not registered by it: add that path to the `agy` skills config by hand. Undo with `agy-migrate --uninstall --apply`.

Re-run it when a skill moves, a new `AGENTS.md` appears in a subproject, or a plugin is installed.
