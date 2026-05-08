# release

Release and repository bootstrap helpers.

Current helpers:

- `bootstrap_repo.sh`
  create a local virtual environment and install the editable packages
- `build_release_bundle.sh`
  shell entrypoint for generating a distributable bundle
- `package_release.py`
  packaging implementation that emits archives and a manifest

## Build a release bundle

From the repository root:

```bash
make package
```

Equivalent direct command:

```bash
bash scripts/release/build_release_bundle.sh
```

## Output convention

Every packaging run creates:

```text
dist/release/<package-name>-<version>/
```

That bundle root contains:

- `payload/<package-name>-<version>/`
  unpacked release tree for inspection
- `archives/<package-name>-<version>.zip`
  primary GitHub release asset
- `archives/<package-name>-<version>.tar.gz`
  secondary Unix-style release asset
- `release_manifest.json`
  machine-readable release metadata
- `SHA256SUMS`
  checksums for the generated archives
