---
description: Research a subject, profile, or piece with the tools enabled in memory/config.md, then write referencia/pesquisas/<slug>/RESUMO.md. One agent frames, collects, reads the files, and writes the note.
---

# Research workflow

Read this file and follow it. It is a workflow.

One agent does the whole job. Frame the target, collect with only the tools enabled in `memory/config.md`, read the files it produced, and write `referencia/pesquisas/<slug>/RESUMO.md`. There is no required second agent. Do not hand collection or the note to another agent.

No single source covers a niche. The value is the cross-check. Do not cite a URL or a number that is not in a file you wrote or a page you opened.

Read `memory/ambiente-maquina.md` before running a collector. Availability of an item enters the note only after the item itself is opened, including a stretch from the beginning, the middle, and the end. A title, a thumbnail, a duration, or a view count is not proof. What could not be opened is "unverified", separate from what was opened. A login wall or an age gate stops that item and goes to the creator. At least one primary source (real comments, a forum the audience uses) is required.

Instagram: hashtag search is the minet call that kept working. Profile, posts, and comments have returned HTML. For a known post, use `instagram-transcript` with comments. Space the calls, at most 2 or 3 profiles, and stop on `401 require_login`. Say that the session expired. See `memory/minet_niche_research_tool.md`.

## Input

The creator names a target, and may add:

- **Type** `subject` (default) — a theme or a trend.
- **Type** `profile` — an account, a channel, or a person.
- **Type** `piece` — one specific video or post to take apart. It becomes the base of a case study.
- **`deep`** — also run the deep tier. The default is the quick tier. Use `deep` for a flagship piece or a case study.

If the type is not obvious, ask. Do not assume. If the target is missing, ask before collecting.

## Frame

1. **Slug:** `referencia/pesquisas/<slug>/` (kebab-case). A dated trend gets a `YYYY-MM-` prefix. Create the folder.
2. **Sub-targets:** niche tags, known accounts, related repos, the person's name plus variants, video channels. A specific brief collects better.
3. Read `memory/growth_sales_critical_lens.md`. If the algorithm or benchmark note is **older than two or three months**, mark it to be researched again. Do not treat it as current.
4. Read `memory/config.md`. A key set to `no` is a gap. Do not run that tool. Record the gap in the RESUMO.

## Collect

Save everything under `referencia/pesquisas/<slug>/`. If a step fails, note it and continue. Do not invent links or counts.

Public web search, keyword suggestions, and public video search are part of this workflow. They are not account switches. Account tools run only when their key allows it.

### Quick tier

1. **Web search.** Save `web.md`:
   - (a) 6–10 of the most relevant links from about the last 3 months (URL plus one line on what it is and why it matters);
   - (b) 3–5 bullets of what people complain about or ask;
   - (c) recent numbers worth citing (price, benchmark, dates), each with a real URL.
2. **Search terms.** `python3 ferramentas/keyword-mining/suggest.py "<target>" ["<variant>"] --no-alpha --lang <content language> --out "referencia/pesquisas/<slug>/termos-de-busca.md"`. If `content_language` is not English, run it again with `--lang en`. The first sections (pains and questions) are what someone types when they have the problem. That is hook material. See `ferramentas/keyword-mining/README.md`.
3. **YouTube.**
   ```bash
   yt-dlp "ytsearch20:<target>" --flat-playlist --print $'%(view_count)s\t%(title)s\t%(channel)s\thttps://youtu.be/%(id)s' 2>/dev/null | sort -rn > "referencia/pesquisas/<slug>/youtube.tsv"
   ```
   For a profile, list that channel's recent videos (about 30), same columns, sorted by views, as `youtube_<channel>.tsv`. The separator in the file must be a real tab. If a tool writes the two characters `\` and `t`, split on that when you read it.
4. **`last30days` — only when `last30days` is `yes`.** Otherwise record the gap and skip.
   ```bash
   python3 "ferramentas/last30days-skill/skills/last30days/scripts/last30days.py" "<target>" --quick --emit md --output "referencia/pesquisas/<slug>/last30days.md"
   ```
   `--emit md` alone does not write a file. `--output` has to be there too. A profile or a person: add `--competitors-list "<target>,<competitors>"`. A subject tied to a repo: add `--github-repo "owner/repo"`. If the file comes back empty or noisy, note it and continue. For a platform-algorithm or marketing question, if two tries return nothing usable, stop retrying and use the web search. TikTok and Instagram are off inside this tool on purpose. Do not turn them on. Detail: `memory/last30days_case_study_research.md`.
