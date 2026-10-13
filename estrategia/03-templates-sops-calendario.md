# Templates, SOPs, and the calendar method

Platforms are the ones listed in `memory/social_media_handles.md`. Still images use real photos the creator supplies and native Canva elements. Scheduling uses each platform's official scheduler. Do not use unofficial automation that can put the account at risk.

The canonical store is `storage` in `memory/config.md`. The carousel build is `carousel` in the same file. Read both before a SOP step that writes or designs.

---

## 1. Scheduling

Until a scheduler is chosen, use the official native tools:

- **Instagram:** native scheduling in Meta Business Suite, on the professional account.
- **TikTok:** native scheduling in TikTok Studio (desktop or web).
- **Any other active platform:** its official scheduler, or a manual post after approval.

That avoids paying for, or learning, a third-party tool the creator may replace.

### Optional later build

A first-party scheduler with an MCP the agent can call is optional infrastructure. It is not a content calendar, and it is not required to publish. If it is built, v1 is:

- `create_post` — copy, asset path, platform, and date; creates a draft
- `schedule_post` — schedules on the platform at a time
- `list_scheduled` — what is queued, so the agent can look it up and suggest a change
- `get_post_status` — published, failed, or pending
- Auth through each platform's official API only. Nothing unofficial that risks the account.

---

## 2. Visual system

Palette, type, and photo rules live in `estrategia/00-identidade-visual.md` and `memory/visual_identity_standard.md` after onboarding. Do not copy hex values into this file. Set up the Canva kit with `estrategia/06-brand-kit-canva-plano.md` and record every id in `estrategia/marca/ids.md`.

Base sizes, already in the brand kit once it exists:

- Carousel and feed portrait: 1080×1350 (4:5). This is the current feed default. It is not the old 1080×1080 square.
- Single square image: 1080×1080.
- Vertical cover or short video: 1080×1920 (9:16).

**Per post, when `carousel` is `canva` or the piece is a still:**

1. Start from a real photo the creator supplies (a place, the bench, or the screen).
2. Background removal is allowed only to isolate a real object and place it on a solid color from the visual identity.
3. Do not generate a design, an illustration, or a texture with AI.
4. Resize by duplicating the layout into the other size. Do not regenerate the design.

### 2.1 Carousel — native Canva, or markdown

**Do not use `generate-design` or any other AI carousel.** It was tried and rejected. The generator inserts generic illustration and texture that do not match the visual identity.

When `carousel` in `memory/config.md` is `md`, skip the Canva steps. The markdown file is the piece: `conteudo/carrosseis/<slug>.md`. Canva is not used.

When `carousel` is `canva`, build slides as native Canva elements (text, shape, line) inside one multi-page project. Duplicate the master template whose id is in `estrategia/marca/ids.md`. The Canva API does not set the font family, so a new text box lands on the wrong face. **Never create a new text box from scratch.** Copy a slide that already has the right font and replace the text.

If the master id is missing, stop and follow `estrategia/06-brand-kit-canva-plano.md`. Do not invent an id.

**Structure to keep on every duplicate:**

- Solid background in the base color from the visual identity. Page 1080×1350.
- Counter tag, top left: a pill with an accent stroke (about 3px, corner radius about 32, no visible fill — the fill matches the page). Label `0N/0X`, centered, mono face, accent color, about 26px.
- Main text: about 90px side margins, width about 900px, body face at a normal weight. Slide 1 (the hook) uses the title face, heavier, so it reads first. Text color is the light color from the visual identity. Line height about 1.25–1.3.
- Closing slide: text centered (the other slides stay left aligned) and one thin accent line (about 4px) near the bottom of the page, to mark the end. No extra icon.

**How to reuse the master:**

1. Duplicate the whole project, or duplicate the pages into a new project. That keeps the fonts. Do not rebuild them.
2. Replace only the text of each slide (`replace_text`, or in the Canva editor). Layout, colors, fonts, and the counter tag stay. Change the counter numbers if the new piece is not the same length as the master.
3. Need more slides or fewer: duplicate or delete pages inside the copy before editing the text. A new page is a copy of a page that already has the right font, not a blank page plus a new text box.
4. A different structure (a side-by-side comparison, not running text) may adapt the base. It still uses one solid background, the brand type, a single accent, and no generic stock image.

