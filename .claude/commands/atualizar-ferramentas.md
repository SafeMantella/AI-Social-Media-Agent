---
description: Check the cloned tools under ferramentas/ against their remotes, and fast-forward the ones that are behind.
---

# Update cloned tools in `ferramentas/`

Read this file and follow it. It is a workflow.

Each subfolder of `ferramentas/` may be its own nested git repository, cloned from an external project. `fontastic-text-image-generator` is one. The set grows. This workflow keeps a tool from sitting on an old commit without anyone noticing.

If the request names one tool, check only that folder. If the folder is missing or is not a git repo, say so and stop.

## What to do

1. **List the targets.** The equivalent of `find ferramentas -mindepth 1 -maxdepth 1 -type d`. For each subfolder, check that it is a git work tree (`git -C <folder> rev-parse --is-inside-work-tree`). Skip any folder that is not a git repo.

2. **For each git tool:**
   - `git -C <folder> fetch --quiet`. The remote is not always named `origin`. Confirm with `git -C <folder> remote`. In practice it has been `origin`.
   - **Do not assume the local branch tracks an upstream.** `fontastic-text-image-generator`, for example, has `origin` but no tracking on `main`, so `HEAD..@{u}` fails with "no upstream configured". Find the matching remote branch in a way that survives that: take the current branch (`git -C <folder> rev-parse --abbrev-ref HEAD`) and compare with `<remote>/<current branch>` if that ref exists after the fetch. Otherwise use the remote's default branch (`git -C <folder> symbolic-ref refs/remotes/<remote>/HEAD`).
   - Count how many commits the local branch is behind: `git -C <folder> rev-list --count HEAD.."<remote>/<remote-branch>"`.
   - If the count is `0`, it is current. Do nothing.
   - If the count is greater than `0`, first check for uncommitted local changes (`git -C <folder> status --porcelain`). If there are any, **do not touch the repo**. Report it as blocked and list the changed files so the creator can decide. If the tree is clean, run `git -C <folder> pull --ff-only "<remote>" "<remote-branch>"`. Pass the remote and the branch explicitly. Do not depend on an upstream being configured. The same convention is in the `local-video-use` skill's `install.md`, section "Keeping the skill current".

3. **After a successful pull, check whether a dependency manifest changed** (`git -C <folder> diff --name-only ORIG_HEAD HEAD`, intersected with `requirements.txt`, `pyproject.toml`, `package.json`, `Pipfile`). If one changed, **do not install anything automatically**. Tell the creator they may need to reinstall (`pip install -r requirements.txt`, `npm install`, or whatever matches the file that changed).

4. **Report at the end,** one line per tool: already current / updated now (with `git log --oneline ORIG_HEAD..HEAD`) / blocked by uncommitted local changes / error (for example no remote, or no network). If no git folder was found under `ferramentas/`, say that. Do not report an empty list with no context.
