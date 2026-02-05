# Init-Project-Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/release/buenhyden/Init-Project-Template.svg)](https://github.com/buenhyden/Init-Project-Template/releases/latest)
[![Agent Ready](https://img.shields.io/badge/Agent-Ready-blue?style=flat&logo=robot)](AGENTS.md)

**A standardized, AI-optimized project template designed for high-fidelity
agentic software development.**

This template provides a robust foundation for cooperative development between
human engineers and AI coding agents (Gemini, Claude, GPT). It ensures
consistency, security, and engineering excellence through a system of strict,
machine-parseable rules.

---

## 🚀 Key Features

* **🤖 Agent-Ready**: Built-in specialized personas ([AGENTS.md](AGENTS.md)) and
  specific rule sets for deterministic AI reasoning.
* **🏛️ 5-Pillar Governance**: Development is governed by five pillars:
  [1. Standards](docs/core/03-governance-standards.md),
  [2. Workflows](docs/manuals/06-development-guide.md),
  [3. Security/QA](docs/manuals/09-security-qa.md),
  [4. Tech Stack](docs/core/08-tech-stack.md), and
  [5. Operations/Monitoring](OPERATIONS.md).
* **⚡ Polyglot Orchestration**: Unified `Makefile` and PowerShell/Shell
  `scripts/` support Node.js, Python, Go, and Rust.
* **📝 Documentation-Driven**: Integrated 4-pillar hierarchy: **PRD** (What), **Architecture Blueprint** (Vision), **ADR** (Why), and **ARD** (How) to ensure transparency and traceability.
* **🛡️ Secure by Default**: Security and dependency automation templates are
  included (e.g., TruffleHog, Dependabot). Enable and customize them to match
  your stack and repository policy.

---

## 📂 Repository Map

```text
.
├── .agent/                 # Active AI Agent configurations
├── .github/                # GitHub Workflows & Templates
├── agent_settings/         # (Transient) Initial template settings (deleted after setup)
├── docs/                   # 📚 Project Documentation
├── scripts/                # Utility scripts
├── specs/                  # Technical Specifications
├── templates/              # PRD & Spec Templates
├── tests/                  # Test Suites
├── ARCHITECTURE.md         # 🏗️ Architecture Blueprint
├── COLLABORATING.md        # 🤝 Collaboration & SLA Guide
├── OPERATIONS.md           # ⚙️ Operations & Monitoring Pillar
├── AGENTS.md               # AI Persona Definitions
└── Makefile                # Unified Command Interface
```

> [!TIP]
> For a detailed folder breakdown and logical flow, see the
> **[Detailed Repository Structure](docs/core/05-repository-structure.md)**.

---

## 🛠️ Getting Started

### Prerequisites

* **Node.js**: >= 20
* **Python**: >= 3.10
* **Docker**: Desktop or Engine

### 1. Initialize Project

#### Unix (Mac/Linux)

```bash
./scripts/bootstrap-new-project.sh
# OR
make init
```

#### Windows (PowerShell)

```powershell
./scripts/bootstrap-new-project.ps1
```

### 2. Setup Workspace

Configure your local environment and sync the AI agent settings:

```bash
# Unix (Run setup script to migrate settings and cleanup)
make setup
# OR
./scripts/setup-workspace.sh

# Windows (Run setup script to migrate settings and cleanup)
./scripts/setup-workspace.ps1
```

---

## 📚 Documentation Index

We have organized documentation into the `docs/` directory. Start here:

* **[Project Overview](docs/core/01-project-overview.md)**: Philosophy and Mission.
* **[Architecture Blueprint](ARCHITECTURE.md)**: System design and logical layering.
* **[Architecture Decision Records (ADRs)](docs/adr/README.md)**: The "Why" behind technical choices.
* **[Architecture Reference Documents (ARDs)](docs/ard/README.md)**: The "How" of current implementation.
* **[Product Requirement Documents (PRDs)](docs/prd/README.md)**: The "What" we are building.
* **[Governance Standards](docs/core/03-governance-standards.md)**: The rules that govern this repo.
* **[Agent Integration](docs/agents/04-agent-integration.md)**: How to work with
  the AI personas.
* **[05-repository-structure.md](docs/core/05-repository-structure.md)**: Detailed
  map of directories and files.
* **[Development Guide](docs/manuals/06-development-guide.md)**: Workflow,
  branching, and testing.
* **[COLLABORATING.md](COLLABORATING.md)**: Collaboration model and SLA
  (links to the collaboration guide).
* **[Collaboration Guide](docs/manuals/11-collaboration-guide.md)**: Communication
  channels, decision ownership, and review guidelines.
* **[Tech Stack](docs/core/08-tech-stack.md)**: Languages and tools.
* **[Operations & Monitoring](OPERATIONS.md)**: Deployment and observability standards.
* **[Developer Guides](docs/guides/README.md)**: Practical checklists and
  how-to guides.
  * [Business & Product](docs/guides/business-product-checklist.md)
  * [Architecture & Stack](docs/guides/architecture-tech-stack-checklist.md)
  * [Development Process](docs/guides/development-process-collaboration-checklist.md)
  * [Quality & Security](docs/guides/quality-testing-security-checklist.md)
  * [Ops & Deployment](docs/guides/operations-deployment-monitoring-checklist.md)
  * [Agent Rules Map](docs/guides/agent-rules-checklist.md)

---

## 🤖 AI Agent Instructions

When asking an AI agent to work on this repository, explicitly reference a
**Persona** and **Workflow**.

> "Act as the **[Architect]**. Review `docs/prd/my-feature-prd.md` and create a
> technical spec in `specs/my-feature/spec.md` following the
> [Requirements & Specifications Standard](.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md)."

See **[AGENTS.md](AGENTS.md)** for the full list of available personas.

---

## 🤝 Contributing

We welcome contributions! Please see **[CONTRIBUTING.md](CONTRIBUTING.md)** for
details on our code of conduct and development process.

## 📄 License

This project is licensed under the MIT License - see the **[LICENSE](LICENSE)**
file for details.
