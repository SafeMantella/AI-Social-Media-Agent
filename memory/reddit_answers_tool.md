# Reddit Answers — local collection (read only)

Script: `ferramentas/reddit-answers/reddit-answers`. It uses `patchright` from the Scrapling virtualenv and its own profile at `ferramentas/reddit-answers/.profile/` (gitignored), separate from the everyday browser. The script browses. The agent does not.

Whether it runs is the `reddit` key in `memory/config.md`: `no` skips it, `manual` keeps the creator in the loop for login and challenges, `auto` reuses the saved profile for read-only research.

## Why it exists

The in-app browser blocks `reddit.com`. Other agents in this setup have no browser, or they treat the browser as read-only. Reddit Answers (Reddit's own search) needs a signed-in session and client-side rendering, so plain Scrapling does not get it. The fix is a local script that is already signed in.

## Rule: research only, never post

Do not post anything on Reddit. Only look up information and data. No comments, no posts, no votes, and no draft meant to be posted. Use it for audience pain, facts, and hook angles.

## Use

```bash
ferramentas/reddit-answers/reddit-answers login      # once: sign in in the window, then press Enter
ferramentas/reddit-answers/reddit-answers research "question in English" -d folder/ [-s SubOne,SubTwo] [-t 12] [--show]
```

`research` does the whole pass in one command and writes into `folder/`:

1. `reddit-answers.md` — the generated answer (citations, links, and communities) plus the threads it cited.
2. `reddit-top.tsv` — candidates: threads cited by Answers, plus a **relevance** search (past year) in each cited community (or in `-s`), with score and comment count.
3. `reddit-threads.md` — the first `-t` threads (Answers citations first, then by score), read on **old.reddit.com**: title, community, points, percent upvoted, comments read versus total, body, and top comments by score. It clicks "load more comments" for six rounds. Virality is points plus percent upvoted. A low percent means rejection or controversy.
4. `reddit-structure.txt` — custom elements on the page (debug).

Wired in as step 1c of PART B of `/pesquisar`.

## Gotchas

- An Answers link can be a comment permalink. The script keeps only the post id (`old.reddit.com/comments/<id>/`).
- The generated answer lives in a **shadow DOM** (`shreddit-*` web components). `inner_text("body")` only catches the menu and the links. The script walks shadow roots in JS.
- It waits until the text stabilizes (three checks, two seconds apart, about 60 seconds max) instead of a fixed sleep.
- The text cut does not depend on language (it starts after the echo of the question and ends at the follow-up field placeholder). The page context is `locale=en-US`.
- **True headless is blocked by Reddit** (the question field never appears). The script opens the Chromium window **off screen** (`--window-position=-3000,-3000`). `--show` brings it on screen (use that to clear a challenge).
- Clear errors: an expired session tells you to run `login` again; a rate limit or a challenge returns a message; Answers with no answer saves `reddit-answers-erro.png`. If Answers fails, the script continues with the community search only.
- Gap: a thread that Answers cited but search did not score shows as -1 in the `.tsv`. The real score is in `reddit-threads.md`.
- Reddit's terms forbid automation, and a signed-in automated browser can draw a limit or a ban. Few searches, spaced out, read only.
- Questions in English return more threads.
