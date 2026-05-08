"""Canonical run layout and retention rules."""

from __future__ import annotations

from pathlib import Path

RUN_STAGE_DIRS = (
    "00_source",
    "01_probe",
    "02_normalized",
    "03_text_raw",
    "04_text_clean",
    "05_final",
    "_delivery",
    "_logs",
    "_manifests",
    "_flags",
    "_reports",
)

RETAIN_AFTER_DELIVERY = (
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

PRUNABLE_AFTER_DELIVERY = (
    "00_source",
    "02_normalized",
)


def existing_entries(run_dir: Path) -> list[str]:
    """Return sorted direct child names for a run directory."""
    if not run_dir.exists():
        return []
    return sorted(child.name for child in run_dir.iterdir())


def retention_plan_for_entries(run_dir: Path, entries: list[str]) -> dict[str, object]:
    """Build a filesystem-agnostic retention plan."""
    entry_set = set(entries)
    keep = [name for name in RETAIN_AFTER_DELIVERY if name in entry_set]
    prune = [name for name in PRUNABLE_AFTER_DELIVERY if name in entry_set]
    unknown = [name for name in entries if name not in RUN_STAGE_DIRS]
    return {
        "run_dir": str(run_dir),
        "keep": keep,
        "prune": prune,
        "missing_known_entries": [name for name in RUN_STAGE_DIRS if name not in entry_set],
        "unknown_entries": unknown,
    }
