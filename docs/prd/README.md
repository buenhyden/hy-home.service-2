# Product Requirement Documents (PRDs)

## ❓ What is a PRD?

A **Product Requirement Document (PRD)** outlines the purpose, features,
behavior, and success metrics of a new product feature. It serves as the
single source of truth for "What" we are building and "Why".

For the **technical implementation** and architectural details, see:

- **[Architecture Blueprint](../../ARCHITECTURE.md)**: Overall vision and principles.
- **[Architecture Decision Records (ADRs)](../adr/README.md)**: "Why" technical choices were made.
- **[Architecture Reference Documents (ARDs)](../ard/README.md)**: "How" the features are implemented.

## 📂 PRD Principles (Best Practices)

- **Problem-First**: Define the customer pain point or business opportunity before detailing the solution.
- **Living Document**: A PRD is not a static artifact. It should be updated as requirements evolve or as new data arrives.
- **Collaboration**: PRDs should be co-created by Product, Engineering, and Design to ensure technical feasibility and user value.
- **Traceability**: Link requirements (`[REQ-PRD-xxx]`) to technical specs and test cases.

## ✍️ How to Create a PRD

1. **Use the Template**: Copy `../../templates/prd-template.md` to this directory.
   - **Optional scaffolding**:
     - Windows: `./scripts/new-prd.ps1 -Feature "my-feature" -WithSpec`
     - Unix: `WITH_SPEC=1 ./scripts/new-prd.sh "my-feature"`

2. **Define Requirements**: Use the `[REQ-PRD-xxx]` ID format for traceable
   requirements (e.g., `[REQ-PRD-FUN-01]`).

3. **Status Lifecycle**:
   - **Draft**: Initial ideas being documented.
   - **Review**: Open for stakeholder and team feedback.
   - **Approved**: Finalized and ready for implementation.

4. **Review Gate**: Ensure stakeholders approve the PRD before technical implementation begins.

## ✅ Organization & Validation

- PRDs should be named clearly, often prefixed with the EPIC or Feature name.
- Example: `auth-system-prd.md`, `dashboard-v2-prd.md`
- Validate documentation structure:
  - Windows: `./scripts/validate-docs.ps1 -Strict`
  - Unix: `./scripts/validate-docs.sh --strict`
