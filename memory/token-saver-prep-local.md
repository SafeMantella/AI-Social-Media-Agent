# Context cost: prepare locally before reading

An audit of tool results in this project (about 1,500 units assumed per image) put the largest costs at: long `.md` reads and raw file dumps (about 440k), PNG and JPG frames and overlays (about 243k), browser screenshots (about 199k), page fetches from the workspace (about 113k, about 4.7k each), and long search or text dumps (about 180k).

Tools added (nothing new installed; ffmpeg, swiftc, sips, and python only):

- `ferramentas/prep-frames/prep-frames <video|image> [-n 9]` writes `sheet.jpg` (a 3x3 contact sheet) and `resumo.md` (text recognition and faces, per frame, via the system vision framework). Read those two instead of N frames. Open a full frame only to fine-tune an overlay. A 25-frame video dropped from about 37k units to about 2k.
- `ferramentas/prep-texto/prep-texto <file> [--max 40]` writes an index with line numbers. Then read with an offset and a limit on the section you need. Calibrated on a 42 KB strategy doc, which dropped to about 5 KB.
- The `token-saver` mod (a hook on read) refuses **once** a raw read of an image over 150 KB or of text over 30 KB, and it points at the prep tool. Repeating the read goes through. It ignores `memory/`, the root agent guide, and `SKILL.md` (rule docs are read whole). The versioned source is `ferramentas/token-saver/`. A session copy may sit outside the repo and can be discarded. Register it once, at project scope, from that folder. The creator runs that install once.

**Rule:** a visual review of a video starts with `prep-frames`. A long doc you are only consulting starts with `prep-texto`. Never summarize a rule doc.

## Second pass

- The `token-saver` mod also refuses, once, a `cat` of a file over 30 KB in the shell (that bypasses the read hook), and refuses, once, the second fetch of the same workspace page in the session. It allows the page again after an update to that page, or on the third attempt.
- `ferramentas/transcrever/leitura.py` (called by `transcrever.py`) writes `<output>.leitura.txt` (sentence plus time). **Read that file, not the word-level JSON.** Measured: 15,894 bytes down to 1,618 bytes, about 90% less.
- The root agent guide stays short. The full index is `memory/INDEX.md`. The long posture and tooling sections live in `memory/regras-projeto.md`.
- Unused plugins stay off at project scope. They add context on every turn. Leave enabled only what the creator has decided to keep.
- Still manual: turn off unused account connectors (mail, calendar, and any connector this project does not call). If a skill is synced from the account and differs from the project copy, remove the account-side duplicate. The project copy is the one that counts.
