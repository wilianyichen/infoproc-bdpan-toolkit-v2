#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "" ]]; then
  cat <<'EOF'
Usage:
  infoproc_remote_first.sh <remote_input_path> [run_name]

Purpose:
  Release-facing scaffold for the remote-first workflow.

Expected steps:
  1. Materialize the remote input path locally.
  2. Run infoproc with an explicit run name.
  3. Verify the run completed.
  4. Upload text, distill, and rank outputs to fixed remote roots.
  5. Flag no-valid-text exceptions.
  6. Write REMOTE_POINTER.json for the local input tree.
  7. Prune 00_source and 02_normalized from the run.

This scaffold intentionally does not call the installed private environment directly.
It is a release placeholder that shows the stable contract and argument surface.
EOF
  exit 1
fi

REMOTE_INPUT_PATH="$1"
RUN_NAME="${2:-}"

if [[ "$RUN_NAME" == "" ]]; then
  RUN_NAME="$(basename "$REMOTE_INPUT_PATH")-$(date +%Y%m%d)"
fi

cat <<EOF
{
  "remote_input_path": "${REMOTE_INPUT_PATH}",
  "run_name": "${RUN_NAME}",
  "text_output_root": "/开智/视频文本蒸馏/文本/录播文本",
  "final_output_root": "/开智/视频文本蒸馏/蒸馏/录播",
  "next_step": "Replace this scaffold with the released integration CLI or local environment wrapper."
}
EOF
