#!/usr/bin/env python3
"""Prune bulky run cache directories while preserving audit-friendly outputs."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

PRUNE_DIRS = ("00_source", "02_normalized")
KEEP_HINT = (
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually delete the prunable directories. Default is dry-run.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    run_dir = Path(args.run_dir)
    candidates = [run_dir / name for name in PRUNE_DIRS if (run_dir / name).exists()]
    payload = {
        "run_dir": str(run_dir),
        "execute": args.execute,
        "prune_candidates": [str(path) for path in candidates],
        "keep_hint": list(KEEP_HINT),
    }

    if args.execute:
        for path in candidates:
            shutil.rmtree(path)
        payload["status"] = "pruned"
    else:
        payload["status"] = "dry-run"

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
