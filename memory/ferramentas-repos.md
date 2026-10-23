# Owned tools live in five public repositories (2026-10-23)

The code for the owned tools under `ferramentas/` lives in five public repositories on the SafeMantella account. This project pulls those repositories. It does not keep a second copy of the code.

Read this file before editing any tool.

## Where each tool lives

| repo | URL | tools (the old path still works) |
|---|---|---|
| token-kit | https://github.com/SafeMantella/token-kit | `prep-frames`, `prep-texto`, `token-saver` |
| video-cut-pipeline | https://github.com/SafeMantella/video-cut-pipeline | `corte-silencio`, `evals`, `evals-edicao` |
| transcrever-ptbr | https://github.com/SafeMantella/transcrever-ptbr | `transcrever` (repository root) |
| video-tools | https://github.com/SafeMantella/video-tools | `video-camadas`, `slides-pdf` |
| social-toolbox | https://github.com/SafeMantella/social-toolbox | `keyword-mining`, `minerar-hooks`, `pdf-to-markdown`, `grokbot`, `links`, `extrair-audio`, `grok-imagem` |

Older SafeMantella clones, already gitignored under `ferramentas/`: `Pytho-inator`, `adobe-podcast`, `fontastic-text-image-generator`.

Third-party clones, also gitignored: `last30days-skill` (mvanhorn), `ln` (fogleman), `social-auto-upload` (dreammis). `editonny` is a vendored skill slice, not a clone. `minet` and `scrapling` are local environments. `local-video-use` is a separate fork.

`separar-voz` is only a virtualenv. It is not a repository.

A private index of these repositories may exist in the creator's notes. It is not stored in this template.

## How the folder is wired

- The real clone is `ferramentas/_repos/<repo>/`. That folder is gitignored.
- `ferramentas/<tool>` is a symlink into the clone. Skills, commands, and memory keep the path `ferramentas/<tool>/...`. Do not retarget them.
- Local state stays inside the clone and out of git: `venv/`, `.profile/`, `.env`, cookies, `__pycache__/`. Never commit those. `grokbot/.env` holds a webhook and a token once it has been filled in.
- `ferramentas/_old/`, when present, is the pre-move backup. It is gitignored. Do not copy it into this repository.
- This repository does not track the code of these 16 tools.

## Recreate on a new machine

```bash
cd ferramentas && mkdir -p _repos
for r in token-kit video-cut-pipeline transcrever-ptbr video-tools social-toolbox; do
  git clone "https://github.com/SafeMantella/${r}.git" "_repos/${r}"
done
ln -s _repos/token-kit/prep-frames prep-frames
ln -s _repos/token-kit/prep-texto prep-texto
ln -s _repos/token-kit/token-saver token-saver
ln -s _repos/video-cut-pipeline/corte-silencio corte-silencio
ln -s _repos/video-cut-pipeline/evals evals
ln -s _repos/video-cut-pipeline/evals-edicao evals-edicao
ln -s _repos/transcrever-ptbr transcrever
ln -s _repos/video-tools/video-camadas video-camadas
ln -s _repos/video-tools/slides-pdf slides-pdf
ln -s _repos/social-toolbox/keyword-mining keyword-mining
ln -s _repos/social-toolbox/minerar-hooks minerar-hooks
ln -s _repos/social-toolbox/pdf-to-markdown pdf-to-markdown
ln -s _repos/social-toolbox/grokbot grokbot
ln -s _repos/social-toolbox/links links
ln -s _repos/social-toolbox/extrair-audio extrair-audio
ln -s _repos/social-toolbox/grok-imagem grok-imagem
```

Then recreate the virtualenvs for `transcrever` and `video-camadas`, and create `grokbot/.env` from `.env.example`. Do not commit them.

## Update and edit

- `/atualizar-ferramentas` scans `ferramentas/_repos/*` and the loose clones under `ferramentas/`. It skips symlinks, so each repository is pulled once.
- To change an owned tool, commit and push inside `ferramentas/_repos/<repo>/`. The author name is SafeMantella. The email is the GitHub noreply address already on that repository (`git log -1 --format='%ae'`). Pass both with `git -c` for that commit only. Do not change the global git config. Do not use a personal mailbox. The history is public.
- Some scripts in those repositories still assume one absolute machine path and a sibling `ferramentas/` folder. Each repository README says so. Do not copy that path into this template.
- Do not edit a public tool repository from this template to strip content that is already published there.