5. **Reddit — only when `reddit` is `manual` or `auto`.** When it is `no`, record the gap and skip. The question is always in English, even when `content_language` is not. Read only. Never post, comment, or vote. Output: `reddit-answers.md`, `reddit-top.tsv`, `reddit-threads.md` under `referencia/pesquisas/<slug>/reddit/`. Virality is points plus percent upvoted. A low or negative percent is rejection, not reach. Detail: `memory/reddit_answers_tool.md`.
   - `auto` — run `ferramentas/reddit-answers/reddit-answers research "<target in English>" -d "referencia/pesquisas/<slug>/reddit" -t 12`. The window stays off-screen. Headless is blocked. Automation can conflict with Reddit's rules, and the account can be limited. If the session is expired, ask the creator to log in again (`ferramentas/reddit-answers/reddit-answers login`) and continue without Reddit.
   - `manual` — do not drive the browser. Give the creator the same read-only command and wait. If they skip it, record the gap and continue.
6. **Instagram — only when `instagram_research` is `yes`, and only for a profile or when the brief names accounts.** Otherwise record the gap and skip. Use the browser session file the READMEs in `ferramentas/minet/` and `ferramentas/instagram-transcript/` describe. Do not print the session. The file stays out of git. If the session is missing, ask the creator to export it before this step.
   Call the wrapper `ferramentas/minet/minet`. Space the calls. At most 2–3 profiles. If a call returns `401 require_login`, stop Instagram and report that the session expired.
   - Account info and about 30 recent posts, saved as `ig_<account>_infos.csv` and `ig_<account>_posts.csv`.
7. **`grok_image` is not a research source.** Do not generate images while collecting. If the creator asked for an image and the key is `yes`, that is a later production step (`ferramentas/grok-imagem/gerar.sh`, `memory/prompt-imagem-fotografico.md`), billed per image. If the key is `no` and they asked for an image, record the gap. Do not call the Grok CLI to search, and never pass its always-approve flag.

### Deep tier

Only when the creator asked for `deep`, and only for keys that are already enabled. Add:

1. `last30days --deep --output "referencia/pesquisas/<slug>/last30days-deep.md"` when `last30days` is `yes`.
2. `suggest.py` without `--no-alpha` (the a–z sweep), plus English if needed → `termos-de-busca-completo.md`.
3. A deeper web note → `web-deep.md`: the landscape, 3–4 open debates, reference voices with links, quantitative data. Cite the sources.
4. When `instagram_research` is `yes` and the type is `subject`: hashtag sample, about 40 posts, saved as `ig_tag_<tag>.csv`. This grid has no likes and no short-video ranking. It only shows who is posting.
5. When `instagram_research` is `yes` and the type is `profile`: following list, about 200, saved as `ig_<account>_following.csv`.
6. **Scrapling** on articles or docs that already appeared. Start with `ferramentas/scrapling/scrapling extract get "<url>" "referencia/pesquisas/<slug>/fonte_<n>.md" --ai-targeted`. Escalate to `fetch`, then `stealthy-fetch --solve-cloudflare`, only if the file is empty. Always `--ai-targeted`. See `ferramentas/scrapling/README.md`.
7. When `instagram_research` is `yes`: transcribe 2–3 key clips with `python3 ferramentas/instagram-transcript/instagram_transcript.py "<url>"` plus the session file the README describes, and `--comments`. Copy the result into the slug folder.

**TikTok discovery does not work for free from this machine.** minet, Scrapling, and the tested TikTok API are blocked. If the target is mostly TikTok, report that and stop. Do not retry. See `memory/tiktok_scraping_evaluated.md`. The only path that has worked is a manual browser capture, and it is not part of this workflow.

## Read the files and write the note

