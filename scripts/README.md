# Scripts

These scripts are mono-repo scaffolds for the v2 release direction.

## Why scripts exist next to packages

The packages define stable data contracts and policy. The scripts show how operators are expected to use those contracts in a repository checkout before formal packaging is finished.

## Included scripts

- `infoproc_remote_first.sh`
  release-facing wrapper skeleton for the end-to-end remote-first flow
- `generate_remote_pointer.py`
  write a `REMOTE_POINTER.json` file after cleanup
- `prune_run_cache.py`
  dry-run or execute run cache pruning for `00_source` and `02_normalized`
- `summarize_run_audit.py`
  emit a compact audit summary from a run directory

## Contract

- Scripts should stay dependency-light.
- Scripts should emit machine-readable JSON where possible.
- Destructive actions should default to dry-run and require `--execute`.
