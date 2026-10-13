# Grok CLI — validated for research on X

The headless `grok` CLI (xAI) can search X live. It is the best X coverage to use when the other collectors are weak there: `last30days` covers X but is unstable on that source; `minet` and Scrapling do not cover X.

Flag syntax lives in the grok CLI skill. That skill is agent infrastructure, not a project decision, and it is kept outside this repo on purpose.

**What a live search returns:** `grok -p "<search on X about a topic>" --output-format json --no-alt-screen` uses live X search without being asked, and it returns real posts with a link, a date, and exact engagement (views, likes, replies). The validation run did not invent posts.

**Cost:** it is not free. One X search with reasoning cost about **$0.28** (on the order of 118k billed units with cache, and about 2.5k output units). Use it for a real research question, not a trivial lookup.

**Place in research:** formal step of `/pesquisar`, quick tier, step 1b, always — not only on `--deep`:

`grok -p "<search on X about the target>" --output-format json --no-alt-screen | jq -r '.text' > referencia/pesquisas/<slug>/grok-x.md`

Run it with the rest of collection. It does not replace `last30days` on X. Cross-check the two. See `.claude/commands/pesquisar.md` and `memory/pipeline_pesquisa.md`.

**Security:** never call it with `--always-approve`. That flag lets Grok approve its own file and shell actions with no supervision. Use Grok here only for **answers** (search, research, a second opinion), never for **actions** on the machine.

## When to use it

- Research that needs fresh X (a thread, a hashtag, a profile): add `grok -p "..."` as an extra source, and always cross it with what `last30days` and `minet` already returned. Never trust it alone. Same verification rule as any external tool.
- Never use `--always-approve`.

## Image generation

The `grok` CLI also has native `image_gen` (Imagine), via headless `grok -p`. Wrapper: `ferramentas/grok-imagem/gerar.sh`. Test results, cost, limits (720p, invented text, moderation that still charges on a refusal), and how to write the prompt are in `prompt-imagem-fotografico.md`. Use this instead of Higgsfield, which was turned down.

Generate images only when `grok_image` is enabled in `memory/config.md`.
