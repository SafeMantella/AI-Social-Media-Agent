---
name: sistema-social-media
description: Operating rules for this social-media system — visual identity, a carousel built with Claude's design tools or HyperFrames (Canva only on a legacy copy), the content store, and hook and repurposing rules. Use when creating or editing a script, carousel, post, caption, video, or calendar, or when changing the store or Canva setup for this system.
---

# Social media system

Read `memory/config.md` and `memory/project_social_media_status.md` before content work. Niche, voice, pillars, and visuals come from the brand files after onboarding, not from this skill. The full memory index is `memory/INDEX.md`.

For a piece, also read `memory/visual_identity_standard.md` (palette and type), `memory/feedback_hook_writing_no_jargon.md` (hook rule), `memory/growth_sales_critical_lens.md` (growth lens), and `memory/estilo-de-escrita/` (long-form voice). Write posts, scripts, captions, and hooks in `content_language`.

**Copy** (hook, script, carousel, caption) starts at `estrategia/10-copywriting.md`. Read the sections that apply before writing. The prioritized operating layer is `memory/estrategias-principais.md`; the pointer is `memory/diretrizes-copywriting.md`. Precedence that the copy guide already respects: long-form voice → `memory/estilo-de-escrita/guia-voz.md`; hook → `memory/feedback_hook_writing_no_jargon.md` and `referencia/swipe-openers.md`; algorithm claims → `memory/growth_sales_critical_lens.md` (research them again if the source is older than two or three months).

Strategy docs live in `estrategia/` (`00`–`10`). The canonical store is `storage` in `memory/config.md`: `notion` (ideas, ready content, analytics — open the live databases; do not trust a stale summary) or `md` (`conteudo/`). If a login fails, stop and ask the creator to reconnect. Do not switch stores.

This skill is `sistema-social-media`. The file the agent reads is `.claude/skills/sistema-social-media/SKILL.md`.

## Script and hook pipeline

Interview, then research, then write. Always in that order.

1. **Interview the creator first.** Before any research or draft, align with concrete options (not an open question): the goal of the video, the specific pain the hook attacks, the audience, and the limits of the hook and the turn (what must not appear). The interview sets the research angle. **Two questions are mandatory every time. Never assume the answer,** even when the channel goal or the previous piece suggests one:
   - Will this piece have a CTA?
   - Is the format a short video (a closed, timed script) or loose talking (longer, guided by bullets rather than a word-for-word script)?
   See `memory/feedback-notion-canonical-roteiro-hook.md`.
2. **Research, quick tier, on that angle.** Follow `.claude/commands/pesquisar.md`. It is a workflow, not a separate command the creator must type. Quick tier unless the piece is a flagship (`deep`). The note is `referencia/pesquisas/<slug>/RESUMO.md`. Use it for hook language that already performed, a pain that showed up in a real post, the top pieces in the niche, and open angles. Only the tools enabled in `memory/config.md` run.
3. **Write the script and the hook to the canonical store.** Apply `estrategia/10-copywriting.md` (hook and formulas, frameworks, short-video anatomy, ready models). Do not leave the script only in the chat. When `writes_scripts` is `yes`, do not do this step unless the creator explicitly asks for a script. Deliver the research instead. See `memory/feedback-so-a-peca-pedida.md`. When the conversation has several pieces, deliver only the one they named, then wait.
   - `storage: notion` — the piece's page. Include the Hook property, the script table, the hook alternatives that were considered, production notes, and a dated "Research sources" section with links to the RESUMO.
   - `storage: md` — `conteudo/roteiros/<slug>.md`, with the same parts.

This template has no built-in light-format exception. See `memory/feedback-repo-do-dia-format.md`.

## Carousel pipeline

Always in this order.

