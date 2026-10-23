---
name: slides-pdf
description: Turn an HTML slide deck into a PDF, one page per slide, and fail when a slide overflows its box. Use when the creator asks for a slide PDF or finishes an HTML deck.
---

# slides-pdf

The deck is HTML. The PDF is the export.

1. Edit the HTML. Each slide is one `<div class="slide">`.
2. Run `ferramentas/slides-pdf/slides-pdf "<deck>.html"`.
3. Say it is done only when the command prints matching page and slide counts and no `ERRO`. If a slide overflows, shorten the text or the type and run it again.
4. To check the picture, pass `--png` and read the result with `prep-frames`.

Detail: `ferramentas/slides-pdf/README.md`.
