# Developer Onboarding Guide

Welcome to the **Init-Project-Template**. This guide will walk you through the
structural principles, governance standards, and automated workflows that make
this repository AI-optimized and highly scalable.

---

## 🏗️ 1. Understanding the Architecture

This project is governed by a **5-pillar model** (Standards, Workflows, Security/QA,
Tech Stack, and Operations/Monitoring). Project-level blueprints live in
`ARCHITECTURE.md` and `OPERATIONS.md`, and the detailed rules live under
`.agent/rules/`.

Common rule families:

1. **[0000] Agents**: Specialized AI personas (see [AGENTS.md](../../AGENTS.md)).
2. **[0100] Standards**: Core engineering principles, architecture, documentation.
3. **[0200] Workflows**: SDLC, Git branching, and repeatable workflows.
4. **[0700] Testing & QA** and **[2200] Security**: Quality and security governance.
5. **[0400+] Domains / Stack**: Tech-specific rules (TypeScript, React, Cloud, etc.).
6. **[2600] Observability**: Monitoring and reliability standards.

### Coded Identifier System

Every requirement in this project is pinned to a unique identifier:
`[REQ-XXX-NNN]`. This allows agents and developers to trace functionality
directly back to governance standards.

---

## 🤖 2. Working with AI Agents

AI agents are "First-Class Citizens" in this repository.

- **Persona Switch**: When starting a task, instruct the agent to adopt a
  specific persona from [AGENTS.md](../../AGENTS.md).
- **Rule Adherence**: Agents are governed by the `.md` files in `.agent/rules`.
  If you identify a structural flaw, update the rule file, and the agent will
  adapt instantly.

---

## 🛠️ 3. Essential Workflows

### Project Initialization

IF starting a new feature THEN MUST follow the [Project Init Workflow](../../.agent/workflows/Global/workflow-project-init.md).

### Creating Requirements (PRD)

1. Copy `templates/prd-template.md` to `../../docs/prd/[feature]-prd.md`.
2. Define success metrics using `[REQ-PRD-MET-NN]`.
3. Optional scaffolding:
   - Windows: `./scripts/new-prd.ps1 -Feature "my-feature" -WithSpec`
   - Unix: `WITH_SPEC=1 ./scripts/new-prd.sh "my-feature"`

### Implementing Features

1. Create a Technical Specification using `templates/spec-template.md`.
2. Map implementation requirements to the PRD using coded IDs.
3. Confirm project-level architecture and baseline stack docs:
    - `ARCHITECTURE.md`
    - `docs/core/08-tech-stack.md`
    - `docs/adr/README.md` (ADR process)
4. Validate docs (recommended before opening a PR):
    - Windows: `./scripts/validate-docs.ps1 -Strict`
    - Unix: `./scripts/validate-docs.sh --strict`

---

## ✅ 4. Definition of Done (DoD)

Before merging any code, verify:

1. **Skeleton Compliance**: All rules follow the 8-section skeleton.
2. **Traceability**: 100% of functional logic maps back to a requirement ID.

---

## 🆘 Support & Resources

- **ADRs**: check `docs/adr/` for historical architectural decisions.
- **Rules Master**: see [0100-unified-master.md](../../.agent/rules/0100-Standards/0100-unified-master.md).
