#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

if [[ ! -f "AI_RULES.md" || ! -d "unity/Assets/Editor" || ! -d "unity/Assets/Generated" ]]; then
  echo "Refusing to run: expected Unity repository structure was not found." >&2
  exit 1
fi

UNITY_BIN="${UNITY_BIN:-Unity}"
"${UNITY_BIN}" \
  -batchmode \
  -quit \
  -projectPath "unity" \
  -executeMethod "AquaPlay.Editor.GeneratedAssetPipeline.Run"
