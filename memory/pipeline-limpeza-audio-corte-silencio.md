# Clean audio, transcribe, cut silence, full-resolution delivery

This is the silence-measurement procedure the agent still runs. It removes measured silence only. Retakes, tangents, and other content cuts stay with the creator, who returns `base.mp4` for the edit pipeline (`memory/feedback-video-editing-pipeline.md`). Do not drop a word the transcript contains. If a non-lexical hold is ambiguous, keep it and flag it.

Full resolution (step 7, and any 4K overlay) runs only when the creator has explicitly authorized it. Otherwise the preview rule in the edit pipeline still applies.

Tools live in `ferramentas/corte-silencio/`. Raw files live in `gravações/short form/<topic>/`. Work files live in `<topic>/edit/{audio,transcripts}`.

## Flow

1. Raws stay in `gravações/short form/<topic>/`. Work stays in `<topic>/edit/{audio,transcripts}`.
2. `ferramentas/extrair-audio/extrair-audio -o edit/audio/ <mp4>` writes a lossless `.m4a`. For the enhancer, convert to **mp3 128k**. The enhancer rejects `.m4a`. The browser upload accepts **under 10MB per call**. 192k overflows on a video longer than about 6 minutes. 128k fits about 10:40 of audio.
3. Enhancer, with the creator already signed in. Find the file input with "Choose files button (file input)". That returns the `<input type=file>`. The button ref is not a file input and errors with "Element is not a file input". `file_upload` on the input ref. Wait until "Get transcript" appears. Click **Download by coordinate (966, 613)**. A click by element ref sometimes does not fire. The file lands in the browser download folder as a temp with no extension, already complete, mp3 128k at 48kHz, named like `.com.brave.Browser.*`. Move it to `edit/audio/<stem>-enhanced.mp3`. Each Download click creates a new temp. Trash the duplicates. One file at a time. Bulk is paid.

   A wait loop inside the page script dies past about 35s because the CDP timeout is 45s. Poll instead: loops of at most 25s looking for the Download button. If the renderer freezes and the call hits the 45s CDP timeout, processing has usually finished. Take a screenshot before clicking again.

   **Script:** `ferramentas/adobe-enhance/adobe-enhance preparar|juntar <topic-folder>` does step 2 (mp3 128k, and a warning over 10MB) and the file match in step 3 (find the download temp by duration, rename, build the swapped-audio copy). Upload and download stay in the browser. Use the script instead of hand-running ffmpeg for those steps. The scripts follow this `raw/` + `edit/` layout.

3b. **Swap the enhanced audio onto a copy of the original.** This step is part of the pipeline. Run it as soon as the enhanced audio is on disk, before transcription. It also applies to a piece that skips the silence cut.

```bash
ffmpeg -i raw/<stem>.mp4 -i edit/audio/<stem>-enhanced.mp3 \
  -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 320k \
  -movflags +faststart -map_metadata 0 edit/<stem>-enhanced.mp4
```

The video is not recompressed. The original in `raw/` stays untouched.

