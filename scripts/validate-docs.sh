#!/bin/bash
set -euo pipefail

strict=0
changed_only=0

for arg in "$@"; do
  case "$arg" in
    --strict) strict=1 ;;
    --changed-only) changed_only=1 ;;
    *)
      echo "Unknown argument: $arg"
      echo "Usage: $0 [--strict] [--changed-only]"
      exit 2
      ;;
  esac
done

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root_dir"

python_bin="python3"
if ! command -v "$python_bin" >/dev/null 2>&1; then
  python_bin="python"
fi

args=()
if [ "$strict" -eq 1 ]; then args+=("--strict"); fi

if [ "$changed_only" -eq 1 ]; then
  "$python_bin" -B "scripts/validate_prd.py" "${args[@]}" "--changed-only"
  "$python_bin" -B "scripts/validate_spec.py" "${args[@]}" "--changed-only"
else
  prd_targets=()
  spec_targets=()

  if [ -d "docs/prd" ]; then
    while IFS= read -r -d '' file; do
      prd_targets+=("$file")
    done < <(find "docs/prd" -type f -name "*.md" ! -name "README.md" -print0)
  fi

  if [ -d "specs" ]; then
    while IFS= read -r -d '' file; do
      spec_targets+=("$file")
    done < <(find "specs" -type f -name "*.md" ! -name "README.md" ! -name "plan.md" -print0)
  fi

  if [ "${#prd_targets[@]}" -gt 0 ]; then
    "$python_bin" -B "scripts/validate_prd.py" "${args[@]}" "${prd_targets[@]}"
  fi
  if [ "${#spec_targets[@]}" -gt 0 ]; then
    "$python_bin" -B "scripts/validate_spec.py" "${args[@]}" "${spec_targets[@]}"
  fi
fi

echo "✅ Docs validation passed."
