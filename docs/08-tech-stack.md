# Technology Stack

The **Init-Project-Template** is language-agnostic in its core governance but optimized for a modern, full-stack ecosystem.

## 💻 Core Stack

* **Languages**:
  * **TypeScript**: Primary language for frontend and full-stack logic.
  * **Python**: Primary language for backend services, data processing, and scripting (3.10+).
  * **Bash / PowerShell**: For orchestration scripts.
* **Frameworks**:
  * **Next.js**: Recommended for frontend applications.
  * **Node.js / Python / Go**: Support for various backend implementations.
* **Runtime**: Node.js (>= 20).

## 🛠️ Tooling & Utilities

* **Orchestration**: Universal Shell/PowerShell scripts in `scripts/`, `Makefile`.
* **CI/CD**: GitHub Actions.
* **Quality**: ESLint, Prettier, Husky (Git Hooks).
* **Documentation**: Markdown (GFM), Mermaid.js (Diagrams), C4 Modeling.

## 🤖 AI Integration Stack

* **Models**: Optimized for Gemini, Claude, and GPT-4o.
* **Protocol**: MCP (Model Context Protocol) support.
* **Configuration**: `.agent/` directory for active rules and skills.

## ⚖️ Reasoning

We choose this stack to balance **performance**, **developer experience**, and **AI-compatibility**. TypeScript and Python offer the best support for modern AI coding agents, while Docker ensures consistent environments.
