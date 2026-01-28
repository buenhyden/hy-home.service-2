# Development Guide

This guide outlines the standard development lifecycle (SDLC), workflows, and best practices for contributing to the project.

## 🔄 Development Workflow

### 1. Project Initialization

When starting a new feature, you must follow the Project Init Workflow.

* **Action**: Create a Plan. All features start with a plan.

### 2. Creating Requirements (PRD)

1. Copy `templates/prd-template.md` to `docs/prd/[feature]-prd.md`.
2. Define success metrics using `[REQ-PRD-MET-NN]`.

### 3. Implementation

1. **Spec**: Create a Technical Specification using `templates/spec-template.md`.
2. **Map**: Map implementation requirements to the PRD using coded IDs.
3. **Code**: Write code that follows the [0100] Standards.

## 🌿 Branching Strategy

* **Main Branch**: `main` (Production-ready code).
* **Feature Branches**: `feature/[feature-name]`.
* **Fix Branches**: `fix/[issue-description]`.

## 📦 Commits & PRs

* **Commits**: Use Conventional Commits (e.g., `feat: login page`, `fix: header alignment`).
* **Pull Requests**:
  * Must reference the related Issue or PRD.
  * Must pass CI checks.
  * Must generally pass the [Code Review Standard](../../.agent/rules/0000-Agents/0012-code-review-standard.md).

## ✅ Definition of Done (DoD)

Before merging any code, verify:

1. **Skeleton Compliance**: All rules follow the 8-section skeleton.
2. **Traceability**: 100% of functional logic maps back to a requirement ID.
3. **Tests**: 100% coverage for new logic.

