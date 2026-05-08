# Contributing

## Scope

This repository already contains root docs plus early package skeletons. Keep root metadata, `docs/`, `examples/`, `specs/`, and cross-package release rules coherent.

## Principles

- keep storage remote-first
- preserve auditability
- avoid adding large local retention by default
- prefer explicit policies over ad hoc operator behavior

## Repository expectations

- update docs when changing workflow
- update examples when changing metadata formats
- keep package boundaries clear: `infoproc-core`, `bdpan-ops`, `integration`
- update `CHANGELOG.md` for release-facing root changes
- run `make check` before handing off root-scaffold edits

## Before proposing changes

Read:

- [docs/workflow.md](docs/workflow.md)
- [docs/audit-and-retention.md](docs/audit-and-retention.md)
- [specs/remote-storage-model.md](specs/remote-storage-model.md)
