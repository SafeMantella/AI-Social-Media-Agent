# Canva brand kit

How to set up the kit, and where the ids go. Colors and type are not in this file. After onboarding they live in `estrategia/00-identidade-visual.md` and `memory/visual_identity_standard.md`. Copy from those files into Canva. If a color or a font is missing there, stop and finish onboarding. Do not invent a palette here.

Record every id in `estrategia/marca/ids.md`. Other docs name the role ("carousel master", "cover master", "brand kit") and point at that file. They do not paste the id. Do not put a Canva URL in `ids.md` or in any other doc. Paste the id Canva shows. Do not invent one.

Nothing is uploaded until the creator confirms that section, or asks for a change.

---

## 1. Create the kit and record it

1. Create a Brand Kit in Canva for this brand only. Do not mix in designs from another project.
2. Add the colors from the visual identity, with the role each one has (dominant, background, accent, text). If the plan caps how many colors a kit can store, record the cap in `estrategia/marca/ids.md` and keep the full palette in the visual identity files. Do not drop a color from the identity to fit the cap without saying so.
3. Add the fonts from the visual identity: title, body, and the mono or technical face, with the weights the identity specifies.
4. Copy the brand kit id into `estrategia/marca/ids.md` under a Brand kit heading.

Free plans often cap the palette. Pro is what removes that cap. Record which plan the kit is on.

---

## 2. Logos

Direction: a typographic wordmark, no symbol, set in the title face from the visual identity. The logo is an extension of the type, not a separate drawing.

If the creator already has logo files, they live in `estrategia/marca/`. Upload the light variant (for dark backgrounds) and the dark variant (for light backgrounds). Previews are for checking. They are not a third logo.

If a wordmark is wide, it will not fit a round avatar. Ask before making a compact version (initials or a single letter). Do not upload a compact mark they have not approved.

Record each uploaded asset id in `estrategia/marca/ids.md`.

---

## 3. Brand voice

Canva has a free-text voice field it uses to keep generated copy on tone. Paste a short paragraph distilled from `estrategia/01-posicionamento-e-pilares.md` and `memory/estilo-de-escrita/guia-voz.md`. Do not paste a private sample that is only in the voice examples file unless the creator says to.

Use their words. A usable paragraph usually covers: who they sound like, what they never say, and the test a piece has to pass (if it does not answer the promise in the positioning doc, it is not a piece for this brand).

Generated copy inside Canva is still a draft. Carousel designs are not generated. See section 9.

---

## 4. Photos

Paste the photo rules from the visual identity into the kit's photo guidelines. They should say, in the creator's own terms:

- Backgrounds and textures are treated, never raw, so posts match. Strength of the treatment is whatever the visual identity specifies.
- People: follow `face` in `memory/config.md`. `yes` means a face on camera is welcome. `no` means the face is not the subject. Hands, over-the-shoulder, screen, silhouette, and profile can still be valid. Do not hide or show a face against that setting.
- Project and hardware photos, when the niche has them, are real. No studio fiction.
- Do not use generic stock of a person smiling at a laptop. It breaks the brand.

The creator chooses which files to upload. Do not pick a folder for them.

---

## 5. Graphic elements

Do not upload a set until the creator approves it. A minimal set that matches the carousel vocabulary:

- **Technical tag or pill** — a small stroked rectangle, mono face, for a term or a category.
- **Thin divider** — a 1px line in the text color or the accent, between sections of a carousel.
- **Quotation brackets** `[ ]` — to hold a sentence or a code fragment. These belong to carousel slides, not to the short-video cover.

Skip a texture that belongs to only one pillar unless the positioning doc asks for it. Do not mix two visual languages.

Record approved asset ids in `estrategia/marca/ids.md`.

---

## 6. Icons

Proposed style, pending approval: **outline, thin stroke** (a filled glyph is heavier than a quiet identity), about 2px, one color. Light color on a dark background, base color on a light background. The accent is not used on a large icon. The accent stays a small highlight.

Take icons from Canva's own library, filtered to line or outline. Do not commission a custom set for v1. Build the shortlist from the pillars in `estrategia/01-posicionamento-e-pilares.md`: one icon per pillar, plus one for a long-form or newsletter piece if that platform is active. Drop any icon that does not match a real pillar.

---

## 7. Charts

This Canva section is only for a chart placed inside a design. Do not add colors in this file.

The brand palette is often too small, or too neutral, for a multi-series chart. If a chart needs more series than the identity has:

1. Extend the palette in `estrategia/00-identidade-visual.md` and `memory/visual_identity_standard.md` first, marked as chart-only, not for dominant use on a normal piece.
2. Mirror those colors into the Canva chart palette.
3. Note the extension in `estrategia/marca/ids.md`.

Do not invent the extra hex values in this doc.

---

## 8. Guidelines page inside the kit

Canva can compile a one-page summary of story, values, and usage rules. Build it from the strategy docs, not from memory:

1. Positioning line and short bio, from `estrategia/01-posicionamento-e-pilares.md` and `memory/social_media_handles.md`
2. Voice (the same text as section 3)
3. Colors, with the usage rule from the visual identity (which color dominates, which one is the only accent, never more than one accent per piece)
4. Type (which face, which weight, when)
5. Photo rules (section 4)
6. Short do and don't: no bubble or rounded display face, no neon as the dominant color, no empty hype in the copy

---

## 9. Brand templates

Publish a reusable template only when a repeatable layout exists. A carousel master and a short-video cover are the two that matter first. Do not publish unrelated designs into this kit.

When a master exists:

- Carousel master — duplicate it for every new carousel. Never generate a design with AI. Never create a new text box from scratch; copy a slide that already has the right font. Page size 1080×1350 unless the visual identity says otherwise.
- Short-video cover — 1080×1920. Duplicate it and change the central word and, if needed, the handle from `memory/social_media_handles.md`.

Record both ids, plus any shared texture or icon, in `estrategia/marca/ids.md`. The operating rules are in `.claude/skills/sistema-social-media/SKILL.md`. If `carousel` in `memory/config.md` is `md`, do not create a carousel master. The markdown file is the piece.

---

## Checklist

Confirm with the creator before uploading the matching section.

- [ ] Brand kit created. Colors and fonts copied from the visual identity. Id recorded in `estrategia/marca/ids.md`
- [ ] Logo — wordmark approved, including whether a compact avatar version is needed
- [ ] Voice — paragraph approved and pasted
- [ ] Photos — guidelines approved, and the creator chose the real files
- [ ] Graphic elements — proposal approved (section 5)
- [ ] Icons — style and shortlist approved (section 6)
- [ ] Charts — any extra series colors written into the visual identity first (section 7)
- [ ] Guidelines page — compiled from the docs above
- [ ] Templates — carousel master and cover master recorded in `estrategia/marca/ids.md`, or explicitly skipped because `carousel` is `md`
