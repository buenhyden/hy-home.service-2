# Development Guide

This guide outlines the standard development lifecycle (SDLC), workflows, and
best practices for contributing to the project. For team-specific operations and
communication, see the **[Collaboration Guide](./11-collaboration-guide.md)**.

## 🔄 Development Workflow

### 1. Project Initialization

When starting a new feature, you must follow the Project Init Workflow.

* **Action**: Create a Plan. All features start with a plan.

### 2. Creating Requirements (PRD)

1. Copy `templates/prd-template.md` to `docs/prd/[feature]-prd.md`.
2. **Business/Product Checklist**: Treat the PRD as the checklist source of truth
   (Vision, Metrics, Personas, Use Cases, Scope, Milestones, Risks, Compliance).
3. **Define Product Vision**: Ensure the core vision and business goals are
   clearly articulated.
4. **Core Scenarios**: Document at least 3-5 representative scenarios (Key Use Cases).
5. **Define Success Metrics**: Use `[REQ-PRD-MET-NN]` format.
6. **Timeline & Milestones**: Define the target dates for PoC, MVP, Beta, and v1.0.
7. **Governance**: Explicitly address compliance and security risks in Section 8.
8. **Approval Gate**: Do not start implementation until the PRD status is
   **Approved** and stakeholders have aligned.

### 3. Technical Design & Implementation

1. **Spec**: Create a Technical Specification using `templates/spec-template.md`.
2. **Decision History (ADR)**: If a new architectural choice is made, record it in `docs/adr/` (Pillar 3: Why).
3. **Implementation Patterns (ARD)**: Document the authoritative "How" in `docs/ard/` (Pillar 4: How) to maintain a living technical reference.
4. **Architecture Focus**: Ensure the spec explicitly defines:
   * **NFRs**: Performance, availability, and security metrics (Section 5).
   * **Storage Strategy**: Database choice and schema design (Section 3).
   * **Scalability**: Caching and infrastructure requirements (Section 6).
   * **Architecture/Stack Checklist**: Confirm architecture style/boundaries/stack
     decisions (Section 0).
5. **Map**: Map implementation requirements to the PRD using coded IDs.
6. **Code**: Write code that follows the [0100] Standards.

## 🟩 Definition of Ready (DoR)

Before starting implementation work (coding), verify:

1. **PRD Gate**: PRD exists in `docs/prd/` and Status includes **Approved**.
2. **Spec Gate**: `specs/<feature>/spec.md` exists and references the PRD.
3. **QA Definition (Spec)**:
   - Spec Section 0 **Quality / Testing / Security Checklist** is completed.
   - Spec Section 7 **Verification Plan** defines Unit/Integration tests and coverage targets.
   - E2E and Load/Performance tests are defined when risk/impact requires them, otherwise documented as `N/A (reason: ...)`.
4. **Strict Docs Validation**: `./scripts/validate-docs.ps1 -Strict` (Windows) or `./scripts/validate-docs.sh --strict` (Unix) passes.

## 🌿 Branching Strategy

* **Main Branch**: `main` (Production-ready code).
* **Feature Branches**: `feature/[issue-id]-[name]` (e.g., `feature/123-login-page`).
* **Fix Branches**: `fix/[issue-id]-[name]` (e.g., `fix/456-header-alignment`).
* **Hotfix Branches**: `hotfix/[issue-id]-[name]` (Critical production fixes).

## 📦 Commits & PRs

* **Commits**: Use Conventional Commits (e.g., `feat: login page`,
  `fix: header alignment`, `docs: update readme`).
* **Pull Requests**:
  * Must reference the related Issue or PRD.
  * Must pass CI checks.
  * Must generally pass the [Code Review Standard](../../.agent/rules/0000-Agents/0012-code-review-standard.md).

## ✅ Definition of Done (DoD)

Before merging any code, verify:

1. **Skeleton Compliance**: All rules follow the 8-section skeleton.
2. **Traceability**: 100% of functional logic maps back to a requirement ID.
3. **Standards**: Code follows [0100] Standards and architectural principles.
4. **Quality Gates**:
   * 100% coverage for new logic.
   * Total project coverage >= 80%.
5. **Security Review**: No hardcoded secrets and passing SAST scans.
6. **PRD/Spec Completeness**: PRD exists and is Approved, Spec references PRD,
   and docs validation passes (`./scripts/validate-docs.* --strict`).
