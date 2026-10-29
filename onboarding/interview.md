# Onboarding interview

Follow this on the first open, and whenever `memory/config.md` is not `ready`.

Ask one question at a time. Question 1 chooses the language. Ask it in the language the creator is already writing in. From question 2 on, ask and write in `content_language`. Keep the creator's own words for their niche, promise, voice samples, and bios. Folder names stay as they are until the language command, which runs once after the readback.

Write each answer immediately, then ask the next unanswered question. If the creator answers several questions in one message, write what is already clear and ask only what is missing. If an answer is vague, reflect it in one sentence and wait for a yes before writing. If a new answer contradicts an earlier one, the file keeps the new answer.

Skipping a question does not finish onboarding. Say why the answer is required and ask again.

Remove the line `FILL VIA ONBOARDING` from a section when you replace it. `status: ready` is forbidden while that marker remains in a brand file.

## Questions

1. Language. One language for the whole system and for posts, scripts, captions, and hooks. Write `content_language` in `memory/config.md`. Then ask question 2. Do not rename folders yet.

### Workspace first (questions 1a and 1b)

Ask these right after question 1, in `content_language`, before the brand name. They decide how every later step reaches the creator's accounts.

1a. Claude in Chrome. This is the browser extension that lets the agent work in the creator's own logged-in Chrome: open a profile that needs a login, read a live post, click through Notion or Canva, check that something published. With it, many steps need no cookie export and no API key. Without it, the agent can only read public pages and ask for session files. Teach it in four lines, encourage it, then ask permission:

- What it does for this toolkit: profile reads, research on logged-in sites, checking published posts, Notion and Canva when there is no connector, forms and dashboards that have no API.
- What it can see: only the tabs it opens or is given, in the browser profile where the extension is installed. It asks before sensitive actions, and the agent here never publishes, pays, or sends without an explicit yes.
- How to install, if the creator says yes: Chrome from `google.com/chrome` if missing, then the extension "Claude in Chrome" from the Chrome Web Store, signed in with the same Claude account as the agent. In Claude Code, run `/chrome` to connect it (or start with `claude --chrome`). Another agent: say it needs a browser connector and skip to `no`.
- Test: with the extension on, the agent opens a new tab on a public URL the creator picks and reads the title. Only a passing test writes `claude_in_chrome: yes`. A failed test is retried once, then offered again at a later task. It does not block `ready`.

A no is allowed. Say once what they lose, write `claude_in_chrome: no`, and move on. Never install anything on the creator's machine without their yes.

1b. Tools they already use. Ask which tools they use today for each job: notes and ideas, design, video editing, scheduling, analytics, transcription, DMs, files. Offer examples, never a menu to pick from. For each tool, the agent decides how to connect, in this order: a connector or MCP server already installed (check `claude mcp list`), a command-line tool, Claude in Chrome, or a manual file the creator drops in. Write the result in `memory/ferramentas-existentes.md`. The rule is to integrate, not to replace: the creator keeps their tool, and the toolkit's own tool only fills a job that has none. If the list includes Notion or Canva, propose `storage: notion` or `carousel: canva` at questions 16 and 17. If it names a tool with no way in, say so and record it as `manual`.

1c. Express or full. Say what each costs. **Express** gets to `ready` with the core: brand, profile references, voice, visuals, platforms, storage, and carousel. Every optional integration (`last30days`, `reddit`, `instagram_research`, `grok_image`, `dm_automation`, `behind_the_scenes`) is written as `no`, and the heavy install of `transcription` waits for the first video task. They are turned on later with `/ativar-ferramenta`. **Full** asks every question below. Recommend express when the creator has not published a video through this system yet. Write the choice in `memory/ferramentas-existentes.md` under "Mode".

Then ask whether any job repeats for them every week that no tool covers. Do not build anything now. Write it in the same file under "Repeated jobs". After `ready`, `ferramentas/Pytho-inator/pytho-inator` is how those jobs become one local CLI each (see `.claude/skills/pytho-inator/SKILL.md`).

2. Brand name. Write `brand_name` and the Brand name section of `estrategia/01-posicionamento-e-pilares.md`, in `content_language`.

3. Already publishing? Yes or no. Write `existing_content` in `memory/config.md`. `no` skips question 4 and the profile read.

4. Profiles where they are most active. Ask only if question 3 is yes. At least one public URL. Write the URLs in `referencia/perfil-atual/fontes.md` immediately. A profile that cannot be opened is dropped, and the list has to be confirmed again. The list cannot end empty unless they change question 3 to `no`.