4. Transcribe: `ferramentas/corte-silencio/transcrever_ambos.sh <edit> <stem>...` (whisperx plus vad). Point the script at the binary and models that exist on this machine. The binary is `/opt/homebrew/bin/whisper-cli`. The models `ggml-large-v3.bin` and `ggml-silero-v5.1.2.bin` sit together in the `local-video-use` skill models directory. A default whisper.cpp build on an external drive is not there. Without the models, the vad engine dies with "failed to initialize whisper context". Then run `glossario.py` and `comparar.py`.
5. **Resolve every divergence by re-transcribing that window alone.** The vad engine can drop a whole block of 20 seconds or more and can drift the timestamps. The other engine can miss names. Misses go into `glossario.json`. Neither engine wins by default. The isolated window decides.
6. `ferramentas/corte-silencio/cortes.py <edit> <stem>...` writes `edl.json`. Silence is measured on the **clean audio** (−50dB, at least 0.7s). End margin +0.37s. Start margin −0.12s. Drop a segment with no speech (the click at the end of a recording). **The whisperx `.end` is inflated at the end of a sentence** (it includes the following silence, sometimes 5–7s). Never validate or decide from `.end` or from a midpoint. Use the word **start**. A validator checks that every word start falls inside a segment. That is what stops a short utterance from being dropped. Do not add a second pad on top of these margins.
7. `ferramentas/corte-silencio/render.py <edit> "<name>.mp4" [stem...]` when full resolution is authorized. One ffmpeg trims and concatenates. Video stays at the **original 4K, no scale**. A 3840×2160 recording with `rotation=90` comes out 2160×3840, 29.97fps. x264 `slow`, crf 14 (about 70Mbps, above the source bitrate). Audio is the **enhanced** track in AAC 320k. An 8ms fade on each join. Speed is about 0.23× (about 30 minutes per 7 minutes of program). Run it in the background. Do not run it against whisperx at the same time. Fade and frame-snap can make the file longer than the sum of the segments. `ffprobe` the file. Do not size later layers from the EDL total.
8. Validate the final file: `ffprobe`, a contact sheet, and **a fresh transcription of the final audio, diffed** against the source text (no sentence missing). Sync of the clean track against the original is an envelope correlation (lag 0ms).

Do not verify a word ending by running the recognizer on a short clip or on the already concatenated file. A short clip that starts mid-sentence comes back as garbage, and the concatenated file has no tail of silence between segments. Measure the silence on the source before the cut. If a word sounds cut after the render, inspect `showwavespic` or windowed `astats` at that point.

## Access

- **The Drive connector does not download video.** `download_file_content` returns base64 inside the conversation. Files of 1–5GB do not fit, and it does not write to disk. Use it to list and find. A browser download works. A file over 100MB raises a warning; confirm the download by coordinate. The fastest path is the creator placing the raws in `gravações/`.
- Two takes in one folder may be a **continuation** or a **re-record of the ending**. Tell them apart by reading the text before concatenating. Never join unread.

## Captions from a hand edit

When the creator delivers a hand edit, that file becomes the base. Discard the agent's earlier silence-cut videos (trash the mp4s). Keep the scripts, the EDL, the audio, and the transcripts.

Flow: extract the audio from the hand edit, run whisperx plus vad, run `glossario.py`, resolve each divergence on an isolated window (vad can still drop a long block), then `ferramentas/corte-silencio/gerar_legendas.py`. Run it from the folder that holds `t.json` and `audio.wav`. It writes `palavras.json`, `cues.json`, and `legendas.srt`.

