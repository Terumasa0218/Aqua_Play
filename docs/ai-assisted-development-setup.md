# AI-Assisted Unity and Blender Development Setup

This document defines the repository setup for AI-assisted development of Aqua_Play with Unity, Blender, and Git.

## Canonical Repository

```text
https://github.com/Terumasa0218/Aqua_Play
```

The GitHub repository is the source of truth. Local folders are working copies and should be checked against `origin/main` before important work.

## Objectives

The environment should allow an AI agent and human developer to:

- Build a Unity-first 3D garden waterway simulation.
- Generate or update supporting 3D assets with Blender.
- Export Blender assets into predictable repository folders.
- Import generated assets into Unity as reviewed prefabs.
- Keep game design, implementation plans, and safety rules in Markdown.
- Commit and push reviewable changes unless the user requests discussion only.

Safety and predictability take priority over speed.

## Recommended Repository Structure

```text
Aqua_Play/
├── AGENTS.md
├── AI_RULES.md
├── PLAN.md
├── README.md
├── AQUAPLAY_GARDEN_SPEC.md
├── docs/
│   └── ai-assisted-development-setup.md
├── blender/
│   ├── scripts/
│   │   └── generate_modular_asset.py
│   └── exports/
│       └── .gitkeep
├── unity/
│   └── Assets/
│       ├── Scenes/
│       ├── Scripts/
│       ├── Prefabs/
│       ├── Materials/
│       ├── Art/
│       ├── Editor/
│       │   └── GeneratedAssetPipeline.cs
│       └── Generated/
│           └── .gitkeep
└── tools/
    ├── run_blender_generator.sh
    ├── run_unity_generated_pipeline.sh
    └── safe_git_checkpoint.sh
```

## Directory Responsibilities

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Startup instructions and default delivery behavior for AI agents. |
| `AI_RULES.md` | Safety, scope, tool, and Git rules. |
| `PLAN.md` | Current decisions, phase plan, and open questions. |
| `AQUAPLAY_GARDEN_SPEC.md` | Game design and MVP behavior. |
| `docs/` | Setup guides and workflow documentation. |
| `blender/scripts/` | Blender Python scripts for procedural generation and export. |
| `blender/exports/` | Generated `.fbx`, `.glb`, and optional `.blend` outputs. |
| `unity/` | Unity project root. |
| `unity/Assets/Scripts/` | Runtime C# scripts. |
| `unity/Assets/Editor/` | Unity Editor-only automation scripts. |
| `unity/Assets/Generated/` | Imported/generated assets and prefabs managed by automation. |
| `tools/` | Repository-local wrappers for safe command execution. |

## First-Read Checklist

Every AI task should start with:

```bash
pwd
git fetch --all --prune
git status --short
cat AGENTS.md
cat AI_RULES.md
cat PLAN.md
```

For game behavior or implementation-direction tasks, also read:

```bash
cat AQUAPLAY_GARDEN_SPEC.md
```

## Unity Setup

Unity is the active engine direction.

Recommended project rules:

- Keep the Unity project under `unity/`.
- Use C# for gameplay and editor automation.
- Keep runtime code under `unity/Assets/Scripts/`.
- Keep editor-only code under `unity/Assets/Editor/`.
- Keep generated imports and prefabs under `unity/Assets/Generated/`.
- Prefer prefabs and data assets over direct scene mutation.
- Use a Unity LTS version once the project version is locked.

Suggested runtime script groups:

```text
unity/Assets/Scripts/
├── Core/
├── Grid/
├── Parts/
├── Water/
├── Economy/
├── Wind/
└── UI/
```

## Blender Setup

Blender is a supporting asset pipeline for Unity.

Rules:

- Blender source scripts live in `blender/scripts/`.
- Generated exports go to `blender/exports/`.
- `.fbx` is the default Unity import format.
- `.glb` may be exported for preview or interchange.
- Scripts should be deterministic and repository-relative.

Run the Blender wrapper:

```bash
./tools/run_blender_generator.sh
```

If Blender is not on `PATH`, pass an explicit executable:

```bash
BLENDER_BIN="/path/to/blender" ./tools/run_blender_generator.sh
```

## Unity Import Pipeline

The intended asset flow is:

1. Blender creates or updates assets under `blender/exports/`.
2. Unity editor automation copies supported exports into `unity/Assets/Generated/Imported/`.
3. Unity refreshes the AssetDatabase.
4. Unity creates or updates generated prefabs under `unity/Assets/Generated/Prefabs/`.
5. The user reviews generated assets before using them in production scenes.

Run the Unity wrapper:

```bash
./tools/run_unity_generated_pipeline.sh
```

If Unity is not on `PATH`, pass an explicit executable:

```bash
UNITY_BIN="/path/to/Unity" ./tools/run_unity_generated_pipeline.sh
```

Equivalent direct command shape:

```bash
Unity \
  -batchmode \
  -quit \
  -projectPath unity \
  -executeMethod AquaPlay.Editor.GeneratedAssetPipeline.Run
```

## MVP Development Strategy

The MVP should not use real fluid simulation. Use symbolic grid-based water data:

- water units,
- flow rate,
- capacity,
- water level,
- overflow,
- wetness,
- connection directions,
- visual flow intensity.

The first playable target is:

```text
place canals
start pump
water moves
water level changes
overflow wets ground
water wheel rotates
coins increase
coins buy more parts
light wind adds motion
```

## Git Workflow

Work on dated branches:

```bash
git switch -c ai/YYYY-MM-DD-short-description
```

Before committing:

```bash
git status --short
git diff --check
git diff
```

Commit with focused prefixes:

```text
docs: align markdown with unity direction
unity: add grid placement foundation
blender: update modular asset generator
pipeline: wire generated asset import
gameplay: add symbolic water tick
```

Push the branch unless the user requested discussion only:

```bash
git push -u origin ai/YYYY-MM-DD-short-description
```

Do not force push. Do not rewrite history. Direct pushes to `main` require explicit user instruction.

## Review Points

Before accepting generated or AI-made changes, review:

- Markdown consistency.
- `git diff`.
- Unity scene and prefab changes.
- Generated assets under `unity/Assets/Generated/`.
- Blender exports under `blender/exports/`.
- Any editor automation before running it on valuable project assets.
