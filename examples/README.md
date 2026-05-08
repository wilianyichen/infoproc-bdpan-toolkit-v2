# Examples

Concrete example payloads for the v2 mono-repo direction.

## What is here

- root examples
  legacy examples already referenced by the docs
- `jobs/`
  remote-first job specs and remote root maps
- `pointers/`
  durable remote pointer metadata
- `audit/`
  upload verification, run audit, and exception metadata

## How to use them

- Treat these files as shape references, not production secrets.
- Keep field names stable once external operators start depending on them.
- Prefer adding fields over renaming fields.
