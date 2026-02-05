# Architecture Reference Documents (ARDs)

## ❓ What is an ARD?

An **Architecture Reference Document (ARD)** is a living technical specification that describes **"How"** a specific part of the system is implemented. Unlike an ADR (which records a decision at a point in time), an ARD reflects the **current state** and serves as the authoritative implementation guide.

## 📂 ARD vs. ADR vs. ARCHITECTURE.md

| Document | Scope | Nature | Purpose | Role |
| --- | --- | --- | --- | --- |
| **[PRDs](../prd/README.md)** | Feature | Living | Business Requirements | **Pillar 1 (What)** |
| **[ARCHITECTURE.md](../../ARCHITECTURE.md)**| Global | Static | High-level Vision | **Pillar 2 (Vision)** |
| **[ADRs](../adr/README.md)** | Decision | Immutable | Historical Choices | **Pillar 3 (Why)** |
| **ARDs** (This Dir) | Component | Living | Detailed Technical Patterns | **Pillar 4 (How)** |

## 📝 ARD Quality Guidelines

- **Always Current**: ARDs must be updated when implementation patterns change.
- **Visual-First**: Use diagrams (Mermaid, C4) to explain complex interactions.
- **Actionable**: Code snippets and interface definitions should be clear enough for a developer to follow.
- **Referential**: Link to the relevant ADRs that gave birth to the patterns described.

## ✍️ How to Create an ARD

1. **Use the Template**: Copy `../../templates/ard-template.md` to this directory.
2. **Standard Naming**: Use descriptive names, e.g., `api-error-handling.md`, `event-driven-messaging.md`.
3. **Traceability**: Reference requirements from the Governance Layer (e.g., `[REQ-ARC-xxx]`).

## ✅ Validation

- Windows: `./scripts/validate-docs.ps1 -Strict`
- Unix: `./scripts/validate-docs.sh --strict`
