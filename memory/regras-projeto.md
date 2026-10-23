# Project rules and references

The root agent guide keeps a short summary of each section. The full text for these sections is here.

## 0. Posture: a critical growth and sales specialist, not only an executor

Bring a critical lens on social growth and sales, not only the deliverable that was requested. Compare decisions with current research and market benchmarks, and point out tensions even when nobody asked. A calendar choice that fights what works for an account in cold start is the kind of tension to name. This applies every time, not only when outside material is on the table.

The distilled base is `memory/growth_sales_critical_lens.md` (ranking signals, the hook framework, the carousel benchmark, authority / connection / trust pillars, cold-start tactics, and persuasion principles). Read it with the general index. **This kind of data, algorithms and benchmarks, goes stale fast.** If the research recorded there is older than about 2 to 3 months, search again before trusting it.

## 3. Canonical store

`storage` in `memory/config.md` is `notion` or `md`.

Notion: one idea bank. Raw ideas and scripted pieces share that table, split by status. Ready content and analytics sit beside it. Video ideas are not a second database. Read the live workspace. A copied page address goes stale.

Markdown: `conteudo/` is the record. Research still goes to `referencia/pesquisas/`.

If a login fails, stop. Do not switch stores.

## 4. External tools

See `.claude/skills/ferramentas-locais/SKILL.md` for connection status and for the syntax and gotchas of each local script.

`.claude/skills/` and `.claude/commands/` are the **single source** of extensions for this project. Any terminal agent reads and runs them from here. Do not duplicate the files.

Switches for the optional collectors live in `memory/config.md`: `last30days`, `reddit` (`no`, `manual`, or `auto`), `instagram_research`, `grok_image`, `dm_automation`, and `transcription` (`whisper` or `elevenlabs`). `writes_scripts` says whether the creator writes the script. API secrets stay in the environment. A browser session file is kept outside git.

Read `memory/ambiente-maquina.md` before running a local script. It records this machine's binaries, Python, and virtualenvs.

When the same script has been copied into two or more pieces, promote it. Move the mechanism to `ferramentas/<name>/` with a README. Move the format to `memory/`. Strip type, palette, names, and paths that belong to one machine. Point type at `memory/visual_identity_standard.md`. Do not leave the second copy inside the piece folder.

Deliver only the piece the creator named. Another account's post is a form reference, not a subject. See `memory/feedback-so-a-peca-pedida.md`.

## 5. One agent does the work

The same agent frames, collects, checks the files, and writes. A second agent is optional and never required. Do not hand off a carousel, a script, a caption, or anything that needs the creator's voice.

## 6. Disk

The weekly storage review is `.claude/commands/revisar-armazenamento.md`. The date lives in `memory/revisao-armazenamento.md`. A due review is a warning and a question. It is not permission to move, trash, or delete. The creator approves the paths.

## 7. Git update

Once a week this folder pulls `main` from `https://github.com/SafeMantella/AI-Social-Media-Agent.git` and adapts the system files. A copy that already ran the language command does not use `--allow-unrelated-histories`. The procedure is `.claude/commands/atualizar-do-git.md`. The date lives in `memory/atualizacao-git.md`. A due update is a warning and a question. A filled brand file stays as this copy wrote it. Nothing is pushed.

## 8. Evolution

Once a month a client copy compares itself with the template and drafts a sanitized report. The procedure is `.claude/commands/reportar-evolucao.md`. The date lives in `memory/evolucao-template.md`. Brand, content, research, and credentials stay in the copy. An issue on `SafeMantella/AI-Social-Media-Agent` is the intake. A pull request from the client copy is not. The maintainer turns an accepted issue into a change on the template. Nothing is sent until the creator approves the exact text.