1. **Interview the creator first** (concrete options): the angle and the takeaway, the universal pain slide 1 attacks, the reference tool, the scope, the CTA on the last slide, and what must not appear in the hook or the turn.
2. **Research, quick tier,** on that angle. Same workflow as the script pipeline. The RESUMO feeds the plan: hook language that performed, a pain validated in a real post, concrete examples, top pieces, and open angles.
3. **Write the plan, then stop.** Slide-by-slide structure, one native visual element per slide (the vocabulary below — never an illustration or clipart), the **caption (1–3 sentences)**, the hashtags, and a dated "Research sources" section. The carousel already carries the content. The caption is a short note in the creator's voice (`memory/estilo-de-escrita/`): no coach talk, no "follow for more". The CTA is already on the last slide. Write the short caption first. Do not draft a long one and trim it later.
   - `carousel: md` — the markdown file is the piece. Write `conteudo/carrosseis/<slug>.md`. Nothing is built.
   - `carousel: claude` or `hyperframes` — the plan goes in the store (`storage: notion`: the body of the ready-content page; `storage: md`: `conteudo/carrosseis/<slug>.md`). The build comes after approval.
   - `carousel: canva` and `storage: notion` — the plan goes in the body of the ready-content page. Create the page if it does not exist.
   - `carousel: canva` and `storage: md` — the plan goes in `conteudo/carrosseis/<slug>.md`. Canva is only the build, after approval.
4. **The plan is approved before the build.** Wait for an explicit yes. If `carousel` is `md`, this approval is on the markdown file and there is no build step.
5. **Build.** `claude` and `hyperframes` follow `.claude/commands/carousel.md`. The rest of this step is for a legacy `carousel: canva` copy. Duplicate the master template whose id is in `estrategia/marca/ids.md`. Never generate a design with AI (`generate-design` or any other generator). Never create a new text box from scratch: copy a slide that already has the right font, then replace the text (`replace_text` keeps the font of the run). The Canva API does not set the font family; a fresh text box lands on the mono face and becomes manual rework. If the master id is missing, stop and follow `estrategia/06-brand-kit-canva-plano.md`. Do not invent an id. Show the link in the chat and keep Status, the asset link, and the plan in the store in sync with the design.

**After the build.** What the agent delivers is a draft. The creator may still do a manual pass (shorter, more casual lines, vertical rhythm, sometimes the close). When the piece is finished, reread the final design and the final caption, compare them with what was delivered, and save what changed in `memory/feedback-carousel-pipeline.md`. Do that without being asked. The aim is less correction on the next one.

Construction rules (native elements, the decorative vocabulary, slide 1 driving most of the result) are below and in `estrategia/03-templates-sops-calendario.md`.

## Video edit pipeline

Transcribe, check, correct, interview. The creator cuts and returns `base.mp4`. Then overlays and captions. Preview render until the creator asks for full resolution.

Do not cut the video. Do not suggest a cut list and then execute it. HyperFrames is for overlays and captions, not for the cut. Visual punch-ins only when the creator asks, and only on the clean `base.mp4`, before any overlay (zooming a frame that already has overlays resamples the overlay).

`face` in `memory/config.md`: `no` skips face-coverage checks and skips cutaways whose job is to remove the face. Captions still go on.

