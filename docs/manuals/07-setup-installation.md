# Setup & Installation

## 📋 Prerequisites

Before starting, ensure you have the following installed:

* **Node.js**: >= 20
* **Python**: >= 3.10
* **Docker**: Desktop or Engine
* **Make**: (Optional but recommended for Unix users)

## 🚀 Quick Start

### 1. Instantiate the Template

The `bootstrap-new-project` script automates the personalization of the codebase:

1. **Prompts** for your new Project Name and Description.
2. **Updates** `README.md` and `package.json`.
3. **Replaces** `Init-Project-Template` with your project name across all
   documentation (`docs/`, `ARCHITECTURE.md`, etc.) and config files.
4. **Runs** the workspace setup to migrate agent rules.

Choose the method that fits your workflow:

#### Option A: Universal Scripts (Recommended)

##### Windows

```powershell
./scripts/bootstrap-new-project.ps1
```

##### Mac/Linux

```bash
./scripts/bootstrap-new-project.sh
```

#### Option B: Unix Make

```bash
make init
```

#### Option C: Node.js (Secondary)

```bash
npm install
npm run init
```

### 2. Workspace Setup

After bootstrapping, set up your personal workspace. This step:

1. **Migrates** agent settings (rules, workflows, skills) to `.agent/` and `.opencode/`.
2. **Configures** repo-local Git settings (for example `commit.template` via `.gitmessage`).
3. **Cleans up** the temporary `agent_settings` directory.

```bash
# Windows
./scripts/setup-workspace.ps1

# Mac/Linux
./scripts/setup-workspace.sh
```

## 🧪 Verifying Installation

To ensure everything is set up correctly, run the documentation validator and
the template's unit tests:

```bash
# Docs validation (strict)
# Windows
pwsh -NoProfile -File scripts/validate-docs.ps1 -Strict
# Mac/Linux
./scripts/validate-docs.sh --strict

# Validator unit tests
python -m unittest discover -s tests -p "test*.py" -q
```

If you enable a Node-based stack, you can also run `npm test` for your project
tests after you set them up.
