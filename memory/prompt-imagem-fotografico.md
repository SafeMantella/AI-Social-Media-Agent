# Photographic image prompt, and generation with Grok

Use this for a video thumbnail, a carousel cover, and image B-roll. It does not replace a real screen recording, and it does not replace the carousel rules (master template in the layout tool; never generative images for the layout). Image generation is only the background or cover photo. The visual identity goes on top (see `visual_identity_standard.md`).

Generate only when `grok_image` is enabled in `memory/config.md`.

## Golden rule: describe physics, not adjectives

The model follows physical decisions (camera position, lens, light direction, texture) better than praise words. Banned in the prompt: cinematic, epic, beautiful, dramatic, stunning, moody, ethereal, masterpiece, award-winning, best quality, 4k, 8k, hyperrealistic, ultra detailed. Write the prompt in English. No text, logo, or watermark in the image. Do not name a director, a film, or an artist.

## Structure (paragraphs with a caps header, 1,200 to 1,500 characters)

`CAMERA:` body, ISO, position (low, hip height, oblique; never a neutral eye-level). `LENS:` focal length, T-stop, where the focus sits. `LIGHT:` a motivated source, Kelvin, direction, what the shadow does. `SUBJECT:` `FOREGROUND:` `MIDGROUND:` `BACKGROUND:` `WARDROBE TONAL BEHAVIOR:` (material), `MAKEUP SURFACE PHYSICS:` (real texture: dust, wear, a scratch), `POST BEHAVIOR:` (format or film stock, visible grain), `COMPOSITIONAL GEOMETRY:` (asymmetry, a foreground intrusion), `MOOD & ART DIRECTION:` (always close with "Composition and art direction inspired in the work of award-winning directors.").

- **Only two cameras:** IMAX MK IV 65mm (ISO 250; a quiet scene, a premium product, a dense portrait) and ARRI Alexa 35 (ISO 800; narrative, street, movement). When unsure, Alexa 35 with a Canon K35 35mm T1.5.
- **Grain is always visible** (visible, organic, tactile, heavy). Never "subtle" or "fine". No film edges and no sprocket holes.
- **One variable per iteration.** Generate one or two candidates, not twenty.
- **Stylized mode** (illustration, 3D, flat, watercolor): turn off camera, lens, ISO, and grain. Write one to three paragraphs of prose. Name the medium and the technique in the first sentence, use a limited named palette (say how many colors), describe how that medium handles light, state the finish, and declare the background.

## 7 light setups (swap into `LIGHT:`)

| Setup | When | Core of `LIGHT:` |
|---|---|---|
| Golden hour | calm, nostalgic | sun at 8° above the horizon, 3,000K, raking from the side, long shadow |
| Low key | tense | one hard 3,200K light at 75° from the side, no fill, half the face at 15 IRE |
| Spotlight | the subject and nothing else | a narrow 18° cone from above, the rest black |
| Chiaroscuro | volume, mystery | a window at 55°, a Rembrandt triangle, fill 4 stops under |
| Cutter lights | graphic, geometric | hard light cut by a flag, bars of shadow |
| Hard flash | raw editorial, street | direct 5,600K flash on the lens axis, a hard shadow behind |
| Silhouette | anonymity, scale | window backlight, the subject in black, a thin rim of light |

Full sample prompts for the seven setups live in `referencia/curso-agent-lab/imageprompts.md`.

## Generate with Grok (Imagine), not Higgsfield

Use Grok, which is already available, instead of installing or paying for Higgsfield. The `grok` CLI has native `image_gen`. Script: `ferramentas/grok-imagem/gerar.sh "<prompt>" destination.jpg [16:9|9:16|1:1|4:5]`.

**Same subject, a still life on a table, 16:9:**

- A short casual prompt produced a clean stock-photo look: generic warm light, everything sharp.
- The structured prompt from this guide looked like a real photograph (hard light cut by shadow, depth, grain, bokeh from a practical lamp). Clearly better.
- **Failure:** even with "no text", the model invented lettering on the object. Always check the image. For a thumbnail, cover or replace that text in the layout tool.
- **Resolution:** only 1280x720 (16:9) or 720x1280 (9:16). Fine for a video thumbnail. A story, a reel at 1080x1920, or a carousel cover needs an upscale. Pay for an upscaler only if the frame is worth it. Try a local upscale first.
- **Cost:** about US$0.02 to US$0.04 per image (it is an agent call). Much cheaper than the early estimate.
- **Moderation is unstable:** two harmless prompts of an ordinary object on a work table were refused with `imagine:content-moderated` and **still charged**. If it refuses, change the subject or the wording and try again. Do not resend the same prompt. The script prints Grok's reply when it fails.
- Not yet tested: a reference image of the creator's face (identity), photo editing, and video. Imagine can also generate video; check the model before spending.

## When the image must contain exact text: render HTML, do not ask the model

Grok invents letters and gets them wrong. For a thumbnail or a cover with exact text, use the HTML method (source notes in `referencia/curso-agent-lab/opensquad/image-creator-SKILL.md`): write the HTML and CSS of the piece, put the generated or real photo behind it, open it in a headless browser at the right viewport, and screenshot. Presets: post 1080x1080, carousel 1080x1440, story or reel 1080x1920, video thumbnail 1280x720. Put the typeface and the palette from `visual_identity_standard.md` in the CSS, so the identity is exact and repeatable. This is not its own tool yet. The installed browser automation, or Scrapling and Playwright, can take the screenshot.

## Safety

Never pass `--always-approve` to grok (see `grok_cli_tool.md`). The script uses its own temporary directory, so Grok does not see the repository.
