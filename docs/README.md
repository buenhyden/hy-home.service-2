# Project Documentation

Welcome to the **Init-Project-Template** documentation. This folder serves as
the central knowledge base for understanding, building, and maintaining
applications using this template.

For a complete list of all documentation files and the future roadmap, see the
**[Documentation Catalog](./core/00-catalog.md)**.

## 📚 Core Documentation

These documents provide the foundational knowledge for the project.

### 1. General

* **[01-project-overview.md](./core/01-project-overview.md)**: Mission,
  philosophy, and key features.
* **[05-repository-structure.md](./core/05-repository-structure.md)**: Detailed
  map of directories and files.

### 2. Architecture & Standards

* **[ARCHITECTURE.md](../ARCHITECTURE.md)**: High-level system design and
  layers (C4 Model).
* **[OPERATIONS.md](../OPERATIONS.md)**: Operations, deployment, observability,
  and continuity standards.
* **[COLLABORATING.md](../COLLABORATING.md)**: Collaboration model and SLA
  (links to the collaboration guide).
* **[03-governance-standards.md](./core/03-governance-standards.md)**:
  Governance pillars and Rule ID system.
* **[08-tech-stack.md](./core/08-tech-stack.md)**: Languages, frameworks, and
  tooling choices.

### 3. Agent Integration

* **[04-agent-integration.md](./agents/04-agent-integration.md)**: Personas,
  Skills, Workflows, and how to collaborate with AI.

### 4. Development

* **[07-setup-installation.md](./manuals/07-setup-installation.md)**:
  Prerequisites and quick start guide.
* **[06-development-guide.md](./manuals/06-development-guide.md)**: SDLC,
  branching strategy, and "Definition of Done".
* **[11-collaboration-guide.md](./manuals/11-collaboration-guide.md)**: Team
  collaboration, meetings, decision ownership, and review guidelines.
* **[09-security-qa.md](./manuals/09-security-qa.md)**: Security protocols,
  testing standards, and audits.
* **[10-infrastructure.md](./manuals/10-infrastructure.md)**: Docker, CI/CD,
  and orchestration scripts.

---

## 📂 Living Documentation Hierarchy

This project follows a "Document-First" approach, organized into a clear hierarchy from business requirements to technical implementation.

| Level | Folder | Description | Role |
| :--- | :--- | :--- | :--- |
| **Pillar 1** | **[prd/](./prd/)** | Product Requirement Documents | **What** we are building. |
| **Pillar 2** | **[ARCHITECTURE.md](../ARCHITECTURE.md)** | Architecture Blueprint | **Why & How** (High-level vision). |
| **Pillar 3** | **[adr/](./adr/)** | Architecture Decision Records | **Why** (Specific technical choices). |
| **Pillar 4** | **[ard/](./ard/)** | Architecture Reference Docs | **How** (Detailed implementation). |
| **Guides** | **[guides/](./guides/)** | Developer How-to Manuals | Step-by-step task execution. |

---

## 📝 Templates

When creating new documentation, please use the standard templates located in
the root `templates/` directory to ensure consistency.

* `templates/prd-template.md`: For new Product Requirements (Pillar 1).
* `templates/adr-template.md`: For Architecture Decision Records (Pillar 3).
* `templates/ard-template.md`: For Architecture Reference Documents (Pillar 4).
* `templates/spec-template.md`: For Technical Specifications.

---

## 🔍 How to Use This Documentation

1. **New to the project?** Start with `docs/core/01-project-overview.md` and `docs/manuals/07-setup-installation.md`.
2. **Planning a feature?** Create a PRD in `docs/prd/` using the template.
3. **Designing a system?** Create an ADR in `docs/adr/` and consult [ARCHITECTURE.md](../ARCHITECTURE.md).
4. **Implementing details?** Document patterns in `docs/ard/` and check `docs/guides/` for workflows.
5. **Working with AI?** Read `docs/agents/04-agent-integration.md` to leverage agents effectively.
