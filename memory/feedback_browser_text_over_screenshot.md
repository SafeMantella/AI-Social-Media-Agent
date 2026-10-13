# Browser tools: read the page as text, not as a screenshot

When a browser automation tool can do both, prefer text extraction (`get_page_text` / `read_page`, or the DOM text) over a screenshot action for read-only inspection. Reserve screenshots for work that actually requires clicking, typing, or judging layout and design.

**Why:** a browser-tool audit found 74 screenshot calls against 8 text-extraction calls. A screenshot embeds a large image cost each time (on the order of a thousand units or more). Text extraction costs a fraction of that. This is a standing rule, not a one-off finding.

**How to apply:** before taking a screenshot in a browser task, check whether the goal is read-only (page content or state, verifying text) or whether it needs interaction (click or type) or a visual judgment (layout, design fidelity). Default to text extraction for the first case. Fall through to a screenshot only for the other two.
