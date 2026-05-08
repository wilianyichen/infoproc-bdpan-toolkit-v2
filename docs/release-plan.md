# Release Plan

## Repository Shape

The v2 direction is a mono-repo with three implementation areas:

- `packages/infoproc-core`
- `packages/bdpan-ops`
- `packages/integration`

Those package directories now exist in early form. The root repository still defines the cross-package contract they should converge on.

## Release Order

1. stabilize root metadata and docs
2. migrate integration wrappers
3. migrate reusable Netdisk operations
4. migrate reusable processing wrappers
5. cut the first code-bearing public release

## First Public Tag Requirements

- coherent root repository metadata
- stable workflow docs
- stable storage and audit policy
- example data shapes for input pointers and exception markers
- a documented command surface, even if some commands are still wrappers in transition
