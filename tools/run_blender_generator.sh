#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

if [[ ! -f "AI_RULES.md" || ! -d "blender/scripts" || ! -d "blender/exports" ]]; then
  echo "Refusing to run: expected repository structure was not found." >&2
  exit 1
fi

BLENDER_BIN="${BLENDER_BIN:-blender}"
"${BLENDER_BIN}" --background --python "blender/scripts/generate_modular_asset.py"
