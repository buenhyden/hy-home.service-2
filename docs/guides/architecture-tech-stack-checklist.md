# Architecture / Tech Stack Checklist (Spec-Driven)

This template defines architecture and tech stack choices in two places:

- **Project-level** decisions: [`ARCHITECTURE.md`](../../ARCHITECTURE.md) and [`docs/core/08-tech-stack.md`](../core/08-tech-stack.md)
- **Feature-level** decisions: Specs in `specs/` using [`templates/spec-template.md`](../../templates/spec-template.md)

Major decisions (Why) should be recorded as ADRs in [`docs/adr/`](../adr/).
Implementation patterns (How) should be recorded as ARDs in [`docs/ard/`](../ard/).

## Checklist Items → Where to Document

| Item | Where to document |
| --- | --- |
| Architecture style | [`ARCHITECTURE.md`](../../ARCHITECTURE.md) + Spec Section 1 |
| Service/module boundaries | [`ARCHITECTURE.md`](../../ARCHITECTURE.md) (C4/Boundaries) + Spec Section 1 |
| Domain model (ER/UML) | Spec Section 3 (Mermaid ER) |
| Backend stack | Spec Section 1 + ADR (optional) |
| Frontend stack | Spec Section 1 + ADR (optional) |
| Database engine + schema strategy | Spec Section 3 + ADR (optional) |
| Messaging / async processing | Spec Section 4 (Async) + ADR (optional) |
| Infrastructure (cloud/K8s/serverless) | Spec Section 6 + [`OPERATIONS.md`](../../OPERATIONS.md) + ADR (optional) |
| NFR targets (numbers) | Spec Section 5 |
| Scalability strategy (caching/partitioning) | Spec Section 6 |
| Architecture principles (“don’ts”) | [`ARCHITECTURE.md`](../../ARCHITECTURE.md) Section 5 |
| ADR & ARD process | [`docs/adr/README.md`](../adr/README.md) + [`docs/ard/README.md`](../ard/README.md) |

## Recommended Workflow

1. Confirm project-level baseline: [`ARCHITECTURE.md`](../../ARCHITECTURE.md) and
   [`docs/core/08-tech-stack.md`](../core/08-tech-stack.md)
2. Create PRD + get Approved: `docs/prd/<feature>-prd.md`
3. Create Spec: `specs/<feature>/spec.md` and complete Spec Section 0 checklist
4. If a decision is significant, create an ADR (Pillar 3) and link it:
   - Windows: `./scripts/new-adr.ps1 -Title "..." -Authors "..."`
   - Unix: `./scripts/new-adr.sh "..." "..."`
5. Document detailed patterns in an ARD (Pillar 4):
   - Copy `../../templates/ard-template.md` to `docs/ard/`

## Validation

- Windows: `./scripts/validate-docs.ps1 -Strict`
- Unix: `./scripts/validate-docs.sh --strict`
