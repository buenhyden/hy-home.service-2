#!/bin/bash

# 1. agent_settings/rules -> .agent/rules
echo "Syncing agent_settings/rules to .agent/rules..."
mkdir -p .agent/rules
cp -r agent_settings/rules/* .agent/rules/
rm -f .agent/rules/.gitkeep

# 2. agent_settings/skills -> .agent/skills
echo "Syncing agent_settings/skills to .agent/skills..."
mkdir -p .agent/skills
cp -r agent_settings/skills/* .agent/skills/
rm -f .agent/skills/.gitkeep

# 3. agent_settings/workflows -> .agent/workflows
echo "Syncing agent_settings/workflows to .agent/workflows..."
mkdir -p .agent/workflows
cp -r agent_settings/workflows/* .agent/workflows/
rm -f .agent/workflows/.gitkeep

# 4. agent_settings/skills -> .opencode/skills
echo "Syncing agent_settings/skills to .opencode/skills..."
mkdir -p .opencode/skills
cp -r agent_settings/skills/* .opencode/skills/
rm -f .opencode/skills/.gitkeep

echo "Done."
