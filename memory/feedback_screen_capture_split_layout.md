# Sliding split for screen capture

When `face` in `memory/config.md` is `yes`, a stretch that shows a screen uses this sliding split. An opaque full-screen cutaway (`memory/feedback_fullscreen_cutaway_production.md`) would take the face off and drop the connection. The split shows the screen and keeps the face in frame the whole time.

When `face` is `no`, skip this layout. Show the capture full frame. The split exists only to keep a face on screen.

This assembles a screen band over the creator's `base.mp4`. It does not recut `base.mp4`.

## Layout

Canvas 9:16. The reference size is 1920×3414 (a 9:16 frame at the scale used for that master). During the capture stretch:

```
┌───────────────────────┐ y 0
│   CAPTURE (full frame, │  top band ≈ 31%  (1920×1084, from 1360×768 scaled to 1920 wide)
│   no region crop)      │  the cursor stays visible on clicks
├───────────────────────┤ y 1084
│                        │
│   FACE (base, NOT      │  bottom band ≈ 69%
│   resized, shifted     │  the base moves down by D≈300px (about 9% cropped at the bottom:
│   down by D≈300px)     │  a low resting hand; a gesture at chin height stays in frame)
└───────────────────────┘ y 3414
```

- **The capture is the full frame.** Cuts between moments, plus a speed ramp so the action fits the line. Do not crop "the app window" and scale it up. The creator wants the whole screen, at the original resolution.
- **The face is not resized.** It only moves down. `D` is a spatial measurement against the first composite frame: chin and mouth clear of the capture edge. Measure it. Do not ask for a pixel value (`memory/feedback_ask_dont_assume_creative_fixes.md`).
- Outside the capture stretch, the frame is the full face and the base is untouched.

## Transitions, 0.5s, sliding

- **In.** The capture slides down from the top (`y: -1084 → 0`). The face moves down with it (`y: 0 → D`). The capture looks like it pushes the face down.
- **Out.** The capture slides up off screen (`y: 0 → -1084`). The face returns (`y: D → 0`).
- **No black gap** as long as `D` is less than the capture height. During the ramp the bottom of the capture moves down faster than the top of the face comes up. Proof: `2·1084·τ ≥ 2·D·τ`.

## Where the stretch starts and ends

Measure real T0 and T1 on frames of the base. Do not trust the nominal EDL time. The 30ms fades in `render.py` drift about +0.07s per 8 cuts. Extract tiles at 30fps around the expected cut and find the frame where the pose actually changes.

## ffmpeg

- **Overlaying `[0:v]` on a generated source (`color`) requires `setpts=PTS-STARTPTS` on `[0:v]`.** Without it the timestamps do not match and the overlay vanishes with no error. The output is only the generated background.
- **Do not `setpts` the capture input.** It comes in with `-itsoffset T0`, and `setpts` zeroes that offset.
- **A window test that seeks with `-ss` on the base and also uses `setpts` is a false negative.** The timeline becomes 0-based and the ramp expressions take the "before T0" branch, so the capture never appears. Test without a seek on the base. Limit with `-t`, or render the whole span.
- **Re-encode each beat.** `-c copy` sticks to keyframes and the sync drifts across the supercut.
- The final composite is one ffmpeg: `color black[bg]`, then `[bg][face]overlay y=FACE_Y`, then `[s1][sr]overlay y=SR_Y enable='between(t,T0,T1)'`. On 1920×3414 for about 150s this takes about 2 minutes. Always run it in the background (`memory/feedback-generated-video-in-project.md`).

## Accepted tradeoff

A full frame in a 31% band makes the screen text small and shows a lot of empty wallpaper. That is the standard anyway. The priority is the face plus the real context, not the legibility of the screen text. Motion graphics and the captions carry what has to be read.

## Reuse

`edit/verify/build_insets.py` is the template. A `BEATS` table of `(out_rel_ini, out_rel_fim, src, src_ini, src_fim)` with no crop. `face_y_expr()` and `sr_y_expr()` hold the ramps. `T0`, `T1`, `D`, `RAMP`, and `SRH` sit at the top. Copy it and refit the beats and T0/T1 for the new piece.
