# Motion-card layout (1080×1920, Lato 600)

The face in the title is the face these measures were taken on. Use the face in `memory/visual_identity_standard.md`. Re-measure line width when the face changes. Layout, sizes, and method stay. This card is one mold, not the only one. See `memory/direcoes-motion.md`.

Applies to every card overlay above the face. Reference implementation: the piece's `edit/overlays/build.py`.

`face` in `memory/config.md`: when `face` is `yes`, keep the card above the head. In the reference framing the head started near y510–520, so a card that ends near y500 cleared it. Remeasure this take. When `face` is `no`, skip the head clearance. The caption band stays empty either way.

## Box

Card at `left: 60`, `width: 960`, `top: 236`, radius 30, petroleum `rgba(30,58,71,.96)`, with a shadow. Max height about 262, so it ends near y500. The caption band (about y1400) stays free.

**Inner padding 40px** on everything (text on the left, the tag at the top, a bar label at `right: 40`). Minimum bottom margin about 28px. Nothing touches the bottom edge of the card. If it does not fit, drop a line (a list of 5 items becomes 4). Do not squeeze.

## Type

Title or phrase in Lato 600 (italic 600 for emphasis), 52–88px depending on the card. Tag in Inter 500, uppercase, amber, 30px. Support label in Inter 500, 30–32px. A number, an address, or a short monospace string is JetBrains Mono, 28–30px. Nothing under 28px. Below that it reads small in a 960px-wide preview.

Font files and the caption serif are `memory/feedback-legenda-serifada-hoefler-overlay-pillow.md`.

## Image cards

Image on the left, `width: 280`, `height: 262`, flush to the edge (rounded corners on the left only). Text starts at `left: 320`. The same size on every card so the frame does not jump.

## Diagrams

Arrow with a triangular head (`::after`). A dashed arrow uses a width that is a multiple of the step (32px) so it does not end on a fragment. The arrow label sits above. The number sits just under the solid arrow. A detail badge sits under the dashed arrow. The two nodes being compared are 220px wide, with 20px of clearance to the arrow. The nodes are the objects the creator is describing, not a second brand system.

## CSS gotcha

`.am{color}` declared before `.h1{color}` loses. An amber title needs an explicit `.h1.am`. Without it the title stays white and nobody notices in a small preview.

## How to review

Snapshot (`npx hyperframes snapshot --at ...`) composited on a real frame at 1080 wide, cropped to the band y200–620, one frame per card type. A contact sheet at 360px hides an edge collision and a label overlap.

## Standard motion

Every HyperFrames overlay uses the same entrance and exit. The helpers in `build.py` (`pop`, `grow`, `clip`) are the standard. Do not redesign them per piece.

- **Card, pill, or chip in:** drop 14px (`y: -14 → 0`) plus a fade (`autoAlpha 0 → 1`). **0.22s for a card, 0.18s for an inner item.** `power2.out`. Inner items stagger. Each one lands **on the word the line says** (the time in `transcripts/master.json`), never on an invented time.
- **Card out (never a hard disappear):** the mirror. Up 14px plus a fade, **0.22s, `power2.in`**, `fromTo` with `immediateRender: false`. Extend the clip 0.2s past the end of the line and play the exit in those last 0.22s, so the card holds the whole line and then leaves. Exception: another card enters immediately in the same place. Do not extend. The exit uses the end of its own clip.
- **Bars and meters:** `scaleX 0 → 1` (origin on the left edge), 0.6–0.9s, `power2.out`. Never animate `width`, except replacing a value that already exists, with `immediateRender: false`. A counter uses `textContent` with `snap` so a seek stays correct.
- **A single emphasis:** pulse `scale 1 → 1.18 → 1` (yoyo, 0.18s).
- **Opaque full-screen cut:** in and out **hard**, no opacity tween (it paints a gray frame). Only `scale 0.94 → 1` on the content. No exit animation. See `memory/feedback_fullscreen_cutaway_production.md`.
- **HyperFrames lint:** never `autoAlpha` on the `.clip` element. The framework owns that visibility. Animate the children (`#clipN > *`).

A repeated `fromTo` on the same target with the default `immediateRender` forces the second tween's start value from frame 0. Set `immediateRender: false` on the exit tween.

## Sound: a click on every animation

Clicks, not pops. `build.py` writes each animation event to `events.json`. `sfx.py` synthesizes `clicks.wav` (filtered noise plus a short sine, no pop).

