"""CLI helpers for bdpan-ops."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone

from .models import RemoteInputIndexEntry, RemotePointer, UploadVerification


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="bdpan-ops")
    subparsers = parser.add_subparsers(dest="command", required=True)

    pointer = subparsers.add_parser("pointer-template", help="Emit a remote pointer JSON.")
    pointer.add_argument("--local-dir-name", required=True)
    pointer.add_argument("--remote-path", required=True)
    pointer.add_argument("--note", action="append", default=[])

    index_entry = subparsers.add_parser(
        "index-entry-template",
        help="Emit a remote input index entry JSON.",
    )
    index_entry.add_argument("--local-dir-name", required=True)
    index_entry.add_argument("--remote-path", required=True)
    index_entry.add_argument("--files-before-cleanup", type=int)
    index_entry.add_argument("--removed-entries", type=int)

    verification = subparsers.add_parser(
        "upload-verification-template",
        help="Emit an upload verification summary JSON.",
    )
    verification.add_argument("--local-output-root", required=True)
    verification.add_argument("--remote-output-root", required=True)
    verification.add_argument("--matched-files", type=int, default=0)
    verification.add_argument("--left-only-files", type=int, default=0)
    verification.add_argument("--right-only-files", type=int, default=0)
    verification.add_argument("--ignored-target", action="append", default=[])
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "pointer-template":
        payload = RemotePointer(
            schema_version="1",
            generated_at=utc_now(),
            local_dir_name=args.local_dir_name,
            remote_path=args.remote_path,
            notes=args.note,
        ).to_dict()
    elif args.command == "index-entry-template":
        payload = RemoteInputIndexEntry(
            generated_at=utc_now(),
            local_dir_name=args.local_dir_name,
            remote_path=args.remote_path,
            files_before_cleanup=args.files_before_cleanup,
            removed_entries=args.removed_entries,
        ).to_dict()
    else:
        payload = UploadVerification(
            generated_at=utc_now(),
            local_output_root=args.local_output_root,
            remote_output_root=args.remote_output_root,
            matched_files=args.matched_files,
            left_only_files=args.left_only_files,
            right_only_files=args.right_only_files,
            ignored_targets=args.ignored_target,
        ).to_dict()

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
