<img src="assets/readme-cover.svg" alt="API Fixture Check cover" width="100%" />

# API Fixture Check

Audit API test fixtures for realism, identifiers, and brittle values.

![stack](https://img.shields.io/badge/stack-Python-dc2626?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-7c3aed?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-0891b2?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-b45309?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `api-fixture-check` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `placeholder-identity` | high | placeholder identity detected |
| `happy-path-only` | medium | fixture set lacks negative cases |
| `brittle-timestamp` | low | timestamp fixture may be brittle |

## Command line

```bash
python -m pip install -e ".[dev]"
api-fixture-check examples/sample.txt
api-fixture-check examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
examples/sample.txt
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
