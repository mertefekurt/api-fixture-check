# API Fixture Check

Audit API test fixtures for realism, identifiers, and brittle values. The repository is intentionally plain: a small command, a visible rule surface, and enough examples to make the behavior inspectable.

<img src="assets/readme-cover.svg" alt="API Fixture Check cover" width="100%" />

## Review checklist

- [ ] placeholder identity detected (`placeholder-identity`, high)
- [ ] fixture set lacks negative cases (`happy-path-only`, medium)
- [ ] timestamp fixture may be brittle (`brittle-timestamp`, low)

## Command path

```bash
git clone https://github.com/mertefekurt/api-fixture-check.git
cd api-fixture-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
api-fixture-check examples/sample.txt
api-fixture-check examples/sample.txt --json
```

## Fixture worth keeping

```text

```

## Files I look at first

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
