# Aqua_Play

Aqua_Play is a Unity-first 3D garden waterway simulation game. The player builds a small toy-like water garden by placing canals, pumps, water wheels, and decorative parts on a grid.

Canonical repository:

```text
https://github.com/Terumasa0218/Aqua_Play
```

Treat the GitHub repository as the most accurate source of project truth.

## Current Direction

- Engine: Unity.
- Primary language: C#.
- Asset companion: Blender, used for Unity-oriented generated or hand-authored 3D assets.
- Project name: `Aqua_Play` for now. It may change later.
- MVP: fixed by `AQUAPLAY_GARDEN_SPEC.md`.

The previous Godot direction has been superseded. Any remaining Godot references should be treated as old context unless explicitly preserved for comparison.

## Start Here

Before using any AI coding agent in this repository, read:

- [`AGENTS.md`](AGENTS.md)
- [`AI_RULES.md`](AI_RULES.md)
- [`PLAN.md`](PLAN.md)
- [`AQUAPLAY_GARDEN_SPEC.md`](AQUAPLAY_GARDEN_SPEC.md)
- [`docs/ai-assisted-development-setup.md`](docs/ai-assisted-development-setup.md)

## MVP Baseline

The minimum playable loop must include:

1. Place canal parts.
2. Start a pump.
3. Move symbolic water through connected parts.
4. Display water level.
5. Trigger overflow when capacity is exceeded.
6. Mark nearby ground as wet.
7. Rotate a water wheel.
8. Earn coins.
9. Use coins to buy more parts.
10. Show a light wind effect that gives the garden motion.

## Repository Layout

```text
Aqua_Play/
├── AGENTS.md
├── AI_RULES.md
├── PLAN.md
├── README.md
├── AQUAPLAY_GARDEN_SPEC.md
├── docs/
├── blender/
├── unity/
└── tools/
```

Main responsibilities:

- `AQUAPLAY_GARDEN_SPEC.md`: game design, MVP behavior, and phase definitions.
- `PLAN.md`: current decisions, next tasks, and open design questions.
- `AGENTS.md`: startup instructions for AI agents.
- `AI_RULES.md`: safety and Git operating rules.
- `docs/`: setup and workflow documentation.
- `blender/`: Blender source scripts and exports for Unity assets.
- `unity/`: Unity project and generated Unity assets.
- `tools/`: repository-local automation wrappers.

## Automation Entry Points

Generate Blender assets:

```bash
./tools/run_blender_generator.sh
```

Run the Unity generated asset import/prefab pipeline:

```bash
./tools/run_unity_generated_pipeline.sh
```

Create a safe Git checkpoint:

```bash
./tools/safe_git_checkpoint.sh "pipeline: describe checkpoint"
```

## Default Delivery Policy

Unless the user explicitly says `議論のみ`, `相談のみ`, or says not to commit or push, code and documentation changes should be carried through to a Git commit and pushed to a dated branch.

Default branch pattern:

```text
ai/YYYY-MM-DD-short-description
```

Do not force push. Do not rewrite history. Direct pushes to `main` require explicit user instruction.
