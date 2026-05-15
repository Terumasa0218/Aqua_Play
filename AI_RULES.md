# AI Rules for Aqua_Play

These rules define the mandatory operating contract for any AI coding agent working in this repository.

## 1. Scope Boundary

The AI agent may read and modify only this repository and its subdirectories.

Allowed areas:

- `AI_RULES.md`
- `README.md`
- `docs/`
- `blender/`
- `unity/`
- `tools/`
- Git metadata for normal non-destructive status, diff, add, commit, and branch operations

The AI agent must not access, inspect, or modify:

- User home directories outside this repository
- Desktop, Documents, Downloads, cloud-sync folders, SSH keys, browser profiles, or credential stores
- System directories such as `/etc`, `/usr`, `/bin`, `/var`, `/Library`, `C:\Windows`, or `C:\Users` outside the repository
- Other repositories or unrelated projects
- OS settings, services, launch agents, registry entries, package managers, or global editor settings

## 2. Required Startup Checklist

Before making changes, the AI agent must:

1. Read `AI_RULES.md`.
2. Confirm the current working directory is the repository root.
3. Run `git status --short`.
4. Identify the files it expects to change.
5. Avoid touching unrelated files.

## 3. Tool Execution Restrictions

The AI agent may run repository-local automation only through scripts in `tools/` or explicit commands documented in `docs/ai-assisted-development-setup.md`.

Allowed command categories:

- `git status`, `git diff`, `git add`, `git commit`, `git branch`, `git switch`, `git log`
- Blender batch execution against scripts in `blender/scripts/`
- Unity batch execution against project path `unity/`
- Repository-local validation commands

Prohibited command categories:

- `sudo`
- Force pushing
- History rewriting
- Deleting untracked repository content without explicit user approval
- Recursive destructive shell commands such as `rm -rf` outside generated build/cache directories
- Network downloads or package installs without explicit user approval
- Commands that read or write outside the repository root

## 4. Blender Rules

- Blender scripts must live in `blender/scripts/`.
- Generated Blender exports must be written to `blender/exports/`.
- Exported runtime assets should use `.glb` and `.fbx` formats.
- Scripts must be deterministic when possible and should avoid absolute paths.
- Scripts must resolve output paths relative to the repository root.

## 5. Unity Rules

- Unity project files must live under `unity/`.
- Editor automation scripts must live under `unity/Assets/Editor/`.
- Generated Unity assets and prefabs must live under `unity/Assets/Generated/`.
- Unity command line execution must use `-batchmode`, `-quit`, and `-projectPath unity`.
- Editor scripts must validate paths before importing, creating, or deleting assets.

## 6. Git Rules

Branch names must include an ISO date in `YYYY-MM-DD` format.

Recommended branch pattern:

```text
ai/YYYY-MM-DD-short-description
```

Commit rules:

- Commit frequently at safe checkpoints.
- Keep commits focused and reviewable.
- Include a clear prefix such as `docs:`, `tools:`, `blender:`, `unity:`, or `pipeline:`.
- Review `git diff` before every commit.

Prohibited Git operations:

- `git push --force`
- `git push --force-with-lease`
- `git reset --hard` unless explicitly requested by the user
- `git rebase` unless explicitly requested by the user
- `git commit --amend` unless explicitly requested by the user
- Filtering or rewriting history

## 7. Rollback Requirements

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

## 8. Human Approval Policy

The AI agent should behave conservatively:

- Explain planned changes before large refactors.
- Prefer small diffs.
- Never assume destructive cleanup is acceptable.
- Require user approval before deleting or replacing valuable assets.
- Treat user-created art, scenes, prefabs, and scripts as protected unless explicitly instructed otherwise.
