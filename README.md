# Aqua_Play

Aqua_Play is structured for safe AI-assisted game development with Blender, Unity, and Git.

## Start Here

Before using any AI coding agent in this repository, read:

- [`AI_RULES.md`](AI_RULES.md)
- [`docs/ai-assisted-development-setup.md`](docs/ai-assisted-development-setup.md)

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

## Safety Model

AI agents are restricted to repository-local work and should only interact with:

- Blender scripts and exports under `blender/`
- Unity project assets under `unity/`
- Documentation and tooling under `docs/`, `tools/`, and `AI_RULES.md`

Generated assets are isolated under `blender/exports/` and `unity/Assets/Generated/` for easy review and rollback.
