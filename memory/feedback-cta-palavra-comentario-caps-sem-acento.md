# Comment-bait call to action: the word only, in capitals, with no accent

On a comment-bait call to action ("comment this word and I will send it"), the card or pill shows **only the trigger word, in capitals, with no accent marks**. No tag, no sentence around it, no image: one large amber pill on its own.

**Why:** the word people type in comments is the automation trigger (PilotDM; see `pilotdm-instagram-automation.md`). Capitals and no accents match what people will type, so an accent variant cannot break the match. A single word stays readable in about a second.

**How to apply:** on every video with a comment-bait call to action, the overlay is one pill in that style (Lato 600, about 116px, amber, centered near y=250, entering and rising like a standard card in `padrao-cards-motion-lato.md`). It enters on the spoken trigger ("comment") and leaves with the end of that sentence. The caption keeps the normal spelling of the spoken line. The trigger stored in PilotDM must be the same word, in capitals, with no accent. The flow sends two messages. Details the creator confirms are stored in `memory/dm-automation.md`. Do not put a sample keyword or a sample message in the script.

Use this only when `dm_automation` is enabled in `memory/config.md`.
