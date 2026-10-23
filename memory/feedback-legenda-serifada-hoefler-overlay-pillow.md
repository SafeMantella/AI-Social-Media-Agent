# Caption serif and Pillow overlays

The faces named below are the faces these measures were taken on. A brand with another face uses `memory/visual_identity_standard.md`. Do not copy the face name, or a font file path from another machine, into a new piece. Keep the layout, the measures as a starting point, and the method. Re-measure width when the face changes.

## Current type

- **Motion (title, hook card, pill, cutaway, overlay):** **Lato SemiBold 600**. Italic is Lato SemiBold Italic. The Google Fonts cut of Lato has no 600 (only 400, 700, and 900). SemiBold comes from the Lato 3 source: `Lato-Semibold.ttf` and `Lato-SemiboldItalic.ttf`. Put them in the piece's `edit/overlays/fonts/`. Inter 500 is support only (tag, label, chip). JetBrains Mono 500 is only for a number, an address, or a short monospace string. Sora stays off motion.
- **Captions:** **Hoefler Text**, the weight used on CTA videos: `Hoefler Text.ttc` **index 0 (Regular)**, loaded with `ImageFont.truetype(FONT, size)` and no index. The file on this system is `/System/Library/Fonts/Supplemental/Hoefler Text.ttc`. Off-white `#F7F5F0`, **no background**, a light shadow for legibility.
- Card layout and motion animation are `memory/padrao-cards-motion-lato.md`.
- **Carousel type does not follow motion.** Titles stay Sora. Body stays Inter.

An earlier rule put the serif on every motion element. That is retired. Motion is Lato 600. The serif is captions only.

To compare font options, render **one** image with every candidate on a real frame. Do not render a separate preview per face.

## List layout and normal captions

A "list" piece stacks each item as it is spoken. The stack can sit on the frame, then clears at the end of the list and normal captions return. On a 960-wide canvas the line spacing is 1.4 and the gap between items is 34px. Shorten a long on-screen label when that helps. The object the creator is describing can use a short label instead of the full name.

When `face` in `memory/config.md` is `yes`, that list stack may cover the face while it is on screen. Normal captions must not. When `face` is `no`, there is no face to clear.

Normal captions: at most 5 words per cue. When `face` is `yes`, center them below the chin (about 73% of the height) after measuring this take (`memory/hyperframes_caption_style.md`). When `face` is `no`, place them in the safe area. Do not inherit a chin position from another piece.

## Pillow when ffmpeg has no drawtext

Build the overlays as transparent PNGs with Pillow (text plus a shadow via GaussianBlur) and chain `overlay=enable='between(t,a,b)'`. Preview at 960px wide. The final frame is 2160×3840, so scale every measure by 2.25. Final encode: libx264, crf 15, `-c:a copy`, bt709 tags. `build.py` lives in the piece's `edit/preview/`.

## Gotcha

On a long list, the last line can pass the vertical safe zone (about 82% of the height against a safe line near 77%). If the layout is reused, narrow the width or reduce the spacing. Do not assume the last line is inside the zone because the first lines are.
