#!/usr/bin/env bash
set -euo pipefail

if [[ ! -f "pyproject.toml" || ! -d "packages" ]]; then
  echo "Run this from the oss-v2 repository root." >&2
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ./packages/infoproc-core
pip install -e ./packages/bdpan-ops
pip install -e ./packages/integration

echo "Repository bootstrap complete."
echo "Next:"
echo "  make check"
echo "  python -m infoproc_bdpan_integration workflow-summary"