1. **Transcribe.** Skill `transcricao-confiavel` when `transcription` is `whisper` (`ferramentas/transcrever/transcrever.py`, engine `whisperx`) → `transcripts/base.json`. Do not use `transcribe.py` from `local-video-use`. The `-dtw` path of whisper.cpp drops speech without warning (`memory/diretrizes-transcricao.md`). If `transcription` is not `whisper`, use the configured provider and do not write a secret into the repo.
2. **Check completeness by a cross-check, not by a time gap.** `transcrever.py --verificar` (a second engine, then a diff) or `comparar.py` between two runs. A time-gap search does not work: the worst measured loss had continuous timestamps and the gap detector found nothing. Every difference of 3 or more words is re-transcribed on that window alone, which is where the model is accurate.
3. **Correct the transcript.** `glossario.py` fixes recurring names. A new misspelled proper name becomes an entry in `ferramentas/transcrever/glossario.json`, not a one-off hand edit. The rest (false starts, chopped endings) is a direct patch on `transcripts/base.json`, which is canonical. Regenerate `takes_packed.md`. See `memory/feedback_video_editing_recording_patterns.md`.
4. **Interview the creator** (concrete options). Read the video's script first (the Notion page, or the file in `conteudo/roteiros/`). Align: (a) any still or clip besides the master, and for each one whether the creator places it or the agent composites it, and where it enters; (b) what the cut must keep, what may go, and the target duration — the creator will cut; (c) motion intent (density, what to emphasize). The script plus this interview are the context for the rest.
5. **Wait for `base.mp4`.** The creator cuts and returns it. Do not render a cut. Punch-ins, reframes, speed ramps, or an extra grid happen only if the creator asks, on that clean file, before overlays. Anchor any suggestion to the interview, the script notes, and the cadence audit in `memory/feedback_video_editing_alex_hormozi_benchmark.md` (a new visual stimulus about every 2–3 seconds; captions do not count). **Full-screen cutaways,** only when `face` is `yes`: scan for speech that describes something concrete and visual (an object, a process, a list, about 5 seconds or more, not the hook, the CTA, or the turn) that would play better as opaque full-screen b-roll. List the candidates and let the creator choose. See `memory/feedback_fullscreen_cutaway_production.md`. When `face` is `no`, skip this scan.
6. **Overlays.** Before the first overlay, detect cuts on `base.mp4` with `ffmpeg -vf "select='gt(scene,0.08)',showinfo"`. Word times sit a few frames off the creator's cut. Text that starts just after a cut goes on the cut frame. Text that leaves is gone on the frame before. Check a contact sheet around each cut. The threshold came from one copy. Re-measure if it misses or invents cuts. HyperFrames slots live in `edit/animations/slot_*/`. Suggestions come from the real speech (`captions_cues.json`), the script notes, and saved feedback. Check each slot composited on a real frame before the full render. Pick a direction per beat from `memory/direcoes-motion.md`. Do not repeat a mold on two beats in a row. When `face` is `yes`, fixed glitch or VHS bands stay off the face height. Overall wear may cover the frame. See "Motion graphics" below. A list piece also follows `memory/formato-lista.md`.
7. **External assets the creator kept.** Remind them before the final assembly and wait for the version that includes those assets. Assets the agent composites are a layer in the preview step.
8. **Captions, last layer, always.** Spec in `memory/hyperframes_caption_style.md`. Do not redesign it. Instant cut, no fade. **At most 5 words per cue.** Cues follow the **phrase** transcript, not word-level timing. When `face` is `yes`, never cover the face (re-check the worst frame of this take). When `face` is `no`, skip the face-coverage check. Captions still go on. **Show the cues to the creator and ask for corrections before rendering.**
9. **Preview render until the creator asks for full resolution.** One ffmpeg command, layers by `-itsoffset` in chronological order, captions last, in the background. Preview only: `scale=960:-2`, crf 24. Check the real file with `ffprobe` and a contact sheet, never the log alone. Run the cadence audit again. Music, if any, comes from the `media-use` skill. **Do not render the full-resolution master until the creator explicitly asks.** Do not delete any render until the creator approves the piece and authorizes cleanup, folder by folder. **Cleanup exception:** when they explicitly say both that the video is finished and that the originals are backed up, move superseded intermediate renders to the trash. Use `trash`, never `rm`. Always keep `base.mp4`, `edl.json`, `project.md`, `transcripts/`, and the slot HTML.

**When they say the video is done, ask about sped-up versions.** Do not wait for them to remember. Default 1.1x and 1.2x as separate files. The original stays intact. The sped-up file keeps the original frame rate (read it with `ffprobe`; do not hardcode it). Render from `base.mp4` plus the caption layer, not from an already compressed final. Captions go on before `setpts` so sync holds. Audio uses `atempo` (pitch stays). Never `asetrate`. See `memory/feedback-video-speed-versions.md`.

