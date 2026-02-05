#!/bin/bash
# Bootstraps a new project from the Init-Project-Template.

PROJECT_NAME="$1"
DESCRIPTION="$2"

# 1. Gather Info
if [ -z "$PROJECT_NAME" ]; then
    read -r -p "Enter New Project Name (e.g., my-awesome-app): " PROJECT_NAME
fi
if [ -z "$DESCRIPTION" ]; then
    read -r -p "Enter Project Description: " DESCRIPTION
fi

echo "🚀 Bootstrapping '$PROJECT_NAME'..."

SCRIPT_DIR="$(dirname "$0")"
ROOT_DIR="$SCRIPT_DIR/.."
README_PATH="$ROOT_DIR/README.md"
PACKAGE_JSON_PATH="$ROOT_DIR/package.json"

# 2. Update README.md
if [ -f "$README_PATH" ]; then
    sed -i "s/# Init-Project-Template/# $PROJECT_NAME/" "$README_PATH"
    # Note: Simple sed line replacement for description might be brittle, assuming top lines
    sed -i "3s/^.*$/$DESCRIPTION/" "$README_PATH"
    echo "✅ Updated README.md"
fi

# 3. Update package.json (using sed for basics to avoid jq dependency requirement)
if [ -f "$PACKAGE_JSON_PATH" ]; then
    sed -i "s/\"name\": \".*\"/\"name\": \"$PROJECT_NAME\"/" "$PACKAGE_JSON_PATH"
    sed -i "s/\"description\": \".*\"/\"description\": \"$DESCRIPTION\"/" "$PACKAGE_JSON_PATH"
    sed -i "s/\"version\": \".*\"/\"version\": \"0.1.0\"/" "$PACKAGE_JSON_PATH"
    echo "✅ Updated package.json"
fi

# 3.5. Global Replacement of "Init-Project-Template"
echo "🔄 Updating 'Init-Project-Template' to '$PROJECT_NAME' in project files..."
find "$ROOT_DIR" -type f \( -name "*.md" -o -name "*.yml" -o -name "*.json" \) \
    -not -path "*/node_modules/*" \
    -not -path "*/.git/*" \
    -not -path "*/.agent/*" \
    -not -path "*/agent_settings/*" \
    -not -path "*/scripts/*" \
    -exec grep -l "Init-Project-Template" {} + | while read -r file; do
        sed -i "s/Init-Project-Template/$PROJECT_NAME/g" "$file"
        echo "  Use: Updated $(basename "$file")"
done

# 4. Run Workspace Setup
echo "⚙️  Running Workspace Setup..."
"$SCRIPT_DIR/setup-workspace.sh"

echo "✨ Project '$PROJECT_NAME' is ready!"
echo "👉 Next Step: Create your first plan in 'specs/'"
