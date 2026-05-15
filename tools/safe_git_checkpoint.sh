#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 \"scope: concise commit message\"" >&2
  exit 1
fi

MESSAGE="$1"

case "${MESSAGE}" in
  *$'\n'*|"" )
    echo "Commit message must be a single non-empty line." >&2
    exit 1
    ;;
esac

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

if [[ ! -f "AI_RULES.md" ]]; then
  echo "Refusing to commit outside the expected repository." >&2
  exit 1
fi

BRANCH="$(git branch --show-current)"
if [[ ! "${BRANCH}" =~ [0-9]{4}-[0-9]{2}-[0-9]{2} ]]; then
  echo "Warning: branch name does not contain an ISO date (YYYY-MM-DD): ${BRANCH}" >&2
fi

git status --short
git diff --check
git add AI_RULES.md README.md docs blender unity tools .gitignore
git commit -m "${MESSAGE}"
