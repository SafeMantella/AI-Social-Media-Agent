---
description: Correct an overlay that is already composited on a video in this folder. Measure in pixels, fix, re-render, reassemble, and write down the lesson.
---

# Refine an overlay on a video that is already composited

Read this file and follow it. It is a workflow.

## When to use it

The creator corrected something already rendered on a video in this folder (`gravações/.../edit/`) — wrong position, an overlap, wrong text, wrong color. This workflow is the full cycle: measure for real, correct, re-render, reassemble, verify, document. If the request does not describe the problem clearly enough, ask before measuring anything.

Read `memory/config.md`. When `face` is `no`, do not use the face as a spatial constraint. Captions still go on. Do not add a cutaway whose job is to hide the face.

## Rule: a spatial fix is measured, a style fix is asked

Full criterion: `memory/feedback_ask_dont_assume_creative_fixes.md`. Practical split:

- **"Lower it", "take it off this", "it covers X", "keep it fixed, do not move it"** → spatial. The direction and the success test are already clear. Only the measurement is missing. **Never ask "how many pixels".** Measure a real frame and calculate.
- **"Change the style", "that color", "that wording", "this is confusing"** → style or content. More than one reading is reasonable. Ask with concrete options before implementing.

## Steps (spatial — the common case)

1. **Find the affected slot** in `animations/<slot>/index.html`. If it is not obvious which slot, read `project.md` (it lists the pipeline layers with their offsets and time windows) before asking the creator.
2. **Name the real constraint** — what the overlay must avoid (the face or chin when `face` is `yes`, another overlay, the platform unsafe zone) and in which time windows it exists. When `face` is `no`, skip the face.
3. **Measure. Do not estimate.**
   - Extract real frames (`ffmpeg -ss <t> -i base.mp4 -frames:v 1 ...`) spread across EVERY relevant window, not only the moment that prompted the complaint. The worst case is usually somewhere else (a lower chin with the mouth open, a taller card on another cutaway).
   - Do not trust a number in an old code comment, or a measurement from a previous version. Measure again whenever the value will drive a new decision.
   - Use a ruler overlay in Python/PIL (a line every 20–40px plus a label of the real y) so the position is read, not guessed.
   - If the overlay competes for space with other elements on screen at the same time (another cutaway, a CTA, a stepper), measure the worst case of EACH of them, not only the one that prompted the complaint.
4. **Calculate the new value** with a margin that can be defended (in practice about 50–150px, depending on how much the scene moves between takes) from the worst case you measured, not from the typical case.
5. **If a real trade-off has no clean answer** (the only position that clears everything enters a platform unsafe zone) — apply it anyway when the instruction is clear, and **flag the trade-off in the delivery**. That is not a reason to stop and ask. It is information the creator needs.
6. **Edit** the slot CSS or JS. Comment why the value is what it is (the measurement, not only the number).
7. **Lint and check:** `npx hyperframes lint .` and `npx hyperframes check .` inside the slot folder. Zero errors before a render.
8. **Verify by compositing before a high-quality render.** `npx hyperframes snapshot --at <times>` (one time per critical window), then composite with `PIL.Image.alpha_composite` on the matching real frame (the frame from `base.mp4`, or from the cutaway that is active at that time — never the isolated snapshot on a transparent background). Apply the ruler again and confirm real clearance, with no overlap, at the tightest points.
9. **Render in the background** (`npx hyperframes render --format mov -o render_alpha_vN.mov`, output redirected to a log). Long composites take more than 2 minutes. Watch the process until it exits. Do not poll by sleeping in the chat.
10. **Reassemble the whole pipeline.** Reuse the layer list and offsets documented in `project.md`. Do not rediscover them. Swap only the render of the slot you fixed. Leave the rest. **Captions are always last** (top layer). This step is a preview (`scale=960:-2`, crf 24) until the creator asks for full resolution.
11. **Remix audio or music if the video has it** (same command and volume as the previous version, documented in `project.md`).
12. **Check the final file** (`ffprobe` so the duration matches the previous version, plus a real frame extracted at the points you corrected — not duration alone).
13. **Remove intermediate files that this round superseded** (the previous "no music" version, old renders nothing references anymore). Do not leave a new pile on every round. Do not delete `base.mp4`, `edl.json`, `project.md`, `transcripts/`, or the slot HTML.
14. **Compress a preview** (`scale=960:-2`, crf 24, aac 128k — the project default) and send it. In one or two sentences, say what changed and cite the numbers you measured. Do not say only "fixed".
15. **Write it down.**
    - The video's `project.md`: a new chronological entry with what was measured, the new value, and any trade-off.
    - The relevant file in `memory/` (`hyperframes_caption_style.md` for a caption, `feedback_fullscreen_cutaway_production.md` for a cutaway, or a new file if this element type is new). Save only the reusable lesson (the pattern, not this video's pixel value).
    - If the round reveals a new pattern about HOW to work, not about this video, update `memory/feedback_ask_dont_assume_creative_fixes.md`. Project memory stays in `memory/`. Do not write it into a tool's private memory.

## If the request is not spatial

Use the same render, reassemble, and document cycle, but replace step 3 with concrete options before editing anything.
