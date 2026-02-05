# Init-Project-Template Makefile
# Orchestration for Unix/Linux/Mac users

.PHONY: init setup help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

init: ## Bootstrap a new project (Rename, Git Reset)
	@./scripts/bootstrap-new-project.sh

setup: ## Initialize workspace, sync agent rules, and cleanup temporary settings
	@./scripts/setup-workspace.sh
