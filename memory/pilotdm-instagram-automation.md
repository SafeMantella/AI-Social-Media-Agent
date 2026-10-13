# PilotDM — Instagram DM automation

PilotDM is the supported Instagram DM tool. Use it only when `dm_automation` is enabled in `memory/config.md`.

**What it does:** from a comment on a post or reel, a story reply, or a direct message, it sends an automatic reply. Visual flow builder (no code), comment auto-reply, lead capture (email, phone, username), follow-before-DM, insights, more than one workspace, and an optional model layer on replies.

**Trigger:** the trigger word is capitals with no accent. The flow sends two messages. Details the creator confirms are stored in `memory/dm-automation.md`. Do not invent an account, a keyword, or a message body in any other file.

**Why this class of tool is acceptable:**

- It runs on Meta's official Messaging API. That is what separates a compliant tool from a scraper that puts the account at risk. ManyChat and Chatfuel also use the official API.
- The creator plan is free (unlimited automations and DMs, up to 3 workspaces; only the agency plan is paid). ManyChat moved to per-contact pricing and cut its free plan.
- Safe Mode throttles the reply ratio (25/50/75%) so a viral post does not blow a platform limit.
- The pattern "comment a word and the reply arrives by DM" raises comment volume, which is an Instagram ranking signal, and builds an owned DM list. See `diretrizes-hormozi.md` on lead magnets.

**Limits:**

- **Instagram only.** It does not cover TikTok or YouTube.
- Almost no third-party reviews yet. A directory may still list an old monthly price. Trust the product site for the current creator plan.
- If Meta withdraws third-party access, the automation stops.

**Replaces:** a custom auto-DM feature (do not build one) and the native comment-to-message feature in Meta Business Suite.
