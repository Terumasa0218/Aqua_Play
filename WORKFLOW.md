# Aqua_Play Work Flow

This document defines the working flow for Aqua_Play and should also be used as the default collaboration pattern in other chats and repositories unless the user gives different instructions or the target repository has stronger local rules.

## Core Rule

Work should be divided into phases. A phase is a user-reviewable milestone with a clear outcome.

Do not continue from one phase to the next until:

1. the phase work has been committed and pushed,
2. a dated pull request or equivalent dated merge point has been created,
3. the work report has been provided,
4. the user has checked the result,
5. the user says the phase is OK or gives the next instruction,
6. approved work has been merged into `main`,
7. local `main` has been synchronized with `origin/main`.

## Discussion-Only Mode

If the user says `議論のみ`, `相談のみ`, or clearly asks only to discuss, do not edit files, commit, or push.

In discussion-only mode:

- inspect only if needed,
- summarize findings,
- ask or answer questions,
- do not change repository state.

## Phase Flow

Each phase should follow this flow:

1. Confirm current Git state and the canonical remote.
2. Create or use a dated working branch.
3. Break the phase into smaller tasks.
4. Implement one task at a time.
5. Validate the task.
6. Commit and push at task boundaries when useful.
7. Finish the full phase.
8. Validate the phase.
9. Commit and push the phase result.
10. Create or update a pull request with the date in the title.
11. Report what changed, what was validated, and what remains.
12. Stop and wait for user confirmation before merging the phase and before starting the next phase.
13. After user approval, merge the phase into `main`.
14. Synchronize local `main` with `origin/main`.

Recommended branch pattern:

```text
ai/YYYY-MM-DD-short-description
```

## Task Flow Inside a Phase

Tasks inside a phase do not require user confirmation before continuing, but they should still preserve rollback points.

For each meaningful task:

1. keep the change focused,
2. validate the change,
3. commit with a clear message,
4. push the branch,
5. include a date in the commit message or pull request/update note when it helps identify a rollback point.

This makes it possible to return to a known-good point if the user reviews the final phase result and says it is not acceptable.

## Rollback Requirement

Every phase and meaningful task should leave Git restore points.

Preferred rollback methods:

- revert a commit,
- return to a previous pushed branch commit,
- create a corrective commit.

Avoid destructive history operations. Do not force push. Do not use `git reset --hard` unless the user explicitly requests it.

## User Review Gate

After each phase:

- stop work,
- report the pushed branch and commit,
- report the dated pull request or merge point,
- summarize validation,
- tell the user what to check,
- wait for the user's approval or correction request.

After the user approves the phase, merge it into `main`, synchronize local `main`, report the merge commit or resulting `main` commit, and then stop. Do not start the next phase on your own.

## Specification Uncertainty Gate

The Markdown specifications are not final. If implementation reveals that a spec is missing, ambiguous, contradictory, or likely wrong, stop at a clean boundary.

When this happens:

1. finish or revert any partial task so the repository is coherent,
2. commit and push useful completed work if any,
3. report the uncertainty,
4. ask the user what direction to take,
5. treat the next step as discussion unless the user explicitly resumes implementation.

This applies even in the middle of a phase.

## Push and Pull Request Policy

Default behavior:

- commit and push unless the user says discussion only or says not to push,
- push to a dated branch,
- create or update a pull request,
- include the date in the pull request title,
- merge approved work into `main`,
- synchronize local `main` after merge,
- do not push directly to `main` unless explicitly asked or unless a repository intentionally does not use pull requests,
- do not force push.

Pull request titles should include a date so the user can easily identify rollback points.

Recommended title pattern:

```text
YYYY-MM-DD: short description
```

Example:

```text
2026-05-15: docs add phase workflow policy
```

Merging into `main` is part of the normal completion flow after user approval. If the user has clearly delegated automatic PR creation and merging for a class of work, complete that flow and report the final `main` commit.

## Cross-Chat and Cross-Repository Use

Use this workflow as the default in future chats and other repositories when the user is asking for implementation work.

If another repository has its own `AGENTS.md`, `WORKFLOW.md`, or stronger local instructions, follow that repository's rules first and adapt this workflow only where it does not conflict.

If a future chat does not include this file in context, the user may point the agent back to this workflow or ask to copy it into that repository.