The plan is approved before the Canva build. Caption is 1–3 sentences. See `.claude/skills/sistema-social-media/SKILL.md`.

### 2.1.1 Content techniques

Apply these on every carousel, together with the visual rules above. The market notes live in `memory/growth_sales_critical_lens.md`. If they are older than two or three months, research them again before treating the numbers as current.

1. **Slide 2 is almost as decisive as the hook.** Slide 1 wins the swipe. Slide 2 is where someone saves or leaves. It cannot be a mild continuation. It has to confirm concrete value immediately.
2. **Obvious beats clever.** The slides that perform are often the ones that felt too simple while writing. Do not cut or complicate a line only because it sounds unsophisticated. Clarity wins.
3. **Reuse the layout. Do not redesign it.** Duplicating the master is evidence, not only a production preference. A recognizable layout is identified before the text is read.
4. **Real value, not a line that only sounds interesting.** A save happens when the slide actually teaches something. Check each slide: does this teach something concrete, or does it only sound insightful?
5. **One good carousel does not move the curve alone.** An audience learns the pattern over many posts. Judging one piece by its own result is misleading. What matters is showing up consistently.

Format notes to re-check when the research is fresh: about 7–10 slides is a useful range, slide 1 drives most of the result (which is why the hook cannot carry unexplained jargon — `memory/feedback_hook_writing_no_jargon.md`), and a carousel tends to earn more saves than a single image, especially on teaching and how-to pieces.

---

## 3. Script and hook pipeline

Before the prompt templates below, the order is fixed. Interview, then research, then write.

1. **Interview the creator** with concrete options: the goal of the video, the specific pain of the hook, the audience, and what must not appear in the hook or the turn. Without that, research runs on the wrong angle. Always ask whether there is a CTA, and whether the piece is a short timed script or loose talking points. Do not assume.
2. **Run the research workflow** (`.claude/commands/pesquisar.md`) at the quick tier, on the angle from the interview. One agent collects, and only with the tools enabled in `memory/config.md`. The note is `referencia/pesquisas/<slug>/RESUMO.md`. It anchors the hook and the script in real data: hook language that performed, a validated pain, top pieces, open angles. Use the deep tier for a flagship. A tool set to `no` is a gap. Do not route around it.
3. **Write the script and the hook to the store.** `storage: notion` — the piece's page, with a dated "Research sources" section pointing at the RESUMO. `storage: md` — `conteudo/roteiros/<slug>.md`, with the same parts. Apply `estrategia/10-copywriting.md`.

Operating detail: `.claude/skills/sistema-social-media/SKILL.md` and `memory/pipeline_pesquisa.md`.

---

## 4. Prompt templates

Copy these. Fill the brackets from the brand files, not from memory of an old niche. Pillars come from `estrategia/01-posicionamento-e-pilares.md`. Voice comes from `memory/estilo-de-escrita/guia-voz.md`. Write the result in `content_language`.

### 4.1 Teaching carousel

```
Build a 6–8 slide carousel about: [TOPIC]
Pillar: [one pillar from the positioning doc]
Audience: [who this is for]

Rules:
- Slide 1: a strong hook, one question or claim that creates curiosity, with no empty clickbait and no unexplained jargon
- Slides 2–6: one idea per slide, one short sentence plus one analogy or concrete example. Slide 2 confirms concrete value immediately
- Second to last: the point in one sentence
- Last slide: a light CTA (never a hard sell). The caption does not repeat it
- Tone: follow the voice guide. Technical when the pillar is technical, no hype, dry humor only where the voice guide allows it
- Each slide is short enough to read in one swipe. One idea. No paragraph
- Caption: 1–3 sentences. The slides already carry the lesson. No coach talk, no "follow for more"
- 5 niche hashtags, not generic ones
- For each slide, one native visual element (a bar, a comparison, a grid, a counter) that reinforces THAT slide. Do not repeat the same element on every slide. Follow the visual identity. No stock illustration and no AI-generated design
```

