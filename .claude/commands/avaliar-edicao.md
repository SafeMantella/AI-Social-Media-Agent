---
description: Prepare a video for the manual edit review, then wait for the creator's decisions.
argument-hint: <raw video, and the clean audio if it exists>
---

# Review an edit

Read `ferramentas/evals-edicao/README.md` before the first step. If `memory/evals-edicao-manual.md` exists, read the lessons there.

1. Run `preparar.py` on the video. Pass `-a` when a clean audio file exists. Pass `--texto` only when retake suggestions need the words. Check the real output: chunk count, duration kept, proxy under about 20 MB.
2. Write `sugestoes.json`, one note per chunk.
3. Upload `proxy.mp4` to the creator's artifact and run `semear.py`. The artifact URL is not in this template. If they have not given one, stop and ask.
4. Give them the link and stop. Do not publish and do not render a final.
5. When they say they are done, read the reviews, compare them with the suggestions, and append the lesson to `memory/evals-edicao-manual.md`.
