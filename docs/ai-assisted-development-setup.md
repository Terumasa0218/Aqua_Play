# AI-Assisted Game Development Environment Setup

This document defines a production-oriented repository setup for AI-assisted game development with Blender, Unity, and Git. It is intended for AI coding agents such as Codex, Cursor, or AI CLI tools that need to safely generate game assets and automation scripts while remaining restricted to repository files.

## Objectives

The environment allows an AI agent to:

- Generate procedural Blender assets with Python.
- Execute Blender scripts from terminal commands.
- Export generated assets as `.glb` and `.fbx` files.
- Generate and modify Unity assets with Unity Editor scripts.
- Execute Unity Editor automation from the command line.
- Work only inside this repository.
- Follow strict safety, review, and rollback rules.

Safety and predictability take priority over speed.

## Repository Structure

Recommended structure:

```text
Aqua_Play/
├── AI_RULES.md
├── README.md
├── docs/
│   └── ai-assisted-development-setup.md
├── blender/
│   ├── scripts/
│   │   └── generate_modular_asset.py
│   └── exports/
│       └── .gitkeep
├── unity/
│   └── Assets/
│       ├── Editor/
│       │   └── GeneratedAssetPipeline.cs
│       └── Generated/
│           └── .gitkeep
└── tools/
    ├── run_blender_generator.sh
    ├── run_unity_generated_pipeline.sh
    └── safe_git_checkpoint.sh
```

Directory responsibilities:

| Path | Purpose |
| --- | --- |
| `AI_RULES.md` | Persistent operating rules for AI agents. |
| `docs/` | Setup guides, workflow documentation, and pipeline notes. |
| `blender/scripts/` | Blender Python scripts for procedural generation and export. |
| `blender/exports/` | Generated `.glb`, `.fbx`, and optional `.blend` outputs. |
| `unity/` | Unity project root. |
| `unity/Assets/Editor/` | Unity Editor-only automation scripts. |
| `unity/Assets/Generated/` | Imported/generated assets and prefabs managed by automation. |
| `tools/` | Repository-local wrappers for safe command execution. |

## AI Rules Integration

`AI_RULES.md` is the persistent safety contract for AI agents. The agent must read it before making repository changes.

Required startup checklist for every AI task:

```bash
pwd
cat AI_RULES.md
git status --short
```

The agent should then identify the intended files to change and avoid unrelated edits.

Recommended instruction for AI tools:

```text
Before performing any task, read AI_RULES.md and follow it exactly. Work only inside this repository. Prefer small, reviewable changes and preserve rollback capability through Git commits.
```

## Blender Automation Setup

Blender automation is implemented through Python scripts in `blender/scripts/` and shell wrappers in `tools/`.

### Example Generator

`blender/scripts/generate_modular_asset.py` creates a deterministic modular blockout asset and exports it to:

- `blender/exports/modular_block.glb`
- `blender/exports/modular_block.fbx`

The script resolves paths relative to the repository root and does not require absolute user-specific paths.

### Terminal Execution

Use the repository-local wrapper:

```bash
BLENDER_BIN="/path/to/blender" ./tools/run_blender_generator.sh
```

If `blender` is already on `PATH`:

```bash
./tools/run_blender_generator.sh
```

Equivalent direct command:

```bash
blender --background --python blender/scripts/generate_modular_asset.py
```

### Blender Export Pipeline

The generator performs this sequence:

1. Clear the default scene.
2. Create procedural modular geometry.
3. Assign materials and object names.
4. Set transforms and origin-friendly placement.
5. Export `.glb` for modern runtime pipelines.
6. Export `.fbx` for broad DCC and Unity compatibility.

Recommended asset conventions:

- Use metric-friendly units.
- Keep asset origins at ground center or logical snap points.
- Name generated objects consistently.
- Export to `blender/exports/` only.
- Keep scripts deterministic for reproducible output.

## Unity Automation Setup

Unity automation is implemented with Editor scripts under `unity/Assets/Editor/`.

### Example Editor Script

`unity/Assets/Editor/GeneratedAssetPipeline.cs` provides command-line callable methods for:

- Refreshing the AssetDatabase.
- Importing generated Blender exports.
- Creating prefabs under `unity/Assets/Generated/Prefabs/`.
- Validating that generated work remains under `Assets/Generated`.

### Terminal Execution

Use the repository-local wrapper:

```bash
UNITY_BIN="/path/to/Unity" ./tools/run_unity_generated_pipeline.sh
```

If the Unity executable is on `PATH`:

```bash
./tools/run_unity_generated_pipeline.sh
```

Equivalent direct command:

```bash
Unity \
  -batchmode \
  -quit \
  -projectPath unity \
  -executeMethod AquaPlay.Editor.GeneratedAssetPipeline.Run
```

On macOS, the executable is often similar to:

```bash
/Applications/Unity/Hub/Editor/2022.3.XXf1/Unity.app/Contents/MacOS/Unity
```

On Windows, it is often similar to:

```powershell
"C:\Program Files\Unity\Hub\Editor\2022.3.XXf1\Editor\Unity.exe"
```

### Unity Import Pipeline

