# PDF to Markdown

Turns a PDF into local markdown so the agent reads text instead of one image per page.

```bash
python3 pdf_to_md.py "/path/to/file.pdf"
python3 pdf_to_md.py "/path/to/file.pdf" --pages 1,2,3
```

Install: `pip install pymupdf4llm`. It extracts reading order and falls back to local OCR on pages with no text layer. No API key.

If the text comes out scrambled, try Marker (`pip install marker-pdf`). The first run downloads layout models.

Output: `output/<name>.md`, gitignored.
