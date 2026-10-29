---
description: Turn on an optional integration after express onboarding: ask its question, install it, test the capability, and write the key.
argument-hint: <tool or config key>
---

# Turn on a tool

Read this file and follow it. It is a workflow. Run it only when `status` is `ready`. `$ARGUMENTS` is a config key from `memory/config.md` (`transcription`, `last30days`, `reddit`, `instagram_research`, `grok_image`, `dm_automation`, `behind_the_scenes`, `claude_in_chrome`) or a tool name from `.claude/skills/catalogo-ferramentas/SKILL.md`. With no argument, list the keys that are `no` and what each one gives, and ask which.

1. Run `/doctor` for the machine. Say the download size, the time, and the cost before installing anything.
2. Find the question for that key in `onboarding/interview.md` (questions 18 to 24, and 1a for Chrome). Ask it as written, with the recommendation.
3. A **risky** key (`reddit: auto`, `instagram_research: yes`, `grok_image: yes`, `dm_automation: yes`) needs the creator to type the tool name after hearing the risk. "Yes" alone does not count.
4. Run the install check listed under "Install checks" in that file. Test the capability the creator will use, not only that the command starts. Launch a browser-based tool yourself once before asking the creator to log in.
5. Write the key in `memory/config.md` only when the check passes. Record what works and what does not in `memory/ambiente-maquina.md`. A failed check leaves the key as it was.
6. Run `ferramentas/manual-comandos/gerar` if a tool folder appeared.
