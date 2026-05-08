# Workflow

## Standard remote-first workflow

1. Identify the remote input directory on Baidu Netdisk.
2. Download it into a temporary local input tree.
3. Run `infoproc process`.
4. Verify the run completed successfully.
5. Upload clean text results to the remote text tree.
6. Upload distill and rank results to the remote final trees.
7. Flag any `no_valid_text` exceptions.
8. Convert the local input tree into a remote pointer.
9. Prune bulky `00_source` and `02_normalized` caches from the run.
10. Keep only compact audit residues.

## Command Layers

Low-level command groups:

- `infoproc`
- `infoproc-run`
- `bdpan`

Planned high-level entry point:

- `infoproc-bdpan run-remote`

That command should encapsulate:

1. remote download
2. local processing
3. upload verification
4. input pointer conversion
5. post-success pruning

## Remote Result Roots

Deployments should define fixed remote output roots for:

- clean text
- distill markdown
- rank markdown

The exact remote paths are deployment policy, not repository policy. They should be recorded in operator docs and input indexes.

## Exception workflow

If a file produces:

- empty transcript segments
- empty raw text
- empty clean text

then:

1. classify it as `no_valid_text`
2. exclude it from upload
3. preserve the exception in the audit layer

Reference:

- [../specs/empty-transcript-policy.md](../specs/empty-transcript-policy.md)
