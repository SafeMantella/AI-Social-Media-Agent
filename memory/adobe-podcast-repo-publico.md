# Adobe Podcast Enhance

Pipeline for any coding agent: extract the audio, clean it in Adobe Podcast Enhance, and put the cleaned track back on the video.

- Procedure lives in the enhance skill. CLI: `python3 enhance.py prepare|collect|replace`.
- In this repo, `ferramentas/adobe-enhance/adobe-enhance` keeps the `raw/` + `edit/` flow. It calls `ferramentas/adobe-podcast/enhance.py` with the Scrapling environment. That folder is a gitignored clone of `https://github.com/SafeMantella/Adobe-Podcast-for-Claude-Code.git`. The login profile is `ferramentas/adobe-enhance/.profile/` and is gitignored. The picture is copied. The original file is not overwritten.
- Limits checked on the Adobe Podcast features page: the free plan is audio, one file at a time, 30 minutes, 500 MB, about one hour per day. The ~10 MB ceiling belongs to the browser upload tool, not to Enhance. The default split is mp3 at 192 kbps, under 9 MB. `--max-mb 0` delivers the whole file when the browser will accept that path.

Use it before the edit, and before transcription, when the voice track is noisy. Do not re-encode the picture. Do not overwrite the source.