The creator may ask for a 20–30 second assembled excerpt, or a contact sheet, at any step. Compress (`scale=960:-2`, crf 24) before sending. Technical recipes for each overlay step live in the `local-video-use` skill. Fixing an overlay that is already composited is the workflow `.claude/commands/refinar-overlay.md`.

**On all three pipelines:** a correction that is clearly a reusable preference is saved in `memory/` at the time, with one line saying so. If it is unclear whether it is a one-off, ask. See `memory/feedback-evolve-feedback-loop.md`.

## Posture

Be a critical growth and sales partner, not only an executor. Compare a request with current research and name the tension even when nobody asked (for example a calendar that fights what works in a cold start). Base: `memory/growth_sales_critical_lens.md`. If an algorithm claim is older than about two or three months, search again before trusting it.

**Ranking signals (Instagram, publicly stated):** watch time, including rewatches, then sends per reach (a private share outweighs a like for reaching people who do not follow), then likes per reach.

**Pillar jobs,** on top of the thematic pillars in `estrategia/01-posicionamento-e-pilares.md`: each week needs authority (a framework or a lesson), connection (values or a personal story), and trust (a real result or proof). Direct self-promotion stays at or below about 20%.

**Cold start (under about 1,000 followers):** research has pointed to 3–4 short videos and 1–2 carousels a week, not to waiting for a large backlog. This is the most sensitive phase. Raise the tension with the creator. Do not change the calendar automatically.

## Reference profiles

When the creator sends another account's post as a reference for one piece, it is a form reference only: sequence, template, type, and rhythm. The subject still comes from the pillars. Do not mix two references on one piece. Measure a rhythm reference cut by cut. See `memory/feedback-so-a-peca-pedida.md`.

When the creator sends a new profile as a reference, do both steps, not only the first.

1. Register it. `storage: notion` — the profiles database described in `estrategia/02-arquitetura-notion.md` (name, URL, platform, what they publish). `storage: md` — a folder under `referencia/estudos-de-caso/`.
2. Write a full case study on that page or in that folder, not only the reason it was saved. Six fields: **Profile** (real data: followers, bio, link), **Content pillars**, **Format and cadence**, **Hook**, **Proof / monetization** (how the path to a customer is visible), **Application to this brand** (2–4 concrete tactics).

That requires the actual profile (grid, highlights, 2–3 representative posts or videos, the link in the bio). The landing view is not enough to judge format or hook. Why the bank exists is in `memory/growth_sales_critical_lens.md`.

## Carousels: Claude's design tools, HyperFrames, or markdown

When `carousel` is `claude` or `hyperframes`, the slides are built from `memory/visual_identity_standard.md` and `estrategia/00-identidade-visual.md`: one native type-and-shape element per slide, never clipart or a generated illustration. Type is the title face, heavier on slide 1 (the hook), the body face on the rest. Pipeline and build: `.claude/commands/carousel.md`.

Legacy `carousel: canva`. **Never generate a design with AI** there: it was tried and rejected, generic and off the identity.

- Duplicate the master template whose id is in `estrategia/marca/ids.md`. Never generate from scratch. Duplicating keeps the fonts that were set by hand.
- **A slide or element that is not on the master: copy a slide that already has the right font and change only the text. Never create a new text box from scratch.**
- Type: the title face, heavier on slide 1 (the hook), the body face on the other slides, the mono face only on tags and counters. Faces and colors come from `estrategia/00-identidade-visual.md` and `memory/visual_identity_standard.md`. Do not hardcode a palette in this skill.

When `carousel` is `md`, the markdown file is the piece and nothing is built.

### Decorative vocabulary

Every slide carries at least one element, and it reinforces the content. Empty decoration does not count. Colors follow the visual identity: one dominant accent per slide.

