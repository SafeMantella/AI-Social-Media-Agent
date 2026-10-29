# Social media agent

A toolkit that lets a coding agent help one creator plan, write, edit, and publish social-media content. The folder ships empty. You open it with your agent, answer an interview, and it becomes your system: your brand, your platforms, your tools, your way of working.

Português (Brasil): [README.pt-BR.md](README.pt-BR.md)

`AGENTS.md` is the entry file every agent reads. `CLAUDE.md` points at it. Claude Code is the agent this toolkit is built and tested with.

## What you get

- **An onboarding interview** that writes your niche, audience, promise, pillars, voice, visual identity, platforms, and handles into files. If you already publish, it reads your profiles first and proposes from what it saw.
- **Pipelines** with a fixed order (interview, research, write, approval, build) for scripts, hooks, carousels, video edits, research, transcription, and pre-publish review.
- **Integrations with what you already use.** Onboarding asks which tools you have (Notion, an editor, a scheduler) and connects to them. It does not replace them.
- **Claude in Chrome**, so the agent can work inside your own logged-in browser. See below.
- **Local tools**, one folder each in `ferramentas/` (transcription, silence cutting, contact sheets, keyword mining, uploads, and more). A generated skill, `catalogo-ferramentas`, lists every tool and what it does, so the agent finds the right one. Owned tools live in public repositories and stay updatable.
- **Pytho-inator**, which turns any task you repeat into one local Python command. This is how the toolkit grows with you.
- **An update routine.** `/update-toolkit` checks this template and every tool repository and records when it last did.

## Install, step by step

1. **Get the folder.** Either clone it, or download the zip from the repository page (Code, then Download ZIP) and unzip it somewhere you will keep it.
   ```bash
   git clone https://github.com/SafeMantella/AI-Social-Media-Agent.git "my-social-media"
   ```
   A clone keeps `/update-toolkit` working with full history. A zip works too: the first update links it to the template.
