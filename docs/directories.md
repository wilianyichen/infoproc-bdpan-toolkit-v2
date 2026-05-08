# Directories

## Recommended Layout

```text
workspace/
├── input/
│   ├── REMOTE_INPUT_INDEX.json
│   └── <source-name>/
│       └── REMOTE_POINTER.json
├── runs/
│   └── <run-name>/
├── models/
└── hf_home/
```

## input

`input/` is remote-pointer-first.

Each logical source tree should eventually contain:

- `REMOTE_POINTER.json`
- optional operator notes

Shared registry:

- `REMOTE_INPUT_INDEX.json`

## runs

Each run directory may contain:

- `00_source`
- `01_probe`
- `02_normalized`
- `03_text_raw`
- `04_text_clean`
- `05_final`
- `_delivery`
- `_logs`
- `_manifests`
- `_flags`
- `_reports`

### Post-delivery retention

Keep:

- `01_probe`
- `03_text_raw`
- `04_text_clean`
- `05_final`
- `_delivery` if present
- `_logs`
- `_manifests`
- `_flags`
- `_reports`

Delete:

- `00_source`
- `02_normalized`

## models

Persistent local model cache for transcription and related runtimes.

## hf_home

Persistent local cache for diarization-related assets.
