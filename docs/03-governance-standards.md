# Governance & The 4 Pillars

Project stability and quality are maintained through a strict **Multi-Pillar Governance** model. This ensures that every line of code complies with our established technical standards.

## 🏷️ Rule Identification System

Each rule in the project is assigned a unique, coded identifier in the format `[REQ-XXX-NN]`:

* **XXX**: Represents the category code (e.g., `0130` for Architecture).
* **NN**: Represents the specific requirement number.

This allows for deterministic traceability. AI agents can cite specific rules when making decisions or reviewing code.

## 🏛️ The Technical Pillars

The codebase is governed by four core technical pillars:

### 1. General Standards (0100)

* **Focus**: Engineering Excellence, Documentation, Clean Code.
* **Goal**: Maintain high maintainability and readability across all logic.
* **Reference**: [0100-unified-master.md](../../.agent/rules/0100-Standards/0100-unified-master.md)

### 2. Workflow Standards (0200)

* **Focus**: SDLC, Git Branching, Pull Request Flow, Automation.
* **Goal**: Standardize how we move from idea to production.
* **Reference**: [0200-workflow-standard.md](../../.agent/rules/0200-Workflows/0200-workflow-standard.md)

### 3. Security & QA (0500/0700)

* **Focus**: Vulnerability Management, Testing Coverage, Security Auditing.
* **Goal**: Ensure the codebase is secure-by-default and error-resilient.
* **Reference**: [2200-security-pillar.md](../../.agent/rules/2200-Security/2200-security-pillar.md)

### 4. Technology Stack (0150/1000)

* **Focus**: Strict Typing, Framework Patterns, Dependency Management.
* **Goal**: Enforce technical consistency and leverage framework best practices.
* **Reference**: [0150-tech-stack-standard.md](../../.agent/rules/0100-Standards/0150-tech-stack-standard.md)

## 🔄 Governance Lifecycle

1. **Planning**: PRDs and Specs must reference relevant `[REQ]` IDs.
2. **Implementation**: Code must follow the ID-indexed rules.
3. **Review**: Pull Requests are audited against the pillars before merging.

