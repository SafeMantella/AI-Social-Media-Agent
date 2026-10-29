# Motion-graphics ad from a talking shot

Distilled from an external paid-social playbook: one raw talking shot becomes a motion-graphics ad. One card per spoken sentence, word-timed captions, a sound-effect kit, a music bed, and two hook variants from one master.

This is a different delivery from the sibling notes. `memory/feedback_video_editing_recording_patterns.md`, `memory/feedback_video_editing_alex_hormozi_benchmark.md`, `memory/feedback_animation_composite_preview.md`, and `memory/hyperframes_caption_style.md` cover pacing, reframing, and captioning a talking shot. They do not build a card ad on top of it. Offer this format as an option. It does not replace rules that are already validated.

The caption chunking in section 5 is for this ad format. It does not replace the caption spec (at most 5 words, no fade, serif, no background).

One outside source, one ads niche, not yet run on this project's pieces. Treat it as a technique to validate, not as a law. Same as the pacing benchmark: if the source is old when you use it, re-check before trusting it.

The creator still cuts and returns `base.mp4`. This playbook designs cards, captions, and sound on top of that cut. It is not a content cut.

## 1. Seven phases

1. **Probe and crop.** Inspect the source. When both deliveries are needed, prepare two display crops from `base.mp4`: a wide band, and a full 9:16.
2. **Transcribe with a time on every word.** The transcript is the spine. Every card, caption, and sound effect lands on a word (`transcripts/master.json`).
3. **Take the brand from the site.** Palette, logo, and real screenshots. Study the ads that already win for that product. Copy the motion, not the pixel.
4. **Storyboard one card per sentence.** Map each sentence to a proven card type.
5. **Build and score.** Draw the judgment cards by hand. Generate captions from the transcript. Add sound effects and a bed.
6. **QA and render.** A contact sheet of snapshots. Fix what you can see. Render. Check the file itself.
7. **Hooks.** Two hook variants from one master. The creator marks the cut. The agent remaps the overlays.

Draw by hand only the few cards where taste lives (about 18). Generate the other about 90% (captions, sound-effect markup) from the transcript. That avoids drift across hundreds of caption tweens nobody would write by hand and still trust.

## 2. Card types

| Spoken beat | Card |
|---|---|
| A number is spoken | A large count-up, then a sub-label. Loss and gain use two different colors. |
| The usual way is wrong | A real screenshot on a white card, plus a rotated stamp on the key word. |
| From this to that | Two real screenshots slide in. Before, after, an arrow between them. |
| Everyone says one thing, then another, then a third, but… | Lines appear one by one and get struck through. The real answer lights in the brand color. |
| One emotional word | Full-screen takeover. One giant word. |
| Social proof | A count-up, stars, and a reviews page as b-roll. |
| A guarantee | An outlined shield card, one pulse. |
| CTA (last 3 seconds) | Logo, offer line, a pulsing button, a bouncing arrow. |

Four frames, so the edit does not sit in one layout:

- **Split.** Video in a band at the bottom. Graphics in banners above and below.
- **Solo.** Speaker centered in a 1:1 square. Graphics as chips on the image.
- **Full.** Tight vertical crop. A full-screen graphic takes the beat. The workhorse. At most 3 beats.
- **Hidden.** The video is hidden. A graphic floats alone.

When `face` is `yes`, a full or hidden beat removes the face. Do not put those beats on the hook or the close. See `memory/feedback_fullscreen_cutaway_production.md`.

## 3. Brand kit from the site

Local, no API, about 15 minutes. No other video note covers this.

```bash
curl -sL -A "Mozilla/5.0" "$SITE" -o site.html
grep -oE "#[0-9a-fA-F]{6}\b" site.html | sort | uniq -c | sort -rn | head -20
grep -oE '(src|href)="[^"]*(logo|icon)[^"]*"' site.html | sort -u
# Repeat the color histogram on linked stylesheets. They are usually richer.
```

`$SITE` is the product page the creator named. Turn the result into CSS variables (`--brand-accent`, `--bg-dark`, `--panel`, `--muted`, and semantic `--green`, `--red`, `--gold`). Every card, caption, and chip inherits them. A new brand is a reskin of about five lines.

A real screenshot beats a redraw. If an asset folder already exists, use it.

## 4. B-roll of the product site

The pacing benchmark leaves archive b-roll dependent on licensed footage. Live UI proof does not. Record the product site with Puppeteer in kiosk (`npm i puppeteer`, local, no API).

