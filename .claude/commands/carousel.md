---
description: Build a carousel with the fixed pipeline: interview, research, plan in the store, approval, then build with Claude's design tools or HyperFrames.
argument-hint: <idea or topic>
---

# Carousel: $ARGUMENTS

Read this file and follow it. It is a workflow.

1. Read `memory/feedback-carousel-pipeline.md` and the carousel section of `.claude/skills/sistema-social-media/SKILL.md`. Read `memory/config.md` for `carousel`.
2. Before writing copy, read the sections that apply in `estrategia/10-copywriting.md` (use `ferramentas/prep-texto/prep-texto` for the index).
3. Run the pipeline in order: interview, quick research, plan in the canonical store, wait for approval. Do not build before an explicit yes.
4. Build by the `carousel` value:
   - `claude` — design the slides with Claude's own design tools. Start with `Artifact` `action: "quickstart"`, `intent: "design"`, and load the `artifact-design` skill. Slides are HTML at 1080×1350, one per slide, with type and palette taken from `memory/visual_identity_standard.md`. Publish the draft as a private Artifact for the review. Export the PNGs only after a yes (a headless-browser screenshot of each slide at full size).
   - `hyperframes` — only when the creator chose to install it. Check that the `hyperframes` skills are available. If they are not, stop and ask the creator to install the HyperFrames plugin. Do not install it yourself. Build one composition with one scene per slide at 1080×1350, review it in Studio, and render a still per slide only after a yes.
   - `canva` — kept for copies that already use it. Duplicate the master id in `estrategia/marca/ids.md`. Never generate the design with an image model.
   - `md` — the plan file is the piece. Nothing is built.
5. Record the link or the files on the canonical page or file. Stop for the creator's approval before anything is scheduled or published.
6. After the creator edits the finished piece, compare it with what you delivered and save the reusable difference in `memory/feedback-carousel-pipeline.md`.
