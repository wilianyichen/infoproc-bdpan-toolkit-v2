# infoproc-core

Release-oriented scaffold for the processing side of the v2 system.

## Scope

`infoproc-core` owns the local processing model:

- canonical run directory layout
- post-delivery retention policy
- compact run summaries for audit tooling
- CLI helpers that describe run structure without depending on the full installed bundle

## Why this package exists

The installed `infoproc` bundle already processes media. This package is the open-source-facing control surface that documents and standardizes:

- what a run should contain
- what can be deleted after delivery
- what must remain for audit

It is intentionally small. It should not re-implement the heavy transcription pipeline here.

## Initial module surface

- `infoproc_core.layout`
  run stage names and retention rules
- `infoproc_core.models`
  structured summaries and retention plans
- `infoproc_core.cli`
  JSON-emitting helper CLI

## Example commands

```bash
python -m infoproc_core describe-layout
python -m infoproc_core retention-plan /path/to/run
```

## Non-goals for this scaffold

- whisper or diarization runtime
- llm distillation runtime
- external API calls
- direct integration with the installed local bundle

## Release note

This scaffold is meant to become a stable metadata/control package in a mono-repo release where the heavy runtime stays separable from policy and audit tooling.
