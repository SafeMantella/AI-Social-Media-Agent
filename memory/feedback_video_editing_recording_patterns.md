# Recording setup and edit preferences

The creator records many takes of the same line, sometimes with long pauses, sometimes with a restart in the middle. The creator cuts and returns `base.mp4`. The agent does not cut and does not suggest cuts. Silence measurement, when that job is assigned, is `memory/pipeline-limpeza-audio-corte-silencio.md`.

`face` in `memory/config.md` gates every rule that only exists to keep a face visible or uncovered. When `face` is `no`, skip those rules.

## Render facts

**Output frame rate is the source frame rate.** `render.py` in the `local-video-use` skill detects the source fps, snaps to the nearest broadcast standard, and `--fps` overrides. Do not leave a hardcoded `-r 24` on a higher-rate source: the step down judders a talking shot, and 24 is not the usual rate for short vertical video. After any render, check `ffprobe` `r_frame_rate` on `base.mp4`. Multi-source pieces use the lowest source rate (`memory/feedback-video-lowest-fps.md`).

**Assembled duration is not the sum in `edl.json`.** A concat that fades and snaps frames runs about 0.8s long once many segments add up. Never size captions, music, or a slot from the EDL total. `ffprobe` the rendered file.

**Quote `-map "0:a?"`.** The `?` makes the audio stream optional to ffmpeg and is also a zsh glob. Unquoted, zsh expands `0:a?`, finds nothing, and aborts with "no matches found" before ffmpeg runs. Quote any map specifier that contains `?`.

## Post order

Fixed order: record, then the creator's cut (`base.mp4`), then visual variations, then motion graphics, then captions last.

Visual variations are anything that changes the base image itself (zoom, punch-in, reframe, speed ramp, an extra grade). Apply them only when the creator asks, and only on the clean cut, before any overlay. Scaling a frame that already has burned-in type or a pill resamples that UI: edges double or warp. If the zoom changes later, every overlay would have to be built again.

In `local-video-use`, zoom is `scale(eval=frame)` plus `crop`. Crop alone reads `w` and `h` once, at init. Only `x` and `y` update with `t`.

On this project the clean cut is `base.mp4`. A zoomed pass is `edit/final_vN_zoomed.mp4`. Motion slots in `edit/animations/slot_*` and the captions are composited after that.

## What not to delete

Do not delete a rendered `.mp4` or `.mov` until the creator says the piece is finished and that a backup exists. That includes superseded versions, intermediates, and files with a known bug (`final_vN.mp4`, `final_animado_vN.mp4`, `*_zoomed.mp4`, a slot `render_alpha.mov`).

Notes that say "safe to delete once a version is approved" are obsolete. If the disk fills up, ask. Do not decide.

After the creator names the cleanup, remove only those folders. Use trash, never `rm`. Do not touch the raw `master.mp4`, the clean `base.mp4`, or the approved deliverable unless the creator names those files.

Generated video stays in the piece's `edit/` folder. See `memory/feedback-generated-video-in-project.md`.

## Full-length preview

`scale=960:-2`, crf 24 is calibrated for a 20–30s clip. On a full piece of about 150s that preset can pass 49MB, over the 30MB send limit. For a full-length preview use `scale=720:-2`, crf 28, audio 96k (about 18MB for 150s). If it still will not send, raise crf (30 or higher) and retry. Do not assume the short-clip preset fits every duration. Full resolution waits until the creator asks for it.

## Music bed under speech

The `media-use` audio engine sizes a bed from synthesized speech lines. A talking piece has no synthesized speech, so that path does not deliver. If the default provider is not configured, call `generateBgmDetached()` in `media-use/audio/scripts/lib/bgm.mjs` with `durationS` set to the real duration (`ffprobe`, never the EDL sum) and `hasVoice: true`. The engine then picks volume `0.12` (about 18dB under the voice).

It runs MusicGen (`facebook/musicgen-small`, local, no API) as a detached process and writes `assets/bgm/track.wav` at the exact duration, mono 32kHz. Mix with `ffmpeg amix=inputs=2:duration=first:normalize=0` and `[bgm]volume=0.12`. Check `mean_volume` near −17dB.

Before generating, reuse an existing instrumental bed when the mood already matches. Generate a new one only when it does not.

## Two production modes

Pick the mode from the subject, not from a deadline.

- **Dense (default).** Tight cut, screen recording, on-screen text, and the rest of this pipeline. Use it when the piece has to carry a lot of concrete information. The creator still makes the cut.
- **Light.** Minimal setup, few cuts, a fast edit. Behind-the-scenes, opinion, reaction, a trend. Density is not the point. A single take is not required.

Do not hollow a dense edit to hit a publishing count. Drop a piece instead.

## Recording setup

Update this section when a new physical-setup observation holds for the next recording. Do not start a second note.

- **One static shot for the whole piece is the main retention risk.** No angle change, punch-in, or b-roll means the frame at the end matches the frame at the start. Watch time needs a pattern break every few seconds (`memory/feedback_video_editing_alex_hormozi_benchmark.md`). Plan the variation while recording: pause and reframe between sections, or record a second take closer or wider to intercut. Two cameras are not required.
- **The background follows the visual identity.** A dominant neon or high-saturation light fights `memory/visual_identity_standard.md`. Close it out of frame, change the angle, or test the room light before recording the whole piece.
- **When `face` is `yes`:** put the camera at eye level. Looking down or to the side reads as a camera below the eyes. An uncurated background competes with the face. Neutral or intentional is enough. It does not need to be a studio.
- **Record a spoken close.** The last 3–5 seconds ask for the follow or the comment out loud. On-screen text can repeat it. Two channels beat one. A text-only close is the fallback, not the default.

Caption style is `memory/hyperframes_caption_style.md`. Composite previews are `memory/feedback_animation_composite_preview.md`. If a recording checklist lives in the content system, update it when this section changes. This note is the source.
