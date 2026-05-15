# AI Development Rules

## 1. Purpose

This repository is operated with AI-assisted development. Any AI coding agent working in this repository must strictly follow all rules in this document.

These rules define the required safety boundaries, workflow expectations, repository restrictions, and development standards for AI-assisted work on this game development project.

## 2. Allowed Scope

The AI agent is only allowed to interact with the following:

- Blender
- Unity
- Files inside the specified repository

The AI agent must not:

- Access files outside the repository
- Access system directories
- Access personal files
- Access browser data
- Access passwords or credentials
- Modify operating system settings
- Install unrelated software
- Execute unrelated shell commands

## 3. Repository Restriction

The AI agent may only modify files inside the specified repository.

The AI agent must not:

- Access other repositories
- Clone unrelated repositories
- Modify global Git configuration
- Push to unrelated remotes

All repository work must remain limited to the current project unless the user explicitly authorizes otherwise.

## 4. Allowed Applications

Allowed applications and tools:

- Blender
- Unity
- Git
- Terminal commands required for project development

Forbidden applications and tools:

- Any unrelated application or tool

The AI agent must use only the applications and tools required to complete the requested project development task.

## 5. Mandatory Workflow

The AI agent must follow this workflow exactly.

### Step 1: Perform Only the Requested Task

- Perform only the task explicitly requested by the user.
- Do not expand the scope of work without approval.
- Do not begin unrelated improvements, cleanup, refactors, or optimizations.

### Step 2: Stop After Task Completion

After completing the requested task, the AI agent must:

- Stop work immediately.
- Explain all changes clearly.
- Wait for user confirmation before continuing.

The AI agent must not continue automatically.

### Step 3: Create a Backup Point Before the Next Task

Before starting the next task, the AI agent must create a backup point and ensure rollback capability.

Preferred backup methods include:

- Git commit
- Git tag
- Branch snapshot

Rollback capability is mandatory before additional work begins.

### Step 4: Use a Date-Based Branch Name

The AI agent must use a branch name that contains the current date.

Branch name format:

```text
yyyy-mm-dd-task-name
```

Example:

```text
2026-05-15-create-ai-rules
```

## 6. Git Rules

The AI agent must:

- Commit frequently.
- Keep commits small.
- Write clear commit messages.
- Avoid destructive Git operations.

The AI agent must not:

- Force push.
- Delete branches without permission.
- Rewrite commit history.
- Execute dangerous Git commands without explicit user approval.

Forbidden Git command examples include:

```bash
git push --force
git reset --hard
git clean -fd
```

These commands must not be executed unless explicitly approved by the user.

## 7. File Safety Rules

The AI agent must:

- Preserve existing assets whenever possible.
- Avoid overwriting files without confirmation.
- Avoid deleting files unless necessary.

Before deleting files, the AI agent must:

- Explain why deletion is necessary.
- Wait for user approval.

The AI agent must treat all existing project files, assets, scenes, prefabs, scripts, and configuration files as valuable unless the user states otherwise.

## 8. Blender Rules

The AI agent must:

- Preserve scale consistency.
- Preserve coordinate conventions.
- Preserve modular connection standards.

Generated Blender assets should:

- Be reusable.
- Follow project scale rules.
- Use clean naming conventions.

The AI agent must avoid introducing assets that conflict with established scale, orientation, naming, or modular assembly conventions.

## 9. Unity Rules

The AI agent must:

- Avoid breaking scenes.
- Avoid changing project-wide settings unnecessarily.
- Avoid modifying unrelated prefabs or assets.

Before finalizing work, the AI agent must explain:

- Scene changes.
- Prefab changes.
- Serialized asset changes.

Unity changes must be limited to the requested task and must preserve existing project behavior whenever possible.

## 10. Error Handling

If uncertain, the AI agent must:

- Stop.
- Explain the uncertainty.
- Ask for clarification.

The AI agent must not guess when destructive operations are involved.

Destructive or high-risk operations require explicit user approval before execution.

## 11. Core Principle

Safety is prioritized over speed.

Rollback capability is mandatory.

The AI agent must behave conservatively and predictably at all times. The agent must protect existing work, minimize risk, and avoid unnecessary changes while completing only the task requested by the user.
