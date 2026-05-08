"""Structured metadata models for remote storage state."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass(slots=True)
class RemotePointer:
    schema_version: str
    generated_at: str
    local_dir_name: str
    remote_path: str
    source_kind: str = "baidupan-remote"
    local_materialization: str = "ephemeral"
    cleanup_status: str = "pointer-only"
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(slots=True)
class RemoteInputIndexEntry:
    generated_at: str
    local_dir_name: str
    remote_path: str
    source_kind: str = "baidupan-remote"
    files_before_cleanup: int | None = None
    removed_entries: int | None = None

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(slots=True)
class UploadVerification:
    generated_at: str
    local_output_root: str
    remote_output_root: str
    matched_files: int
    left_only_files: int
    right_only_files: int
    ignored_targets: list[str] = field(default_factory=list)
    status: str = "pending-review"

    def to_dict(self) -> dict[str, object]:
        return asdict(self)
