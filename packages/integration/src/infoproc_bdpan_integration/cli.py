"""CLI helpers for the integration layer."""

from __future__ import annotations

import argparse
import json

from .policy import FIXED_REMOTE_ROOTS, NO_VALID_TEXT_SKIP_TARGETS, RETENTION_POLICY
from .workflow import build_job_spec


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="infoproc-bdpan-integration")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("remote-roots", help="Emit fixed remote output roots.")
    subparsers.add_parser("retention-policy", help="Emit the run retention policy.")
    subparsers.add_parser("no-valid-text-policy", help="Emit the exceptional-file upload skip policy.")

    job = subparsers.add_parser("job-template", help="Emit a remote-first job spec.")
    job.add_argument("--remote-input-path", required=True)
    job.add_argument("--run-name", required=True)

    subparsers.add_parser("workflow-summary", help="Emit the workflow policy summary.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "remote-roots":
        payload = FIXED_REMOTE_ROOTS
    elif args.command == "retention-policy":
        payload = RETENTION_POLICY
    elif args.command == "no-valid-text-policy":
        payload = {"skip_upload_targets": list(NO_VALID_TEXT_SKIP_TARGETS)}
    elif args.command == "job-template":
        payload = build_job_spec(args.remote_input_path, args.run_name).to_dict()
    else:
        payload = {
            "fixed_remote_roots": FIXED_REMOTE_ROOTS,
            "retention_policy": RETENTION_POLICY,
            "no_valid_text_skip_targets": list(NO_VALID_TEXT_SKIP_TARGETS),
        }

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
