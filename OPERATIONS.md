# Operational Blueprint

This document outlines the operational concerns, deployment strategies, and
monitoring standards defined by the **Ops / Deploy / Monitoring** pillar
(`[REQ-OPS-01]`).

## 0. Operations / Deployment / Monitoring Checklist

Use this checklist at project kickoff and for each major release.

| Item | Check Question | Required | Alignment Notes (Agreement) | Primary Document |
| :--- | :--- | :---: | :--- | :--- |
| Environment Hierarchy | Are environments defined (dev/staging/prod) and promotion rules agreed? | Must |  | Section 1 |
| Deployment Strategy | Is the deployment/release strategy decided (manual vs CI/CD; rolling/blue-green/canary)? | Must |  | Section 3 |
| Deployment Approval | Is production approval defined (who approves, what criteria)? | Must |  | Section 3 + release workflow |
| Health Checks | Does the app expose /healthz and /readyz endpoints? | Must |  | Specs |
| Config & Secrets | Is configuration/secrets management decided (env vars, secret manager, etc.)? | Must |  | Section 6 |
| Logging Strategy | Is structured logging defined and where logs are stored/queried? | Must |  | Section 2 |
| Monitoring | Are metrics and dashboards defined (traffic/errors/latency/saturation)? | Must | Every feature MUST have a corresponding dashboard with RED metrics (Rate, Error, Duration). | Section 2 |
| Alerts | Are alert thresholds and notification channels defined? | Must |  | Section 2 + alerting rules |
| Incident Response | Is incident process defined (on-call/escalation/post-mortem)? | Optional |  | Section 5 |
| Backup Strategy | Are backup frequency, retention, and storage location defined? | Must | We follow the [3-2-1 Backup Rule](https://www.backblaze.com/blog/the-3-2-1-backup-strategy/). | Section 4 |
| RTO/RPO | Are RTO/RPO targets defined as numbers? | Optional | The **Disaster Recovery Plan** is triggered when RTO/RPO targets are breached. (See `docs/manuals/10-infrastructure.md` for full playbook). | Section 4 |
| Cost Monitoring | Is cost monitoring/alerting and tagging policy defined? | Optional |  | Section 7 |

## 1. Environment Hierarchy

| Tier | Description | RPO | RTO | Examples |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | Critical user-facing flows (Login, Checkout) | 5 min | 1 hour | Auth Service, Payment API |
| **Tier 2** | Internal business ops (Reports, Admin) | 1 hour | 4 hours | Back-office Admin, ETL jobs |
| **Tier 3** | Non-critical (Archives, Experimental) | 24 hours | 24 hours | Old logs, Alpha features |

| Environment | Purpose | Promotion Rule |
| :--- | :--- | :--- |
| **Local** | Individual developer testing. | N/A |
| **Dev** | Shared integration testing. | Automatic on Merge to `main`. |
| **Staging** | Pre-production validation. | Manual approval on `v*` tag. |
| **Production** | Live user traffic. | Manual gate after Staging sign-off. |

## 2. Observability Standards (Logging/Monitoring/Alerts)

- **Structured Logging**: All applications MUST emit logs in **JSON format**
  with shared correlation IDs.
- **Metric Baseline**: Core services MUST expose `/metrics` for Prometheus
  (Latency, Traffic, Errors, Saturation).
- **Critical Alerts**:
  - **Error Rate**: > 1% over 5 minutes.
  - **Latency**: P95 > 500ms for core endpoints.
  - **Disk/Memory**: Use > 85%.

## 3. Deployment & Release Strategy

- **Strategy**: Default is **Rolling Update**. High-risk changes use **Blue-Green**.
- **Approval Gate**: Production deployments require a verified technical spec
  and QA sign-off.
- **Rollback**: Automatic rollback on health-check failure.

## 4. Continuity & Data Protection

- **Backup**: Database backups MUST occur daily (Automated).
- **Retention**: Backups are kept for 30 days.
- **RTO / RPO**:
  - **RPO (Recovery Point Objective)**: 24 hours (Daily backups). Maximum data loss.
  - **RTO (Recovery Time Objective)**: 4 hours. Maximum time to restore service.

## 5. Incident Response

- **Escalation**: Tech Lead -> Architect -> Stakeholders.
- **Post-Mortem**: Every P0/P1 incident requires a "Blameless Post-Mortem" and
  action items.
- **Error Tracking**: We use **Sentry** (or equivalent) for error tracking.
  DSNs must be configured via environment variables.

## 6. Configuration & Secrets

- **Configuration**: Use environment variables for runtime config; keep
  defaults documented in `.env.example`.
- **Secrets**: Never commit secrets to git. Use a Secret Manager (recommended)
  or CI-managed encrypted secrets.
- **Rotation**: Define a rotation policy for keys/tokens (at minimum for
  production).

Note: In the absence of a dedicated SRE team, define explicit expectations for
every feature team to ensure reliability and maintainability.

## 7. Cost Monitoring (Optional)

- **Tagging Policy**: Tag infrastructure resources with `Project`, `Owner`,
  `Env` for cost attribution.
- **Alerts**: Define budget alerts and escalation (monthly review recommended).

---

## Related Documentation

- [Pillar 1 (What): Product Requirement Documents (PRDs)](./docs/prd/README.md)
- [Pillar 2 (Vision): Architecture Blueprint (ARCHITECTURE.md)](./ARCHITECTURE.md)
- [Pillar 3 (Why): Architecture Decision Records (ADRs)](./docs/adr/README.md)
- [Pillar 4 (How): Architecture Reference Documents (ARDs)](./docs/ard/README.md)
