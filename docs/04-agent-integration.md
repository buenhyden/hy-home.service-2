# AI Agent Integration

This template is designed to treat AI agents as "First-Class Citizens," providing them with specialized personas, skills, and standardized workflows.

## 👥 Specialized Personas

We define specialized roles to avoid generic AI behavior. These are detailed in [AGENTS.md](../../AGENTS.md).

### Core Personas

* **The Strong Reasoner**: The primary reasoning engine for complex tasks.
* **The Architect**: Focuses on system design, logical layering, and API contracts.
* **The DevOps**: Manages CI/CD, orchestration, and infrastructure.
* **The Auditor**: Performs security checks and engineering excellence audits.

## 🛠️ Integrated Skills

"Skills" are atomic instruction sets that give agents specific capabilities, located in `agent_settings/skills/`.

* **Scope**: Covers everything from `git-commit` logic to `browser-automation` and `sast-configuration`.
* **Syncing**: Active skills are automatically migrated during workspace setup to:
  * `.agent/skills/` (for immediate use by agents)
  * `.opencode/skills/` (as a standard library)

## 🔄 Declarative Workflows

Workflows are step-by-step automation guides found in `.agent/workflows/`. They ensure agents follow a consistent process for recurring tasks.

### Collaboration Model

1. **Workstream Initiated**: A task starts (e.g., "Build Login Page").
2. **Workflow Identification**: Agent identifies the relevant workflow (e.g., `feature-development`).
3. **Persona Adoption**: Agent adopts the necessary Persona (e.g., Frontend Developer).
4. **Execution**: Agent executes steps using specific Skills while being governed by the Rules.

## 🤖 Working with Agents

* **Persona Switch**: When starting a task, explicitly instruct the agent to adopt a persona:
    > "As your **[Persona Name]**, I will follow **[Standard ID]** to execute this task."
* **Rule Adherence**: Agents are governed by the .md files in `.agent/rules`.
