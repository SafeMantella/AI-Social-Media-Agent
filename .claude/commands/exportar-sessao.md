---
description: Export this session to a Markdown file with personal strings masked, only if the creator asks for it.
---

# Export the session

Read this file and follow it. It is a workflow. Run it only when the creator asks to save or send the conversation.

1. Say what the file holds: everything said in this session, one line per tool call, and anything the creator pasted. Personal data they pasted stays in it. The tool masks the home path, emails, and key-like strings, and nothing else. Ask for a yes.
2. Run `ferramentas/exportar-sessao/exportar-sessao`. It writes to the Desktop, never inside this folder, and uploads nothing.
3. Tell the creator the path. Suggest they read it before sharing it. If they want to send it to the template's maintainer, they do that themselves, or `/reportar-evolucao` drafts a sanitized report. Do not send the file anywhere.
