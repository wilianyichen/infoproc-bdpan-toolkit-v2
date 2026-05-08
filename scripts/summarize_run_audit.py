#!/usr/bin/env python3
"""Emit a compact audit summary for a completed remote-first run."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

RETAINED_NAMES = (
    "01_probe",
    "03_text_raw",
    "04_text_clean",
    "05_final",
    "_delivery",
    "_logs",
    "_manifests",
    "_flags",
    "_reports",
)

DELETED_NAMES = (
    "00_source",
    "02_normalized",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--run-name", required=True)
    parser.add_argument("--remote-input-path", required=True)
    parser.add_argument(
        "--upload-completed",
        action="store_true",
        help="Mark the upload stage as verified.",
    )
    parser.add_argument(
        "--output",
        help="Optional JSON file path.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    run_dir = Path(args.run_dir)
    no_valid_text_report = run_dir / "_reports" / "no_valid_text.json"
    exceptional_files = 0
    if no_valid_text_report.exists():
        report = json.loads(no_valid_text_report.read_text(encoding="utf-8"))
        exceptional_files = int(report.get("flagged_count", 0))

    retained = [name for name in RETAINED_NAMES if (run_dir / name).exists()]
    deleted = [name for name in DELETED_NAMES if not (run_dir / name).exists()]
    payload = {
        "generated_at": utc_now(),
        "run_name": args.run_name,
        "remote_input_path": args.remote_input_path,
        "upload_completed": args.upload_completed,
        "exceptional_files": exceptional_files,
        "intentionally_deleted_artifacts": deleted,
        "retained_artifacts": retained,
    }

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
