# Overview

## Two tools, one workflow

### infoproc

`infoproc` is the processing engine.

Core functions:

- audio/video transcription
- text cleanup
- markdown distillation
- markdown rank reduction
- run manifests and per-file stage tracking

### baidupan-tools

`baidupan-tools` is the remote storage and reconciliation layer.

Core functions:

- browse and search Netdisk
- upload and download trees
- compare local and remote structures
- generate safe operation manifests
- validate and apply filesystem plans

## Why they must be documented together

The real operator workflow is not:

- download something manually
- run a processor
- upload things manually

The real workflow is:

1. choose a remote source directory
2. materialize it locally only while needed
3. process with stage-aware manifests
4. upload to fixed remote output roots
5. prune local caches
6. preserve only compact audit traces

That means the processing engine and the remote storage toolkit form one operational system.

## Design goals

- Minimize local disk usage
- Preserve auditability
- Make reruns deterministic
- Make upload status easy to verify
- Make cleanup safe and rule-based
