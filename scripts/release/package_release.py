#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tarfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


REPO_FILES = [
    ".gitignore",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "Makefile",
    "README.md",
    "VERSION",
    "pyproject.toml",
]

REPO_DIRS = [
    "docs",
    "examples",
    "packages",
    "scripts",
    "specs",
]

IGNORE_NAMES = {
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "htmlcov",
    "logs",
    "tmp",
}

IGNORE_SUFFIXES = (".egg-info", ".pyc")


@dataclass(frozen=True)
class ArchiveRecord:
    format: str
    path: str
    sha256: str
    size_bytes: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a distributable oss-v2 release bundle."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Path to the oss-v2 repository root.",
    )
    parser.add_argument(
        "--name",
        default="infoproc-bdpan-toolkit-v2",
        help="Release package name.",
    )
    parser.add_argument(
        "--version",
        default=None,
        help="Override the version read from VERSION.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help="Output root. Defaults to <repo>/dist/release.",
    )
    parser.add_argument(
        "--formats",
        nargs="+",
        choices=("zip", "tar.gz"),
        default=("zip", "tar.gz"),
        help="Archives to emit.",
    )
    parser.add_argument(
        "--keep-existing",
        action="store_true",
        help="Keep an existing bundle root instead of replacing it.",
    )
    return parser.parse_args()


def read_version(repo_root: Path, override: str | None) -> str:
    if override:
        return override
    return (repo_root / "VERSION").read_text(encoding="utf-8").strip()


def git_commit(repo_root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def should_ignore(path: Path) -> bool:
    if path.name in IGNORE_NAMES:
        return True
    return any(path.name.endswith(suffix) for suffix in IGNORE_SUFFIXES)


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_tree(source: Path, destination: Path) -> None:
    for path in sorted(source.rglob("*")):
        rel = path.relative_to(source)
        if any(part in IGNORE_NAMES for part in rel.parts):
            continue
        if should_ignore(path):
            continue
        target = destination / rel
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            copy_file(path, target)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def included_paths(payload_root: Path) -> list[str]:
    paths: list[str] = []
    for path in sorted(payload_root.rglob("*")):
        if path.is_dir():
            continue
        paths.append(path.relative_to(payload_root).as_posix())
    return paths


def build_zip(payload_root: Path, archive_path: Path) -> ArchiveRecord:
    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(payload_root.rglob("*")):
            if path.is_dir():
                continue
            archive.write(path, arcname=path.relative_to(payload_root.parent))
    return ArchiveRecord(
        format="zip",
        path=archive_path.as_posix(),
        sha256=sha256_file(archive_path),
        size_bytes=archive_path.stat().st_size,
    )


def build_tar_gz(payload_root: Path, archive_path: Path) -> ArchiveRecord:
    with tarfile.open(archive_path, "w:gz") as archive:
        archive.add(payload_root, arcname=payload_root.name)
    return ArchiveRecord(
        format="tar.gz",
        path=archive_path.as_posix(),
        sha256=sha256_file(archive_path),
        size_bytes=archive_path.stat().st_size,
    )


def write_checksums(path: Path, archives: list[ArchiveRecord]) -> None:
    content = "\n".join(f"{item.sha256}  {Path(item.path).name}" for item in archives)
    path.write_text(content + "\n", encoding="utf-8")


def write_manifest(
    path: Path,
    *,
    package_name: str,
    version: str,
    bundle_root: Path,
    payload_root: Path,
    commit: str | None,
    archives: list[ArchiveRecord],
) -> None:
    manifest = {
        "schema_version": 1,
        "package_name": package_name,
        "version": version,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "git_commit": commit,
        "bundle_root": bundle_root.as_posix(),
        "payload_root": payload_root.as_posix(),
        "archives": [asdict(item) for item in archives],
        "included_paths": included_paths(payload_root),
    }
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    if not (repo_root / "pyproject.toml").exists():
        raise SystemExit(f"Repository root not found: {repo_root}")

    version = read_version(repo_root, args.version)
    package_name = args.name
    output_root = (
        args.output_root.resolve()
        if args.output_root is not None
        else (repo_root / "dist" / "release").resolve()
    )
    bundle_name = f"{package_name}-{version}"
    bundle_root = output_root / bundle_name
    payload_root = bundle_root / "payload" / bundle_name
    archives_root = bundle_root / "archives"

    if bundle_root.exists() and not args.keep_existing:
        shutil.rmtree(bundle_root)

    payload_root.mkdir(parents=True, exist_ok=True)
    archives_root.mkdir(parents=True, exist_ok=True)

    for rel in REPO_FILES:
        source = repo_root / rel
        if source.exists():
            copy_file(source, payload_root / rel)

    for rel in REPO_DIRS:
        source = repo_root / rel
        if source.exists():
            copy_tree(source, payload_root / rel)

    archives: list[ArchiveRecord] = []
    for archive_format in args.formats:
        if archive_format == "zip":
            archives.append(build_zip(payload_root, archives_root / f"{bundle_name}.zip"))
        elif archive_format == "tar.gz":
            archives.append(
                build_tar_gz(payload_root, archives_root / f"{bundle_name}.tar.gz")
            )

    write_checksums(bundle_root / "SHA256SUMS", archives)
    manifest_path = bundle_root / "release_manifest.json"
    write_manifest(
        manifest_path,
        package_name=package_name,
        version=version,
        bundle_root=bundle_root,
        payload_root=payload_root,
        commit=git_commit(repo_root),
        archives=archives,
    )

    print(
        json.dumps(
            {
                "package_name": package_name,
                "version": version,
                "bundle_root": bundle_root.as_posix(),
                "payload_root": payload_root.as_posix(),
                "manifest": manifest_path.as_posix(),
                "archives": [asdict(item) for item in archives],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
