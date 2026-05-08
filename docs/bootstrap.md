# Bootstrap

## Definition

Bootstrap means turning a repository checkout into a usable operator workspace.

## Minimal checklist

1. create a virtual environment
2. install the three local packages in editable mode
3. configure token and key files outside Git
4. run repository checks
5. verify the integration CLI prints a workflow summary

## Suggested first commands

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ./packages/infoproc-core
pip install -e ./packages/bdpan-ops
pip install -e ./packages/integration
make check
python -m infoproc_bdpan_integration workflow-summary
```
