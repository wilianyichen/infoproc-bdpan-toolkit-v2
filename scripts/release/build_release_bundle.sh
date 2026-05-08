#!/usr/bin/env bash
set -euo pipefail

if [[ ! -f "pyproject.toml" || ! -d "packages" ]]; then
  echo "Run this from the oss-v2 repository root." >&2
  exit 1
fi

python3 scripts/release/package_release.py "$@"
