# Infoproc x Baidupan Toolkit v2

Remote-first media processing and Baidu Netdisk operations for knowledge workflows.

This repository is the release-oriented v2 scaffold for a combined system:

- `infoproc` as the processing engine
- `baidupan-tools` as the remote storage and reconciliation layer

## Status

Version `0.1.0` is a docs-first open-source scaffold.

What exists now:

- repository metadata for public releases
- operator documentation for the remote-first workflow
- examples and specs for audit and storage contracts

What is still in progress:

- a stable public CLI surface for every workflow step
- polished packaging and release automation across all packages

## Scope

This project defines one operational system:

1. materialize selected remote media locally
2. process it with `infoproc`
3. upload results back to fixed remote roots
4. keep audit residues
5. prune bulky local caches

The design goal is simple:

- remote storage is durable
- local storage is execution cache
- every run is auditable
- cleanup is explicit and safe

## Start Here

- Product overview: [docs/overview.md](docs/overview.md)
- End-to-end workflow: [docs/workflow.md](docs/workflow.md)
- Environment model: [docs/environment.md](docs/environment.md)
- Directory model: [docs/directories.md](docs/directories.md)
- Command surface: [docs/commands.md](docs/commands.md)
- Audit and retention: [docs/audit-and-retention.md](docs/audit-and-retention.md)
- Release direction: [docs/release-plan.md](docs/release-plan.md)

## Repository Layout

```text
oss-v2/
├── README.md
├── LICENSE
├── VERSION
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
├── pyproject.toml
├── Makefile
├── docs/
├── examples/
├── packages/
├── scripts/
└── specs/
```

## Planned Code Layout

The intended v2 mono-repo shape is:

```text
packages/
├── infoproc-core/
├── bdpan-ops/
└── integration/
```

The package directories now exist, but the root release surface is still centered on metadata, docs, examples, and specs while the package implementations stabilize.

## Release Principles

- Do not hardcode personal absolute paths in public docs.
- Keep storage policy and audit policy explicit.
- Treat upload verification as part of the workflow, not an optional follow-up.
- Keep bulky source and normalized caches disposable.

## Quick Check

```bash
make check
make version
```
