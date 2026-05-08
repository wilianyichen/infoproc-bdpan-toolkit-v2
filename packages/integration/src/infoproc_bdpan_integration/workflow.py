"""Workflow models for the remote-first integration layer."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone

from .policy import FIXED_REMOTE_ROOTS, NO_VALID_TEXT_SKIP_TARGETS, RETENTION_POLICY


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass(slots=True)
class RemoteFirstJobSpec:
    generated_at: str
    remote_input_path: str
    local_input_dir_name: str
    run_name: str
    profile: str = "quality"
    distill_mode: str = "both"
    text_output_root: str = FIXED_REMOTE_ROOTS["text"]
    final_output_root: str = FIXED_REMOTE_ROOTS["final"]
    retention_policy: dict[str, list[str]] = field(
        default_factory=lambda: {
            "keep": list(RETENTION_POLICY["keep"]),
            "prune": list(RETENTION_POLICY["prune"]),
        }
    )
    exception_policy: dict[str, object] = field(
        default_factory=lambda: {
            "classification": "no_valid_text",
            "skip_upload_targets": list(NO_VALID_TEXT_SKIP_TARGETS),
        }
    )

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(slots=True)
class RunAuditSummary:
    generated_at: str
    run_name: str
    remote_input_path: str
    upload_completed: bool
    exceptional_files: int
    intentionally_deleted_artifacts: list[str]
    retained_artifacts: list[str]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def derive_local_input_dir_name(remote_input_path: str) -> str:
    stripped = remote_input_path.strip("/")
    if not stripped:
        return "root"
    return stripped.split("/")[-1].replace(" ", "_")


def build_job_spec(remote_input_path: str, run_name: str) -> RemoteFirstJobSpec:
    return RemoteFirstJobSpec(
        generated_at=utc_now(),
        remote_input_path=remote_input_path,
        local_input_dir_name=derive_local_input_dir_name(remote_input_path),
        run_name=run_name,
    )
