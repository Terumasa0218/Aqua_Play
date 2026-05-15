# Aqua_Play Plan

## Source of Truth

The canonical repository is:

```text
https://github.com/Terumasa0218/Aqua_Play
```

Use the GitHub repository as the most accurate source. Local working copies are temporary views of that repository and should be checked against `origin/main` before important planning, implementation, or documentation changes.

## Current Decisions

- Project name is `Aqua_Play` for now.
- The name may change later.
- Unity is the active engine direction.
- C# is the active implementation language.
- Blender remains part of the workflow as a Unity asset companion.
- Keep `blender/` and `unity/` separated.
- Move generated assets or metadata from Blender to Unity through explicit export/import steps.
- `AQUAPLAY_GARDEN_SPEC.md` defines the confirmed minimum MVP scope.

## MVP Minimum Line

The MVP is not complete until all of these work together:

1. place canal parts on a grid,
2. start a pump,
3. move symbolic water through connected parts,
4. show water level,
5. overflow when capacity is exceeded,
6. mark nearby ground wet,
7. rotate a water wheel,
8. increase coins,
9. spend coins on more parts,
10. show a light wind effect.

Everything else is additive after this loop feels good.

## Unity Implementation Direction

Recommended initial Unity structure:

```text
unity/
└── Assets/
    ├── Scenes/
    ├── Scripts/
    │   ├── Core/
    │   ├── Grid/
    │   ├── Water/
    │   ├── Parts/
    │   ├── Economy/
    │   ├── Wind/
    │   └── UI/
    ├── Prefabs/
    ├── Materials/
    ├── Art/
    ├── Generated/
    │   ├── Imported/
    │   └── Prefabs/
    └── Editor/
```

The simulation should be data-driven and grid-based. Do not use real fluid simulation for MVP.

## Planned Phases

### Phase 0: Unity Foundation

- Create or normalize the Unity project under `unity/`.
- Add a 10x10 garden grid.
- Add a top-down 3D camera.
- Add cell picking and debug coordinate display.

### Phase 1: Part Placement

- Add straight canal, corner canal, water wheel, and mini pump placement.
- Add rotation and deletion.
- Store placed parts as grid data.

### Phase 2: Symbolic Water Simulation

- Add water units, capacity, water level, flow rate, loss rate, overflow, and wetness.
- Use fixed ticks and double buffering.

### Phase 3: Coin Loop

- Rotate water wheels from water flow.
- Generate coins.
- Spend coins on additional parts.

### Phase 4: Light Wind

- Add wind power variation.
- Let wind lightly move water wheels, leaves, grass, or water surfaces.
- Keep wind income very small so water remains the main system.

### Later Phases

- Junctions and flow splitting.
- Terrain and soil.
- Storage, dams, and gates.
- Height and waterfalls.
- Larger water events.
- Visual polish and theme sets.

## Open Design Questions

These are not blockers for the MVP direction:

1. Which Unity LTS version should be locked for the project?
2. Should the water visuals use mesh fill, shader fill, particles, or a hybrid?
3. Should pump activation be manual forever, or only manual in MVP?
4. Should coins be generated directly by water wheels, or should an Energy resource be introduced later?
5. How strict should water conservation become after MVP?
6. Which Blender export format should be canonical for Unity: `.fbx` only, or `.fbx` plus `.glb` preview?
7. When should the project name change from `Aqua_Play` to a more player-facing title?

## Documentation Cleanup Targets

- Keep `README.md` short and current.
- Keep `AGENTS.md` focused on agent startup and push behavior.
- Keep `AI_RULES.md` focused on safe operating rules.
- Keep `PLAN.md` focused on decisions and next implementation phases.
- Keep `AQUAPLAY_GARDEN_SPEC.md` focused on game behavior.
- Keep `docs/ai-assisted-development-setup.md` focused on Unity and Blender setup.