4b. Three specific posts. Ask only if question 3 is yes. Ask the creator to paste the links of three posts or videos that show their work best: for example one that performed, one that is typical, and one they are proud of. Tell them to open the profile, tap the post, and copy the link. Do not choose the posts yourself. Write the three links under a `Posts` heading in `referencia/perfil-atual/fontes.md` immediately, with one line on why each was picked if they say. A link that does not open is asked for again. If they refuse, say once that the read will be weaker, take the three newest public pieces, and record in the notes that the creator did not choose them.

## Machine check

Run this before the profile read, because that read needs `yt-dlp`, `ffmpeg`, and a transcription engine. Run `/doctor` (`ferramentas/verificar-ambiente/verificar-ambiente`) and fix what it lists before asking the next question.

- **No password path first.** Do not assume Homebrew and do not assume a recent Python. When something is missing, propose installing it in the creator's user folder (`~/.local/bin`, with `uv` for Python tools) and ask for a yes. Homebrew is the optional route, and the creator runs its installer themselves because it asks for their password.
- **Say size and time before a heavy download.** Local transcription models are several GB and take minutes. Check free disk first (`/doctor` wants 30 GB). If the disk is nearly full, say so and let the creator free space before you start.
- **`yt-dlp` must be current.** An old version is refused by YouTube. Upgrade it when `/doctor` says it is over 90 days old.
- **A fresh terminal may not see a new `PATH`.** Give the full path to a command you just installed (for example `~/.local/bin/yt-dlp`).
- **One command at a time, and say where to run it.** If the creator must run something (a login, a cookie export), say which app (Terminal, not this chat), what they will see, and what to tell you afterwards. Never ask for a directory listing or other broad output. Ask for the narrowest output that answers the question.
- **Which browser holds the login?** Run `ferramentas/detectar-sessao/detectar-sessao "<one of their post links>"` in their Terminal. It tries each installed browser and exports the cookie file from the one that works, so do not assume Chrome and do not write a cookie-export command by hand. Warn once that the exported file holds the sessions of every site in that browser, stays outside the folder and outside git, and is not to be shared.

## Profile read

Do this after question 4, before question 5, whenever `existing_content` is `yes`. Skipping it does not finish onboarding. If the conversation stops, resume here before any later question.

Open every URL in `referencia/perfil-atual/fontes.md`. Read the public page. Do not invent a view you did not open. Record a gap in the notes when a step fails. Never write a home-directory path, a session-file path, or a secret into the notes.

For each profile, read the bio, the highlights or featured items, and anything pinned. Then read the pieces below.

**Instagram, and any profile whose grid is short video.** Read the three posts the creator named in question 4b, not the first three in the grid. Still open the grid and say what a visitor sees first and which items are pinned, so the creator hears the gap between what they picked and what a stranger meets.

For each of those videos:

- Save the full caption.
- Download and transcribe with `ferramentas/instagram-transcript/instagram_transcript.py`. Pass `--language auto`. Instagram and TikTok need a session file that stays outside git. The tool README says how to export it. Ask once. If that file already exists, do not ask again. The same file can satisfy question 21 later. If they will not provide it, keep the caption, mark the transcript as a gap, and do not pretend you heard the audio.
- Print frames with `ferramentas/prep-frames/prep-frames` on the downloaded file. Read `resumo.md` and the contact sheet. Note the hook frame, on-screen text, cut rhythm, face, color, and music when the picture shows them.
- Write `referencia/perfil-atual/<platform>/<id>.md` with the URL, the full caption, the transcript, and what the frames show. The video file stays in the tool's download folder and is gitignored. Frame images under `referencia/perfil-atual/` are gitignored. The markdown is the record that remains.
- Append the opener to `referencia/swipe-openers.md`: the first on-screen line, and the first spoken sentence when there is speech. Copy them. Do not invent a line. Remove the "None yet" line once a real opener is there. The sprint later fills this file out to 15–20 lines. These three start it.

**Other platforms.** Open the page. Read the posts named in question 4b. If none was named for this platform, take the three newest public pieces. A video gets a transcript when the same tool accepts the URL, plus frames when a file was downloaded. A text post gets the full text. A channel or a list gets the bio and those three pieces, not the whole archive.

