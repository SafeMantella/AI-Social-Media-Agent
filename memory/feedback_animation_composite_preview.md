# Animation preview: composite on a real frame

When building motion overlays for a piece (title, captions, a list stepper, a file badge), **never treat the animation on a green or transparent field as "done".** Composite the real recording frame and the rendered animation frame at the same timestamp, and judge that.

A green-screen `test_composite` hides scale, contrast, and collisions. Those show up only against the real background, and a full render is the expensive moment to discover them. One composited frame is the cheap checkpoint.

Stay inside the current visual system while adjusting. Do not invent a second palette or type pair. Motion type is Lato 600. Captions are the serif spec. Card color and type are `memory/padrao-cards-motion-lato.md`. Change size and the amount of detail, not the system.

`face` in `memory/config.md`: when `face` is `yes`, also check that the overlay does not cover the face, except a list layout that is explicitly allowed to (`memory/feedback-legenda-serifada-hoefler-overlay-pillow.md`). Keep type near the reading area, not scattered on the edges. When `face` is `no`, skip the face check. Safe zones still apply.

## Safe zones

On a 1080×1920 canvas, about 220px at the top and about 450px at the bottom are unsafe (platform controls and the native caption). Sides are about 60–150px. The right-hand icon column is the tighter one. Scale in proportion for the real canvas. Platform safe zones go stale. Reconfirm if the last check is more than about 2–3 months old.

## Recipe

1. Render each slot with real alpha: `npx hyperframes render --format mov -o render_alpha.mov` (ProRes 4444, `yuva444p12le`). `--format webm` can log `needsAlpha:true` and still decode opaque black in ffmpeg. Do not use webm for compositing.
2. Composite with `-itsoffset <global_offset> -i slot/render_alpha.mov` and `overlay=enable='between(t,start,end)'`, chained on the base. If the slot does not start at t=0, compare the slot's internal times (when an item activates) with `beat_offsets.json`. They usually match some beat's `segment_offset`.
3. Extract a frame of the clean video at that time (`ffmpeg -ss <t> -frames:v 1`) and the animation frame at the same time. Look at the composite, not the isolated green test.
4. After a background render, `ffprobe` can confirm the new duration while ffmpeg still reads a stale file of that same duration. The composite then shows the pre-fix version. Do not trust a duration check. Recomposite to a new filename and check the content.
5. An overlay that runs the whole piece (captions) can collide with a short overlay (a stepper) even when each one looks safe alone. Test the full stack.

Slots live in `edit/animations/slot_*`. Caption style that can be pasted into a new project is `memory/hyperframes_caption_style.md`.

## Opaque full-screen test

Never test an opaque full-screen cutaway on a file that already has captions burned in. The opaque card covers the captions and nothing warns you. They are simply gone.

Cut the test from a clean `base.mp4` (no overlay). Cut the matching span from the caption alpha (`edit/animations/slot_captions/render_alpha.mov`). Composite in this order: the opaque graphic at the real timestamp, then the captions on top. Captions are always the last layer. This applies to every full-screen cutaway test.

A short test clip (`ffmpeg -ss` / `-to`, about 20–30s) around the real cut is enough. Extract frames every 30–40ms at the entrance and the exit. A contact sheet stepped by a full second misses a one-frame flash. `hstack`, `vstack`, and `drawtext` make one sheet.

## Hard-cut entrance

An opacity tween on a hard cut produces a real muddy frame, not a soft fade. An opaque shape (light type on a dark panel) tweened from 0 to 1, even in 0.08–0.3s, spends 1–2 frames at a fractional opacity. Those frames are the mixed color of the shape and the background. On a hard cut that reads as a glitch.

Fix: no opacity tween on a b-roll or hard-cut entrance. The element is opaque from frame 0 (`opacity: 1` in CSS). Use only scale (for example 0.94 to 1) as the entrance accent. Scale does not mix color. The bug shows up only in a real composite, frame by frame. It does not show on an isolated preview or on a +1s contact sheet.

## Timing comes from the transcript

Checklist items, labels, and beats land on the real words in `captions_cues.json`, `edl.json`, or `transcripts/master.json`. Do not invent categories and then hope the line matches. A label for the object the creator is describing appears when that object is spoken. Pull the times. Do not estimate them.

## Before compositing

- Confirm whether a title slot is for the video or only for the thumbnail. Do not assume every built slot goes into the piece.
- A "pending" node that stays transparent until it activates is a bug when a line is drawn behind it. The line shows through the number. Any node that sits on a connector (a progress line, a timeline) needs an opaque fill from the first frame, in the panel color. Only the fill color changes on activation. Never use a transparent rest state when something is drawn behind it.
- The scrim has to clear the widest item. The last item in a horizontal list, especially right-aligned text, is what clips on the right edge. Test that item, not only the general preview.
- If caption cues were cut or moved only because of another slot, and that slot is later kept out of the video, revert those cue changes with it. Do not leave a conditional edit behind after its cause is gone.

Full-screen production detail is `memory/feedback_fullscreen_cutaway_production.md`.
