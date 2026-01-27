# Infrastructure & Orchestration

This project prioritizes **OS-agnostic orchestration** and **containerization** to ensure a consistent experience across all environments.

## 🐳 Containerization

* **Docker**: Used to containerize applications and services.
* **Dockerfile**: Defines the image for the application.
* **docker-compose.yml**: Orchestrates multi-container environments (e.g., App + DB).

## ⚡ Orchestration

We provide a unified interface for both humans and automation scripts, ensuring that complex tasks can be executed with a single command.

### Scripts (`scripts/`)

* **`bootstrap-new-project`**: Initializes a new repository.
* **`setup-workspace`**: Configures the local developer environment.
* **`sync-agent-settings`**: Updates local agent configurations from the master.

### Make

For Unix users, a `Makefile` wraps common script commands for convenience:

* `make init`: Runs the bootstrap script.
* `make test`: Runs the test suite.

## 🚀 CI/CD

Our infrastructure is designed to integrate seamlessly with GitHub Actions.

* **Workflows**: Located in `.github/workflows/`.
* **Jobs**: Build, Test, Lint, Security Scan.

## 🌍 Environments

* **Local**: Controlled by `docker-compose.yml` and local scripts.
* **Production**: Images built via Dockerfile are deployed to target cloud providers (AWS, GCP, Vercel).
