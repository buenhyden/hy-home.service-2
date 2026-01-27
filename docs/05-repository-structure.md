# Repository Structure

This document provides a detailed map of the project's directory structure and the purpose of each component.

## 📂 Directory Map

```text
.
├── .agent/                 # Active AI Agent configurations (local rules, skills, workflows)
├── .github/                # GitHub-specific configs (Actions, PR templates)
├── agent_settings/         # (Transient) Initial template settings (Deleted after setup)
├── docs/                   # Project documentation (ADRs, Guides, PRDs, Onboarding)
│   ├── adr/                # Architecture Decision Records
│   ├── guides/             # Developer guides and how-tos
│   └── prd/                # Product Requirement Documents
├── examples/               # Example implementations and usage patterns
├── scripts/                # Utility scripts for bootstrap, sync, and setup
├── specs/                  # Technical specifications and design docs
├── templates/              # Standardized templates for new PRDs, specs, etc.
├── tests/                  # Test suites (unit, integration, e2e)
├── AGENTS.md               # Directory of specialized AI personas
├── ARCHITECTURE.md         # High-level system design and logical layering
├── CHANGELOG.md            # Version history and major changes
├── CONTRIBUTING.md         # Guidelines for contributing to the template
├── Dockerfile              # Containerization instructions
├── Makefile                # Unified build/task orchestration
└── package.json            # Node.js dependencies
```

## 🧱 Logic Flow

1. **Initialize**: Use `scripts/` to bootstrap a new project.
2. **Govern**: AI Agents read rules from `.agent/`.
3. **Develop**: Features are defined in `docs/prd/`, designed in `specs/`, and implemented in `src/`.
4. **Orchestrate**: Use `Makefile` and `scripts/` for consistent execution across environments.

## 🔑 Key Directories Detail

### `.agent/` vs `agent_settings/`

* `agent_settings/` is the **Template Source**. It contains the initial library of rules and skills but is removed after setup.
* `.agent/` is the **Active Instance**. It contains the currently enabled rules and skills for this workspace. Scripts sync changes from Master to Active.

### `templates/`

Empty but standardized skeletons used to create consistent documentation:

* `prd-template.md`: For defining new product features.
* `spec-template.md`: For technical implementation designs.
