# Release Checklist

## Before tagging

- update [VERSION](/mnt/disk2/wuxiaoran/infoproc/oss-v2/VERSION:1)
- update [CHANGELOG.md](/mnt/disk2/wuxiaoran/infoproc/oss-v2/CHANGELOG.md:1)
- run `make check`
- run package compile checks
- verify example JSON files still match the documented schemas

## Release-facing surfaces

- root README
- install and bootstrap docs
- workflow docs
- audit and retention docs
- package skeletons
- scripts

## After tagging

- publish release notes
- note unresolved placeholders for the next version
