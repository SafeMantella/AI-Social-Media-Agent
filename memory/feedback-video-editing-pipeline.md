# Video editing pipeline

From the uncut master to a publishable cut, in this order. Post order is fixed: cut, then visual variations, then motion graphics, then captions.

`face` in `memory/config.md` controls face-specific checks. When it is `no`, skip rules whose only job is to keep a face visible or to cover it. Captions still go on.

When `memory/edicao-observada.md` says `decision: keep`, match that recipe: the open, the cut density, the on-screen text, the color, and the job of the caption. The creator still cuts and still returns `base.mp4`. A later correction from the creator overrides the recipe. When the decision is `change`, or the file does not exist, do not copy the old edit.

1. Transcribe with the engine in `transcription`. Skill `transcricao-confiavel`. Cache at `transcripts/master.json`. See `memory/diretrizes-transcricao.md`.
2. Check completeness. Whisper with two local engines: diff the transcripts. One local engine, or ElevenLabs: check timings and say that a second engine was not available.
3. Correct the transcript in `transcripts/master.json`. Show the cues to the creator before rendering captions.
4. Interview the creator with concrete options. Read the script from the canonical store first (Notion page, or `conteudo/roteiros/<slug>.md`). Align external assets, what is sacred in the cut, target duration, and motion density.
5. The creator cuts and returns `base.mp4`. The agent does not cut and does not suggest cuts. HyperFrames is for overlays and captions, not for cutting.
6. Visual variations (zoom, punch-in, reframe) only when the creator asks, and only on the clean `base.mp4` before any overlay.
7. When `face` is `yes`, scan the transcript for stretches of at least 5 seconds that describe a concrete object or process. Offer those as full-screen cutaways. Hook, CTA, and identity beats stay on camera. The creator picks which ones to build. See `memory/feedback_fullscreen_cutaway_production.md`.
8. Before any overlay on `base.mp4`, detect the creator's cuts. Word times from the transcript fall a few frames early or late relative to that cut. Text that starts just after a cut goes on the cut frame. Text that leaves is gone on the frame before the cut. Check with a contact sheet around each cut. The threshold below came from one copy. Re-measure if cuts are missed or invented.

```bash
ffmpeg -i base.mp4 -vf "select='gt(scene,0.08)',showinfo" -f null -
```

9. Build motion overlays from the real speech and the production notes. Preview each overlay on a real frame from this recording. See `memory/feedback_animation_composite_preview.md`. Pick a direction per beat from `memory/direcoes-motion.md`. Do not use the same mold twice in a row. When `face` is `yes`, fixed glitch or VHS bands (tracking lines, tears) stay off the face height. Overall wear (grain, color bleed, a scan) may cover the frame. A band that travels during a short transition may cross the face.
10. Remind the creator of assets they said they would place themselves. Wait for those files before the final assembly.
11. Captions last. Do not cover the face when `face` is `yes`. No fade. At most 5 words per cue. Spec in `memory/hyperframes_caption_style.md`. An alpha track measured on one copy is `ferramentas/faixa-legenda/README.md`. Do not replace the 5-word rule with that copy's 3-word track until it is re-measured.
12. Render a preview only (`scale=960:-2`, crf 24) until the creator explicitly asks for full resolution. Do not delete a render until the creator says the piece is finished and that a backup exists.

A correction during the edit is a candidate for `memory/`. Ask when it is unclear whether it is reusable. See `memory/feedback-evolve-feedback-loop.md`.

Generated video files stay in the piece's `edit/` folder. See `memory/feedback-generated-video-in-project.md`.
