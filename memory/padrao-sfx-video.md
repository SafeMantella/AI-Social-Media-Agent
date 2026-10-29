# Sound design standard for videos

Defaults for every video the agent builds. The creator's taste overrides any line here; save the override in `memory/` when they state it.

## Rules

- **Real samples, not synthesis.** Use only royalty-free sounds (CC0 or equivalent), for example the Kenney packs (interface, digital, impact) and the Unicae Keyboard Soundpack on OpenGameArt. Log source and license in `sfx_samples/LICENCAS.md` inside the video's folder. Never take sounds from commercial games: copyright risk on Instagram and TikTok. A retro feel comes from CC0 blips or from sfxr.
- **No swoosh or whoosh by default.** A card sliding in becomes a pop, a paper sound, or a click. Drop this default if the creator likes swooshes.
- **Tactile and light.** Keyboard clicks, mouse clicks, pop, ding, paper, retro game blips.
- **Sound to beat map.** Text typing on screen (a prompt, "typing…" bubbles): mechanical keyboard, two keys per line. A card, pill, or note entering: pop. A document flying: paper. A sticky note or block landing: a soft place or impact. A win, a lightbulb, a link in the bio, the key word: ding or a retro coin. A slam or a triple yes: a low impact. Cuts and toggles: a mouse or switch click.
- **Riser only at the climaxes** (before a full-screen moment and before the CTA), never on every beat.
- **Variety is mandatory.** Draw with a fixed seed so the same sample never plays twice in a row. Pitch ±8 percent, gain ±2 dB. No beat sounds like the one before it.
- **Level.** Start from a PEAK of 0.075 (clicks near −16 dB peak, voice peaking near −7 dB with a mean near −27 dB). Scale by type: impact ×1.2, place ×1.1, paper ×1.1, ding ×0.7, coin ×0.6, key ×0.8, riser ×0.55. Check with `volumedetect` or `ebur128`, and report the loudness you measured.
- **No background music** unless the creator asks.
- **The agent cannot hear audio.** Sync and timbre are judged by the creator. Say so when delivering.

## Implementation

Keep one `sfx.py` per video: a pool per type, a `make()` that applies the variation, and an event list anchored to the times of the motions. Key presses come from the timing of the lines in the slot. When the same script has been copied into two videos, promote it to `ferramentas/` under the repeated-script rule in `memory/regras-projeto.md`.
