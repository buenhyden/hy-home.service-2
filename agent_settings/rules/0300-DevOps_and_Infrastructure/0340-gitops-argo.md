---
trigger: model_decision
glob: ["k8s/**"]
description: "GitOps standards: deterministic Argo CD app structure, environment overlays, drift control, and safe sync policies."
---
# 0500-GitOps-Argo-Deployment-Standards

## Activation
- [ ] Apply when Adding/updating Kubernetes manifests, Helm charts, Kustomize overlays, or Argo CD Applications..
- [ ] Apply when editing files matching: `k8s/**`.

## Rules
- **Role**: GitOps Platform Owner
- **Purpose**: Ensure deployments are fully Git-driven, repeatable, and drift-free with deterministic Argo CD practices.
- **Activates When**: Adding/updating Kubernetes manifests, Helm charts, Kustomize overlays, or Argo CD Applications.

---

### 1. Standards (Mandatory Compliance)

### 1.1 Prerequisites (Executable Contract)

- **[REQ-GITOPS-PREREQ-01] Git Is the Source of Truth**
  - Desired state MUST be stored in Git.
  - Manual “kubectl apply” changes MUST NOT be used as the delivery mechanism.

- **[REQ-GITOPS-OUT-01] Out of Scope**
  - This Rule does NOT define CI build pipelines.
  - This Rule defines GitOps deployment structure and drift control.

---

### 1.2 Structure & Overlays

- **[REQ-GITOPS-STR-01] Environment Overlays**
  - Environments MUST be represented via overlays (e.g., `dev/`, `stage/`, `prod/`).
  - Overlays MUST NOT duplicate entire bases; they MUST express deltas only.

- **[REQ-GITOPS-STR-02] Single Responsibility per App**
  - Each Argo CD Application MUST map to a single deployable unit.

- **[BAN-GITOPS-STR-01] Hidden Configuration**
  - Critical configuration MUST NOT live outside Git without explicit references.

---

### 1.3 Sync, Drift, and Safety

- **[REQ-GITOPS-SYNC-01] Deterministic Sync Policy**
  - Sync policy MUST be explicitly declared:
    - auto-sync on/off
    - prune behavior
    - self-heal behavior

- **[REQ-GITOPS-DRIFT-01] Drift Detection**
  - Drift detection MUST be enabled for managed workloads.
  - If drift is detected, the system MUST converge to Git state or block as policy dictates.

- **[BAN-GITOPS-SYNC-01] Uncontrolled Prune**
  - Prune MUST NOT be enabled for high-risk namespaces unless explicitly approved and validated.

---

### 1.4 Success & Failure Behavior

- **[REQ-GITOPS-SUCCESS-01] Success Criteria**
  - Deployments are valid ONLY if:
    - state is fully reproducible from Git
    - drift is detectable
    - sync policies are explicit

- **[REQ-GITOPS-FAIL-01] Failure Behavior**
  - If deployment requires manual steps not encoded in Git, the change MUST be rejected.

---

### 1.5 Reference-First

- **[REQ-GITOPS-REF-01] Canonical Examples**
  - Use canonical structures:
    - `gitops/_examples/app-of-apps.yaml`
    - `gitops/_examples/kustomize-overlay-structure.md`
    - `gitops/_examples/argocd-application.yaml`

---

### 2. Procedures (Phased Execution)

### Phase P1 — Define Base and Overlays

1) Create base manifests.
2) Create overlays with deltas only.

- **Outcome**: Overlay strategy is deterministic.

### Phase P2 — Define Argo Application

1) Map one app to one deployable unit.
2) Set explicit sync policy.

- **Outcome**: App is declarative and predictable.

### Phase P3 — Validate Drift Behavior

1) Introduce a controlled drift in a safe environment.
2) Confirm detection and convergence.

- **Outcome**: Drift control works as intended.

---

### 3. Examples

### Good Example — Delta-Only Overlays

**Input**

- Base defines deployment; overlay only changes replicas and environment variables.

**Expected Output**

- No duplicated base content; overlay remains minimal.

### Bad Example — Manual-only Change

**Input**

- “After deploy, run kubectl patch manually.”

**Rejected Because**

- Violates `[REQ-GITOPS-PREREQ-01]` and `[REQ-GITOPS-FAIL-01]`.

---

### 4. Validation Criteria (Final Checklist)

- [ ] Desired state is in Git; no manual-only steps. (`[REQ-GITOPS-PREREQ-01]`)
- [ ] Overlays are delta-only. (`[REQ-GITOPS-STR-01]`)
- [ ] Sync policies are explicit. (`[REQ-GITOPS-SYNC-01]`)
- [ ] Drift detection is enabled and verified. (`[REQ-GITOPS-DRIFT-01]`)

---

### See Also

- @0000-Rule-Writing-Standard-Master-v3.md
- examples/gitops/app-of-apps.yaml
- examples/gitops/kustomize-overlay-structure.md
- examples/gitops/argocd-application.yaml

## References
- None.