- Ambiguous text is decided with **two models** (`large-v3` and `large-v3-turbo-q5_0`) on a window of about 2.7s.
- The recognizer marks the **start of a stretched word, or a word before a pause, too early**. The script pulls it back from the audio (an internal pause of at least 0.22s). Still read the cues before burning captions.
- Cues are at most 5 words. Break on a comma or a pause. Never end on a function word ("que", "o", "de", and the equivalent in the recording's language). Continuous speech keeps the cue open until the next one. A real pause (at least 0.25s) closes on the end of the energy.
- An odd phrase that two transcripts and an isolated window all agree on is real speech, not a hallucination. If it still sounds wrong, ask the creator. Do not delete it.

Burned-in captions follow `memory/hyperframes_caption_style.md` and `memory/feedback-legenda-serifada-hoefler-overlay-pillow.md` (serif, no background, at most 5 words). An older petroleum pill in a sans face is retired. Do not bring it back.

## Motion on a hand edit

- One HyperFrames project in `<topic>/edit/overlays/` (`index.html`, canvas 1080×1920, one timeline). Preview: `render --format mov --quality draft --fps 30`, then `compor.py preview <overlay.mov> <out.mp4>` (base scaled to 1080, zoom by `scale` with `eval=frame` plus a crop anchored at y=30%, alpha overlay). Final, only when authorized: `render --resolution portrait-4k --fps 60`, then `compor.py final`. A draft render of an overlay near 90 seconds takes about a minute.
- When `face` is `yes`, measure the face band and put chips on the empty background above the head. End large cards above any chapter marker already on screen. Do not cover the face unless the layout is the list exception in the caption note. Card geometry is `memory/padrao-cards-motion-lato.md`.
- A tall table (on the order of 654×2020) is illegible if it is fitted whole into a full-screen cut. It reads with a pan and zoom per row (about 950px wide) plus a note underneath.
- Overlay sound is **clicks, not pops**. `edit/overlays/sfx.py` builds the track (`clicks.wav`: a main click on each card or chip, a soft click on inner steps, a "cut" on full-screen changes, very quiet ticks on counters). A worked mix peaked near −22 dBFS against a voice at −19 LUFS. `compor.py` mixes with `amix`. Measure this piece. Do not copy the gain. No music bed unless the creator asks. The click map (`main`, `soft`, `tick`, `cut`) is `memory/padrao-cards-motion-lato.md`.

## Replacing raw audio inside a hand edit, then a bed

- **The hand edit's audio may be the raw track, not the enhanced one.** Check correlation. A shape near 1.0 against the raw (a worked case was 0.997) and lower against the enhanced file (0.913), with a noise floor near −45 dBFS against −65 to −70 on the enhanced file, means the edit was cut on the original audio. `overlays/align_audio.py` finds where each segment of the edit came from by waveform correlation and stitches the `-enhanced` audio at those points (6ms crossfade, level matched to the edit) into `voz_limpa.wav`. Always run this check when the creator delivers a hand edit.
- **A bed with vocals fights intelligibility.** A center cut (L−R) on a near-mono track leaves only the bass. It does not remove the vocal. What works: `ferramentas/separar-voz/` (its own venv, Demucs `htdemucs --two-stems=vocals`, about 20s per 100s of music on CPU). Transcribe the instrumental stem. If the recognizer only emits a stock phrase, the stem has no lyric. Use that stem.
- Mix (`overlays/mix_audio.py`): music about 21dB under the speech (RMS), about 15dB in the pauses, attack 100ms, release 350ms, EQ −5dB at 2.2kHz and −2.5dB at 300Hz, fade in 0.8s, fade out 2.5s. The final loudness target is −16 LUFS and −1.5 dBTP. Pauses in a tight edit are short (about 0.25–0.42s), so the music barely rises. Treat it as a continuous bed, not a dance-style duck. Worst-case metric: voice against music in the 300–3400Hz band stays at least 15dB.
- When `face` is `yes`, anchor zooms and reframes on the chin (y 73%) so a bottom caption is never scaled. Full-screen cut content ends above the caption band.

## Long audio, when the creator wants the best quality

Do not crush the whole file to fit the 10MB upload. **Split into two parts on a silence near the middle** (`silencedetect -35dB:d=0.4`). Each part is mp3 **192k** and under 10MB. Enhance each one. **Join** them (`concat` in ffmpeg, decoding to wav) and store the clean audio as **FLAC**. The `-enhanced.mp4` carries that audio as AAC 320k with `-c:v copy`. The joined duration must match the original.

The browser download is slow and inconsistent. It lands either as `.com.brave.Browser.*` in the download folder or in the project working folder (`<topic>/<stem>-enhanced-v2.mp3`), up to about a minute late. Repeated clicks make identical duplicates. Check `md5` and trash the copies. Wait and look in both places before clicking again.

## App panel over the face (preview)

A split plus an app panel, preview only. The HyperFrames project in `<topic>/edit/overlays/` is generated by `build.py` (real speech times become `index.html` and `events.json`), `sfx.py` (clicks), and `compor.py`. When `face` is `yes`, the face moves down 200px and does not resize. The panel is 1080×720 on top. Clearance against the head is at least 20px. Measure it.

`fromTo` repeated on the same target with the default `immediateRender` forces the second tween's start value from frame 0. Set `immediateRender: false` on the exit tween.

A background render has to be a direct command. A subshell `( ... ) &` is cancelled when the parent exits.
