# Quality / Testing / Security Checklist (Spec-Driven)

This template operationalizes quality, testing, and security decisions through:

- **Project-level guidance**: [`docs/manuals/09-security-qa.md`](../manuals/09-security-qa.md),
  [`.agent/rules/0700-Testing_and_QA/`](../../.agent/rules/0700-Testing_and_QA/),
  [`.agent/rules/2200-Security/`](../../.agent/rules/2200-Security/)
- **Feature-level decisions**: Specs in `specs/` using
  [`templates/spec-template.md`](../../templates/spec-template.md)
- **Local baseline checks**: [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml)
- **PR review gates**: [`.github/PULL_REQUEST_TEMPLATE.md`](../../.github/PULL_REQUEST_TEMPLATE.md)

## Checklist Items → Where to Define

| Item | Required | Where to define / enforce |
| --- | --- | --- |
| Test Strategy (Unit/Integration/E2E/Load) | Must | [`templates/spec-template.md`][spec-template] Section 7 + [`docs/manuals/09-security-qa.md`][security-qa] |
| Test Tooling (framework/mock/fixtures) | Must | Spec Section 7 + rules under `.agent/rules/` |
| Coverage Policy (numbers) | Must | [`docs/manuals/09-security-qa.md`][security-qa] + Spec Section 7 |
| Coverage Gate (fail CI/PR) | Must | CI workflow + [`docs/manuals/09-security-qa.md`][security-qa] |
| Lint/Format baseline | Must | [`.pre-commit-config.yaml`][pre-commit] + style config |
| Style guide (naming/structure/modules) | Optional | Standards in `.agent/rules/` |
| Complexity policy | Optional | [`.pre-commit-config.yaml`][pre-commit] (complexity hook) |
| Security baseline (secrets/deps/SAST) | Must | [`.pre-commit-config.yaml`][pre-commit] + [`docs/manuals/09-security-qa.md`][security-qa] |
| AuthN/AuthZ design | Must | Spec (Interface/Decision log) + safety pillar + ADRs |
| Data protection (encrypt/mask/access) | Must | Spec Section 9 + security pillar + ADRs |
| Security review process | Optional | [`docs/manuals/09-security-qa.md`][security-qa] + PR checklist |

## Practical Workflow

1. Confirm baseline rules: [`docs/manuals/09-security-qa.md`](../manuals/09-security-qa.md)
2. In the Spec, complete:
   - Section 0 Quality/Testing/Security checklist
   - Section 7 Verification plan (tests + coverage targets)
   - Section 8 ADR links (if major decision)
   - Section 9 Ops/Observability + data protection
3. Ensure CI is configured for your stack (uncomment appropriate job in `.github/workflows/ci.yml`)

## PR / CI Gates

This template can enforce QA expectations at PR time:

- **Spec strict validation**: changed Specs must pass `scripts/validate_spec.py --strict` (no placeholders; PRD reference exists and PRD Status includes Approved).
- **Test-change gate (heuristic)**: if `src/**` changes but no test files change, CI fails to prevent untested logic changes.

Exception policy:
- Apply the PR label `skip-tests-gate` only when you have a clear justification (document it in the PR description and in the Spec Verification Plan).

[spec-template]: ../../templates/spec-template.md
[security-qa]: ../manuals/09-security-qa.md
[pre-commit]: ../../.pre-commit-config.yaml
