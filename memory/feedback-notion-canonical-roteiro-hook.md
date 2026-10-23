# Script and hook pipeline

Every script or hook follows these three steps, in this order.

1. Interview the creator first, with concrete options. Cover the goal of the video, the specific pain the hook attacks, the audience, and what must not appear. Two questions are mandatory even if the creator already gave other direction:
   - Will there be a CTA?
   - Format: a closed short script (timed table) or a looser talk (guide points, not a word-for-word script)?
2. Run research at the quick tier with the angle from the interview. Write `referencia/pesquisas/<slug>/RESUMO.md`. Use only the tools enabled in `memory/config.md`. See `pipeline_pesquisa.md`.
3. Write the script in the canonical store from `storage`:
   - `notion`: the idea page (hook property, script table or guide points, hook alternatives, production notes, dated sources).
   - `md`: `conteudo/roteiros/<slug>.md` with the same sections.

When `writes_scripts` is `yes`, stop after step 2. Deliver the research: checked facts, angles, and sources. Do not write spoken lines, a script table, a hook, or a caption. Step 3 runs only when the creator explicitly asks for a script. When the key is empty, ask once, write it, and do not reopen onboarding. See `memory/feedback-so-a-peca-pedida.md`.

When `storage` is `md` and the creator writes in their own editor, read the script from that store. Do not ask them to paste it, and do not edit their text unless they ask. A speech-time counter, if one is built, estimates at 3.3 words per second. That rate was measured on one copy's reference videos. Re-measure before treating it as this creator's rate.

When the conversation has several pieces, deliver only the one they named, then wait.

The chat is not the record. A new research pass updates the same page or file and dates the change at the top.

Read `memory/feedback_hook_writing_no_jargon.md` and `memory/estilo-de-escrita/guia-voz.md` before writing. The script is the context for `memory/feedback-video-editing-pipeline.md`.

There is no built-in light-format exception. A recurring light series is added later through the feedback loop if the creator wants one.
