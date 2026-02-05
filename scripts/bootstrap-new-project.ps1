<#
.SYNOPSIS
    Bootstraps a new project from the Init-Project-Template.
.DESCRIPTION
    This script automates the "Clone -> Own" process:
    1. Prompts for Project Name and Description.
    2. Updates README.md and package.json.
    3. (Optional) Resets git history.
    4. Initializes the workspace rules.
#>

param (
    [string]$ProjectName = "",
    [string]$Description = ""
)

# 1. Gather Info
if ([string]::IsNullOrWhiteSpace($ProjectName)) {
    $ProjectName = Read-Host "Enter New Project Name (e.g., my-awesome-app)"
}
if ([string]::IsNullOrWhiteSpace($Description)) {
    $Description = Read-Host "Enter Project Description"
}

Write-Host "🚀 Bootstrapping '$ProjectName'..."

# 2. Update README.md
$ReadmePath = Join-Path $PSScriptRoot "..\README.md"
if (Test-Path $ReadmePath) {
    $Content = Get-Content $ReadmePath -Raw
    # Replace Title
    $Content = $Content -replace "# Init-Project-Template", "# $ProjectName"
    # Replace Description
    $Content = $Content -replace "A standardized, AI-optimized project template.*", "$Description"
    Set-Content -Path $ReadmePath -Value $Content
    Write-Host "✅ Updated README.md"
}

# 3. Update package.json
$PackageJsonPath = Join-Path $PSScriptRoot "..\package.json"
if (Test-Path $PackageJsonPath) {
    try {
        $Json = Get-Content $PackageJsonPath -Raw | ConvertFrom-Json
        $Json.name = $ProjectName
        $Json.description = $Description
        $Json.version = "0.1.0"
        $Json | ConvertTo-Json -Depth 10 | Set-Content $PackageJsonPath
        Write-Host "✅ Updated package.json"
    } catch {
        Write-Warning "Failed to update package.json: $_"
    }
}

# 3.5. Global Replacement of "Init-Project-Template"
Write-Host "🔄 Updating 'Init-Project-Template' to '$ProjectName' in project files..."
$TargetExtensions = @("*.md", "*.yml", "*.yaml", "*.json")
$ExcludeFolders = @("node_modules", ".git", ".agent", "agent_settings", "scripts")
$RootPath = Resolve-Path (Join-Path $PSScriptRoot "..")

Get-ChildItem -Path $RootPath -Recurse -Include $TargetExtensions | Where-Object {
    $Item = $_
    $IsExcluded = $false
    foreach ($Exclude in $ExcludeFolders) {
        if ($Item.FullName -match [regex]::Escape([System.IO.Path]::DirectorySeparatorChar + $Exclude + [System.IO.Path]::DirectorySeparatorChar)) {
            $IsExcluded = $true
            break
        }
    }
    return -not $IsExcluded
} | ForEach-Object {
    try {
        $Content = Get-Content $_.FullName -Raw
        if ($Content -match "Init-Project-Template") {
            $Content = $Content -replace "Init-Project-Template", $ProjectName
            Set-Content -Path $_.FullName -Value $Content
            Write-Host "  Use: Updated $($_.Name)"
        }
    } catch {
        Write-Warning "Could not process file: $($_.Name)"
    }
}

# 4. Run Workspace Setup
Write-Host "⚙️  Running Workspace Setup..."
& "$PSScriptRoot\setup-workspace.ps1"

Write-Host "✨ Project '$ProjectName' is ready!"
Write-Host "👉 Next Step: Create your first plan in 'specs/'"