2. **Install the base tools.** macOS is what the scripts were written for. See Requirements below (`brew install python@3.13 node ffmpeg git`).
3. **Install [Claude Code](https://claude.com/claude-code)** and sign in.
4. **Open the folder in Claude Code.** In a terminal: `cd my-social-media && claude`. In the desktop app or an IDE extension, open the folder as the project.
5. **Type `/onboarding` inside Claude Code.** That command is the whole setup. It clones what is missing, then asks you one question at a time and writes each answer into your files. Nothing else to paste or install first.
6. **Answer the interview.** The first question is the language of the whole system. Then it asks for your brand, whether you already publish (if so, the links of three posts you pick), your niche, voice, visuals, platforms, and handles. It also offers Claude in Chrome and asks which tools you already use. It asks your permission before installing anything. You choose **express** (the core only: brand, references, voice, visuals; integrations later with `/ativar-ferramenta`) or **full**. Before the profile read it runs `/doctor` and fixes what the machine lacks, without needing your password.
7. **Done when `memory/config.md` says `status: ready`.** Run `/doctor` to check the machine, then `/iniciar` to start working. If the chat stops halfway, open the folder again and type `/onboarding`: it resumes at the first unanswered question.

If you skip step 5 and just say hello, the agent still sees an empty setup and starts the interview.

The folders are renamed once, after the readback, into the language you chose, and only when `python3 onboarding/language_paths.py check` prints `ok`. The session-start checks (storage review, toolkit update, template report) are written in `AGENTS.md`.

## Claude in Chrome

Claude in Chrome is a browser extension that lets the agent work in your own Chrome, with your own logins. For this toolkit it covers what has no API: reading a profile that needs a login, researching behind a login, checking that a post is live, and clicking through Notion when no connector exists. Without it, the agent reads public pages only and asks you for session files.

Onboarding question 1a teaches it, asks your permission, installs it with you, and tests it:

1. Install Chrome if you do not have it.
2. Install the "Claude in Chrome" extension from the Chrome Web Store and sign in with the same Claude account as the agent.
3. In Claude Code, run `/chrome` to connect it (or start Claude Code with `claude --chrome`).
4. The agent opens a tab on a public URL and reads its title. Only a passing test sets `claude_in_chrome: yes`.

It is optional for `ready`, and you can say no. The agent never installs it without your yes, and never publishes, pays, or sends anything through it without your yes. Browser policy (cheapest route first, screenshots last): `memory/regras-execucao-robusta.md`.

## How the day-to-day works

1. `/iniciar` recalls what is pending, in five lines.
2. You name a piece. The agent reads the pipeline for that task and follows its order.
3. Research uses only the tools you turned on. A tool set to `no` becomes a recorded gap, not a silent skip.
4. Writing goes to the canonical store (Notion or `conteudo/`). You approve. Then the agent builds.
5. Nothing is published, exported as a carousel, or rendered at full resolution without an explicit yes.
6. At the end of a task that created files, Pytho-inator may offer one local CLI for the repeated work. Nothing is built without your yes.

## Commands

Type these in Claude Code, or ask any other agent to read the file and follow it. `COMANDOS.md` is the generated manual (`/comandos`).

| Command | What it does |
|---|---|
| `/onboarding` | The whole setup. Type it once after opening the folder |
| `/doctor` | Check the machine against your config and say what is missing |
| `/ativar-ferramenta` | Turn on an optional integration later, with its install and test |
| `/learn-from-edit` | Paste your own version of a draft and the system learns your rules from the difference |
| `/exportar-sessao` | Save this conversation as Markdown (personal strings masked), only when you ask |
| `/iniciar` | Open a session: what is pending, in five lines |
| `/carousel` | Build a carousel: interview, research, plan, approval, then build with Claude's design tools or HyperFrames |
| `/pesquisar` | Research a subject, profile, or piece with the tools you enabled |
| `/update-toolkit` | Check the template and every tool repository, update what is behind, record the dates |
| `/atualizar-ferramentas` | Only the tool repositories |
| `/atualizar-do-git` | Only the template |
| `/revisar-armazenamento` | Measure the folder and propose what to move. Nothing moves without your approval |
| `/reportar-evolucao` | Draft a sanitized report of what you changed, for the template. Publishes nothing until you approve the text |
| `/revisar-video`, `/edicao`, `/avaliar-edicao`, `/refinar-overlay` | Video review and edit loop |
| `/sugerir-conteudo` | Content ideas from the work of the session |
| `/registrar-bastidores` | Behind-the-scenes series, only when you turned it on |
| `/atualizar-memoria` | Save decisions and corrections from this session in `memory/` |
| `/map-automation-opportunities`, `/check-skills` | Where Pytho-inator can shrink a workflow to one command |
| `/aplicar-idioma` | Runs once, after onboarding |
| `/comandos` | Regenerate and show the manual |

## What is here

| Path | Role |
|---|---|
| `AGENTS.md` | Rules. Read on every open |
| `onboarding/` | The interview, the language path check, and the leak check |
| `memory/` | Config, decisions, pipelines, and the brand once onboarding fills it. Start at `memory/INDEX.md` |
| `estrategia/` | Strategy guides (the method). Brand files stay blank until onboarding |
| `.claude/commands/`, `.claude/skills/` | Workflows and SOPs, shared by every agent |
| `ferramentas/` | Local tools |
| `conteudo/` | Canonical pieces when storage is markdown |
| `referencia/pesquisas/` | Research output |
| `referencia/perfil-atual/` | What onboarding read from profiles you already publish |
| `freebies/` | One folder per lead magnet |
| `gravações/` | Local video input. Gitignored |
| `COMANDOS.md` | Generated manual of commands and skills |

Folder names are the template's. The language pass renames the ones you see (for example `estrategia` to `strategy`), and the paths in the files follow.

## Tools

Each tool is one folder with a README. The agent reads the generated catalog (`.claude/skills/catalogo-ferramentas/SKILL.md`), which `ferramentas/manual-comandos/gerar` rewrites whenever you add, remove, or rename a tool folder. The owned tools are symlinks into six public repositories cloned under `ferramentas/_repos/`. The code is not tracked here, so a tool update never dirties your copy. Details and the clone commands: `memory/ferramentas-repos.md`.

| Repository | Tools |
|---|---|
| [token-kit](https://github.com/SafeMantella/token-kit) | `prep-frames`, `prep-texto`, `token-saver`: read a video or a big file without spending tokens |
| [video-cut-pipeline](https://github.com/SafeMantella/video-cut-pipeline) | `corte-silencio`, `evals`, `evals-edicao`: silence and retake cutting, and the manual cut review |
| [transcrever-ptbr](https://github.com/SafeMantella/transcrever-ptbr) | `transcrever`: local transcription with two engines and a check for dropped speech |
| [video-tools](https://github.com/SafeMantella/video-tools) | `video-camadas`, `slides-pdf`: text behind the person, HTML slides to PDF |
| [social-toolbox](https://github.com/SafeMantella/social-toolbox) | `keyword-mining`, `minerar-hooks`, `pdf-to-markdown`, `grokbot`, `links`, `extrair-audio`, `grok-imagem` |
| [sau-tools](https://github.com/SafeMantella/sau-tools) | `sau-yt`, `sau-tiktok`: upload to YouTube (private by default) and TikTok, only on your yes |

Other clones live directly under `ferramentas/` and are gitignored: [Pytho-inator](https://github.com/SafeMantella/Pytho-inator), [Adobe Podcast for Claude Code](https://github.com/SafeMantella/Adobe-Podcast-for-Claude-Code), [Fontastic](https://github.com/SafeMantella/Fontastic-Text-Image-Generator), and third-party tools ([last30days-skill](https://github.com/mvanhorn/last30days-skill), [social-auto-upload](https://github.com/dreammis/social-auto-upload), [ln](https://github.com/fogleman/ln)). Small wrappers that are tracked here: `adobe-enhance`, `reddit-answers`, `instagram-transcript`, `buscar-imagens`, `montar-lista`, `looks-take`, `faixa-legenda`, `manual-comandos`, `atualizar-ferramentas`, `verificar-ambiente`, `checar-legenda`, `detectar-sessao`, `audio-do-reel`, `exportar-sessao`, and the wrappers of `minet` and `scrapling` (their virtualenvs are local). `editonny` is a vendored slice of a motion skill. `separar-voz` is only a virtualenv.

Clone the loose ones when onboarding asks, or by hand:

```bash
cd ferramentas
git clone https://github.com/mvanhorn/last30days-skill.git
git clone https://github.com/SafeMantella/Pytho-inator.git && chmod +x Pytho-inator/pytho-inator
git clone https://github.com/SafeMantella/Fontastic-Text-Image-Generator.git fontastic-text-image-generator
git clone https://github.com/SafeMantella/Adobe-Podcast-for-Claude-Code.git adobe-podcast
git clone https://github.com/dreammis/social-auto-upload.git
git clone https://github.com/fogleman/ln.git
```

Session files, cookies, `.env`, and browser profiles stay out of git. See `.gitignore`.

## Pytho-inator

[Pytho-inator](https://github.com/SafeMantella/Pytho-inator) maps a task you repeat to one local Python command, so the agent runs one line and reads the last line of output instead of re-explaining the steps every time. It is how you add tools to this toolkit.

- Onboarding asks which jobs you repeat each week and records them in `memory/ferramentas-existentes.md`.
- After onboarding, at the end of a task that created files, it may offer one CLI in at most three lines. You say yes or ignore it.
- A yes builds it with the ponytail skill at `ultra`, `uv` instead of system Python, and free open-source dependencies. A paid API or a first test run needs your yes.
- In Claude Code, an optional mod prints the offer under the answer. Onboarding asks before installing it.
- `/map-automation-opportunities` ranks what is worth automating. `/check-skills` shows which skills could shrink.

## Keeping it up to date

At the start of every session the agent reads `memory/toolkit-updates.md`. That file only records when the template and each tool repository were last checked. If anything is empty or older than seven days, the agent says so and asks to run `/update-toolkit`. A yes fetches, fast-forwards what is behind, and writes the dates. It never pushes, and a brand file you filled stays as you wrote it.

Two other routines run the same way and ask before doing anything: a weekly storage review (`memory/revisao-armazenamento.md`) and a monthly report of what you changed in the system, sent to the template only after you approve the exact text (`memory/evolucao-template.md`).

## Requirements

macOS is what the scripts were written for. Python 3.10+, ffmpeg, git, and Node are the base.

```bash
brew install python@3.13 node ffmpeg git
```

Whisper is needed only if onboarding chose local transcription. ElevenLabs is needed only if it chose that, and the key stays in the environment as `ELEVENLABS_API_KEY`. Video edits expect a local video skill that can transcribe, cut, and render, installed where your agent loads skills (the pipeline calls it `local-video-use`).

## Accounts and cost

| Item | When | Cost |
|---|---|---|
| Your coding agent | Always | Depends on that product |
| Claude in Chrome | If you turn it on | Needs a Claude plan that includes it. Check the extension page |
| Adobe account | Audio cleanup step | Free tier exists. Limits not re-verified here |
| Reddit account | If Reddit is manual or auto | Free. Auto is against Reddit's terms and can limit the account |
| ElevenLabs | If transcription is elevenlabs | Billed by ElevenLabs |
| xAI | If Grok image generation is yes | Billed per image |
| Notion | If storage is notion | Their plan |
| HyperFrames | If carousel is hyperframes, and for video overlays | Your choice to install. Check its page for cost |
| Canva | Only a legacy copy with carousel canva | Their plan |
| PilotDM | If Instagram DM automation is yes | Free tier exists |
| GitHub | To publish or share a tool | Their plan |

## Rules for every agent

- Do not publish, export a carousel, or render a full-resolution video without an explicit yes.
- Do not install anything on the creator's machine without their yes.
- Do not store project memory outside `memory/`.
- Do not switch Notion off because a login failed. Stop and ask.
- Corrections that are reusable preferences are saved in `memory/` immediately.
- Read the whole task, keep the step order, and show evidence before saying "done" (`memory/regras-execucao-robusta.md`).

## Check for leaks before you share

```bash
python3 onboarding/test_leak_check.py
python3 onboarding/leak_check.py . --wordlist /path/to/wordlist.txt
```

The second command needs a wordlist that is not part of this repository. Without one it still checks for home paths, emails, and live Notion or Canva URLs.
