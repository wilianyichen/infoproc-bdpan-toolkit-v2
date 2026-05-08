# bdpan-ops

Release-oriented scaffold for the Baidu Netdisk side of the v2 system.

## Scope

`bdpan-ops` owns remote metadata and verification formats:

- remote input pointers
- remote input index entries
- upload verification summaries
- CLI templates that other wrappers can emit or validate

## Why this package exists

The current `baidupan-tools` installation already has operational commands. This package defines the stable data contracts around those commands so the remote-first workflow can be audited without depending on local shell history.

## Initial module surface

- `bdpan_ops.models`
  pointer and verification models
- `bdpan_ops.cli`
  JSON template emitter for pointer and upload metadata

## Example commands

```bash
python -m bdpan_ops pointer-template --local-dir-name kaizhi_audio --remote-path /开智/录屏整理/音频
python -m bdpan_ops upload-verification-template --remote-root /开智/视频文本蒸馏/蒸馏/录播
```

## Non-goals for this scaffold

- bypy authentication
- direct upload/download execution
- remote filesystem diffing

The operational engine stays in the existing Baidupan tooling. This package gives v2 a stable contract layer for release and integration.
