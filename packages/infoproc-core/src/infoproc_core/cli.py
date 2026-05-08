"""CLI helpers for infoproc-core."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .layout import (
    PRUNABLE_AFTER_DELIVERY,
    RETAIN_AFTER_DELIVERY,
    RUN_STAGE_DIRS,
    existing_entries,
    retention_plan_for_entries,
)
from .models import RunDirectorySummary, RunRetentionPlan


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="infoproc-core")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("describe-layout", help="Emit the canonical run layout.")

    retention = subparsers.add_parser(
        "retention-plan",
        help="Build a retention plan for a run directory.",
    )
    retention.add_argument("run_dir", help="Run directory to inspect.")
    retention.add_argument(
        "--existing",
        action="append",
        default=[],
        help="Optional explicit entry names. If omitted, inspect the filesystem.",
    )
    return parser


def command_describe_layout() -> dict[str, object]:
    return {
        "run_stage_dirs": list(RUN_STAGE_DIRS),
        "retain_after_delivery": list(RETAIN_AFTER_DELIVERY),
        "prunable_after_delivery": list(PRUNABLE_AFTER_DELIVERY),
    }


def command_retention_plan(run_dir: str, explicit_entries: list[str]) -> dict[str, object]:
    path = Path(run_dir)
    entries = explicit_entries or existing_entries(path)
    plan = retention_plan_for_entries(path, entries)
    summary = RunDirectorySummary(
        run_dir=str(path),
        existing_entries=entries,
        retained_entries=plan["keep"],
        prunable_entries=plan["prune"],
        audit_ready=bool(plan["keep"]),
    )
    return {
        "retention_plan": RunRetentionPlan(**plan).to_dict(),
        "summary": summary.to_dict(),
    }


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "describe-layout":
        payload = command_describe_layout()
    else:
        payload = command_retention_plan(args.run_dir, args.existing)

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
