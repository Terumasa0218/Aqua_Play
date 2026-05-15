# Repository Agent Instructions

## Canonical Source

The canonical repository for this project is:

```text
https://github.com/Terumasa0218/Aqua_Play
```

Treat the GitHub repository, especially `origin/main`, as the most accurate source of project truth. Before planning or editing, check the current branch, fetch the remote when available, and compare local state with `origin/main`.

## Default Delivery Policy

Unless the user explicitly says `議論のみ`, `相談のみ`, or says not to commit or push, complete repository changes through:

1. implementation or documentation update,
2. validation,
3. Git commit,
4. push to a dated branch.

Use a dated branch such as:

```text
ai/YYYY-MM-DD-short-description
```

Do not force push. Do not push directly to `main` unless the user explicitly asks for it.

## First-Read Rule

At the beginning of every task in this repository:

1. Read this `AGENTS.md` file first.
2. Read `AI_RULES.md`.
3. Read `WORKFLOW.md`.
4. Read `PLAN.md`.
5. Read `AQUAPLAY_GARDEN_SPEC.md` for game design and MVP scope.
6. Confirm the working directory is the repository root.
7. Run `git status --short`.
8. Identify the files expected to change before editing.

## Current Direction

- Project name: `Aqua_Play` for now. It may be renamed later.
- Engine: Unity.
- Primary language: C#.
- Blender role: Unity-oriented asset generation and source asset workflow.
- Repository layout: keep `blender/` and `unity/` separated, with generated exports moving from Blender into Unity as needed.
- MVP scope: follow `AQUAPLAY_GARDEN_SPEC.md` as the confirmed minimum playable baseline.
- Work flow: follow `WORKFLOW.md`; complete phases through push and user review before starting the next phase.

## Conflict Handling

If Markdown files contradict each other, use this order:

1. Latest direct user instruction.
2. `AGENTS.md`, `WORKFLOW.md`, and `PLAN.md` for current project direction and collaboration flow.
3. `AI_RULES.md` for safety and operating rules.
4. `AQUAPLAY_GARDEN_SPEC.md` for game design and MVP requirements.
5. `docs/` for setup and workflow details.

Ask the user before resolving conflicts that affect destructive file operations, generated assets, or Git history.

The engine decision is currently resolved as Unity. Treat remaining Godot references as stale unless the user explicitly reopens that discussion.
