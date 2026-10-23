# Social media agent

An empty system for one creator. Paste the prompt below into the coding agent of your choice, with this folder open. That is the setup. It runs onboarding and fills the brand, the platforms, and the tools.

Português (Brasil): [README.pt-BR.md](README.pt-BR.md)

`AGENTS.md` is the entry file. `CLAUDE.md` points at it.

## Paste this

One prompt. Copy the block and send it as the first message.

```
Set up this folder as my social-media system. This message is the setup. There is no separate install step.

If ferramentas/Pytho-inator is missing, clone https://github.com/SafeMantella/Pytho-inator.git into ferramentas/Pytho-inator and make ferramentas/Pytho-inator/pytho-inator executable. Do not edit that clone. Read AGENTS.md and follow it. Read memory/config.md. If status is not ready, follow onboarding/interview.md and do no other work. Do not suggest an automation during onboarding. The first question is the language of the whole system. After I answer, ask the rest in that language and write my answers in it. Do not rename folders in the middle of the interview. After the readback, follow .claude/commands/aplicar-idioma.md once. That rewrites the markdown, renames the creator-facing folders, and sets files_language only when onboarding/language_paths.py check prints ok. Ask me one question at a time. Write each answer into the file the interview names, immediately. If I already publish, open those profiles and finish the profile read before you ask about niche, voice, or visuals. Copy each video's first on-screen line into the swipe file. Before I choose to keep the old edit, tell me what holds a stranger and what loses them in the first seconds. Propose only from what you actually saw. Run the install check for every tool I set to yes. A failed check does not finish. Do not set status to ready until every required answer is written and every check has passed.

If status is already ready, do not interview me again. Read memory/project_social_media_status.md and wait for a task. After status is ready, at the end of each task that created or edited files, run ferramentas/Pytho-inator/pytho-inator glance on those files. If it prints nothing, say nothing about automation. If it prints a hit, show at most three lines and ask whether to build that Python CLI. Do not build it unless I say yes.

Keep project memory only in memory/ inside this folder, using the folder name from the language pass if it was renamed. Do not publish, build in Canva, or render full resolution unless I explicitly say yes.

On every open, including during setup, read memory/revisao-armazenamento.md. If the storage review is due, warn me and ask before any other question. A scan, a move, or a deletion waits for a yes, and a yes to the scan is not a yes to a path.

On every open, including during setup, read memory/atualizacao-git.md. If started is empty, write today's date and do not ask. If the weekly git update is due, and you did not already ask the storage question this turn, warn me and ask. A yes pulls main from https://github.com/SafeMantella/AI-Social-Media-Agent.git and adapts the system files. A filled brand file stays as I wrote it. Do not push.

On every open, including during setup, read memory/evolucao-template.md. If started is empty, write today's date and do not ask. If the monthly evolution report is due, and you did not already ask the storage question or the git-update question this turn, warn me and ask. Do not push, and do not open an issue or a pull request, until I approve the exact text. Skip this on a checkout whose memory/evolucao-template.local.md says role: upstream.
```

Answer every question. Onboarding ends when `memory/config.md` says `status: ready`. If you already publish, the agent reads those profiles before the rest of the interview.

The first answer sets the language. The interview and the posts use it from the next question. The folder rename runs once, after the readback, and only counts when the path check passes.

## What is here

| Path | Role |
|---|---|
| `AGENTS.md` | Rules. Read on every open. |
| `onboarding/interview.md` | The first-run interview. |
| `memory/` | Decisions, pipelines, and the brand once onboarding fills it. Start at `memory/project_social_media_status.md`. |
| `estrategia/` | Strategy docs. The long guides are the method. Brand files stay blank until onboarding. |
| `.claude/skills/` | SOPs the agent loads. |
| `.claude/commands/` | Workflows. Ask the agent to read the file and follow it. |
| `ferramentas/` | Local tools. |
| `conteudo/` | Canonical pieces when storage is markdown. |
| `referencia/pesquisas/` | Research output. |
| `referencia/perfil-atual/` | What onboarding read from profiles you already publish. |
| `freebies/` | One folder per lead magnet, from the mold in `freebies/README.md`. |
| `gravações/` | Local video input. Gitignored. Empty in the template. |

Notion and Canva are optional. Onboarding records which one you use. Markdown in `conteudo/` is the fallback.

## Requirements

macOS is what the scripts were written for. Python 3.10+, ffmpeg, git, and Node are the base.

```bash
brew install python@3.13 node ffmpeg git
```

Whisper is required only if onboarding chose local transcription. ElevenLabs is required only if onboarding chose it. The secret stays in the environment as `ELEVENLABS_API_KEY`.

Video edits expect a local video skill that can transcribe, cut, and render, installed where your agent loads skills. The pipeline names that skill `local-video-use`.

## Accounts and cost

| Item | When | Cost |
|---|---|---|
| Your coding agent | Always | Depends on that product |
| Adobe account | Audio cleanup step | Free tier exists. Limits were not re-verified here |
| Reddit account | If Reddit is manual or auto | Free. Auto is against Reddit's terms and can limit the account |
| ElevenLabs | If transcription is elevenlabs | Billed by ElevenLabs |
| xAI | If Grok image generation is yes | Billed per image |
| Notion | If storage is notion | Their plan |
| Canva | If carousel is canva | Their plan. Record the master template id |
| PilotDM | If Instagram DM automation is yes | Free tier exists |
| GitHub | To publish or share a tool | Their plan |

## Local tools

Each tool has a README in its folder. Third-party clones are gitignored. Re-clone them when you want that tool:

```bash
cd ferramentas
git clone https://github.com/mvanhorn/last30days-skill.git
git clone https://github.com/SafeMantella/Pytho-inator.git
chmod +x Pytho-inator/pytho-inator
```

Pytho-inator maps a repeated task to one local Python CLI. After onboarding, the agent suggests that CLI at the end of a task. Nothing is built until you say yes.

Session files and browser exports stay out of git. See `.gitignore`.

Onboarding runs the install check for every tool you set to yes. A failed check does not finish onboarding.

## Rules for every agent

- Do not publish, build in Canva, or render a full-resolution video without an explicit yes.
- Do not store project memory outside `memory/`.
- Do not switch Notion or Canva off because a login failed. Stop and ask.
- Corrections that are reusable preferences get saved in `memory/` immediately.

## Quick check

```bash
python3 onboarding/test_leak_check.py
python3 onboarding/leak_check.py . --wordlist /path/to/wordlist.txt
```

The second command needs a wordlist that is not part of this repository. With no wordlist, it still checks for home paths, emails, and live Notion or Canva URLs.
