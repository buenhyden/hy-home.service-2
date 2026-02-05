# Operations / Deployment / Monitoring Checklist

This template operationalizes ops/deploy/monitoring agreements through:

- **Project-level standards**: [`OPERATIONS.md`](../../OPERATIONS.md)
- **Observability governance**: [`.agent/rules/2600-Observability/2600-observability-pillar.md`](../../.agent/rules/2600-Observability/2600-observability-pillar.md)
- **Feature-level requirements**: Specs in `specs/` using [`templates/spec-template.md`](../../templates/spec-template.md)
- **Infrastructure baseline**: [`docs/manuals/10-infrastructure.md`](../manuals/10-infrastructure.md)

## Checklist Items → Where to Define

| Item | Required | Where to define / enforce |
| --- | --- | --- |
| Environment hierarchy (dev/staging/prod) | Must | [`OPERATIONS.md`](../../OPERATIONS.md) Section 1 |
| Deployment strategy (manual vs CI/CD; rolling/blue-green/canary) | Must | [`OPERATIONS.md`](../../OPERATIONS.md) Section 3 + Spec Section 9 |
| Deployment approval process | Must | [`OPERATIONS.md`](../../OPERATIONS.md) Section 3 + GitHub environments/release workflow |
| Config & secrets management | Must | [`OPERATIONS.md`](../../OPERATIONS.md) Section 6 + `.env.example` + secret scanning baseline |
| Logging strategy (structured logs) | Must | [`OPERATIONS.md`](../../OPERATIONS.md) Section 2 + observability pillar |
| Monitoring (metrics + dashboards) | Must | [`OPERATIONS.md`](../../OPERATIONS.md) Section 2 + observability pillar |
| Alerts (thresholds + routing) | Must | [`OPERATIONS.md`](../../OPERATIONS.md) Section 2 + alerting standards |
| Incident response (on-call/escalation/post-mortem) | Optional | [`OPERATIONS.md`](../../OPERATIONS.md) Section 5 + team governance |
| Backup strategy (frequency/retention/location) | Must | [`OPERATIONS.md`](../../OPERATIONS.md) Section 4 |
| RTO/RPO targets (numbers) | Optional | [`OPERATIONS.md`](../../OPERATIONS.md) Section 4 |
| Cost monitoring/tagging policy | Optional | [`OPERATIONS.md`](../../OPERATIONS.md) Section 7 + cloud governance |

## Feature-Level Workflow

1. Confirm project-level defaults in [`OPERATIONS.md`](../../OPERATIONS.md).
2. In your Spec, complete:
   - Section 0 Operations/Deployment/Monitoring checklist
   - Section 9 Operations & Observability (deploy strategy, metrics/alerts,
     data protection)
3. If the feature introduces new infrastructure, define cost tags and alerts and
   document them in the Spec and/or ADR.
