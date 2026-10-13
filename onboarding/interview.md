# Onboarding interview

Follow this on the first open, and whenever `memory/config.md` is not `ready`.

Ask one question at a time. Question 1 chooses the language. Ask it in the language the creator is already writing in. From question 2 on, ask and write in `content_language`. Keep the creator's own words for their niche, promise, voice samples, and bios. Folder names stay as they are until the language command, which runs once after the readback.

Write each answer immediately, then ask the next unanswered question. If the creator answers several questions in one message, write what is already clear and ask only what is missing. If an answer is vague, reflect it in one sentence and wait for a yes before writing. If a new answer contradicts an earlier one, the file keeps the new answer.

Skipping a question does not finish onboarding. Say why the answer is required and ask again.

Remove the line `FILL VIA ONBOARDING` from a section when you replace it. `status: ready` is forbidden while that marker remains in a brand file.

## Questions

1. Language. One language for the whole system and for posts, scripts, captions, and hooks. Write `content_language` in `memory/config.md`. Then ask question 2. Do not rename folders yet.

2. Brand name. Write `brand_name` and the Brand name section of `estrategia/01-posicionamento-e-pilares.md`, in `content_language`.

3. Already publishing? Yes or no. Write `existing_content` in `memory/config.md`. `no` skips question 4 and the profile read.

4. Profiles where they are most active. Ask only if question 3 is yes. At least one public URL. Write the URLs in `referencia/perfil-atual/fontes.md` immediately. A profile that cannot be opened is dropped, and the list has to be confirmed again. The list cannot end empty unless they change question 3 to `no`.

## Profile read

Do this after question 4, before question 5, whenever `existing_content` is `yes`. Skipping it does not finish onboarding. If the conversation stops, resume here before any later question.

Open every URL in `referencia/perfil-atual/fontes.md`. Read the public page. Do not invent a view you did not open. Record a gap in the notes when a step fails. Never write a home-directory path, a session-file path, or a secret into the notes.

For each profile, read the bio, the highlights or featured items, and anything pinned. Then read the pieces below.

**Instagram, and any profile whose grid is short video.** Take the first three videos a visitor sees. A pinned video counts when it sits in those cells. Say which ones are pinned. If a cell is not a video, write down its caption and what the picture shows, then keep going down the grid until there are three videos or the grid runs out.

For each of those videos:

- Save the full caption.
- Download and transcribe with `ferramentas/instagram-transcript/instagram_transcript.py`. Pass `--language auto`. Instagram and TikTok need a session file that stays outside git. The tool README says how to export it. Ask once. If that file already exists, do not ask again. The same file can satisfy question 21 later. If they will not provide it, keep the caption, mark the transcript as a gap, and do not pretend you heard the audio.
- Print frames with `ferramentas/prep-frames/prep-frames` on the downloaded file. Read `resumo.md` and the contact sheet. Note the hook frame, on-screen text, cut rhythm, face, color, and music when the picture shows them.
- Write `referencia/perfil-atual/<platform>/<id>.md` with the URL, the full caption, the transcript, and what the frames show. The video file stays in the tool's download folder and is gitignored. Frame images under `referencia/perfil-atual/` are gitignored. The markdown is the record that remains.
- Append the opener to `referencia/swipe-openers.md`: the first on-screen line, and the first spoken sentence when there is speech. Copy them. Do not invent a line. Remove the "None yet" line once a real opener is there. The sprint later fills this file out to 15–20 lines. These three start it.

**Other platforms.** Open the page. Take the three newest public pieces. A video gets a transcript when the same tool accepts the URL, plus frames when a file was downloaded. A text post gets the full text. A channel or a list gets the bio and those three pieces, not the whole archive.

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

11. Voice. If captions or a transcript exist, propose testable rules from them (person, sentence length, punctuation, words they avoid) and ask for a correction. If there is no read, ask for a sample or a description of how they speak. Write `memory/estilo-de-escrita/guia-voz.md` and put the sample, or the caption excerpts they confirm, in `memory/estilo-de-escrita/exemplos.md`.

