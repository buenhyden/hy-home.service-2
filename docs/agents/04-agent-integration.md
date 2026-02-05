# AI Agent Integration

This template is designed to treat AI agents as "First-Class Citizens,"
providing them with specialized personas, skills, and standardized workflows.

## 👥 Specialized Personas

We define specialized roles to avoid generic AI behavior. These are detailed in
[AGENTS.md](../../AGENTS.md).

### Core Personas

* **The Strong Reasoner**: The primary reasoning engine for complex tasks.
* **The Architect**: Focuses on system design, logical layering, and API contracts.
* **The DevOps**: Manages CI/CD, orchestration, and infrastructure.
* **The Auditor**: Performs security checks and engineering excellence audits.

## 🛠️ Integrated Skills

"Skills" are atomic instruction sets that give agents specific capabilities,
located in `.agent/skills/`.

* **Scope**: Covers everything from `git-commit` logic to `browser-automation`
  and `sast-configuration`.
* **Syncing**: Active skills are automatically migrated during workspace setup to:
  * `.agent/skills/` (for immediate use by agents)
  * `.opencode/skills/` (as a standard library)

## 🧬 Workspace Setup Lifecycle

This template intentionally separates **template payload** from the **active agent instance**:

1. `agent_settings/` ships with the template as the transient source of rules, skills, and workflows.
2. Run `./scripts/setup-workspace.ps1` (Windows) or `./scripts/setup-workspace.sh` (Unix) to copy:
   - `agent_settings/{rules,skills,workflows}` → `.agent/{rules,skills,workflows}`
   - `agent_settings/skills` → `.opencode/skills`
3. On success, the setup script **deletes** `agent_settings/`.

After setup, agents should read and follow rules from `.agent/` only.

## 🔄 Declarative Workflows

Workflows are step-by-step automation guides found in `.agent/workflows/`. They
ensure agents follow a consistent process for recurring tasks.

### Collaboration Model

1. **Workstream Initiated**: A task starts (e.g., "Build Login Page").
2. **Workflow Identification**: Agent identifies the relevant workflow (e.g., `feature-development`).
3. **Persona Adoption**: Agent adopts the necessary Persona (e.g., Frontend Developer).
4. **Execution**: Agent executes steps using specific Skills while being
   governed by the Rules.

## 🤖 Working with Agents

* **Persona Switch**: When starting a task, explicitly instruct the agent to
  adopt a persona:
    > "As your **[Persona Name]**, I will follow **[Standard ID]** to execute
    > this task."
* **Rule Adherence**: Agents are governed by the .md files in `.agent/rules`.

## 🧭 Doc-First Feature Flow (PRD → Spec → Code)

This repository follows a document-first, spec-driven flow for new features:

1. **PRD (What)**: Create and get approval for a PRD in `docs/prd/`.
2. **Spec (How, feature-level)**: Write `specs/<feature>/spec.md` and ensure it references the PRD and includes traceability IDs.
3. **ADR (Why, optional)**: If you make a significant decision, record it in `docs/adr/` and link it from the spec.
4. **ARD (How, patterns)**: If you introduce or change an implementation pattern, document it in `docs/ard/` and keep it up-to-date.
5. **Validate**: Run docs validation before merging: `./scripts/validate-docs.ps1 -Strict` (Windows) or `./scripts/validate-docs.sh --strict` (Unix).

Canonical guides:
* `docs/manuals/06-development-guide.md`
* `docs/guides/business-product-checklist.md`
* `docs/guides/architecture-tech-stack-checklist.md`
* `specs/README.md`
