# prep-frames

Contact sheet (ffmpeg) plus OCR and faces (Apple Vision, `vision.swift` compiled to `.vision` on first run) written to a one-page `resumo.md`. Read `resumo.md` and `sheet.jpg` instead of every raw frame. Open `frames/fNN.jpg` only to adjust an overlay.

```bash
ferramentas/prep-frames/prep-frames video.mp4 [-n 9] [-o folder]
```

Needs ffmpeg, swiftc, and sips. No extra install.
