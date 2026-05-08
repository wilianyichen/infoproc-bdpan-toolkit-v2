"""Structured models for run retention and audit summaries."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass(slots=True)
class RunRetentionPlan:
    run_dir: str
    keep: list[str]
    prune: list[str]
    missing_known_entries: list[str] = field(default_factory=list)
    unknown_entries: list[str] = field(default_factory=list)
    rationale: str = (
        "Keep compact audit and text outputs; prune bulky source and normalized caches."
    )

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(slots=True)
class RunDirectorySummary:
    run_dir: str
    existing_entries: list[str]
    retained_entries: list[str]
    prunable_entries: list[str]
    audit_ready: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)