- Progress or limit bar: outline track, solid accent fill.
- Side-by-side blocks (solid accent, secondary, outline; corner radius about 8–10) when items are split or compared.
- Comparison cards: one solid accent card is the answer, one outline card is the contrast.
- Horizontal bars that compare size.
- A cell grid (outline, one cell in solid accent for the specific index or example).
- Large brackets flanking a closing line, accent, reduced opacity.
- Solid accent means right or highlight. The secondary color means supporting or wrong. Outline means neutral. Never more than one dominant accent per slide. Never clipart or illustration.

Copy prompts and the daily, weekly, and monthly SOPs are in `estrategia/03-templates-sops-calendario.md` (carousel section and SOP section).

### Optional "ASCII art and pills" treatment

For a concept carousel, when the creator asks for this treatment. Any extra color that is not already in the visual identity must be written into that file before it is used. Do not invent a second palette here.

- **Background:** ASCII art of an object that belongs to the post, from a photo the creator supplies, full bleed. If there is no obvious object, use abstract shapes. Inner slides use the same art at about 0.28–0.4 opacity.
- **Word → parts,** as pills in the footer: one pill for the whole word, a large arrow, then pills for the parts.
- **Text:** short title in the title face, left aligned (1–2 lines); short body; the keyword in the accent color, inline.
- **Font gotcha:** copy a slide that already has the right font. Do not build a new text box.

## Short-video cover

This is its own vocabulary. Do not confuse it with the carousel.

The master id is the cover entry in `estrategia/marca/ids.md`. Canvas 1080×1920 (9:16). Same flow as the carousel: duplicate that design and change only the central word, and the handle if it changed. The handle comes from `memory/social_media_handles.md`. Texture and icon assets are the ones recorded in `estrategia/marca/ids.md`. If those ids are missing, stop. Do not invent them.

- Background: the recorded texture, full bleed, over the base color. A cover may use a texture and a graphic icon. That does **not** lift the carousel rule against illustration.
- One graphic icon, centered, above the word.
- One central word, title face, light text color, large, centered, under the icon.
- The handle in the accent color, footer, centered.
- Decorative brackets belong to the carousel, not to the cover. Do not add them back unless the creator asks.

### Carousel content techniques

Slide 2 confirms value immediately (almost as decisive as the hook on slide 1). Prefer the obvious line to the clever one. Never promise value the slides do not deliver. An audience learns a pattern over many posts — do not judge one piece alone. Detail in `estrategia/03-templates-sops-calendario.md` and `memory/growth_sales_critical_lens.md`.

## Hook rule (no unexplained jargon)

The real hook window on a short video is about 1.5 seconds, not 3 (`memory/growth_sales_critical_lens.md`). On a carousel, slide 1 drives most of the result. The hook does not use a technical term that is only explained later. Swap it for a universal consequence. Jargon may enter from block or slide 2. Everyday words may appear in the hook even when they are the subject. Hold back only terms that are specific to the niche. Detail: `memory/feedback_hook_writing_no_jargon.md`.

The full hook treatment (families, formulas, tests, and examples) is `estrategia/10-copywriting.md` section 3. The rule above is the constraint. The copy guide is the repertoire.

## Repurposing

A short video is always the base format. Do not start from a text post. After it is recorded, narrow it into a carousel, a thread, or a long post. Detail: `memory/content-format-cascade.md`.

## Motion graphics and video overlays

These are the overlay and caption steps above. This section is the detail, not a second order.

Before a caption, title, stepper, or any motion overlay (`local-video-use` / HyperFrames), read:

- `memory/padrao-cards-motion.md` — one motion mold: card layout, animated in and out, clicks that match each animation, review checklist. It is not the only mold. Read `memory/direcoes-motion.md` before choosing.
- `memory/hyperframes_caption_style.md` — caption spec already validated. Reuse it. Do not redesign it.
- `memory/feedback_animation_composite_preview.md` — an overlay is not "done" on a green or empty background. Composite a preview on a real frame from the recording before the full render, and test all overlays together so they do not collide.

## Approval

The creator approves before anything is scheduled or published. No autonomous posting. Nothing is built or exported as a carousel, and nothing is rendered at full resolution, without an explicit yes.
