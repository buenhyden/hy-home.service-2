# Security & Quality Assurance

Security and Quality are not afterthoughts; they are embedded in the **Governance Pillars** of this project.

## 🛡️ Security Governance (Pillar 0500)

We follow a "Secure by Default" philosophy.

### Key Protocols

* **Vulnerability Management**: Automated scanning for dependencies.
* **Secret Management**: strict prohibition of hardcoded secrets (use `.env`).
* **Auditing**: Integration with tools like TruffleHog.
* **SAST**: Static Application Security Testing is integrated into the workflow.

**Reference**: [2200-security-pillar.md](../../.agent/rules/2200-Security/2200-security-pillar.md)

## 🧪 Quality Assurance (Pillar 0700)

We promote a "Test-First" philosophy supported by automated CI workflows.

### Testing Strategy

1. **Unit Tests**: Test individual components in isolation.
2. **Integration Tests**: Verify interactions between components.
3. **E2E Tests**: Validate full user journeys.

### Standards

* **Coverage**: New logic requires 100% test coverage.
* **Automation**: All tests must run in CI before merging.
* **Linting**: ESLint and Prettier enforce code style consistency.

## 🔍 Audits

Periodic audits are performed to ensure compliance with all governance rules.

* **Deep Rule Audit**: A script (`deep_rule_audit.py`) is used to verify that code maps back to standard requirements.
