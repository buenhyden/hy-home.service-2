# Architecture Decision Records (ADRs)

## ❓ What is an ADR?

An **Architecture Decision Record (ADR)** is a document that captures an
important architectural decision made along with its context and consequences.
It serves as the historical record of the "Why" behind our architecture.

For the **current state** of our technical patterns and implementation details,
see the **[Architecture Reference Documents (ARDs)](../ard/README.md)**.
For the **business requirements** and feature definitions,
see the **[Product Requirement Documents (PRDs)](../prd/README.md)**.

## 📂 Structure

ADRs are numbered sequentially and stored in this directory.

- `0001-record-architecture-decisions.md` (Example)
- `0002-use-nextjs-for-frontend.md`
- `0003-adopt-postgresql.md`

## 📝 ADR Quality Guidelines (Best Practices)

- **One Decision per ADR**: Each document should focus on a single architectural choice.
- **Immutability**: Once accepted, an ADR should not be edited to change the decision. To change a decision, create a new ADR that **Supersedes** the old one.
- **Problem-First**: Always start with the context and the problem you are trying to solve.
- **Conciseness**: Keep it brief (1-2 pages). It should be readable in 5 minutes.
- **Visibility**: Reference ADRs in `ARCHITECTURE.md` and related technical specifications.

## ✍️ How to Create an ADR

1. **Use the Template**: Copy `../../templates/adr-template.md` to this directory.
   - **Optional scaffolding**:
     - Windows: `./scripts/new-adr.ps1 -Title "Decision Title" -Authors "name"`
     - Unix: `./scripts/new-adr.sh "Decision Title" "name"`

2. **Fill the Lifecycle**:
   - **Proposed**: When the decision is being discussed.
   - **Accepted**: Once the team agrees.
   - **Superseded**: When a newer ADR replaces this decision.
   - **Deprecated**: When the decision is no longer relevant.

3. **Review Process**: Submit a Pull Request. Major architectural changes require a formal review meeting or design document alignment.

## ✅ Process & Validation

- Create an ADR when you decide any of the following:
  - Architecture style, service boundaries, core tech stack, database engine, infra model, messaging strategy, or major security posture.
- Reference ADRs from:
  - `ARCHITECTURE.md` (project-level)
  - Specs in `specs/` (feature-level)
- Validate documentation structure:
  - Windows: `./scripts/validate-docs.ps1 -Strict`
  - Unix: `./scripts/validate-docs.sh --strict`
