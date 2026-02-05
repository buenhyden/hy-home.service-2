# Pull Request Template

## 📝 Pull Request Overview

**Related Issue/Requirement**:

- Issue: #
- Requirement: `[REQ-XXX-NN]`
- PRD (if feature work): `docs/prd/<feature>-prd.md`
- Spec (if feature work): `specs/<feature>/spec.md`

---

## 🔍 Change Description

A clear and concise description of what this PR introduces or fixes.

---

## 🛠️ Type of Change

Please mark the relevant option:

- [ ] ✨ New Feature
- [ ] 🐛 Bug Fix
- [ ] ⚡ Performance Improvement
- [ ] ♻️ Refactoring
- [ ] 📝 Documentation Update
- [ ] 🏗️ Infrastructure / DevOps
- [ ] 🧪 Test Case

---

## 📸 Screenshots / Recordings (if applicable)

*Add visual evidence of UI changes here.*

---

## ✅ Quality Checklist

- [ ] 🧪 **Tests**: Unit and integration tests pass locally.
- [ ] 📏 **Linting**: Code adheres to project styling standards (ESLint/Prettier).
- [ ] 📘 **Documentation**: Relevant `README.md` or `docs/` files have been updated.
- [ ] 🏗️ **Architecture**: Changes follow the defined
[System Architecture](../ARCHITECTURE.md) layering.
- [ ] 🛡️ **Security**: No sensitive data is exposed, and security standards are
  met.
- [ ] 📈 **Coverage**: Coverage targets are met (e.g., total >= 80%, new logic
  100%) and
CI enforces the gate.
- [ ] 🧾 **PRD Gate (Features)**: PRD status is **Approved** and
the Business/Product checklist is aligned.
- [ ] 🔗 **Traceability (Features)**: Spec references PRD, and
requirements map back to `REQ-PRD-*` IDs.
- [ ] 🏗️ **Architecture/Stack (Features)**: `templates/spec-template.md`
Section 0 checklist is completed and ADRs
are linked where applicable.
- [ ] 🧪🛡️ **Quality/Security (Features)**: `templates/spec-template.md`
  Section 0 checklist is completed (test strategy/tooling/coverage/security
  baseline/AuthN/AuthZ/data protection).
- [ ] ⚙️ **Ops/Deploy/Monitoring (Features)**: `templates/spec-template.md`
  Section 0 checklist is completed and Section 9 declares
  logs/metrics/alerts/backup/RPO-RTO as applicable.
- [ ] ✅ **Docs Validation (Recommended)**: `./scripts/validate-docs.ps1
  -Strict` (Windows) or `./scripts/validate-docs.sh --strict` (Unix).

---

## 💬 Additional Notes

Any extra context or warnings for the reviewer.
