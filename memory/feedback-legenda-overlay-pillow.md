# Caption face and Pillow overlays

The measures below were taken on one creator's faces (listed at the end as an example). A brand uses its own faces from `memory/visual_identity_standard.md`. Do not copy a face name, or a font file path from another machine, into a new piece. Keep the layout, the measures as a starting point, and the method. Re-measure width when the face changes.

## Current type

- **Motion (title, hook card, pill, cutaway, overlay):** the **motion face** in `memory/visual_identity_standard.md`, semibold, with its italic for emphasis. Check that the weight you need exists in the font family you installed (a web-font download may lack it). Put the font files in the piece's `edit/overlays/fonts/`. A support face (tag, label, chip) and a monospace face (a number, an address, a short monospace string) come from the same file. The title face of a carousel does not follow motion.
- **Captions:** the **caption face** in `memory/visual_identity_standard.md`, regular weight, loaded with `ImageFont.truetype(FONT, size)`. A `.ttc` collection needs the right face index, so check it. Off-white text with **no background** and a light shadow for legibility; take the exact off-white from the visual identity file.
- Card layout and motion animation are `memory/padrao-cards-motion.md`.


Keep the caption face on captions only. Motion elements use the motion face.

To compare font options, render **one** image with every candidate on a real frame. Do not render a separate preview per face.

## List layout and normal captions

A "list" piece stacks each item as it is spoken. The stack can sit on the frame, then clears at the end of the list and normal captions return. On a 960-wide canvas the line spacing is 1.4 and the gap between items is 34px. Shorten a long on-screen label when that helps. The object the creator is describing can use a short label instead of the full name.

When `face` in `memory/config.md` is `yes`, that list stack may cover the face while it is on screen. Normal captions must not. When `face` is `no`, there is no face to clear.

Normal captions: at most 5 words per cue. When `face` is `yes`, center them below the chin (about 73% of the height) after measuring this take (`memory/hyperframes_caption_style.md`). When `face` is `no`, place them in the safe area. Do not inherit a chin position from another piece.

## Pillow when ffmpeg has no drawtext

Build the overlays as transparent PNGs with Pillow (text plus a shadow via GaussianBlur) and chain `overlay=enable='between(t,a,b)'`. Preview at 960px wide. The final frame is 2160×3840, so scale every measure by 2.25. Final encode: libx264, crf 15, `-c:a copy`, bt709 tags. `build.py` lives in the piece's `edit/preview/`.

## Gotcha

On a long list, the last line can pass the vertical safe zone (about 82% of the height against a safe line near 77%). If the layout is reused, narrow the width or reduce the spacing. Do not assume the last line is inside the zone because the first lines are.

## Example: the faces these measures came from

One creator's motion face was Lato SemiBold (the Google Fonts cut has no 600; it came from the Lato 3 source files). Their caption face was Hoefler Text, `.ttc` index 0 (Regular), at `/System/Library/Fonts/Supplemental/Hoefler Text.ttc`, in off-white `#F7F5F0`. Re-measure line width and size for your own faces.
