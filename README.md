# Social media agent

An empty system for one creator. The first time a coding agent opens this folder, it runs onboarding and fills the brand, the platforms, and the tools. After that, the pipelines are the way of working.

`AGENTS.md` is the entry file. `CLAUDE.md` points at it.

## 1. First open

Open the folder in your coding agent and say you are here. If `memory/config.md` says `status: empty`, the agent interviews you. One question at a time. Answer all of them. `status: ready` is the end of onboarding.

System files stay in English. The agent talks in the language you use. Posts, scripts, and captions are written in the content language you chose.

## 2. What is here

| Path | Role |
|---|---|
| `AGENTS.md` | Rules. Read on every open. |
| `onboarding/interview.md` | The first-run interview. |
| `memory/` | Decisions, pipelines, and the brand once onboarding fills it. Start at `memory/project_social_media_status.md`. |
| `estrategia/` | Strategy docs. Long guides are stubs in this version. |
| `.claude/skills/` | SOPs the agent loads. |
| `.claude/commands/` | Workflows. Ask the agent to read the file and follow it. |
| `ferramentas/` | Local tools. |
| `conteudo/` | Canonical pieces when storage is markdown. |
| `referencia/pesquisas/` | Research output. |
| `freebies/` | One folder per lead magnet, from the mold in `freebies/README.md`. |
| `gravações/` | Local video input. Gitignored. Empty in the template. |

Notion and Canva are optional. Onboarding records which one you use. Markdown in `conteudo/` is the fallback.

## 3. Requirements

macOS is what the scripts were written for. Python 3.10+, ffmpeg, git, and Node are the base.

```bash
brew install python@3.13 node ffmpeg git
```

Whisper is required only if onboarding chose local transcription. ElevenLabs is required only if onboarding chose it. The secret stays in the environment as `ELEVENLABS_API_KEY`.

Video edits expect a local video skill that can transcribe, cut, and render, installed where your agent loads skills. The pipeline names that skill `local-video-use`.

## 4. Accounts and cost

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

## 5. Local tools

Each tool has a README in its folder. Third-party clones are gitignored. Re-clone them when you want that tool:

```bash
cd ferramentas
git clone https://github.com/mvanhorn/last30days-skill.git
```

Session files and browser exports stay out of git. See `.gitignore`.

Onboarding runs the install check for every tool you set to yes. A failed check does not finish onboarding.

## 6. Rules for every agent

- Do not publish, build in Canva, or render a full-resolution video without an explicit yes.
- Do not store project memory outside `memory/`.
- Do not switch Notion or Canva off because a login failed. Stop and ask.
- Corrections that are reusable preferences get saved in `memory/` immediately.

## 7. Quick check

```bash
python3 onboarding/test_leak_check.py
python3 onboarding/leak_check.py . --wordlist /path/to/wordlist.txt
```

The second command needs a wordlist that is not part of this repository. With no wordlist, it still checks for home paths, emails, and live Notion or Canva URLs.