- **`main`** is the click on each featured card or pill. **`soft`** is inner items (chips, lines, labels, bars) **and the card exit**. **`tick`** is a very quiet tick while a counter or a bar runs. **`cut`** is a full-screen cut (each scene in, and the final out).
- Every visible animation has a sound, and every sound has an animation. No orphan sound.
- **Level is measured against this piece's voice.** The click peak sits about 17dB under the voice peak, near the voice average. Measure with `volumedetect` or `ebur128` first. Worked results, not constants to copy: a voice averaging −26.8dB with a peak of −7.9dB used `PEAK = 0.038`. A voice at −19 LUFS used `0.075`. Mix in ffmpeg with `amix=inputs=2:duration=first:normalize=0`.
- No music bed unless the creator asks. Then use the `media-use` skill (`memory/feedback_video_editing_recording_patterns.md`).

## Review before the preview

1. Lato 600 on motion, Hoefler only on captions.
2. Cards from y236 to about y500. Nothing within 28px of the bottom edge. Type at least 28px. When `face` is `yes`, the card clears the head.
3. **Entrance and exit are animated** on every card. A hard full-screen cut is the only exception.
4. A sound on every animation, level measured against this voice.
5. Pacing audit: a new stimulus at least every 2–3 seconds. Captions do not count. Wider gaps go to the creator (punch-in or b-roll). See `memory/feedback_video_editing_alex_hormozi_benchmark.md`.
6. Full-screen scenes: the caption band is empty, and the in and out are hard.
7. The preview is composited on a real frame, not judged alone. The contact sheet is large enough to read. `ffprobe` the delivered file.
8. A real screenshot the creator did not supply is a mock. Say so.

## Final 4K 60fps overlay

- Alpha at 4K: `FFMPEG_ENCODE_TIMEOUT_MS=7200000 npx hyperframes render --format mov --resolution portrait-4k --fps 60 -o render_alpha_final4k.mov`. Without the environment variable the ProRes 4444 encode dies at 700s (`ffmpegEncodeTimeout`). About 10,500 frames: capture near 13 minutes plus encode near 12 minutes on an idle machine (about 5.8GB). Another observed overlay of this class was about 13 minutes of render plus about 6 minutes of composite, 392MB at 41Mbps. Plan for that. Do not start it unless the creator has asked for full resolution.
- Another heavy render on the machine multiplies the time and has killed the job with exit 137 (SIGKILL). Before a long render: `ps -eo pid,etime,command | grep "hyperframes render"`. If another is running, wait or say so. Never a generic `pkill -f "hyperframes render"`. That matches everyone else's render. Filter on this job's `-o <filename>`.
- A background render is a direct command. `a && nohup b &` is cancelled with `render_cancelled_parent_exited`. A subshell `( ... ) &` is cancelled when the parent exits. Chain `render && compor_final.sh` in the same command. Waiting on `pgrep -f "hyperframes render"` matches the wait script itself and loops forever.
- 4K captions: an `ffv1` layer with alpha (`captions_final.mkv`, about 0.9GB) built from Pillow PNGs through the concat demuxer. Hoefler Regular, index 0, 62px at 960 (×2.25), center y=1250 at 960. **One line** (width measured with that font, at most 790px at 62px) and a break that does not end on a function word. The same `build.py` at font 140 on a 2160×3840 canvas at 60fps is the 4K caption pass.
- Final assembly: `libx264 -preset slow -crf 14` plus `-c:a aac -b:a 320k`. About 0.15× realtime (about 20 minutes for 2:54), about 1.25GB (about 57Mbps).

## Variety

A card that is only a title and chips on the petroleum box is weak. **Every spoken stretch that names a concrete object, tool, or list gets an image, a screenshot, or a small graphic**, not text the caption already says.

- **A real screenshot from headless Chrome:**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --force-device-scale-factor=2 --window-size=1200,H \
  --virtual-time-budget=9000 --screenshot=x.png "$URL"
```

`$URL` is the page the creator is describing (a doc, a listing, a public page). Crop with PIL to the part that matters. Highlight with an amber box (`.hi`). Rankings and icons change by day. The crop is of that date. Open the PNG and confirm it shows the object the creator is describing before it goes in.

- **CSS graphics** when there is no screenshot: a small sheet, speech bubbles, `tile → arrow → icon`, a file window, a progress bar, tiles that light on the spoken word.
- A large screenshot is an opaque full-screen scene. Everything else is a card at the top. Invented content is told to the creator.
- HyperFrames lint: a loose child needs `position: absolute` (only `.card > *` inherits it). A duplicate `id` across scenes makes GSAP animate the wrong element.
