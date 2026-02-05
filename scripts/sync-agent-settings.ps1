# 1. agent_settings/rules -> .agent/rules
Write-Host "Syncing agent_settings/rules to .agent/rules..."
New-Item -ItemType Directory -Force -Path .agent/rules | Out-Null
Get-ChildItem -Force ".agent/rules" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -Path "agent_settings/rules/*" -Destination ".agent/rules" -Recurse -Force
Remove-Item -Path ".agent/rules/.gitkeep" -ErrorAction SilentlyContinue

# 2. agent_settings/skills -> .agent/skills
Write-Host "Syncing agent_settings/skills to .agent/skills..."
New-Item -ItemType Directory -Force -Path .agent/skills | Out-Null
Get-ChildItem -Force ".agent/skills" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -Path "agent_settings/skills/*" -Destination ".agent/skills" -Recurse -Force
Remove-Item -Path ".agent/skills/.gitkeep" -ErrorAction SilentlyContinue

# 3. agent_settings/workflows -> .agent/workflows
Write-Host "Syncing agent_settings/workflows to .agent/workflows..."
New-Item -ItemType Directory -Force -Path .agent/workflows | Out-Null
Get-ChildItem -Force ".agent/workflows" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -Path "agent_settings/workflows/*" -Destination ".agent/workflows" -Recurse -Force
Remove-Item -Path ".agent/workflows/.gitkeep" -ErrorAction SilentlyContinue

# 4. agent_settings/skills -> .opencode/skills
Write-Host "Syncing agent_settings/skills to .opencode/skills..."
New-Item -ItemType Directory -Force -Path .opencode/skills | Out-Null
Get-ChildItem -Force ".opencode/skills" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item -Path "agent_settings/skills/*" -Destination ".opencode/skills" -Recurse -Force
Remove-Item -Path ".opencode/skills/.gitkeep" -ErrorAction SilentlyContinue

Write-Host "Done."
