---
description: After onboarding's readback, put the markdown and the creator-facing folders in content_language. Set files_language only when the path check passes.
---

# Apply the chosen language

Read this file and follow it. It is one command. Run it after the readback in `onboarding/interview.md`, before `status: ready`. Do not run it between question 1 and question 2.

## What to do

1. Read `content_language` in `memory/config.md`. If it is empty, stop and ask question 1.
2. Translate the prose of every project markdown file into that language. The interview's answers and the posts are already in it. This step is the rest of the system. Skip `.git`, `venv`, `.venv`, `node_modules`, `site-packages`, downloaded media, and third-party clones (`ferramentas/Pytho-inator`, `ferramentas/last30days-skill`, `ferramentas/fontastic-text-image-generator`). Do not translate source code. Leave these tokens as written: config keys and allowed values, `FILL VIA ONBOARDING`, `decision: keep`, `decision: change`, command flags, and `https://github.com/SafeMantella/Pytho-inator.git`.
3. Leave one README in that language. Remove the other language's README.
4. Run `python3 onboarding/language_paths.py apply`. English and Portuguese are the two maps. Another language stops the script. Say so, rename from the same rows into that language by hand, and do not invent a second map file.
5. Run `python3 onboarding/language_paths.py check`. It prints `ok` only when no markdown still points at an old path.
6. Write `files_language` with the same value as `content_language` only after the check printed `ok`. If it printed hits, fix those paths and run the check again. Do not write `files_language` on a failure, and do not set `status: ready`.

A second run is safe. Folders that already have the target name are left in place.
