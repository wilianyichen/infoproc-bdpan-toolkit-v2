#!/usr/bin/env bash
set -euo pipefail

if [[ ! -f "VERSION" || ! -f "README.md" ]]; then
  echo "Run this from the oss-v2 repository root." >&2
  exit 1
fi

version="$(cat VERSION)"
dist_dir="dist"
tmp_dir="$(mktemp -d /tmp/oss-v2-release.XXXXXX)"
name="infoproc-bdpan-toolkit-v2-${version}"
stage_dir="${tmp_dir}/${name}"

mkdir -p "$stage_dir" "$dist_dir"

rsync -a \
  --exclude '.git' \
  --exclude '.venv' \
  --exclude 'dist' \
  --exclude '__pycache__' \
  ./ "$stage_dir"/

(
  cd "$tmp_dir"
  zip -qr "${name}.zip" "$name"
)

mv "${tmp_dir}/${name}.zip" "${dist_dir}/"
rm -rf "$tmp_dir"

echo "${dist_dir}/${name}.zip"