- 4–6 clips, 3–6 seconds each. A smooth scroll of about 1.4s per move. Hold 3–4 seconds on a section.
- Hide consent and chat popups before recording (`display:none` on an attribute selector). Recheck in a loop.
- A shot list that covers most pages: hero, features, pricing, how it works, reviews, the CTA.
- Place the clip in a dark rounded card with window dots and an address pill, so it reads as a real browser window.
- Extract a frame and look at it (`memory/feedback_animation_composite_preview.md`). That catches a system dialog, a personal window behind the page, or a scroll that never moved. A common trap: the selector hit an ancestor whose `top` is 0, not the smallest node that contains the text.

## 5. Ad caption timing

`memory/hyperframes_caption_style.md` is the visual spec. This is timing for the ad format only.

- A chunk is 1–3 words. Start a new chunk on a speech gap of 0.45s or more, or on punctuation.
- Each chunk runs from `start - 0.04s` until `next.start - 0.04s`. Always cut at the next chunk's entrance. Otherwise two captions sit on screen together.
- Emphasis color: cost or pain in one color, gain in another, the brand color on the CTA.
- Round every time to the frame grid before use.

## 6. Sound

The only paid piece of the source playbook is a hosted sound-generation API and a hosted music API. Do not copy that. Do not suggest a paid sound API.

- **Effects** (whoosh, whip, UI pop, stamp, ticks, bass impact, scratch, chime, shimmer, ding): look for finished clips on Freesound first. They are short and generic. A good one is usually already there.
- **Instrumental bed:** MusicGen (local, `audiocraft`) or Stable Audio Open. A text prompt, no API bill. That replaces the hosted music call.
- **Before building either from scratch:** check the `media-use` skill. Its description already includes generating music or an image when the catalog has nothing.

Mix starting points. The original instruction is to trust the ear. These are not a law.

- Reference voice peaks near −7dB. UI pops 0.32, whooshes 0.30, stamps and impacts 0.50, count-up ticks 0.40–0.45, the chime 0.40, the bed 0.10 (18–20dB under the voice: audible in the gaps, hidden under speech).
- Normalize the whole kit to −3dB after it is generated.
- Audit every generated file. About a third come out nearly silent. Regenerate those before use.
- A music prompt that names an artist is rejected by hosted music APIs. Describe the texture. Do that on the local tools too.

For clicks under motion cards, the card note is stricter: clicks, not pops (`memory/padrao-cards-motion.md`).

## 7. Contact sheet and hook variants

- **Contact sheet:** `hyperframes snapshot` at several times in one call (for example `--at 2.7,12.2,27.8,45.9,68.5`). Review the batch before a full render. It catches more than three full renders. It does not replace compositing on a real frame.
- Check the **rendered file** with `ffprobe` (duration, size, audio). Never trust the render log.
- **Hook A/B from one take.** The creator records two hook lines back to back and marks each cut on a sentence boundary. The agent remaps the overlay times and hides the join inside a frame change. It does not choose the cut. One master becomes two ads. Never overwrite an approved cut. A new version is a new file (`memory/feedback_video_editing_recording_patterns.md`).

## 8. HyperFrames and GSAP

| Symptom | Cause and fix |
|---|---|
| The video renders as a frozen frame | Every video or audio element needs a unique `id`. No exceptions. |
| It freezes on a seek | Sparse keyframes. Re-encode with a keyframe every second (`-g 30 -keyint_min 30`). |
| An element is black or invisible the first time it appears | A later tween hid it at load. Set `immediateRender:false` on any `fromTo` whose element must be visible before that tween. |
| Two captions stuck on screen | The chunk outlived the next start. Always end at `next.start - 0.04s`. |
| A sound effect is inaudible in the mix | About a third of generations are nearly silent. Audit, regenerate, normalize. |
| An emoji or icon renders as an empty box | Headless Chrome has no private picture glyphs. Use a standard emoji or a text label. |
| The rendered duration is wrong | The stage duration attribute is stale after an edit. `ffprobe` the file, not the render log. |

Animation rules (check the HyperFrames skills before treating these as new): one paused, deterministic timeline (no `setTimeout`, no random, no infinite repeat). The hidden initial state lives in CSS, not in `.set()` at time 0 (that does not paint on frame 0). Animate transforms (`y`, `scale`, `opacity`), never `top`, `left`, `width`, or `height`. Every asset is local. The renderer blocks network fetches.

## Checklist

- [ ] When offering a growth piece, offer one-card-per-sentence beside a conventional talking cut. Do not swap the format automatically.
- [ ] Before drawing a card from nothing, check section 2.
- [ ] Brand-kit extraction and a site recording are cheap enough to run whenever the piece names a specific product or page.
- [ ] Sound: no paid sound API. Check `media-use` first, then Freesound, MusicGen, or Stable Audio Open.
- [ ] Run section 8 before debugging a broken HyperFrames render from scratch.
