# Sensitive Data Handling (PII / Secrets / Logs)

This manual defines the baseline rules for handling **sensitive data** in this
repository: what counts as sensitive, where it may appear, and how it must be
protected across code, logs, and operations.

## 1. Scope

Applies to:

- Source code and configuration (`src/`, `scripts/`, CI, IaC)
- Documentation examples (`docs/`, `README.md`)
- Telemetry (logs/metrics/traces), backups, and data exports

## 2. Definitions

- **PII** (Personally Identifiable Information): data that can identify a
  person (email, phone, address, government IDs, etc.).
- **Secrets**: credentials and cryptographic material (API keys, passwords,
  tokens, private keys, signing keys, DB credentials).
- **Sensitive business data**: customer data, financial data, access logs, or
  any data subject to contractual or regulatory constraints.

## 3. Data Minimization (Default)

- Collect only what is necessary for the feature.
- Store the minimum required fields.
- Avoid copying sensitive data into secondary systems (analytics, logs, cache)
  unless explicitly justified in the Spec.

## 4. Storage & Transport Protection

### Encryption at rest

- Datastores containing PII must use encryption at rest.
- If you introduce new sensitive fields, declare them in the Spec (data model +
  operations section) and document the encryption approach.

### Encryption in transit

- All external traffic must use TLS.
- Internal service-to-service traffic should use TLS where supported by the
  deployment model.

## 5. Secrets Management

- **Never commit secrets** to git.
- Use environment variables or a secret manager for runtime secrets.
- Keep `.env.example` as the documented list of required variables (no secret
  values).

## 6. Logging / Metrics / Tracing (No PII by Default)

- Do not log raw PII or secrets.
- Use **stable identifiers** (e.g., `user_id`) instead of email/phone.
- If logging is necessary for debugging, log **redacted** values only.
- Telemetry must include correlation/trace identifiers, but must not include
  sensitive payloads.

## 7. Access Control & Least Privilege

- Restrict access to sensitive resources and admin endpoints.
- Validate object ownership (prevent IDOR) on all resource reads/writes.
- Separate authorization checks from business logic where possible.

## 8. Backups, Retention, and Deletion

- Ensure backups include encryption and controlled access.
- Define retention requirements and deletion behavior when introducing new
  sensitive data.
- If the feature introduces regulated data, document RPO/RTO and retention
  constraints in `OPERATIONS.md` and the feature Spec.

## 9. Checklist (Feature Work)

Before merging a feature that touches sensitive data:

- [ ] Spec documents AuthN/AuthZ and data protection requirements.
- [ ] No secrets committed; configuration uses env/secret manager.
- [ ] Logs/telemetry avoid PII; redaction is implemented where needed.
- [ ] DB queries are parameterized; access checks prevent IDOR.
- [ ] Backup/retention considerations are documented (if applicable).

## References

- Security Pillar: `../../.agent/rules/2200-Security/2200-security-pillar.md`
- Observability Pillar: `../../.agent/rules/2600-Observability/2600-observability-pillar.md`
- Security & QA manual: `./09-security-qa.md`
- Operations blueprint: `../../OPERATIONS.md`
- Env var baseline: `../../.env.example`

