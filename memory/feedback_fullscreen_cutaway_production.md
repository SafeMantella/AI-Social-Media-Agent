# Full-screen cutaways

A full-screen graphic replaces a stretch of the talking shot so the frame does not sit still. The creator cuts and returns `base.mp4`. The agent does not recut that file. The agent proposes cutaway windows, builds the graphics, and composites them.

`face` in `memory/config.md`: when `face` is `yes`, a cutaway takes the face off screen for that span. Use it on purpose, not as the default format. When `face` is `no`, the same graphics are still full-screen b-roll, and the face rules below do not apply.

Slots live in `edit/animations/slot_*`.

## 1. Where a cutaway goes

This is the cutaway step in `memory/feedback-video-editing-pipeline.md`. Do it every time, not only when asked.

A candidate has all of these:

- The line describes something concrete and visual (an object, a process, a list), not an opinion and not a transition.
- The stretch is at least 5 seconds.
- When `face` is `yes`, it is not the hook, the CTA, or an identity beat.
- The graphic starts on the visual payoff, not on the setup sentence.

Read the whole transcript (`beat_offsets.json`, `captions_cues.json`) before suggesting anything. Do not pick windows by skimming.

When `face` is `yes`, do not replace the hook (the first 5–6 seconds) or the close. Those beats need eye contact. Replacing them works against retention.

Start each cutaway a few seconds after the topic actually begins. The setup stays on camera when `face` is `yes`. The graphic takes the payoff: the consequence, the example, the explanation. Applied on every window, that also leaves a face beat between two graphics. Do not compute a separate gap by hand. When `face` is `no`, still start on the payoff so a graphic is not glued to a transition line.

List the candidates (timestamp, duration, concept) and let the creator choose. When `face` is `yes`, say what share of the runtime would have no face. Do not assume they want every candidate. Do not build the set before that choice.

## 2. Design from the real line

Every beat (an element appearing or changing) lands on a real speech time in `captions_cues.json`, word-group timed. Not on an invented time. A label appears when the line says that thing.

Reuse chrome when the concept is the same. A file shares one chrome: a title bar with dots, a folded corner, JetBrains Mono. Only the icon, the name, and the content motion change. A different concept (one word with icons converging, or an app window) gets a new visual family. Two or three families read richer than one generic card repeated.

A full-screen cutaway is **opaque**. It replaces the frame. It is not a translucent overlay. No alpha. No exit tween. Hard in, hold, hard out, like b-roll.

Leave the caption band empty. On the 1920×3414 reference canvas that band is `y[580,960]`. Captions are composited later, as their own pass.

The graphic should look like a real app window, not an abstract composition. Title bar, traffic-light dots, an address pill, a card frame. Minimal and vague fails.

Label every element. Do not leave the meaning implicit. A bar, a bubble, an icon, or a meter gets a short label ("the object", "limit", "current"), synced to that beat.

A card that stands for a file being edited needs four editor signals, not a white panel:

1. A title bar with three graphite dots.
2. A line-number gutter (`01`, `02`, `03`…), one number per content line.
3. Monospace content (JetBrains Mono).
4. A ghost line at the end with a blinking cursor, so it still looks in progress.

A line number at `rgba(51,56,61,0.32)` fails WCAG AA. `hyperframes check` catches it. Use solid `#8d8e8d`.

## 3. GSAP and HyperFrames

Apply these on the first build.

- A hard-cut entrance never tweens opacity up from 0. Even at 0.08–0.3s, one or two fractional frames mix the element color with the background and read as a glitch. The element is opaque in CSS at frame 0. Only `scale` is the entrance accent. Scale does not mix color. Detail and the frame test are in `memory/feedback_animation_composite_preview.md`.
- A meter or a fill animates `transform` (`scaleX` or `scaleY`, `transform-origin` on the edge). Never `width`, `height`, `top`, or `left` directly.
- **`gsap_css_transform_conflict`.** Once any tween touches `transform`, GSAP owns the whole property. If one axis is already tweened (`scaleX` via `fromTo`) and a later impact must pulse another axis (`scaleY`), use `fromTo` and set both axes. A partial `.to()` can drop the axis it does not mention.
- A marker or label that overhangs a container with `overflow: hidden` disappears with no error. Keep the marker inside the container's box, or make it a normal flex item outside the clipped container. Do not absolutely position an overhang inside something that clips.
- `content_overlap` and `content_overflow` from `hyperframes check` can be intentional (icons converging into a word). Set `data-layout-allow-overlap` or `data-layout-allow-overflow` on the right element instead of redesigning to silence the warning.

## 4. Verify on the real video, in this order

Full history of the rule is `memory/feedback_animation_composite_preview.md`. The order that works:

1. Cut a test span from a **clean** `base.mp4` (no overlay, no burned-in captions) around the real cutaway time. Never use a finished composite as the test base.
2. Cut the matching span of the caption alpha (`edit/animations/slot_captions/render_alpha.mov`).
3. Composite in this order: the opaque graphic at the exact time, then the captions on top of everything. Captions are the last layer. Testing on a file that already has captions under the opaque card hides the captions completely.
4. Extract frames every 30–40ms near each entrance and exit. A contact sheet stepped by a second misses a flash.
5. If the file is over the send limit, compress before sending (`scale=960:-2`, crf 24).

## 5. Creative changes

Vague feedback ("this is confusing", "too minimal") gets a multiple-choice question before a redesign. Ask what is wrong: the relationship between elements, the hierarchy, or type that is too small. Then rebuild. A spatial collision is the other case: measure it, do not ask for a pixel value (`memory/feedback_ask_dont_assume_creative_fixes.md`).

Expect more than one pass. Each pass is about 5–10 minutes because the cycle is short: build, lint, check, snapshot, render, composite test.

## 6. Final assembly

After each cutaway is approved, reassemble everything in this order: clean `base.mp4`, then each cutaway slot (`-itsoffset` at the real absolute time, `overlay=enable='between(t,start,end)'`), then the CTA, then captions last.

One ffmpeg command can chain every overlay: N inputs (`-itsoffset X -i edit/animations/slot_*/render.mp4`) and a chained `filter_complex`. Separate passes are not required. Five to seven layers on a 1920×3414 canvas of about 140s takes more than 2 minutes. Run it in the background and log to a file. Do not use the foreground timeout.

The final check does not repeat the frame-by-frame boundary test. That already ran on these same render files. A contact sheet with about one frame per cutaway and one frame per talking stretch, spread across the timeline, is enough to confirm the assembly (offsets and order). That is the only new risk at this step.
