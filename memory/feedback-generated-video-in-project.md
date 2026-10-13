# Generated video stays in the project

Every video file the agent renders for a piece — the clean cut, previews, motion-slot renders, short review clips, a clip flagged for the creator to hear, final masters — **is saved inside the project**, in the `edit/` folder of that recording (`gravações/.../<piece>/edit/`). Use a subfolder when it helps: `edit/trechos-revisao/`, `edit/animations/`. **Never** leave a generated video in the session scratchpad or in `/tmp`.

The scratchpad and `/tmp` are only for a disposable **non-video** working file (analysis JPGs, a trimmed WAV for a fresh transcription). Delete those when the step is done.

This extends Hard Rule 12 of the `local-video-use` skill ("session outputs in `<videos_dir>/edit/`") to review clips and short excerpts, not only `base.mp4`, `preview.mp4`, and `final.mp4`.

It also matches the edit pipeline: a generated video in the project **is not deleted** until the creator says the piece is finished **and** a backup exists, and then only the folders the creator names. Always trash, never `rm`, for `.mp4` and `.mov`.

When sending a short clip, render it in the project's `edit/` and send that file. Do not render it in the scratchpad only to send it.
