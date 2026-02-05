# Development Process / Collaboration Checklist

This template operationalizes development process and collaboration agreements
through documented standards and repository conventions.

## Checklist Items → Where to Define

| Item | Required | Where to define / enforce |
| --- | --- | --- |
| Development Process (Scrum/Kanban/Hybrid) | Must | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 2 |
| Sprint Operation | Optional | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 2 |
| Issue Management tool + required fields | Must | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 5 + `.github/ISSUE_TEMPLATE/*` |
| Branch Strategy | Must | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 6 + [`docs/manuals/06-development-guide.md`][dev-guide] |
| Merge Policy / Protected Branch | Must | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 6 + GitHub branch protection settings |
| Code Review Rules | Must | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 4 + `.github/PULL_REQUEST_TEMPLATE.md` + [`.agent/rules/**/0012-code-review-standard.md`][code-review] |
| PR Size Rule | Optional | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 4 + [`.agent/rules/0200-Workflows/0200-workflow-standard.md`][workflow] |
| Definition of Done (DoD) | Must | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 4 + [`docs/manuals/06-development-guide.md`][dev-guide] |
| Definition of Ready (DoR) | Optional | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 4 + issue templates |
| Communication Channel + SLA | Must | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 1 |
| Decision Making Structure | Must | [`docs/manuals/11-collaboration-guide.md`][collab-guide] Section 3 |

## Notes

- Branch protection (no direct push to `main`, required approvals/checks) is
  configured in GitHub repository settings, not in code, but should be agreed
  and documented at kickoff.
- CODEOWNERS can enforce review requirements for sensitive areas: `.github/CODEOWNERS`

[collab-guide]: ../manuals/11-collaboration-guide.md
[dev-guide]: ../manuals/06-development-guide.md
[code-review]: ../../.agent/rules/0000-Agents/0012-code-review-standard.md
[workflow]: ../../.agent/rules/0200-Workflows/0200-workflow-standard.md
