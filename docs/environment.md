# Environment

## Required Tools

- Python `3.11+`
- `ffmpeg`
- `ffprobe`
- an `infoproc` runtime
- a Baidu Netdisk client/runtime compatible with the documented workflow

## Required Configuration

### infoproc

- `INFOPROC_CONFIG`
- `INFOPROC_API_KEY`
- `HF_TOKEN` when diarization is enabled
- proxy variables when the deployment requires them

### baidupan

- authenticated bypy-compatible token material
- `BYPY_TOKEN_FILE` as an optional explicit token override

## Recommended Local Workspace Roots

These are logical roots, not fixed absolute paths:

- `./input`
- `./runs`
- `./models`
- `./hf_home`

## Public Documentation Rule

Public docs should describe logical paths and environment variables. Personal absolute paths belong only in local deployment notes, not in release-facing repository docs.
