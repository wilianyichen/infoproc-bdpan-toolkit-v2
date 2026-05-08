# Commands

## Command Surface

The v2 workflow standardizes around three logical command groups:

- `infoproc`
- `infoproc-run`
- `bdpan`

## Representative Commands

Run local processing:

```bash
infoproc process --input <path> --recursive --profile quality --distill both --run-name <name>
```

Run background processing:

```bash
infoproc-run --background process --input <path> --recursive --profile quality --distill both --run-name <name>
```

List remote roots:

```bash
bdpan list /
bdpan tree /remote-root --depth 2
```

Download remote input:

```bash
bdpan download-tree /remote/input ./input/<source-name>
```

Upload results:

```bash
bdpan upload-tree ./runs/<run-name>/04_text_clean/clean_text__txt <remote-text-root>
bdpan upload-tree ./runs/<run-name>/05_final/distill__md <remote-final-root>/distill__md
bdpan upload-tree ./runs/<run-name>/05_final/rank__md <remote-final-root>/rank__md
```

Compare local versus remote:

```bash
bdpan reconcile compare-local ./local-dir /remote/dir --ignore-extension --json-output report.json
```

## Planned High-Level Wrapper

The intended operator entry point is:

```bash
infoproc-bdpan run-remote /remote/input --run-name <name>
```

That wrapper should orchestrate:

1. remote download
2. local processing
3. upload
4. upload verification
5. pointer conversion
6. cache pruning
