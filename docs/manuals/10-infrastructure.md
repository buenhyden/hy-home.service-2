# Infrastructure & Orchestration

This project prioritizes **OS-agnostic orchestration** and **containerization**
to ensure a consistent experience across all environments.

## 🐳 Containerization

* **Docker**: Used to containerize applications and services.
* **Dockerfile**: Defines the image for the application.
* **docker-compose.yml**: Orchestrates multi-container environments
  (e.g., App + DB).

## ⚡ Orchestration

We provide a unified interface for both humans and automation scripts, ensuring
that complex tasks can be executed with a single command.

### Scripts (`scripts/`)

* **`bootstrap-new-project`**: Initializes a new repository.
* **`setup-workspace`**: Configures the local developer environment.
* **`sync-agent-settings`**: Updates local agent configurations from the master.

### Make

For Unix users, a `Makefile` wraps common script commands for convenience:

* `make init`: Runs the bootstrap script.
* `make setup`: Runs the workspace setup script.

Project-specific `make test` / `make lint` targets can be added after choosing
a stack.

## 🚀 CI/CD

Our infrastructure is designed to integrate seamlessly with GitHub Actions.

* **Workflows**: Located in `.github/workflows/`.
* **Jobs**: Build, Test, Lint, Security Scan.

## 🌍 Environments & Deployment

* **Local**: Controlled by `docker-compose.yml` and local scripts.
* **Continuous Deployment (CD)**:
  * **Preview**: Spin-up ephemeral environments per PR.
  * **Staging**: Automated deploy on release tags.
  * **Production**: Gated deployment via GitHub Actions environments.

## 💾 Reliability & Maintenance

* **Backup Protocol**: Daily automated backups to off-site object storage.
* **DR Plan**: Reference the authoritative RPO and RTO targets defined in
  [OPERATIONS.md Section 4](../../OPERATIONS.md#4-continuity--data-protection).
* **Cost Monitoring**: Infrastructure components MUST be tagged (`Project`,
  `Owner`, `Env`) for granular billing analysis.
