# hy-home.service-2

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/release/buenhyden/hy-home.service-2.svg)](https://github.com/buenhyden/hy-home.service-2/releases/latest)
[![Agent Ready](https://img.shields.io/badge/Agent-Ready-blue?style=flat&logo=robot)](AGENTS.md)

**입력받은 텍스트의 내용을 분석하고 이 내용을 바탕으로 이미지를 생성하며, 생성된 이미지를 바탕으로 뉴스를 브리핑하는 영상을 제작하도록 한다.

This template provides a robust foundation for cooperative development between human engineers and AI coding agents (Gemini, Claude, GPT). It ensures consistency, security, and engineering excellence through a system of strict, machine-parseable rules.

---

## 🚀 Key Features

* **🤖 Agent-Ready**: Built-in specialized personas ([AGENTS.md](AGENTS.md)) and specific rule sets for deterministic AI reasoning.
* **🏛️ Multi-Pillar Governance**: Development is governed by four pillars: [Standards](docs/03-governance-standards.md), [Workflows](docs/03-governance-standards.md), [Security](docs/09-security-qa.md), and [Tech Stack](docs/08-tech-stack.md).
* **⚡ Polyglot Orchestration**: Unified `Makefile` and PowerShell/Shell `scripts/` support Node.js, Python, Go, and Rust.
* **📝 Documentation-Driven**: Integrated templates for PRDs and Specs to promote "Document First, Code Later".
* **🛡️ Secure by Default**: Pre-configured GitHub Actions for security scanning (TruffleHog) and dependency updates (Dependabot).

---

## 📂 Repository Map

```text
.
├── .agent/                 # Active AI Agent configurations (Active Rules & Skills)
├── .github/                # GitHub Workflows, Templates & Actions
├── agent_settings/         # Master Knowledge Base (Full Rules & Skills Library)
├── docs/                   # 📚 Project Documentation
│   ├── guides/             # "How-To" Guides
│   ├── adr/                # Architecture Decision Records
│   ├── prd/                # Product Requirements
│   ├── 01-overview.md      # Project Mission & Philosophy
│   ├── ...                 # (See docs/README.md for full index)
├── scripts/                # Utility scripts (bootstrap, setup, sync)
├── specs/                  # Technical Specifications
├── templates/              # PRD & Spec Templates
├── tests/                  # Test Suites
├── AGENTS.md               # AI Persona Definitions
├── ARCHITECTURE.md         # System Design & Logical Layers
├── CONTRIBUTING.md         # Developer Guide
├── LICENSE                 # MIT License
└── Makefile                # Unified Command Interface
```

---

## 🛠️ Getting Started

### Prerequisites

* **Node.js**: >= 20
* **Python**: >= 3.10
* **Docker**: Desktop or Engine

### 1. Initialize Project

**Unix (Mac/Linux)**

```bash
./scripts/bootstrap-new-project.sh
# OR
make init
```

**Windows (PowerShell)**

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

* **[Project Overview](docs/01-project-overview.md)**: Philosophy and Mission.
* **[Architecture](docs/02-architecture.md)**: System design and logical layering.
* **[Governance Standards](docs/03-governance-standards.md)**: The rules that govern this repo.
* **[Agent Integration](docs/04-agent-integration.md)**: How to work with the AI personas.
* **[Repository Structure](docs/05-repository-structure.md)**: Detailed folder breakdown.
* **[Development Guide](docs/06-development-guide.md)**: Workflow, branching, and testing.
* **[Tech Stack](docs/08-tech-stack.md)**: Languages and tools.

---

## 🤖 AI Agent Instructions

When asking an AI agent to work on this repository, explicitly reference a **Persona** and **Workflow**.

> "Act as the **[Architect]**. Review `docs/prd/my-feature.md` and create a technical spec in `specs/` following the [Spec/Design Standard](.agent/rules/0100-Standards/0120-requirements-and-specifications-standard.md)."

See **[AGENTS.md](AGENTS.md)** for the full list of available personas.

---

## 🤝 Contributing

We welcome contributions! Please see **[CONTRIBUTING.md](CONTRIBUTING.md)** for details on our code of conduct and development process.

## 📄 License

This project is licensed under the MIT License - see the **[LICENSE](LICENSE)** file for details.
