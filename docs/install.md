# Install

## Purpose

Bring up a fresh checkout of `oss-v2` as an operator/developer workspace.

## Prerequisites

- Python `>= 3.11`
- `ffmpeg` on `PATH`
- shell access on Linux or a compatible environment
- Baidu Netdisk token material available outside Git

## Bootstrap

```bash
git clone <repo-url> infoproc-bdpan-toolkit-v2
cd infoproc-bdpan-toolkit-v2
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ./packages/infoproc-core
pip install -e ./packages/bdpan-ops
pip install -e ./packages/integration
```

## Verify

```bash
make check
make version
python -m infoproc_bdpan_integration workflow-summary
```

## Operator environment

Keep these outside the repository:

- Baidu Netdisk token files
- API keys
- machine-specific proxy settings
- machine-specific model cache paths
