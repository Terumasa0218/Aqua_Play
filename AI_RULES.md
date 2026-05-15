# AI Rules for Aqua_Play

These rules define the mandatory operating contract for any AI coding agent working in this repository.

## Canonical Repository

The canonical repository is:

```text
https://github.com/Terumasa0218/Aqua_Play
```

Treat the GitHub repository, especially `origin/main`, as the most accurate source of truth. Local working copies should be checked against the remote before important planning, implementation, or documentation changes when network access is available.

## Current Technical Direction

- Engine: Unity.
- Primary language: C#.
- Asset companion: Blender for Unity-oriented 3D asset generation and export.
- MVP scope: the confirmed baseline in `AQUAPLAY_GARDEN_SPEC.md`.
- The previous Godot direction is no longer the active implementation target.

## 1. Scope Boundary

The AI agent may read and modify only this repository and its subdirectories.

Allowed areas:

- `AGENTS.md`
- `AI_RULES.md`
- `AQUAPLAY_GARDEN_SPEC.md`
- `PLAN.md`
- `README.md`
- `docs/`
- `blender/`
- `unity/`
- `tools/`
- Git metadata for normal non-destructive status, diff, add, commit, branch, fetch, and push operations

The AI agent must not access, inspect, or modify:

- User home directories outside this repository
- Desktop, Documents, Downloads, cloud-sync folders, SSH keys, browser profiles, or credential stores
- System directories such as `/etc`, `/usr`, `/bin`, `/var`, `/Library`, `C:\Windows`, or `C:\Users` outside this repository
- Other repositories or unrelated projects
- OS settings, services, launch agents, registry entries, package managers, or global editor settings

## 2. Required Startup Checklist

Before making changes, the AI agent must:

1. Read `AGENTS.md` if present.
2. Read `AI_RULES.md`.
3. Read `PLAN.md` if present.
4. Read `AQUAPLAY_GARDEN_SPEC.md` when the task affects game design, MVP scope, or implementation direction.
5. Confirm the current working directory is the repository root.
6. Run `git status --short`.
7. Identify the files it expects to change.
8. Avoid touching unrelated files.

## 3. Default Delivery Policy

Unless the user explicitly says `議論のみ`, `相談のみ`, or says not to commit or push, repository changes should be completed through:

1. focused edits,
2. validation,
3. Git commit,
4. push to a dated branch.

Direct pushes to `main` require explicit user instruction. Force pushing is prohibited.

## 4. Tool Execution Restrictions

The AI agent may run repository-local automation only through scripts in `tools/` or explicit commands documented in `docs/ai-assisted-development-setup.md`.

Allowed command categories:

- `git status`, `git diff`, `git diff --check`, `git add`, `git commit`, `git branch`, `git switch`, `git log`, `git fetch`, `git remote`, `git rev-parse`, `git push`
- Blender batch execution against scripts in `blender/scripts/`
- Unity batch execution against project path `unity/`
- Repository-local validation commands

Prohibited command categories:

- `sudo`
- Force pushing
- History rewriting
- Deleting untracked repository content without explicit user approval
- Recursive destructive shell commands outside generated build/cache directories
- Network downloads or package installs without explicit user approval
- Commands that read or write outside the repository root

## 5. Unity Rules

- Unity project files must live under `unity/`.
- Runtime scripts should live under `unity/Assets/Scripts/`.
- Editor automation scripts must live under `unity/Assets/Editor/`.
- Generated Unity assets and prefabs must live under `unity/Assets/Generated/`.
- Unity command line execution must use `-batchmode`, `-quit`, and `-projectPath unity`.
- Editor scripts must validate paths before importing, creating, or deleting assets.
- Prefer prefabs and generated assets over direct scene mutation unless the user explicitly asks for scene edits.

## 6. Blender Rules

- Blender scripts must live in `blender/scripts/`.
- Generated Blender exports must be written to `blender/exports/`.
- Exported runtime assets should use `.fbx` for Unity import by default.
- `.glb` may also be produced for preview, interchange, or future compatibility.
- Scripts must be deterministic when possible and should avoid absolute paths.
- Scripts must resolve output paths relative to the repository root.

## 7. Git Rules

Branch names must include an ISO date in `YYYY-MM-DD` format.

Recommended branch pattern:

```text
ai/YYYY-MM-DD-short-description
```

Commit rules:

- Commit focused, reviewable changes.
- Include a clear prefix such as `docs:`, `tools:`, `blender:`, `unity:`, `gameplay:`, or `pipeline:`.
- Review `git diff` and run `git diff --check` before every commit.
- Push the dated branch unless the user requested discussion only or asked not to push.

Prohibited Git operations:

- `git push --force`
- `git push --force-with-lease`
- `git reset --hard` unless explicitly requested by the user
- `git rebase` unless explicitly requested by the user
- `git commit --amend` unless explicitly requested by the user
- Filtering or rewriting history

## 8. Rollback Requirements

Every AI task must preserve rollback capability:

- Use Git commits as restore points.
- Prefer adding new generated files over overwriting hand-authored assets.
- Document generated asset sources and commands.
- Keep terminal commands reproducible.

Rollback examples:

```bash
git status --short
git log --oneline --max-count=10
git revert <commit-sha>
```

## 9. Human Approval Policy

The AI agent should behave conservatively:

- Explain planned changes before large refactors.
- Prefer small diffs.
- Never assume destructive cleanup is acceptable.
- Require user approval before deleting or replacing valuable assets.
- Treat user-created art, scenes, prefabs, and scripts as protected unless explicitly instructed otherwise.
