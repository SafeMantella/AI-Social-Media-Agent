# Caption style (HyperFrames)

The face named in this note is the face these measures were taken on. Use the face in `memory/visual_identity_standard.md`. Re-measure line width when the face changes. Keep the layout, the sizes as a starting point, and the method. An alpha-track contract measured on one copy is `ferramentas/faixa-legenda/README.md`.

Copy this into a new HyperFrames caption project instead of rediscovering size, position, and animation. Reference canvas: **1920×3414** (portrait, a 9:16 frame scaled from 1080×1920). If the next piece uses another canvas, scale the pixel values. Do not paste the fixed numbers onto a different frame.

`face` in `memory/config.md` controls the face rules. When `face` is `no`, skip every check whose only job is to keep captions off a face. Safe zones, cue length, and the no-fade cut still apply.

Why each choice was made is in `memory/feedback_animation_composite_preview.md`. The Pillow path, when ffmpeg has no `drawtext`, is in `memory/feedback-legenda-overlay-pillow.md`.

## When `face` is `yes`: never cover the face

This is stricter than the platform safe zone. It is the real position of the face in **this** recording. Framing changes between takes. A fixed `top` that was safe on a previous piece is not evidence.

1. Pull frames from the clean `base.mp4` (no captions) across **every** talking window, not one moment. A closer take puts the head at a very different height.
2. Snapshot the caption composite at those same times (`npx hyperframes snapshot --at <times>`). The PNGs come back with real alpha.
3. Composite the two (`ffmpeg overlay`) and look at the gap between the bottom of the caption and the top of the head on each frame. Check the tight framings, not only the typical one.
4. A tight gap or a touch means change size, position, or both before accepting the layout. Do not only shrink the type and assume that fixed it.

Halving the type size increases the gap when the caption stays vertically centered in the same 380px box (`top: 580` through `top: 960`). A smaller block shrinks toward the center of that box, so the lower edge moves away from the face. It does not only print smaller type in the same place.

Measure the worst case: mouth open, head tilted down. A neutral frame lies. A gap of about 0–20px is a fail. Do not ask for a pixel value. Measure, apply, and composite again (`memory/feedback_ask_dont_assume_creative_fixes.md`).

## Above and below

Same `.caption-block`. Only the container `top` changes.

- **Above** is the copy-paste default: `top: 580px`, just under the top unsafe band on this canvas (about 400px).
- **Below** is measured per take. It is not a number to copy. A closer framing can move the worst-case chin by hundreds of pixels, and a `top` that cleared a wide shot lands on the chest.

Derive `top` from the worst-case chin. `ffmpeg crop` plus a 100px `drawgrid` on about 8 frames of an open mouth or a lowered head, spread through the piece. On the reference canvas a one-line box of about 360px was the shape that kept a clearance of about 100px and still sat near the bottom safe line. Two lines push about 90px further down. Recompute. Do not inherit.

When the creator asks for captions that stay at the bottom and do not jump, the position is fixed for the whole piece. The fixed value has to clear the **deepest** overlay, not only the chin. Measure the real pixels of every full-screen card. Do not trust an old comment in the code. If that fixed position also enters the bottom unsafe zone, say so. The conflict is structural (a deep card against the platform safe zone), not a bad measurement. On this reference canvas the bottom unsafe band starts near y≈2614.

### Full-screen cutaways force a choice

When `face` is `yes` and the piece has full-screen cutaways (`memory/feedback_fullscreen_cutaway_production.md`) that occupy the lower frame, the below variant collides with them unless you choose:

- **Option A — move to the top only during those windows.** Comfortable clearance, and the caption stays out of the bottom unsafe zone. The caption changes place during the piece. Use this only when the creator asks for it.

```js
var FULLSCREEN_WINDOWS = [[START, END]]; // one pair per cutaway, from this piece
var inFullscreenWindow = FULLSCREEN_WINDOWS.some(function (w) {
  return cue.start >= w[0] && cue.start < w[1];
});
if (inFullscreenWindow) clip.style.top = "580px";
```

- **Option B — one fixed position, set from the deepest card.** Measure every cutaway. Take the worst case. Set `top` below it. The caption never moves. If the deepest card is very low, the caption can pass the bottom unsafe zone. **Flag that.** It is the creator's decision. Do not accept it silently.

Any piece that combines "captions below" with full-screen overlays has this choice. Do not assume. Use B only when the request is explicitly that the caption must not move.

## Other fixed overlays

When `face` is `yes`, any static overlay positioned with a fixed `top` (a pill, a badge, a seal) gets the same pixel check against the real face. Do not inherit an old `top`. A follow pill that was never measured against this take will hit the chin.

When captions are fixed at the bottom, put the CTA and badges above the head. That ends the fight for one region and avoids conditional caption logic. Aim for about 100px of clearance over the head after measuring this frame.

## CSS

Paste inside the caption composition's `<style>`. The caption face, off-white, **no background**. A light shadow so it reads on a face or a hand.

```css
.clip {
  position: absolute;
  left: 0;
  top: 580px;          /* ~17% of the height — under the top unsafe band (~400px on this canvas). Replace for the below variant after measuring. */
  width: 1920px;
  height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 120px;
}
.caption-block {
  display: inline-block;
  max-width: 1680px;    /* ~87.5% of the width, inside the side margin */
  color: #f7f5f0;
  font-family: "CAPTION FACE", serif;  /* the caption face from memory/visual_identity_standard.md; see memory/feedback-legenda-overlay-pillow.md */
  font-size: 60px;
  line-height: 1.3;
  text-align: center;
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.55);
  opacity: 0;
}
```

## Cues

