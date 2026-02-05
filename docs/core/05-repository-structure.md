# Repository Structure

This document provides a detailed map of the project's directory structure and
the purpose of each component.

## 📂 Directory Map

```text

.
├── .agent/                 # Active AI Agent configurations (local rules, skills, workflows)
├── .github/                # GitHub-specific configs (Actions, PR templates)
├── agent_settings/         # (Transient) Initial template settings (Deleted after setup)
├── docs/                   # Project documentation (Governance, Manuals, Guides)
│   ├── core/               # Architecture, Governance, Catalog
│   ├── manuals/            # Development, Setup, Security
│   ├── agents/             # Agent Integration Docs
│   ├── guides/             # Practical Developer Guides
│   ├── adr/                # Architecture Decision Records (Pillar 3)
│   ├── prd/                # Product Requirement Documents (Pillar 1)
│   └── ard/                # Architecture Reference Documents (Pillar 4)
├── examples/               # Example implementations and usage patterns
├── scripts/                # Utility scripts for bootstrap, sync, and setup
├── specs/                  # Technical specifications and design docs
├── templates/              # Standardized templates for new PRDs, specs, etc.
├── tests/                  # Test suites (unit, integration, e2e)
├── AGENTS.md               # Directory of specialized AI personas
├── CHANGELOG.md            # Version history and major changes
├── CONTRIBUTING.md         # Guidelines for contributing to the template
├── Dockerfile              # Containerization instructions
├── Makefile                # Unified build/task orchestration
└── package.json            # Node.js dependencies

```

## 🧱 Logic Flow

1. **Govern**: AI Agents read rules from `.agent/`.
2. **Develop**: Features are defined as PRDs (Pillar 1: **PRD**), refined into a Technical Spec (`specs/<feature>/spec.md`), and supported by ADRs (Pillar 3: **ADR**) and ARDs (Pillar 4: **ARD**) before implementation in `src/`.
3. **Orchestrate**: Use `Makefile` and `scripts/` for consistent execution across environments.

## 🔑 Key Directories Detail

### `agent_settings/` vs `.agent/`

* `agent_settings/` is the **Template Source (Transient)**. It ships with the template and contains the initial rules, skills, and workflows. During setup, `./scripts/setup-workspace.*` copies these into `.agent/` (and `.opencode/skills/`) and then **deletes** `agent_settings/`.
* `.agent/` is the **Active Instance**. After setup, agents MUST treat `.agent/` as the authoritative source for rules, skills, and workflows.
* **Maintainers**: Update `agent_settings/` first, then run `./scripts/sync-agent-settings.*` to refresh `.agent/` for local agent usage.

### `templates/`

Empty but standardized skeletons used to create consistent documentation:

* `prd-template.md`: For defining new product features (Pillar 1).
* `adr-template.md`: For recording major architectural decisions (Pillar 3).
* `ard-template.md`: For documenting active implementation patterns (Pillar 4).
* `spec-template.md`: For technical implementation designs.
