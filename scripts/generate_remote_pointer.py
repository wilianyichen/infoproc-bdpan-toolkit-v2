#!/usr/bin/env python3
"""Write a REMOTE_POINTER.json file for a cleaned input directory."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-dir-name", required=True)
    parser.add_argument("--remote-path", required=True)
    parser.add_argument(
        "--output",
        required=True,
        help="Output path for REMOTE_POINTER.json",
    )
    parser.add_argument("--note", action="append", default=[])
    return parser


def main() -> int:
    args = build_parser().parse_args()
    payload = {
        "schema_version": "1",
        "generated_at": utc_now(),
        "local_dir_name": args.local_dir_name,
        "remote_path": args.remote_path,
        "source_kind": "baidupan-remote",
        "local_materialization": "ephemeral",
        "cleanup_status": "pointer-only",
        "notes": args.note,
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
