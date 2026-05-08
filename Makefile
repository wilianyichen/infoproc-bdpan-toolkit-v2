.DEFAULT_GOAL := help

VERSION := $(shell cat VERSION)

.PHONY: help check version clean tree docs

help:
	@printf "Targets:\n"
	@printf "  make check    Validate the root release scaffold\n"
	@printf "  make version  Print the repository version\n"
	@printf "  make tree     Show a shallow repository tree\n"
	@printf "  make docs     Print the docs entrypoint\n"
	@printf "  make clean    Remove local build artifacts\n"

check:
	@test -f README.md
	@test -f LICENSE
	@test -f VERSION
	@test -f CHANGELOG.md
	@test -f CONTRIBUTING.md
	@test -f pyproject.toml
	@test -f docs/overview.md
	@test -f docs/workflow.md
	@test -f docs/environment.md
	@test -f docs/directories.md
	@test -f docs/commands.md
	@test -f docs/audit-and-retention.md
	@printf "release scaffold looks complete (%s)\n" "$(VERSION)"

version:
	@printf "%s\n" "$(VERSION)"

clean:
	@rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage

tree:
	find . -maxdepth 3 \( -type f -o -type d \) | sort

docs:
	@echo "Docs entrypoint: README.md"
