# Init-Project-Template Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-02-05

### Added

- **Documentation**: Complete reorganization of the `docs/` folder with 10 new
  core guides ([#Task-Docs](docs/README.md)).
- **GitHub**: Added `release.yml` and `labeler.yml` for automated repository
  management.
- **Root Docs**: Updated `CONTRIBUTING.md` and `LICENSE` files.

### Fixed

- **Git**: Workspace setup now configures `commit.template` using an absolute path
  to `.gitmessage`, so commits work from any subdirectory.
- **Docs**: Fixed broken internal links and updated installation verification
  commands to match the template defaults.

### Changed

- **Tooling**: `npm test` now runs the template's unit tests by default.

## [1.0.0] - 2026-01-26

### Major Release: Polyglot Agentic Template

This release marks the transition from a prototype to a fully standardized,
production-ready "Golden Master" template.

### Added Version 1.0.0

- **Polyglot Orchestration**: Added `Makefile` and Universal Scripts
  (`bootstrap-new-project`) to support Python, Go, Rust, and Node.js equally.
- **Workflow/Guide Separation**: Migrated 17 "How-To" guides to `docs/guides/`
  and consolidated 49 workflow files.
- **Bootstrapping**: New `npm run init` (or `make init`) command to automate
  project naming and git reset.
- **Specs Directory**: Added `specs/` as the official entry point for
  Spec-Driven Development (SDD).

### Changed Version 1.0.0

- **Rule Consolidation**: Compressed 200+ fragmented rules into 164
  high-fidelity standards with 100% skeleton compliance.
- **Governance**: Updated `ARCHITECTURE.md` to reflect the language-agnostic
  philosophy.
- **Versioning**: Bumped to v1.0.0 to signal API stability for the Rule System.

## [0.2.0] - 2026-01-20

### Added Version 0.2.0

- **Docs**: New `AGENTS.md` operational manual for agent configuration.
- **Docs**: Comprehensive "How to Use" release instructions in `README.md`.
- **Feature**: Tech Stack Agnostic support with "Choose Your Tech Stack" guide.

### Changed Version 0.2.0

- **Structure**: Explicitly defined `.agent` as the source of truth for agent
  settings.
- **Docs**: Updated `README.md` to clearly identify the project as a GitHub
  Template.

## [0.1.0] - 2026-01-13

### Added Version 0.1.0

- Initial project structure with `agent/rules` and `agent/workflows`.
- Comprehensive `.github` templates (Issue, PR, Security, etc.).
- AI-specific configuration files (`.cursorrules`, `AGENTS.md`, etc.).
- Infrastructure templates for common services.

### Changed Version 0.1.0

- Refined repository metadata for better template usability.
- Updated `LICENSE` to MIT for open-source friendliness.
- Optimized linting rules for Markdown and JavaScript.