12. Face on camera: yes or no. If the videos show a face, propose yes. Write `face` in `memory/config.md`, the Face section of `estrategia/00-identidade-visual.md`, and a one-line note at the top of `memory/feedback-video-editing-pipeline.md` under the existing face heading if you add one. Do not change the pipeline order.

13. Visual system. Propose palette and type from the frames and the grid when you saw them. Otherwise build a simple default with them. A default still has to end as a written palette and type. A logo, if they have one, goes in `estrategia/marca/`. Write `estrategia/00-identidade-visual.md` and `memory/visual_identity_standard.md`.

14. Platforms they will actually publish on. At least one. The profiles already read are the starting list, not the whole list. Write the platform list in `memory/social_media_handles.md`.

15. Handle and bio for every platform on that list. Confirm a handle you already saw instead of asking from scratch. A platform without an account comes off the list. The list cannot end empty. Write handles and bios in `memory/social_media_handles.md`.

16. Where the work lives: Notion (`storage: notion`) or markdown in `conteudo/` (`storage: md`). Notion finishes only when the database links are in `estrategia/02-arquitetura-notion.md`. Walk them through creating the databases if they do not have them. Markdown replaces the `FILL VIA ONBOARDING` marker in that file with a line that says the canonical store is `conteudo/`.

17. Carousel: Canva (`carousel: canva`) or markdown (`carousel: md`). Canva finishes only when the master template id is in `estrategia/marca/ids.md`. Walk them through duplicating a blank master if they do not have one. Markdown replaces the markers in `estrategia/marca/ids.md` with a line that says Canva is not used.

18. Transcription: local whisper or ElevenLabs. Whisper finishes only when the install check succeeds. ElevenLabs finishes only when `ELEVENLABS_API_KEY` is set in the environment. Never write the secret into a file. Write `transcription`. The profile read may already have used local transcription. That does not answer this question.

19. last30days: yes or no. Yes finishes only when the install check succeeds. Write `last30days`.

20. Reddit: no, manual, or auto. Auto includes this warning, in their language: Reddit's terms prohibit automation, and the account can be limited or banned. Auto finishes only when a login in the tool's own browser profile has succeeded. Write `reddit`.

21. Instagram research via a browser session file: yes or no. Yes finishes only when the session file exists outside git. A session file already used in the profile read counts. Write `instagram_research`.

22. Image generation via Grok: yes or no. Say that each image is billed by xAI. Yes finishes only when authentication exists outside the repository. Write `grok_image`.

23. Instagram DM automation. Ask only if Instagram is on the platform list. Otherwise write `dm_automation: no`. The supported tool is PilotDM. Yes writes `memory/dm-automation.md` with a trigger word in capitals and no accent, plus the first message and the second message, and finishes only when the creator confirms the account is set up with those three values. Write `dm_automation`.

24. Recurring behind-the-scenes series: yes or no. The workflow file stays in the repo. `no` leaves `.claude/commands/registrar-bastidores.md` dormant. `yes` does not create the series page during onboarding. Write `behind_the_scenes`.

25. Read back niche, audience, promise, pillars, platforms, handles, storage, carousel, tools, the series choice, whether they already publish, and the keep-or-change decision. Apply corrections. Then follow `.claude/commands/aplicar-idioma.md`. Set `files_language` only when `python3 onboarding/language_paths.py check` prints `ok`. Then set `status: ready`. A failed check does not finish onboarding.

## Install checks

`no`, and Reddit `manual`, do not need an install. These do, before `ready`:

- `transcription: whisper` — the local whisper command runs
- `transcription: elevenlabs` — `ELEVENLABS_API_KEY` is set in the environment
- `last30days: yes` — the tool's setup command finishes
- `reddit: auto` — login in the tool profile finishes
- `instagram_research: yes` — session file present and gitignored
- `grok_image: yes` — authentication present outside the repo
- `dm_automation: yes` — `memory/dm-automation.md` is complete and the creator confirms PilotDM

A failed install does not get marked ready. Retry, or the creator changes that tool to `no` (or Reddit to `manual`).
