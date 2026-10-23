# Caption alpha track

Contract only. The caption spec stays `memory/hyperframes_caption_style.md`. This file is the ffmpeg track that one copy used when the caption is a transparent movie over the cut. The face comes from `memory/visual_identity_standard.md`. Re-measure width when the face changes.

`build_cues`, as measured on that copy:

- At most 3 words per cue. The standing caption rule is still 5 until this 3 is re-measured.
- Break on punctuation and on a pause.
- Join a short orphan word to its neighbor.
- Each cue lasts until the next one starts, and at most 0.4 seconds longer, so it does not blink.
- The caption is absent in any window where a plate is on screen.

`build_track`: one PNG per cue, assembled into a `mov` with alpha, then overlaid.

Do not hardcode a font file path from another machine.
