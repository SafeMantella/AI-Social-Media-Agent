# Image search and long-video sheets

Contract only. The script from the copy that proved this carried that brand's files, so it is not in this repository. Build it here when a second piece needs the same steps. Read `memory/ambiente-maquina.md` before running anything on this machine.

Type and color, if a sheet draws them, come from `memory/visual_identity_standard.md`.

## Wide image search

Several queries, several pages of an image search, download all of them, drop duplicates. Write `origem.tsv` with file, query, and URL. Then numbered contact sheets. One copy used 60 images per sheet. The creator picks by number.

A second mode pulls a cover and frames from a public metadata base for that item. That base returned 403 to `urllib` and answered `curl`. Use curl. A variant may run several items in parallel.

The choice sheet the creator sees is 6 to 8 numbered options plus a recommendation (`memory/formato-lista.md`). The wide download is the pool behind that sheet.

## Long video, time burned in

One frame every N seconds. The default tried was 8. Burn the timestamp into the frame so the strong scenes can be named. Then extract the exact frame with `ffmpeg -ss`.