The intended automated flow is:

1. Blender exports assets into `blender/exports/`.
2. Unity Editor script mirrors supported exports into `unity/Assets/Generated/Imported/`.
3. Unity imports refreshed assets through `AssetDatabase.Refresh()`.
4. The script creates or updates generated prefabs in `unity/Assets/Generated/Prefabs/`.
5. The user reviews generated assets before accepting them into gameplay scenes.

Recommended Unity conventions:

- Place AI-generated assets under `Assets/Generated`.
- Keep Editor automation under `Assets/Editor`.
- Avoid modifying hand-authored scenes unless explicitly requested.
- Create prefabs instead of directly editing scenes.
- Make generated changes easy to review and revert.

## Git Workflow for AI-Assisted Development

Git is the rollback mechanism. Every AI-assisted task should be performed on a dated branch and committed at safe checkpoints.

### Branch Naming

Required pattern:

```text
ai/YYYY-MM-DD-short-description
```

Examples:

```bash
git switch -c ai/2026-05-15-blender-unity-pipeline
git switch -c ai/2026-05-15-modular-props
git switch -c ai/2026-05-15-prefab-importer
```

### Commit Message Conventions

Use concise, scoped messages:

```text
docs: add ai-assisted pipeline setup
blender: add modular asset generator
unity: add generated asset importer
tools: add safe automation wrappers
pipeline: update generated prefab workflow
```

### Safe Commit Process

Recommended checkpoint command:

```bash
./tools/safe_git_checkpoint.sh "pipeline: add generated asset workflow"
```

Manual equivalent:

```bash
git status --short
git diff --check
git diff
git add <reviewed-files>
git commit -m "pipeline: add generated asset workflow"
```

### Rollback

Inspect recent checkpoints:

```bash
git log --oneline --max-count=10
```

Rollback a committed change safely:

```bash
git revert <commit-sha>
```

Restore one file before commit:

```bash
git restore path/to/file
```

### Prohibited Git Operations

The AI agent must not run:

```bash
git push --force
git push --force-with-lease
git reset --hard
git rebase
git commit --amend
git filter-branch
git filter-repo
```

These commands either rewrite history, discard work, or make rollback less predictable.

## Safety Restriction Strategy

The environment restricts the AI agent to Blender, Unity, and repository files through layered controls.

### Repository-Only File Policy

- All scripts use paths relative to the repository root.
- Tool wrappers verify they are executed from the repository root.
- Generated exports are written only to `blender/exports/`.
- Unity-generated assets are written only to `unity/Assets/Generated/`.

### Command Policy

Allowed automation entry points:

```bash
./tools/run_blender_generator.sh
./tools/run_unity_generated_pipeline.sh
./tools/safe_git_checkpoint.sh "message"
```

The AI agent must not use commands that inspect personal files, system directories, or unrelated repositories.

### Generated Asset Policy

- Prefer additive generation over overwriting authored content.
- Generated files must be placed in clearly named generated directories.
- Generated prefabs should be reviewed before scene integration.
- Destructive cleanup requires explicit user approval.

### Human Review Gate

The user should review:

- `git diff`
- Generated `.glb` and `.fbx` files
- Unity prefabs under `Assets/Generated/Prefabs/`
- Any Editor script changes before running them in a production project

## Recommended Tooling

| Tool | Use | Why it is useful |
| --- | --- | --- |
| Codex CLI | Repository-local AI coding agent | Good for scripted code changes, terminal workflows, and documented automation. |
| Cursor | AI-assisted IDE | Useful for reviewing diffs, editing C# and Python, and keeping AI context close to source files. |
| VS Code | Lightweight editor | Strong Python, C#, Markdown, and Git extension support. |
| GitHub Desktop | Visual Git review | Helpful for non-terminal diff review, branch management, and safe commits. |
| Blender | Procedural asset generation | Python API supports deterministic mesh creation and batch exports. |
| Unity Editor | Asset import and prefab generation | Batch mode and Editor scripts support automated import, prefab creation, and validation. |
| ripgrep (`rg`) | Fast repository search | Safer and faster than broad recursive shell searches in large game repositories. |

## Automation Philosophy

The intended workflow is conservative and reviewable:

1. The AI agent performs repetitive technical setup and generation tasks.
2. Generated changes are isolated in predictable directories.
3. The user reviews diffs and generated assets.
4. Git commits provide restore points.
5. Rollback is mandatory and must remain simple.

The AI should behave as a cautious automation assistant, not as an autonomous production owner.

Practical rules:

- Prefer small changes over broad refactors.
- Prefer generated prefabs over direct scene edits.
- Prefer deterministic scripts over manual asset mutation.
- Prefer documented terminal commands over ad hoc commands.
- Stop and ask for approval before deleting or replacing valuable assets.

## End-to-End Example

Generate Blender exports:

```bash
./tools/run_blender_generator.sh
```

Run Unity import and prefab generation:

```bash
./tools/run_unity_generated_pipeline.sh
```

Review changes:

```bash
git status --short
git diff
```

Create a safe checkpoint:

```bash
./tools/safe_git_checkpoint.sh "pipeline: generate modular block asset"
```
