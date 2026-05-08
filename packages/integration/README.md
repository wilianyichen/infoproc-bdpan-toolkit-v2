# infoproc-bdpan-integration

Release-oriented scaffold for the remote-first integration layer.

## Scope

This package connects the other two packages into one operator workflow:

- fixed remote result roots
- remote-first job spec
- empty transcript handling policy
- audit-oriented job summaries

## Why this package exists

The v2 system is not just a processor and not just a remote sync tool. It is a controlled workflow:

1. materialize a remote source locally
2. process it
3. verify outputs
4. upload to fixed roots
5. classify exceptions
6. prune local cache

That workflow needs its own package so release users can depend on stable policy without pulling in the full installed local environment.

## Initial module surface

- `infoproc_bdpan_integration.policy`
  fixed roots and exception policy
- `infoproc_bdpan_integration.workflow`
  job spec builders and audit summaries
- `infoproc_bdpan_integration.cli`
  JSON-emitting helper CLI

## Example commands

```bash
python -m infoproc_bdpan_integration remote-roots
python -m infoproc_bdpan_integration job-template --remote-input-path /开智/录屏整理/音频 --run-name kaizhi-audio-20260508
```

## Non-goals for this scaffold

- managing the installed `infoproc` environment directly
- performing real uploads inside the package
- replacing the existing Baidupan operational tooling
