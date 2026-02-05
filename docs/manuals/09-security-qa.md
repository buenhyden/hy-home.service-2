# Security & Quality Assurance

Security and Quality are not afterthoughts; they are embedded in the
**Governance Pillars** of this project.

## ✅ Quality / Testing / Security Checklist (Where it is defined)

This template defines quality/test/security decisions across:

- **Spec (feature-level)**: `templates/spec-template.md` (Verification plan + checklists)
- **Local baseline checks**: `.pre-commit-config.yaml`
- **Governance rules**:
  `.agent/rules/0700-Testing_and_QA/0700-testing-and-qa-standard.md`,
  `.agent/rules/2200-Security/2200-security-pillar.md`
- **CI gates (stack-specific)**: `.github/workflows/ci.yml`
  (uncomment the job for your stack and add coverage gates)

| Item | Must | Primary source |
| --- | --- | --- |
| Test strategy (Unit/Integration/E2E/Load) | Yes | [`0700-testing-and-qa-standard.md`][qa-std] + Spec Section 7 |
| Test tooling (framework/runner/mocks/fixtures) | Yes | Spec Section 7 + stack rules |
| Coverage policy (numbers) | Yes | This doc + QA standard |
| Coverage gate (fail CI/PR) | Yes | CI config + QA standard |
| Lint/format baseline | Yes | `.pre-commit-config.yaml` |
| Complexity threshold | Optional | `.pre-commit-config.yaml` (complexity hook) |
| Security baseline (secrets/deps/SAST) | Yes | This doc + `.pre-commit-config.yaml` + security pillar |
| AuthN/AuthZ design | Yes | security pillar + Spec + ADRs |
| Data protection | Yes | security pillar + Spec (Ops/Data Protection) |
| Security review process | Optional | This doc + PR checklist |

## 🧩 Pre-Implementation QA Definition (Required)

Before implementation starts, the feature Spec MUST define QA methods and requirements:

- **Test levels**: Unit + Integration are required; E2E and Load/Performance are required when risk/impact warrants them.
- **Tooling**: test runner/framework, mocks/fixtures strategy, and how tests run locally and in CI.
- **Coverage targets & gates**: numeric targets and whether CI fails on regression.
- **Verification scope**: what is in-scope/out-of-scope for this release and what will be validated later.

Risk-based rule:
- If E2E or Load/Performance testing is not applicable, document it in the Spec Verification Plan as `N/A (reason: ...)`.

Primary reference for feature-level QA definition:
- `templates/spec-template.md` Section 0 (Quality/Testing/Security checklist) + Section 7 (Verification Plan)

## 🛡️ Security Governance (Pillar 0500)

We follow a "Secure by Default" philosophy.

### Key Protocols

- **Vulnerability Management**: Automated scanning for dependencies.
- **Secret Management**: strict prohibition of hardcoded secrets (use `.env`).
- **Auditing**: Integration with tools like TruffleHog.
- **SAST (Optional)**: Static Application Security Testing can be added to your
  CI workflow (for example Semgrep) based on your project risk profile.
- **AuthN/AuthZ & Data Protection**: Authentication, authorization, and sensitive
  data handling are governed by the Security Pillar and must be specified in
  feature Specs.

**Reference**: [2200-security-pillar.md](../../.agent/rules/2200-Security/2200-security-pillar.md)

## 🧪 Quality Assurance (Pillar 0700)

We promote a "Test-First" philosophy supported by automated CI workflows.

### Testing Strategy

1. **Unit Tests**: Test individual components in isolation.
2. **Integration Tests**: Verify interactions between components.
3. **E2E Tests**: Validate full user journeys.
4. **Load & Performance Tests**: Validate system stability and response times
   under high-concurrency scenarios (e.g., using K6 or Locust).

### Standards

- **Coverage Gate**:
  - **Total Coverage**: Minimum 80% project-wide. CI MUST fail if this
    threshold is not met.
  - **New Logic**: 100% coverage for all new or modified logical branches.
- **Automation**: All tests must run in CI before merging.
- **Linting**: ESLint and Prettier enforce code style consistency.

## 🔧 Local Baseline Checks (Pre-commit)

This repository includes pre-commit hooks for common quality/security baselines
(secrets detection, linting/formatting, security scanners, complexity checks).
See `.pre-commit-config.yaml`.

## 🛡️ Security Scans & Reviews

Periodic scans and manual reviews ensure defense-in-depth:

1. **SAST (Optional)**: Static analysis (for example Semgrep) for new/changed code.
2. **DAST (Optional)**: Dynamic analysis on staging environments where applicable.
3. **Secrets**: Automated leakage detection via TruffleHog.
4. **Review**: High-risk features require a dedicated security review before merge.

[qa-std]: ../../.agent/rules/0700-Testing_and_QA/0700-testing-and-qa-standard.md
