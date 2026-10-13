# `extrair-audio` — lossless audio from video

Bash script at `ferramentas/extrair-audio/extrair-audio` (no virtualenv; ffmpeg and ffprobe only).

```
ferramentas/extrair-audio/extrair-audio "folder or video.mp4"      # -> audio/ beside the video
ferramentas/extrair-audio/extrair-audio -o "destination/" "folder/"  # -> chosen destination
```

- **Copies the track (`-c:a copy`); it does not re-encode.** The file is the same audio as in the container, bit for bit. Re-encoding to WAV or FLAC recovers nothing: the loss already happened at record time.
- The container follows the codec (aac to m4a, opus to opus, pcm to wav, and so on). An unusual codec falls back to FLAC.
- Accepts a file or a folder. It scans mp4, mov, mkv, webm, m4v, and avi, one directory level only. Running it twice on the same folder does not reprocess the `audio/` folder it already created.
- **The default is an `audio/` subfolder** beside the video. `-o` overrides that destination.

## Where it sits in the flow

Step 1 of audio cleanup: extract, upload the file to [Adobe Podcast Enhance](https://podcast.adobe.com/en/enhance), then remux it into the video with `-map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k` before any edit.

This comes **before** step 1 of the edit pipeline (`feedback-video-editing-pipeline`). Transcribing the video after the audio is clean produces a much better transcript. Which engine runs is `transcription` in `memory/config.md` (`whisper` or `elevenlabs`).

## Browser automation gotchas

Upload, wait, and download can be driven by browser automation while the creator is already signed in to Adobe Podcast.

- **`.m4a` is rejected** ("File extension or content not currently supported for enhancement.") even when the AAC inside is valid. Adobe checks the container extension, not only the codec. Convert to `.mp3` before upload (`ffmpeg -i x.m4a -c:a libmp3lame -b:a 192k x.mp3`). `.wav` should also work, but it grows quickly and can pass the browser upload size limit. mp3 at 192 kbps is the practical choice.
- **The Download click stalls on a temporary file with no extension** in the browser download folder (a name like `.com.brave.Browser.XXXXXX`, or `.com.google.Chrome.XXXXXX` on Chrome). The browser does not finish the rename when the click comes from automation. **The file is already complete and valid** (`file` identifies a real MP3, and the duration matches). Do not retry the download. Copy and rename that temp file to the right destination. Each Download click creates a new temp with the same content. Delete the extras after copying the one you need.

**Remux gotcha:** if the cleaned audio came from one file and the target video is another (a re-download or a different export), confirm they are the same take before assuming sync. Run `ffmpeg -i X -map 0:v -c copy -f md5 -` on both. Equal hashes mean the same video stream, so sync holds. Comparing the MD5 of a *decoded frame* with `-ss` does not work: the seek lands on different frames.