### 4.2 Single image (opinion or behind the scenes)

```
Write the caption for a single-image post about: [TOPIC]
Pillar: [one pillar from the positioning doc]

Rules:
- Open with an opinion or an admission of a mistake, not with context
- 3–5 short sentences, frequent line breaks
- Close with a genuine question the audience can answer in the comments
- First person, personal, not performative
- 3–5 niche hashtags at the end
```

### 4.3 Short-video script (hook, value, CTA)

```
Write a 30–60 second video script about: [TOPIC]
Pillar: [one pillar from the positioning doc]
Format: short vertical video

Required structure:
- HOOK (first ~1.5s): a line or a question that stops the scroll. No introduction. Straight into the problem. No unexplained jargon
- VALUE (the middle): the explanation in 3–4 short steps. Each step has one on-screen line plus what to say (if this is recorded) or what to show (if it is only the screen)
- CTA (last 5–10s): one simple action, and only if the interview said this piece has a CTA. If it does not, omit the CTA

For each row, one concrete visual reference — a real screen recording, a still, or a simple diagram. Prefer a real screen recording to a mockup whenever the content allows it. Humor only where the voice guide allows it on that pillar. Teaching pillars stay didactic.

Output as a table: [Time | Screen / action | Speech / on-screen text | Visual suggestion]
```

### 4.4 Expand a raw idea already in the store

```
Here is a raw idea from the ideas store: "[PASTE THE IDEA]"

Adapt it to the current positioning (estrategia/01-posicionamento-e-pilares.md). Return:
1. A short title for the ideas list
2. The best-fit pillar
3. The best format (carousel / single image / short video / thread). A short video is the base format unless it does not fit
4. A 1–2 sentence summary ready to store
```

---

## 5. SOPs

Nothing in these lists is scheduled or published without an explicit yes from the creator.

### Daily (5–10 min)

- [ ] Reply to comments and DMs from the last 24 hours on the active platforms
- [ ] Check that today's post, if one was scheduled, went out correctly
- [ ] Write any idea from the day into the ideas store, even with no detail yet (`storage: notion` — the ideas database; `storage: md` — `conteudo/ideias/`)

### Weekly (30–45 min)

- [ ] Open the prioritized ideas and pick the week's pieces
- [ ] Draft the week's captions and scripts with the templates in section 4, after the interview and the research step in section 3
- [ ] Build or adjust designs only after the plan is approved. `carousel: canva` — duplicate the master in `estrategia/marca/ids.md`. `carousel: md` — the markdown file is the piece. Canva is not used
- [ ] **Creator's approval.** Nothing is scheduled or published without an explicit yes. Mark the piece in review until they confirm
- [ ] Schedule the approved posts in the official native scheduler (section 1)
- [ ] Fill last week's row in analytics (views, likes, one learning)
- [ ] Review the queue and move anything that is not ready

### Monthly (about 1 hour, at the start of the month)

- [ ] Review the month's analytics: which pillars and formats did better
- [ ] Adjust next month's mix of pillars from that
- [ ] Add new ideas to the store (a brainstorm, or an expansion of an idea already there)
- [ ] Build next month's queue from the prioritized ideas. Do not keep a sample month in this file

There is no fixed month-1 calendar here. The queue lives in the ideas store. A cold-start volume suggestion, when the account is under about 1,000 followers, is in `.claude/skills/sistema-social-media/SKILL.md`. It is a recommendation to discuss, not a calendar to paste.

---

## 6. Next steps

1. Set up the Canva brand kit with `estrategia/06-brand-kit-canva-plano.md`. Record ids in `estrategia/marca/ids.md`.
2. Run one weekly SOP on ideas already in the store.
3. At the first weekly review, fill the first analytics row.
4. Do not add a platform until a monthly review shows the current ones are actually publishing.
