# Multi-source frame rate is the lowest source

When an edit uses more than one source and the frame rates differ, the final file uses the **lowest** rate. A 30fps talking shot plus a 60fps screen recording finishes at **30fps**.

Raising a slow source to match a fast one duplicates or interpolates frames. That adds weight, not information. Dropping the fast source to the shared minimum stays consistent and avoids judder. Short vertical video is usually 30fps as well.

Sibling rule: a sped-up export keeps the original rate (`memory/feedback-video-speed-versions.md`). Output rate for a single source is the source rate (`memory/feedback_video_editing_recording_patterns.md`).

## How to apply

- `render.py` in `local-video-use` detects the source fps and snaps to the nearest broadcast standard. `--fps` overrides. For several sources, take the **minimum** across `edl.sources`, or pass `--fps` as that minimum.
- When the creator assembles insets in their own editor, tell them the target rate (the minimum) so the timeline matches.
- Before deciding, run `ffprobe -select_streams v:0 -show_entries stream=r_frame_rate` on each source.
