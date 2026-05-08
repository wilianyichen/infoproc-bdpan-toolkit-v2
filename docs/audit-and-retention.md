# Audit And Retention

## Audit Objects

The minimum audit layer should preserve:

- run manifests
- run logs
- probe metadata
- raw transcript outputs
- clean text outputs
- final markdown outputs
- delivery trees when used
- exceptional file markers

## Empty Transcript Policy

A file should be marked `no_valid_text` when:

- transcript segments are empty
- raw text is empty
- clean text is empty

Optional context:

- very short duration
- language mis-detection

Artifacts:

- per-file marker JSON
- aggregated run report
- skip-upload relpath list

## Retention Policy

### Keep Long-Term

- `REMOTE_INPUT_INDEX.json`
- `REMOTE_POINTER.json`
- run `_manifests`
- run `_logs`
- run `03_text_raw`
- run `04_text_clean`
- run `05_final`
- run `_delivery`
- run `_flags`
- run `_reports`

### Delete After Verification

- local source mirrors
- normalized media caches
- temporary subset input trees

## Repository Rule

Retention policy is part of the public contract. Cleanup that breaks auditability is a product bug, not an operator preference.
