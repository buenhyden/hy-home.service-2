# Contributing to Init-Project-Template

Thank you for your interest in contributing to the **Init-Project-Template**!
This project is designed to be an AI-optimized foundation for modern software
development.

## 🤝 Code of Conduct

By participating in this project, you agree to abide by our
[Code of Conduct](CODE_OF_CONDUCT.md).
We expect all contributors to treat others with respect and facilitate a
collaborative, inclusive environment.

## 🚀 Development Workflow

This project acts as a "Golden Master" template. Contributions should generally
focus on improving the **governance pillars**, **agent rules**, or
**infrastructure scripts**.

### 1. Planning & Design

All significant changes must start with a plan.

* **Feature Request**: Open an issue using the [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md).
* **RFC / Spec**: For complex changes, create a new specification in `specs/`
  using `templates/spec-template.md`.

### 2. The 5 Pillars of Governance

Your code must adhere to the five technical pillars:

* **Standards (0100)**: Clean code, documentation, and architectural integrity.
* **Workflows (0200)**: Git branching, commit messages, and PR flows.
* **Security & QA (0700/2200)**: "Secure by Default" philosophy and test governance.
* **Tech Stack (0150/1000)**: Strict typing and approved libraries.
* **Operations & Monitoring (2600)**: Reliability, observability, and release readiness.

### 3. Agent-Optimized Rules

If you are adding or modifying a Rule (`.agent/rules/`):

* **Skeleton**: MUST follow the 8-section AI-parseable skeleton.
* **ID**: MUST be assigned a unique `[REQ-XXX-NN]` identifier.

## 🌿 Development Standards & Workflows

To ensure consistency and high engineering excellence, we follow a strict set of
standards for branching, commits, and quality gates.

👉 **[Authorized Development Guide](docs/manuals/06-development-guide.md)**

Please refer to the document above for the authoritative source on:

* **Branching Strategy** (GitFlow-lite)
* **Commit Messages** (Conventional Commits)
* **Definition of Done** (Quality & Security gates)

## 📦 Pull Requests

1. **Template**: Fill out the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md)
   completely.
2. **Linting & Tests**: Ensure all automated checks pass.
3. **Traceability**: Link to the relevant Issue or PRD.

## 🐛 Reporting Bugs

Please use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md) to
report issues. Provide as much context as possible (logs, screenshots, steps to
reproduce).
