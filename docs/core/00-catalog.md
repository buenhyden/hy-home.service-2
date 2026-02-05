# Documentation Catalog & Roadmap

This document outlines the complete structure of the project documentation,
including existing core documents, required guides, and templates for future
documentation.

## 📚 1. Core Documentation (Existing)

These documents provide the foundational knowledge for the project.

- **[01-project-overview.md](./01-project-overview.md)**: Mission, Philosophy,
  and Key Features.
- **[ARCHITECTURE.md](../../ARCHITECTURE.md)**: High-level System Architecture (Pillar 2: Vision).
- **[OPERATIONS.md](../../OPERATIONS.md)**: Operations, deployment, and monitoring.
- **[COLLABORATING.md](../../COLLABORATING.md)**: Collaboration model and SLA
  (links to team collaboration guide).
- **[03-governance-standards.md](./03-governance-standards.md)**: Governance
  Pillars and Rule ID System.
- **[04-agent-integration.md](../agents/04-agent-integration.md)**: Working with
  AI Agents (Personas, Rules).
- **[05-repository-structure.md](./05-repository-structure.md)**: File system
  layout and organization.
- **[06-development-guide.md](../manuals/06-development-guide.md)**: SDLC,
  Branching, and Definition of Done.
- **[07-setup-installation.md](../manuals/07-setup-installation.md)**: Getting
  started and environment setup.
- **[08-tech-stack.md](./08-tech-stack.md)**: Technology choices and versions.
- **[09-security-qa.md](../manuals/09-security-qa.md)**: Security protocols and
  testing strategies.
- **[10-infrastructure.md](../manuals/10-infrastructure.md)**: DevOps, Docker,
  and CI/CD pipelines.
- **[11-collaboration-guide.md](../manuals/11-collaboration-guide.md)**: Team
  collaboration, SLA, and decision-making.

## 📂 2. Dynamic Documentation Folders

These folders are intended to grow with the project.

- **[prd/](../prd/)**: Product Requirement Documents (Pillar 1: What).
- **[adr/](../adr/)**: Architecture Decision Records (Pillar 3: Why).
- **[ard/](../ard/)**: Architecture Reference Documents (Pillar 4: How).
- **[guides/](../guides/)**: Step-by-step developer guides.

## 🛠️ 3. Recommended Guides (Roadmap)

The following guides are recommended to be written or generated, based on the
project's **Workflows** (`.agent/workflows/`).
Until fully written, developers should refer to the corresponding workflow files.

### ✅ Implemented Guides (Checklists)

These guides are already available under `docs/guides/`:

- **[business-product-checklist.md](../guides/business-product-checklist.md)**:
  Business/Product checklist via PRDs.
- **[architecture-tech-stack-checklist.md](../guides/architecture-tech-stack-checklist.md)**:
  Architecture/stack checklist via Specs + ADRs.
- **[development-process-collaboration-checklist.md](../guides/development-process-collaboration-checklist.md)**:
  Process/collaboration checklist via manuals + templates.
- **[quality-testing-security-checklist.md](../guides/quality-testing-security-checklist.md)**:
  Quality/testing/security checklist via Specs + gates.
- **[operations-deployment-monitoring-checklist.md](../guides/operations-deployment-monitoring-checklist.md)**:
  Ops/deploy/monitoring checklist via `OPERATIONS.md` + Specs.
- **[agent-rules-checklist.md](../guides/agent-rules-checklist.md)**: Master
  mapping of the 5 pillars to proactive Agent Rules.

### 🌐 Global

- `workflow-project-init`: How to initialize the project.
- `workflow-git-commit`: Standardized commit messages.
- `debug-module-not-found`: Troubleshooting dependency issues.
- `sync-git-fork`: Keeping forks in sync.

### ⚙️ DevOps

- `workflow-deploy-check`: Pre-deployment validation.
- `setup-sentry`: Configuring error tracking.
- `implement-feature-flags`: utilizing flags for rollout.

### ⚛️ React & Next.js

- `workflow-react-component`: Creating new components.
- `migrate-nextjs-pages-router`: Updating routing strategies.
- `optimize-images`: Best practices for media.

### 🔒 Security

- `setup-rbac`: Implementing Role-Based Access Control.
- `audit-accessibility`: Running a11y checks.

## 📝 4. Documentation Templates

Use these templates when creating new files (located in root `templates/`):

- **PRD Template**: `templates/prd-template.md` (Pillar 1)
- **Spec Template**: `templates/spec-template.md`
- **ADR Template**: `templates/adr-template.md` (Pillar 3)
- **ARD Template**: `templates/ard-template.md` (Pillar 4)

---

### Last Updated: 2026-02-04
