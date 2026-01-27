---
trigger: model_decision
glob: ["**/*"]
description: "Web Performance Standards: Enforces Core Web Vitals (LCP, FID, CLS), asset optimization, and efficient caching strategies."
---

# Web Performance Standards

- **Role**: Performance Optimization Engineer
- **Purpose**: Define standards for optimizing web application speed, responsiveness, and visual stability.
- **Activates When**: Developing frontend components, configuring assets, or optimizing rendering paths.

**Trigger**: model_decision — Activate during performance audit or frontend development phases.

## 1. Standards

### Principles

- **[REQ-PERF-01] Vitals-First Optimization**
  - All optimizations MUST prioritize Core Web Vitals (LCP < 2.5s, FID < 100ms, CLS < 0.1).
- **[REQ-PERF-02] Asset Efficiency**
  - Images and scripts MUST be optimized for minimum payload size and delivery speed.
- **[REQ-PERF-03] Resilience in Loading**
  - Applications MUST remain functional during progressive loading of assets.

### Core Metrics (Target)

| Metric | Healthy | Needs Improvement | Poor |
| --- | --- | --- | --- |
| LCP (Largest Contentful Paint) | < 2.5s | 2.5s - 4.0s | > 4.0s |
| FID (First Input Delay) | < 100ms | 100ms - 300ms | > 300ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1 - 0.25 | > 0.25 |

### Must

- **[REQ-PERF-04] Responsive Images**
  - Images MUST use `srcset`, proper dimensions, and modern formats (WebP/AVIF).
- **[REQ-PERF-05] Code Splitting**
  - Large JavaScript bundles MUST be split using dynamic imports and lazy loading.
- **[REQ-PERF-06] Critical Path Optimization**
  - Critical CSS MUST be inlined or prioritized to minimize the critical rendering path.

### Must Not

- **[BAN-PERF-01] Render-Blocking Resources**
  - Non-critical scripts MUST NOT be loaded in a render-blocking manner (use `defer` or `async`).
- **[BAN-PERF-02] Layout Thrashing**
  - Content MUST NOT be inserted above existing content to prevent layout shifts.

### Failure Handling

- **Stop Condition**: Stop deployment if a Lighthouse performance score falls below the established budget.

## 2. Procedures

- **[PROC-PERF-01] Performance Audit**
  - IF a new page is created THEN MUST run a Lighthouse audit and document the scores.
- **[PROC-PERF-02] Asset Optimization**
  - IF adding media THEN MUST compress and convert to efficient formats.

## 3. Examples

### Preload Critical Resource

` <link rel="preload" href="vital-font.woff2" as="font" type="font/woff2" crossorigin> `

## 4. Validation Criteria

- **[VAL-PERF-01] Lighthouse Scores**
  - [ ] Performance score > 90 across mobile and desktop.
- **[VAL-PERF-02] Asset Payload**
  - [ ] Individual JS chunks do not exceed 100KB (gzipped).
- **[VAL-PERF-03] CLS Evidence**
  - [ ] No visual layout shifts are observable during page load.
