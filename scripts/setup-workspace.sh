#!/bin/bash
# Sets up the workspace by copying standard rules, skills, and workflows.
# Configures Git and cleans up temporary settings.

# Paths
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_ROOT="$ROOT_DIR/agent_settings"
AGENT_DEST_ROOT="$ROOT_DIR/.agent"
OPENCODE_DEST_ROOT="$ROOT_DIR/.opencode"
GIT_PATH="$ROOT_DIR/.git"

echo "✨ Initializing Workspace..."

# 1. Migration Checking
if [ ! -d "$SOURCE_ROOT" ]; then
    echo "⚠️ Source directory '$SOURCE_ROOT' not found. Skipping migration."
else
    # Function to safe copy
    safe_copy() {
        local src="$1"
        local dest="$2"
        local name="$3"

        if [ -d "$src" ]; then
            if [ ! -d "$dest" ]; then
                mkdir -p "$dest"
            fi
            # Recursive copy contents of src to dest
            cp -r "$src/"* "$dest/"
            echo "✅ $name migrated."
        fi
    }

    # 1.1 Migrate Rules
    safe_copy "$SOURCE_ROOT/rules" "$AGENT_DEST_ROOT/rules" "Rules"

    # 1.2 Migrate Workflows
    safe_copy "$SOURCE_ROOT/workflows" "$AGENT_DEST_ROOT/workflows" "Workflows"

    # 1.3 Migrate Skills (Dual Copy)
    safe_copy "$SOURCE_ROOT/skills" "$AGENT_DEST_ROOT/skills" "Skills (.agent)"
    safe_copy "$SOURCE_ROOT/skills" "$OPENCODE_DEST_ROOT/skills" "Skills (.opencode)"
fi

# 2. Git Configuration
if [ -e "$GIT_PATH" ]; then
    echo "⚙️ Configuring Git..."

    # Configure commit template if .gitmessage exists
    GIT_MESSAGE_PATH="$ROOT_DIR/.gitmessage"
    if [ -f "$GIT_MESSAGE_PATH" ]; then
        git -C "$ROOT_DIR" config --local commit.template "$GIT_MESSAGE_PATH"
        echo "✅ Git commit template configured."
    fi
else
    echo "ℹ️ .git folder not found. Skipping Git configuration."
fi

echo "✅ Standard Rules applied successfully."

# 3. Cleanup
if [ -d "$SOURCE_ROOT" ]; then
    rm -rf "$SOURCE_ROOT"
    echo "🧹 Cleanup complete (agent_settings removed)."
fi

PLAN_PATH="$1"
if [ -n "$PLAN_PATH" ]; then
    echo "ℹ️  Plan Context: $PLAN_PATH"
fi

echo "🚀 Workspace Ready."
