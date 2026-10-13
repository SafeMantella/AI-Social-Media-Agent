# Adobe Podcast Enhance

Pipeline for any coding agent: extract the audio, clean it in Adobe Podcast Enhance, and put the cleaned track back on the video.

- Procedure lives in the enhance skill. CLI: `python3 enhance.py prepare|collect|replace`.
- In this repo, `ferramentas/adobe-enhance/adobe-enhance` keeps the `raw/` + `edit/` flow. The generalized form accepts any file and any agent and takes no personal path. The picture is copied (`-c:v copy`). The original file is not overwritten.
- Limits checked on the Adobe Podcast features page: the free plan is audio, one file at a time, 30 minutes, 500 MB, about one hour per day. The ~10 MB ceiling belongs to the browser upload tool, not to Enhance. The default split is mp3 at 192 kbps, under 9 MB. `--max-mb 0` delivers the whole file when the browser will accept that path.

Use it before the edit, and before transcription, when the voice track is noisy. Do not re-encode the picture. Do not overwrite the source.
