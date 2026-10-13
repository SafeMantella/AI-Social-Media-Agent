# Sped-up versions

When the creator says the piece is approved, **ask whether to render sped-up versions**. Do not wait to be asked. If they say yes, render 1.1× and 1.2× by default, as separate files, and leave the original untouched.

1.1–1.2× on a talking shot is a retention tactic. It shortens the piece without removing content.

The creator still owns the cut. These versions only change playback speed of the approved file.

## How to apply

- **The sped-up file uses the original frame rate.** If the original is 30, the export is 30. Do not let `setpts` push it to 33 or 36. Read the rate with `ffprobe`. Never hardcode 30. Sibling rule: `memory/feedback-video-lowest-fps.md`.
- Render from **`base.mp4` plus the caption layer**, not from an already compressed final. That avoids a second x264 generation.
- Put the captions **before** `setpts`. They speed up with the picture and stay in sync by construction.
- Audio uses `atempo=<factor>`. That keeps the pitch. `asetrate` does not.

```bash
FPS=$(ffprobe -v error -select_streams v -show_entries stream=r_frame_rate -of csv=p=0 base.mp4)
for s in 1.1 1.2; do
  ffmpeg -i base.mp4 -framerate "$FPS" -i captions/seq/f%05d.png \
    -filter_complex "[0:v][1:v]overlay=0:<top>:shortest=1,setpts=PTS/${s}[v];[0:a]atempo=${s}[a]" \
    -map "[v]" -map "[a]" -r "$FPS" -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p \
    -c:a aac -b:a 256k -movflags +faststart "FINAL-${s}x.mp4"
done
```

`<top>` is the caption overlay y for this piece.

**zsh:** `PTS/$s[v]` is parsed as an array index and the value disappears from the filter. Always use `${s}`.
