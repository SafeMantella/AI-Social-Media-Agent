# Onboarding interview

Follow this on the first open, and whenever `memory/config.md` is not `ready`.

Ask one question at a time, in the language the creator is writing in. Write the system files in English. Keep the creator's own words for their niche, promise, voice samples, and bios.

Write each answer immediately, then ask the next unanswered question. If the creator answers several questions in one message, write what is already clear and ask only what is missing. If an answer is vague, reflect it in one sentence and wait for a yes before writing. If a new answer contradicts an earlier one, the file keeps the new answer.

Skipping a question does not finish onboarding. Say why the answer is required and ask again.

Remove the line `FILL VIA ONBOARDING` from a section when you replace it. `status: ready` is forbidden while that marker remains in a brand file.

## Questions

1. Content language. The language of posts, scripts, captions, and hooks. Write `content_language` in `memory/config.md`.

2. Brand name. Write `brand_name` and the Brand name section of `estrategia/01-posicionamento-e-pilares.md`.

3. Niche, in one sentence. Write the Niche section of `estrategia/01`.

4. Audience, in up to three lines. Write the Audience section.

5. Promise to a follower. Write the Promise section.

6. Current goal. One of: growth, leads, sales, authority. Write the Goal section.

7. What the brand never does. Write the Never do section.

8. Pillars, three to six. Propose a set from the niche and let the creator correct it. Fewer than three does not finish. Write the Pillars section.

9. Voice. Ask for a sample of their writing, or a description of how they speak. Extract testable rules (person, sentence length, punctuation, words they avoid). Write `memory/estilo-de-escrita/guia-voz.md` and put the sample in `memory/estilo-de-escrita/exemplos.md`.

10. Face on camera: yes or no. Write `face` in `memory/config.md`, the Face section of `estrategia/00-identidade-visual.md`, and a one-line note at the top of `memory/feedback-video-editing-pipeline.md` under the existing face heading if you add one. Do not change the pipeline order.

11. Visual system. Palette and type, or build a simple default with them. A default still has to end as a written palette and type. A logo, if they have one, goes in `estrategia/marca/`. Write `estrategia/00-identidade-visual.md` and `memory/visual_identity_standard.md`.

12. Platforms they will actually publish on. At least one. Write the platform list in `memory/social_media_handles.md`.

13. Handle and bio for every platform on that list. A platform without an account comes off the list. The list cannot end empty. Write handles and bios in `memory/social_media_handles.md`.

14. Where the work lives: Notion (`storage: notion`) or markdown in `conteudo/` (`storage: md`). Notion finishes only when the database links are in `estrategia/02-arquitetura-notion.md`. Walk them through creating the databases if they do not have them. Markdown replaces the `FILL VIA ONBOARDING` marker in that file with a line that says the canonical store is `conteudo/`.

15. Carousel: Canva (`carousel: canva`) or markdown (`carousel: md`). Canva finishes only when the master template id is in `estrategia/marca/ids.md`. Walk them through duplicating a blank master if they do not have one. Markdown replaces the markers in `estrategia/marca/ids.md` with a line that says Canva is not used.

16. Transcription: local whisper or ElevenLabs. Whisper finishes only when the install check succeeds. ElevenLabs finishes only when `ELEVENLABS_API_KEY` is set in the environment. Never write the secret into a file. Write `transcription`.

17. last30days: yes or no. Yes finishes only when the install check succeeds. Write `last30days`.

18. Reddit: no, manual, or auto. Auto includes this warning, in their language: Reddit's terms prohibit automation, and the account can be limited or banned. Auto finishes only when a login in the tool's own browser profile has succeeded. Write `reddit`.

19. Instagram research via a browser session file: yes or no. Yes finishes only when the session file exists outside git. Write `instagram_research`.

20. Image generation via Grok: yes or no. Say that each image is billed by xAI. Yes finishes only when authentication exists outside the repository. Write `grok_image`.

21. Instagram DM automation. Ask only if Instagram is on the platform list. Otherwise write `dm_automation: no`. The supported tool is PilotDM. Yes writes `memory/dm-automation.md` with a trigger word in capitals and no accent, plus the first message and the second message, and finishes only when the creator confirms the account is set up with those three values. Write `dm_automation`.

22. Recurring behind-the-scenes series: yes or no. The workflow file stays in the repo. `no` leaves `.claude/commands/registrar-bastidores.md` dormant. `yes` does not create the series page during onboarding. Write `behind_the_scenes`.

23. Read back niche, audience, promise, pillars, platforms, handles, storage, carousel, tools, and the series choice. Apply corrections. Then set `status: ready`.

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
