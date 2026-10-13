# Carousel pipeline

Every carousel follows these five steps, in this order.

1. Interview the creator with concrete options: the angle, the pain slide 1 attacks, the scope, the CTA on the last slide, and what must not appear.
2. Run research at the quick tier. Write `referencia/pesquisas/<slug>/RESUMO.md`. Use only the tools enabled in `memory/config.md`.
3. Write the plan in the canonical store:
   - `storage: notion` — the body of the content page.
   - `storage: md` — `conteudo/carrosseis/<slug>.md`.
   The plan has the slide-by-slide structure, one native visual element per slide, a short caption, hashtags, and dated sources.
4. Wait for the creator to approve the plan.
5. Build.
   - `carousel: canva` — duplicate the master template id in `estrategia/marca/ids.md`. Replace text and elements. Never generate the design with an image model. A new slide is a duplicate of a slide that already has the right font. Do not create an empty slide and a new text box. Record the design link on the canonical page or file.
   - `carousel: md` — the plan file is the piece. Do not open Canva.

The caption is 1 to 3 sentences. The carousel already carries the content. Write the short version first. Voice rules in `memory/estilo-de-escrita/guia-voz.md` apply. Length rules of a long post do not.

After the creator edits the finished piece, reread the final version, compare it with what you delivered, and save the reusable difference in `memory/`. See `memory/feedback-evolve-feedback-loop.md`.

If Canva or Notion login fails, stop and ask the creator to reconnect. Do not switch `storage` or `carousel`.
