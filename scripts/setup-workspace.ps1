<#
.SYNOPSIS
    Sets up the workspace by copying standard rules, skills, and workflows.
    Configures Git and cleans up temporary settings.
.DESCRIPTION
    This script initializes the workspace for the Init-Project-Template.
    It migrates settings from `agent_settings` to `.agent` and `.opencode`.
    It configures the git commit template.
    It removes the `agent_settings` directory upon success.
.PARAMETER PlanPath
    Optional path to an implementation plan (context).
#>

param (
    [string]$PlanPath = ""
)

# Paths
$SourceRoot = Join-Path $PSScriptRoot "..\agent_settings"
$AgentDestRoot = Join-Path $PSScriptRoot "..\.agent"
$OpencodeDestRoot = Join-Path $PSScriptRoot "..\.opencode"
$GitPath = Join-Path $PSScriptRoot "..\.git"

Write-Host "✨ Initializing Workspace..."

# 1. Migration Checking
if (-not (Test-Path $SourceRoot)) {
    Write-Warning "⚠️ Source directory '$SourceRoot' not found. Skipping migration."
} else {
    # Function to safe copy
    function Safe-Copy ($Src, $Dest, $Name) {
        if (Test-Path $Src) {
            if (-not (Test-Path $Dest)) {
                New-Item -ItemType Directory -Force -Path $Dest | Out-Null
            }
            Copy-Item -Path "$Src\*" -Destination $Dest -Recurse -Force
            Write-Host "✅ $Name migrated."
        }
    }

    # 1.1 Migrate Rules
    Safe-Copy "$SourceRoot\rules" "$AgentDestRoot\rules" "Rules"

    # 1.2 Migrate Workflows
    Safe-Copy "$SourceRoot\workflows" "$AgentDestRoot\workflows" "Workflows"

    # 1.3 Migrate Skills (Dual Copy)
    Safe-Copy "$SourceRoot\skills" "$AgentDestRoot\skills" "Skills (.agent)"
    Safe-Copy "$SourceRoot\skills" "$OpencodeDestRoot\skills" "Skills (.opencode)"
}

# 2. Git Configuration
if (Test-Path $GitPath) {
    Write-Host "⚙️ Configuring Git..."
    
    # Configure commit template if .gitmessage exists
    $GitMessagePath = Join-Path $PSScriptRoot "..\.gitmessage"
    if (Test-Path $GitMessagePath) {
        git config commit.template .gitmessage
        Write-Host "✅ Git commit template configured."
    }
} else {
    Write-Host "ℹ️ .git folder not found. Skipping Git configuration."
}

Write-Host "✅ Standard Rules applied successfully."

# 3. Cleanup
if (Test-Path $SourceRoot) {
    Remove-Item -LiteralPath $SourceRoot -Recurse -Force
    Write-Host "🧹 Cleanup complete (agent_settings removed)."
}

if ($PlanPath) {
    Write-Host "ℹ️  Plan Context: $PlanPath"
}

Write-Host "🚀 Workspace Ready."