Then write `referencia/perfil-atual/RESUMO.md`. Cover what repeats across the pieces, what changes, and a draft of niche, audience, promise, pillars, voice, and visual system. Include an edit recipe: how the open works, how dense the cut is, how text sits on screen, whether a face is present, and what the caption is doing.

Show that recipe to the creator. Before asking them to keep or change it, say two sentences from the frames and the transcript, and write both into `referencia/perfil-atual/RESUMO.md` under `Hold` and `Drop`:

- **Hold.** What in this edit gives a stranger a reason to stay.
- **Drop.** What in the first seconds gives them a reason to leave.

Then ask. Write `memory/edicao-observada.md` with `decision: keep` or `decision: change`, and copy the two sentences into that file. `keep` means later videos match the recipe unless they correct it. `change` means the recipe is context only. The next questions decide the new system. Do not fill a brand file from the read alone. Do not ask for the decision before the two sentences have been said.

`status: ready` is forbidden while `existing_content` is `yes` and either `referencia/perfil-atual/RESUMO.md` is missing or `memory/edicao-observada.md` has no decision line.

## Questions, continued

When the profile read exists, questions 5 through 13 are proposals. State what the pages support, in one sentence, and wait for a yes or a correction. Write only the confirmed version.

5. Niche, in one sentence. Write the Niche section of `estrategia/01`.

6. Audience, in up to three lines. Write the Audience section.

7. Promise to a follower. Write the Promise section.

8. Current goal. One of: growth, leads, sales, authority. Write the Goal section.

9. What the brand never does. Write the Never do section.

10. Pillars, three to six. Propose a set from the niche and from the pieces you read. Let the creator correct it. Fewer than three does not finish. Write the Pillars section.

11. Voice, one guide per surface. People talk, caption, and put text on screen in different ways. Write `memory/estilo-de-escrita/guia-voz.md` with three sections: Spoken, Caption, On-screen text. Rules learned from a transcript go under Spoken only. Do not apply them to a caption until the creator confirms them there; ask for a real caption they like and propose the Caption rules from it. If captions or a transcript exist, propose testable rules from them (person, sentence length, punctuation, words they avoid) and ask for a correction. Mark every inferred rule `(inferred)` until the creator edits or confirms it. Never write an opinion for the creator: a rule may say how they voice an opinion, never what the opinion is. If there is no read, ask for a sample or a description of how they speak. Put the sample, or the caption excerpts they confirm, in `memory/estilo-de-escrita/exemplos.md`.

12. Face on camera: yes or no. If the videos show a face, propose yes. Write `face` in `memory/config.md`, the Face section of `estrategia/00-identidade-visual.md`, and a one-line note at the top of `memory/feedback-video-editing-pipeline.md` under the existing face heading if you add one. Do not change the pipeline order.

13. Visual system. Propose palette and type from the frames and the grid when you saw them. Otherwise build a simple default with them. A default still has to end as a written palette and type. A logo, if they have one, goes in `estrategia/marca/`. Write `estrategia/00-identidade-visual.md` and `memory/visual_identity_standard.md`.

14. Platforms they will actually publish on. At least one. The profiles already read are the starting list, not the whole list. Write the platform list in `memory/social_media_handles.md`.

15. Handle and bio for every platform on that list. Confirm a handle you already saw instead of asking from scratch. A platform without an account comes off the list. The list cannot end empty. Write handles and bios in `memory/social_media_handles.md`.

16. Where the work lives: Notion (`storage: notion`) or markdown in `conteudo/` (`storage: md`). Notion finishes only when the database links are in `estrategia/02-arquitetura-notion.md`. Walk them through creating the databases if they do not have them. Markdown replaces the `FILL VIA ONBOARDING` marker in that file with a line that says the canonical store is `conteudo/`.