- **At most 5 words per cue.** A wide caption spills out of the attention area. If a sentence is longer, split it and divide the time evenly across the parts. A long line about the object the creator is describing becomes two or three cues, each of 5 words or fewer. Five words beat full sentences. That is the standard.
- **Show the cues to the creator and get corrections before rendering.** The transcript misses names and fixed phrases only the creator knows. Apply `ferramentas/transcrever/glossario.json`. Do not invent the substitutions.

### Transcribe in sentences, not words

A first pass built from the word-level JSON (`-ml 1 -sow` on the whole file) lands captions with the wrong words and the wrong times. That pass has alignment holes: several words stamped on one timestamp, and the text collapses.

Transcribe **sentence segments** (the default, without `-ml 1 -sow`):

```bash
whisper-cli -m <model> -f full.wav -l <lang> -mc 0 --output-json
```

`<lang>` is the language of this recording. The sentences already come back caption-shaped, with stable times (checked against isolated windows of about 5 seconds: within about 0.2s). Then:

1. Apply word fixes inside each sentence from the glossary (mishearings, command names, proper nouns).
2. Split a sentence longer than about 3.7s or about 15 words. Break on `.` `?` `!`, then on a comma, then **before a conjunction** near the middle. In Portuguese those conjunctions are `e`, `para`, `ou`, `que`, `mas`, `com`, `quando`, `antes`. In English use `and`, `to`, `or`, `that`, `but`, `with`, `when`, `before`. Never split a multi-word name or a fixed pair that has to stay together. The split time is linear interpolation by character position (about ±0.3s, fine for a caption).
3. A fragment under 0.6s or of one word merges into a neighbor. Backward if it does not end a sentence, otherwise forward.

The script is `<piece>/edit/verify/gen_cues.py`. The transcript is `verify/seg_transcript.json`.

**Overlapping windows work poorly.** Words duplicate or disappear at the edges of the trusted zone.

Ad-format chunks of 1–3 words are a different delivery (`memory/feedback_video_editing_motion_graphics_ad_playbook.md`). They do not replace this spec.

## JS: no animation, an instant cut

No fade in or out. Use `gsap.set`, never `fromTo` or `to` with a duration, on captions.

```js
cues.forEach(function (cue, i) {
  var sel = "#cue-" + i + " .caption-block";
  tl.set(sel, { opacity: 1, visibility: "visible" }, cue.start);
  tl.set(sel, { opacity: 0, visibility: "hidden" }, cue.end);
});
```

## Collisions with other overlays

Captions run the whole piece. A short overlay (badge, stepper, card) can occupy the default `top: 580px`. Do not invent a permanent second position per piece. Override `top` only on the cues that fall inside that overlay's window.

```js
if (cue.start >= OVERLAY_START && cue.start < OVERLAY_END) {
  clip.style.top = BELOW_THE_PANEL; // under the panel, not through it
}
```

Test the **full** composite, every overlay together. A collision appears only when two overlays are up at once.

Option B (fixed, never moves) overrides this per-cue jump. If the creator chose B, do not push captions around per overlay. Clear the deepest card instead, and flag the safe-zone tradeoff.

## Vertical safe zone

Canvas 1080×1920, scaled in proportion to the real canvas: about 220px unsafe at the top, about 450px unsafe at the bottom (like, comment, and the platform's own caption), about 60–150px on the sides. The right-hand icon column is the tighter side. Keep text out of those margins. Reconfirm if the last check is more than about 2–3 months old.

On the 1920×3414 reference canvas the bottom unsafe band starts near y≈2614 and the top unsafe band is about 400px.

## Render and composite

```bash
# Real alpha. Never --format webm — ffmpeg decodes it opaque black even when the log claims alpha.
npx hyperframes render --format mov -o render_alpha.mov   # ProRes 4444, yuva444p12le

# Composite on the base. Repeat -itsoffset/-i per overlay and chain the overlay filters.
ffmpeg -y -i base.mp4 \
  -itsoffset 0 -i edit/animations/slot_captions/render_alpha.mov \
  -filter_complex "[0:v][1:v]overlay=enable='between(t,0,<total_duration>)'[out]" \
  -map "[out]" -map "0:a?" -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k \
  final.mp4
```

Quote `"0:a?"`. After a background render, **do not trust `ffprobe` duration alone**. A stale file can share the new duration. Recomposite to a new filename and check the content.

## Large face on a 1080×1920 screen recording

The spec does not scale onto a native **1080×1920** frame by proportion. Two things break.

**1. Size.** 60px at 1920 becomes 34px at 1080 by cross-multiplying. That is illegible when the face fills about half the frame and a screen image sits behind it. The reference size was validated on a small face. On this class of take, a boxed sans trial needed about **58px** and `top: 1650`. Recalibrate the serif on a real composite. Do not treat 58px as the size of your caption face.

**Calibrate size on a real composite of this take, not by scaling the canvas.** Always render a comparison of 2–3 sizes on a real frame before the full render.

**2. There may be no free band.** On this class of take the worst-case chin is about **y1620** and the bottom unsafe zone starts about **y1470**. They overlap. You cannot both avoid the face and stay inside the safe zone. That is structural. Offer three composites on a real frame and let the creator choose:

- A. On the chest, `top: 1650`. The platform name and the native caption may cover the bottom. Say that.
- B. Above the head, `top: 320`. This covers whatever description sits at the top of the frame.
- C. Shrink the video to 86% and open a black band.

Do not choose alone. When `face` is `no`, the chin collision does not apply. Still keep the caption inside the safe zone.

**3. One line by construction.** A second line pushes the box into the unsafe band. Measure each cue with the real font and split anything wider than about 940px. The reusable shape is a PNG per cue, a frame sequence by hardlink, and one `overlay` in ffmpeg, without HyperFrames. For a simple caption at a fixed position that is faster than a full composition. The script for a piece lives at `edit/captions/build.py`.
