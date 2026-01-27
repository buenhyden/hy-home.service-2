# Developer Onboarding Guide

Welcome to the **Init-Project-Template**. This guide will walk you through the structural principles, governance standards, and automated workflows that make this repository AI-optimized and highly scalable.

---

## 🏗️ 1. Understanding the Architecture

This project is built around four core **Standards Pillars** located in `.agent/rules/`:

1. **[0000] Agents**: Specialized AI personas (see [AGENTS.md](file:///d:/hy-home.SourceCode/Init-Project-Template/AGENTS.md)).
2. **[0100] Standards**: Core engineering principles, architecture, and documentation.
3. **[0200] Workflows**: SDLC, Git branching, and automation logic.
4. **[0400+] Domains**: Specific tech stack rules (Python, React, AWS, etc.).

### Coded Identifier System

Every requirement in this project is pinned to a unique identifier: `[REQ-XXX-NNN]`. This allows agents and developers to trace functionality directly back to governance standards.

---

## 🤖 2. Working with AI Agents

AI agents are "First-Class Citizens" in this repository.

- **Persona Switch**: When starting a task, instruct the agent to adopt a specific persona from [AGENTS.md](file:///d:/hy-home.SourceCode/Init-Project-Template/AGENTS.md).
- **Rule Adherence**: Agents are governed by the `.md` files in `.agent/rules`. If you identify a structural flaw, update the rule file, and the agent will adapt instantly.

---

## 🛠️ 3. Essential Workflows

### Project Initialization

IF starting a new feature THEN MUST follow the [Project Init Workflow](file:///d:/hy-home.SourceCode/Init-Project-Template/.agent/workflows/Global/workflow-project-init.md).

### Creating Requirements (PRD)

1. Copy `templates/prd-template.md` to `docs/prd/[feature]-prd.md`.
2. Define success metrics using `[REQ-PRD-MET-NN]`.

### Implementing Features

1. Create a Technical Specification using `templates/spec-template.md`.
2. Map implementation requirements to the PRD using coded IDs.

---

## ✅ 4. Definition of Done (DoD)

Before merging any code, verify:

1. **Skeleton Compliance**: All rules follow the 8-section skeleton.
2. **Traceability**: 100% of functional logic maps back to a requirement ID.
3. **Audit Pass**: Run `python deep_rule_audit.py` (when available) for compliance.

---

## 🆘 Support & Resources

- **ADRs**: check `docs/adr/` for historical architectural decisions.
- **Rules Master**: see [0100-unified-master.md](file:///d:/hy-home.SourceCode/Init-Project-Template/.agent/rules/0100-Standards/0100-unified-master.md).
