# News Briefing Agent Service

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Ready](https://img.shields.io/badge/Agent-Ready-blue?style=flat&logo=robot)](AGENTS.md)

**An autonomous AI service that turns text into engaging news briefing videos.**

The system analyzes input text, generates relevant imagery using AI, and synthesizes a professional news briefing video.

---

## 🚀 Key Features

* **📰 Intelligent Text Analysis**: NLP-driven extraction of key themes, summary points, and sentiment.
* **🎨 Dynamic Image Generation**: Creation of context-aware visuals and illustrations for each news segment.
* **🎬 Automated Video Synthesis**: Assembly of images, voice-over, and transitions into a coherent video brief.
* **🤖 Agent-Ready Core**: Built on the **hy-home.service-2** template, ensuring robust governance and AI-collaboration standards.

---

## 📂 Repository Map

```text
.
├── .agent/                 # Active AI Agent configurations (Active Rules & Skills)
├── .github/                # GitHub Workflows, Templates & Actions
├── agent_settings/         # Master Knowledge Base (Full Rules & Skills Library)
├── docs/                   # 📚 Project Documentation
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

* **[01-project-overview.md](docs/01-project-overview.md)**: Mission, Philosophy, and Key Features.
* **[02-architecture.md](docs/02-architecture.md)**: System design and logical layering (C4 Model).
* **[03-governance-standards.md](docs/03-governance-standards.md)**: The 4 Governance Pillars and Rule ID system.
* **[04-agent-integration.md](docs/04-agent-integration.md)**: Personas, Skills, Workflows, and how to collaborate with AI.
* **[05-repository-structure.md](docs/05-repository-structure.md)**: Detailed folder breakdown and purpose.
* **[06-development-guide.md](docs/06-development-guide.md)**: SDLC, branching strategy, and "Definition of Done".
* **[07-setup-installation.md](docs/07-setup-installation.md)**: Prerequisites and quick start guide.
* **[08-tech-stack.md](docs/08-tech-stack.md)**: Languages, frameworks, and tooling choices.
* **[09-security-qa.md](docs/09-security-qa.md)**: Security protocols, testing standards, and audits.
* **[10-infrastructure.md](docs/10-infrastructure.md)**: Docker, CI/CD, and orchestration scripts.

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
