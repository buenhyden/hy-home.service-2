# Contributing to Init-Project-Template

Thank you for your interest in contributing to the **Init-Project-Template**! This project is designed to be an AI-optimized foundation for modern software development.

## 🤝 Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. We expect all contributors to treat others with respect and facilitate a collaborative, inclusive environment.

## 🚀 Development Workflow

This project acts as a "Golden Master" template. Contributions should generally focus on improving the **governance pillars**, **agent rules**, or **infrastructure scripts**.

### 1. Planning & Design

All significant changes must start with a plan.

* **Feature Request**: Open an issue using the [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md).
* **RFC / Spec**: For complex changes, create a new specification in `specs/` using `templates/spec-template.md`.

### 2. The 4 Pillars of Governance

Your code must adhere to the four technical pillars:

* **Standards (0100)**: Clean code, documentation, and architectural integrity.
* **Workflows (0200)**: Git branching, commit messages, and PR flows.
* **Security (0500)**: "Secure by Default" philosophy.
* **Stack (1000)**: Strict typing and approved libraries.

### 3. Agent-Optimized Rules

If you are adding or modifying a Rule (`.agent/rules/`):

* **Skeleton**: MUST follow the 8-section AI-parseable skeleton.
* **ID**: MUST be assigned a unique `[REQ-XXX-NN]` identifier.

## 🌿 Branching Strategy

We follow a simplified GitFlow:

* `main`: Production-ready code.
* `feature/[description]`: New features or rules.
* `fix/[issue]`: Bug fixes.
* `hotfix/[issue]`: Critical production fixes.

## 📦 Commit Messages

We use **Conventional Commits**. Examples:

* `feat: add new security rule for CORS`
* `fix: update bootstrap script for Windows`
* `docs: reorganize docs folder structure`

## 📝 Pull Requests

1. **Template**: Fill out the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) completely.
2. **Linting**: Ensure all lint checks pass (`npm run lint` / `make lint`).
3. **Tests**: Ensure all tests pass (`npm test` / `make test`).
4. **Traceability**: Link to the relevant Issue or Requirement ID.

## 🐛 Reporting Bugs

Please use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md) to report issues. Provide as much context as possible (logs, screenshots, steps to reproduce).
