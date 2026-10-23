# List assembly

Contract only. Do not copy a piece-local script into here. Those scripts carried one brand's type and colors. Read the face and the palette from `memory/visual_identity_standard.md`, and re-measure line width for that face. Numbers below came from one copy.

## Headline in the safe area

Transparent PNG, 1080×1920. Shrink the type until the longest line fits the maximum width. Top from y=320, width up to 820 px, so the line stays out of the profile 3:4 grid and the Reels buttons. A separate mask paints the keyword. Plate styles: a box per line, a side bar, an underline. Finish with a soft halo and a color split. Re-measure y and width on a real phone preview.

## Cards

One card per item from `cards.tsv` (slug, title, year, cut center). Break lines by measuring pixels, not characters. Assemble with `trim=end_frame=N` per image and the `concat` filter. The concat demuxer with `duration` is one frame short at every cut. Do not use it for this.

## Series

`serie_parte.sh <N>` reads `cards.tsv` and `picks.tsv` from that part's folder. It assembles the graded take, the transition, N fixed-length cards, and the end card, using part 1's identity. The file has no audio. Music is added in the app.

## Three frames per item

For each item: A is the official image full frame. B is scene 1 in one band and half the official image in the other. C is two scenes stacked. Durations come from the environment (`A=45 B=30 C=75` as frame counts on that copy) or from `tempos_ref.tsv`, measured cut by cut on a reference.

## End-card options

Generate 3 mocks for the creator to choose: a diagonal warning tape, a generic "video removed" screen, a redacted document. The chosen one becomes the series end card. Do not ship all three.

## Title, letter by letter

Letters appear one at a time, with blur. Size and position are measured on titles the creator already makes in the app, so the generated piece matches their hand. Measure again for this creator. Do not reuse another creator's pixels.