17. Carousel: how it gets built. Recommend `claude` (Claude's own design tools: HTML slides at 1080×1350, reviewed as a private Artifact, nothing to install). Offer `hyperframes` for creators who want motion-graphics-grade slides and are willing to install the HyperFrames plugin. Say that installing it is their choice, ask permission, and tell them to install it with `/plugin`. Check that the `hyperframes` skills answer before writing the key. Offer `md` for the plan only. Write `carousel`. Canva is not offered. Replace the markers in `estrategia/marca/ids.md` with a line that says Canva is not used. If the creator named Canva in question 1b, record it as `manual` in `memory/ferramentas-existentes.md` and say that the toolkit builds carousels with `claude` or `hyperframes`.

**Tool switches (questions 19 to 24).** In full mode, present them as one table with the recommendation for each row and the cost or risk in a few words. The creator answers "accept" or changes rows. This is the one exception to one question at a time. "Do as you prefer", "yes to all", or "accept" counts as the recommended value for a row, never as a yes to a risky one. A row is **risky** when it can limit or ban an account or bills money: `reddit: auto`, `instagram_research: yes` (queries leave from their own account), `grok_image: yes` (billed per image), and `dm_automation: yes`. For a risky row the creator must type the tool name (for example `reddit auto`) after hearing the risk. Anything else keeps the conservative value.

18. Transcription: local whisper or ElevenLabs. Whisper finishes only when the install check succeeds. ElevenLabs finishes only when `ELEVENLABS_API_KEY` is set in the environment. Never write the secret into a file. Write `transcription`. The profile read may already have used local transcription. That does not answer this question.

19. last30days: yes or no. Yes finishes only when the install check succeeds. Write `last30days`.

20. Reddit: no, manual, or auto. Auto includes this warning, in their language: Reddit's terms prohibit automation, and the account can be limited or banned. Auto finishes only when a login in the tool's own browser profile has succeeded. Write `reddit`.

21. Instagram research via a browser session file: yes or no. Yes finishes only when the session file exists outside git. A session file already used in the profile read counts. Write `instagram_research`.

22. Image generation via Grok: yes or no. Say that each image is billed by xAI. Yes finishes only when authentication exists outside the repository. Write `grok_image`.

23. Instagram DM automation. Ask only if Instagram is on the platform list. Otherwise write `dm_automation: no`. The supported tool is PilotDM. Yes writes `memory/dm-automation.md` with a trigger word in capitals and no accent, plus the first message and the second message, and finishes only when the creator confirms the account is set up with those three values. Write `dm_automation`.

24. Recurring behind-the-scenes series: yes or no. The workflow file stays in the repo. `no` leaves `.claude/commands/registrar-bastidores.md` dormant. `yes` does not create the series page during onboarding. Write `behind_the_scenes`.

25. Who writes the script: the creator, or the agent? Creator writes `writes_scripts: yes`. Agent writes `writes_scripts: no`. When it is `yes`, research comes back as checked facts, angles, and sources, with no spoken lines, no script table, no hook, and no caption, until they explicitly ask for a script. See `memory/feedback-so-a-peca-pedida.md`.

26. Read back, with a table of each tool and whether the capability the creator will use was actually tested and works (for example: Instagram research, hashtag search works, profile and comment reads do not), niche, audience, promise, pillars, platforms, handles, storage, carousel, tools, the series choice, who writes the script, whether they already publish, and the keep-or-change decision. Apply corrections. Then follow `.claude/commands/aplicar-idioma.md`. Set `files_language` only when `python3 onboarding/language_paths.py check` prints `ok`. Then set `status: ready`. A failed check does not finish onboarding.

## Install checks

`no`, and Reddit `manual`, do not need an install. These do, before `ready`:

- Pytho-inator mod, Claude Code only: ask permission, then run the two `claude plugin` commands from the Automation section of `AGENTS.md`. A no is fine; the agent then runs `glance` by hand after tasks. Never run `glance` during onboarding.
- `claude_in_chrome: yes` — the agent opened a tab through the extension and read its title
- `transcription: whisper` — the local whisper command runs
- `transcription: elevenlabs` — `ELEVENLABS_API_KEY` is set in the environment
- `last30days: yes` — the tool's setup command finishes
- `reddit: auto` — login in the tool profile finishes
- `instagram_research: yes` — session file present and gitignored
- `grok_image: yes` — authentication present outside the repo
- `dm_automation: yes` — `memory/dm-automation.md` is complete and the creator confirms PilotDM

Test the capability the creator will use, not that the command starts. Before asking the creator to log in to a tool that opens a browser, launch it yourself once (`/doctor` does this for `reddit-answers`). A login the creator does on a broken build is a failure you caused. For a tool that degrades (a second transcription engine missing, only some Instagram reads working), write what works and what does not in the readback.

When a check runs, fill `memory/ambiente-maquina.md` with what this machine actually has: binaries that exist but are not on `PATH`, the system Python version, which virtualenv runs each tool, and collectors that need Python 3.12 (`uv run --no-project --python 3.12`). After a virtualenv update, reinstall the patchright browser and record the command that worked. Do not invent a path. Do not copy that note into any other file.

A failed install does not get marked ready. Retry, or the creator changes that tool to `no` (or Reddit to `manual`).
