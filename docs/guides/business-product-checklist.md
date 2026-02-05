# Business / Product Checklist (PRD-Driven)

This template operationalizes the **Pillar 1 (What): Business/Product checklist** through the PRD.
Instead of maintaining a separate checklist document, the PRD becomes the single
source of truth for alignment.

## Why PRD-Driven?

- Prevents “checklist drift” by keeping checklist answers and feature
  requirements in the same artifact.
- Enables review gates (Approved PRD) before implementation starts.
- Keeps traceability from PRD → Spec → Code via requirement IDs.

## Checklist Mapping

Use [`templates/prd-template.md`](../../templates/prd-template.md) and fill the
referenced PRD sections:

| Checklist Item | Where to write it |
| --- | --- |
| Vision & Goal | PRD Section 1 |
| Success Metrics | PRD Section 3 (`REQ-PRD-MET-*`) |
| Target Users (Personas) | PRD Section 2 (Metrics/Personas) |
| Core Use Cases (GWT) | PRD Section 4 (Given-When-Then) |
| Scope (In) | PRD Section 5 (`REQ-PRD-FUN-*`) |
| Not in Scope | PRD Section 6 |
| Timeline & Milestones | PRD Section 7 |
| Business Risks | PRD Section 8 |
| Compliance / Privacy | PRD Section 8 |

## Recommended Workflow

1. Create PRD: `docs/prd/<feature>-prd.md`
2. Stakeholder review → set PRD Status to **Approved**
3. Create Spec: `specs/<feature>/spec.md` (must reference PRD)
4. Implement, ensuring code maps back to `REQ-*` IDs

## Validation

- Windows: `./scripts/validate-docs.ps1 -Strict`
- Unix: `./scripts/validate-docs.sh --strict`
