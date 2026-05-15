# Markdown Readiness Review

Last reviewed: 2026-05-15

This document records the current confidence level and remaining concerns in the project Markdown before implementation work proceeds.

## Summary

There are no blocking contradictions in the current Markdown set.

The active direction is consistent:

- `Aqua_Play` is the working project name.
- Unity and C# are the active implementation direction.
- Blender is a supporting Unity asset pipeline.
- The MVP baseline is fixed in `AQUAPLAY_GARDEN_SPEC.md`.
- Work should follow `WORKFLOW.md`.
- The canonical repository is `https://github.com/Terumasa0218/Aqua_Play`.

## Non-Blocking Concerns

These items should be watched during implementation, but they do not block Phase 0.

### Unity Version Is Not Locked

The docs say Unity LTS should be used, but the exact Unity version is not decided yet.

Recommended handling:

- Choose the installed Unity LTS version before or during Phase 0.
- Record the version in `PLAN.md`, `README.md`, and Unity project settings once fixed.

### Unity Project State Needs Verification

The docs describe the desired Unity structure, but implementation must verify the actual `unity/` project contents.

Recommended handling:

- Phase 0 should begin by inspecting the current Unity project.
- If the project is missing or incomplete, stop at a clean boundary and confirm whether to generate or normalize it.

### Water Visual Method Is Still Open

The spec allows mesh fill, shader fill, particles, or simple visual states.

Recommended handling:

- Use the simplest readable visual method for MVP.
- Do not spend Phase 0 or Phase 1 on polished water rendering.

### Water Conservation Is Intentionally Loose

The MVP does not require strict water conservation. This is a design decision, not a contradiction.

Recommended handling:

- Keep MVP water symbolic and easy to debug.
- Revisit stricter conservation only when storage, dams, or tanks are introduced.

### Pump Automation Is Future Scope

The MVP uses manual pump activation. Automatic pump behavior is not decided.

Recommended handling:

- Implement manual activation first.
- Treat automatic behavior as a later design decision.

### Energy Resource Is Not Part of MVP

The design mentions Energy as future scope. MVP coin generation should remain direct and simple.

Recommended handling:

- Do not introduce Energy in the first playable loop.
- Revisit Energy only if later devices need it.

### Project Name May Change

`Aqua_Play` is currently accepted as the working name, but it may change later.

Recommended handling:

- Keep code namespaces reasonably neutral, such as `AquaPlay`.
- Avoid hardcoding a final player-facing title into assets unless needed.

## Current Confidence

The Markdown is ready for Phase 0 planning and Unity project inspection.

The main thing to avoid is overbuilding. If Phase 0 reveals missing Unity setup, version mismatches, or unclear project structure, stop and ask before generating a large Unity project or rewriting core structure.