1. **Read what you wrote.** `ls` the slug folder. Open the files that will feed the note, not every raw dump: `last30days.md` (if any), `reddit/` (if any), `termos-de-busca.md`, `web.md`, `youtube.tsv`, and the `ig_*` files if any. A file the collector did not create is a gap, not a source.
2. **Check facts.** Open the 2–4 links, and check the numbers, that will appear in the RESUMO. Drop anything the file does not support.
3. **Write `referencia/pesquisas/<slug>/RESUMO.md`** in this shape:
   - **Date** at the top.
   - **Pains and questions** — a prioritized list (search-term pains and questions, plus complaints from `web.md` and `last30days` when those files exist). Mark the ones that show up in two or more sources. **This is what feeds the hook.** Each item links the underlying source (`[excerpt](url)`), not only the raw filename.
   - **What people are saying** — 3–5 clusters, plus real quotable lines, each with a source.
   - **Top content** — a table ranked by engagement (YouTube, and Instagram when it was collected): title and author, metric, and the angle of each piece.
   - **Useful links** — only the ones you opened.
   - **Open angles** — a pain with no good answer, contradictions between sources, what nobody covers well.
   - **Growth lens** — how this sits against `memory/growth_sales_critical_lens.md`: tensions, risks, what the benchmark says. If that benchmark is stale, say so.
   - **Gaps** — every config key that was `no`, plus the known gaps below that affect this target.
4. **Mine hooks.** Two sources that **do not mix** (a title is packaging; the first spoken line is the hook). Build `hooks.csv` with columns `hook,views,fonte`:
   - `fonte=yt-titulo` — titles from `youtube.tsv`. The separator is a real tab. If the file contains a literal `\t`, split on that.
   - `fonte=reel-fala` — the first spoken sentence of the key clips that were transcribed.
   Run `python3 ferramentas/minerar-hooks/minerar.py referencia/pesquisas/<slug>/hooks.csv`. Below 15 items for a source, say the sample is small. Rank is a percentile inside each source. The output stays split by source. In the RESUMO, two subsections:
   - **Packaging (titles):** only patterns and angles that repeat among the most-viewed. **Do not remix a title as a spoken opener.** It turns into a thumbnail line.
   - **Hook (first spoken lines):** the dominant families, power words in the niche, and 3–5 remixes in `content_language`. Keep the structure, swap the power word, and follow `memory/feedback_hook_writing_no_jargon.md` and `memory/estilo-de-escrita/guia-voz.md`.
   If there is only a tsv, deliver packaging only and record the missing transcripts under Gaps. **Do not edit `referencia/swipe-openers.md` on your own.** Propose what to promote. A news title is usually packaging, not a spoken hook. That is why the hook signal comes from speech.
5. **Show the RESUMO in the chat and stop.**
6. If the type is `piece`, also scaffold `referencia/estudos-de-caso/<slug>/` (raw/, analysis, timeline).

Keep the raw `last30days.md` intact when you archive or quote it. Do not strip the tool's own boilerplate out of the raw file. The RESUMO is a separate file.

## Known gaps

Record these in the RESUMO when they affect the target.

- **TikTok discovery — no free path** from this machine (`memory/tiktok_scraping_evaluated.md`).
- **Hashtag samples** do not rank. No likes, no short-video list.
- **last30days** is weak on evergreen topics, and its TikTok and Instagram sources stay off.
- **minet** rate-limits hard. Many profiles means several rounds.
- **suggest.py** is autocomplete (what people search, and in what order), not search volume. The endpoint is unofficial.
- **A disabled config key** is a gap even when a public page mentions that network. Do not route around `no`.
- **Reddit `manual`** that the creator did not run is a gap, not a reason to switch the key to `auto`.

## Output

`referencia/pesquisas/<slug>/` holds `RESUMO.md` plus the raw files that the enabled tools actually wrote (`last30days.md`, `termos-de-busca.md`, `web.md`, `youtube.tsv`, `ig_*.csv`, `fonte_*.md`, `reddit/`, transcripts). Always paste the RESUMO in the chat.

## Where this sits

This is the research step of the script and carousel pipelines in `.claude/skills/sistema-social-media/SKILL.md`. The RESUMO, especially "Pains and questions", feeds the interview and the draft. See also `memory/pipeline_pesquisa.md`.
