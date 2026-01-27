# Init-Project-Template Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Documentation**: Complete reorganization of the `docs/` folder with 10 new core guides ([#Task-Docs](file:///d:/hy-home.SourceCode/Init-Project-Template/docs/README.md)).
- **GitHub**: Added `release.yml` and `labeler.yml` for automated repository management.
- **Root Docs**: Updated `CONTRIBUTING.md` and `LICENSE` files.

## [1.0.0] - 2026-01-26

### Major Release: Polyglot Agentic Template

This release marks the transition from a prototype to a fully standardized, production-ready "Golden Master" template.

### Added

- **Polyglot Orchestration**: Added `Makefile` and Universal Scripts (`bootstrap-new-project`) to support Python, Go, Rust, and Node.js equally.
- **Workflow/Guide Separation**: Migrated 17 "How-To" guides to `docs/guides/` and consolidated 49 workflow files.
- **Bootstrapping**: New `npm run init` (or `make init`) command to automate project naming and git reset.
- **Specs Directory**: Added `specs/` as the official entry point for Spec-Driven Development (SDD).

### Changed

- **Rule Consolidation**: Compressed 200+ fragmented rules into 164 high-fidelity standards with 100% skeleton compliance.
- **Governance**: Updated `ARCHITECTURE.md` to reflect the language-agnostic philosophy.
- **Versioning**: Bumped to v1.0.0 to signal API stability for the Rule System.

## [0.2.0] - 2026-01-20

### Added

- **Docs**: New `AGENTS.md` operational manual for agent configuration.
- **Docs**: Comprehensive "How to Use" release instructions in `README.md`.
- **Feature**: Tech Stack Agnostic support with "Choose Your Tech Stack" guide.

### Changed

- **Structure**: Explicitly defined `.agent` as the source of truth for agent settings.
- **Docs**: Updated `README.md` to clearly identify the project as a GitHub Template.

## [0.1.0] - 2026-01-13

### Added

- Initial project structure with `agent/rules` and `agent/workflows`.
- Comprehensive `.github` templates (Issue, PR, Security, etc.).
- AI-specific configuration files (`.cursorrules`, `AGENTS.md`, etc.).
- Infrastructure templates for common services.

### Changed

- Refined repository metadata for better template usability.
- Updated `LICENSE` to MIT for open-source friendliness.
- Optimized linting rules for Markdown and JavaScript.
