# Video editing pipeline

From the uncut master to a publishable cut, in this order. Post order is fixed: cut, then visual variations, then motion graphics, then captions.

`face` in `memory/config.md` controls face-specific checks. When it is `no`, skip rules whose only job is to keep a face visible or to cover it. Captions still go on.

1. Transcribe with the engine in `transcription`. Skill `transcricao-confiavel`. Cache at `transcripts/master.json`. See `memory/diretrizes-transcricao.md`.
2. Check completeness. Whisper with two local engines: diff the transcripts. One local engine, or ElevenLabs: check timings and say that a second engine was not available.
3. Correct the transcript in `transcripts/master.json`. Show the cues to the creator before rendering captions.
4. Interview the creator with concrete options. Read the script from the canonical store first (Notion page, or `conteudo/roteiros/<slug>.md`). Align external assets, what is sacred in the cut, target duration, and motion density.
5. The creator cuts and returns `base.mp4`. The agent does not cut and does not suggest cuts. HyperFrames is for overlays and captions, not for cutting.
6. Visual variations (zoom, punch-in, reframe) only when the creator asks, and only on the clean `base.mp4` before any overlay.
7. When `face` is `yes`, scan the transcript for stretches of at least 5 seconds that describe a concrete object or process. Offer those as full-screen cutaways. Hook, CTA, and identity beats stay on camera. The creator picks which ones to build. See `memory/feedback_fullscreen_cutaway_production.md`.
8. Build motion overlays from the real speech and the production notes. Preview each overlay on a real frame from this recording. See `memory/feedback_animation_composite_preview.md`.
9. Remind the creator of assets they said they would place themselves. Wait for those files before the final assembly.
10. Captions last. Do not cover the face when `face` is `yes`. No fade. At most 5 words per cue. Spec in `memory/hyperframes_caption_style.md`.
11. Render a preview only (`scale=960:-2`, crf 24) until the creator explicitly asks for full resolution. Do not delete a render until the creator says the piece is finished and that a backup exists.

A correction during the edit is a candidate for `memory/`. Ask when it is unclear whether it is reusable. See `memory/feedback-evolve-feedback-loop.md`.

Generated video files stay in the piece's `edit/` folder. See `memory/feedback-generated-video-in-project.md`.
