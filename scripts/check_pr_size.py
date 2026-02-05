#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
import subprocess
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class FileStat:
    path: str
    added: int
    deleted: int


DEFAULT_EXCLUDE_GLOBS = [
    "docs/**",
    "tests/**",
    "**/*.md",
    "**/*.snap",
    "**/*.lock",
    "**/*.baseline",
    "**/*.png",
    "**/*.jpg",
    "**/*.jpeg",
    "**/*.gif",
    "**/*.svg",
]


def _run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        check=False,
        capture_output=True,
        text=True,
    )


def _matches_any(path: str, globs: list[str]) -> bool:
    normalized = path.replace("\\", "/")
    return any(fnmatch.fnmatch(normalized, g) for g in globs)


def _parse_numstat(output: str) -> list[FileStat]:
    stats: list[FileStat] = []
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        added_s, deleted_s, path = parts[0], parts[1], parts[2]
        if added_s == "-" or deleted_s == "-":
            # Binary file; ignore for LOC limits.
            continue
        try:
            added = int(added_s)
            deleted = int(deleted_s)
        except ValueError:
            continue
        stats.append(FileStat(path=path, added=added, deleted=deleted))
    return stats


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Check approximate PR size by summing added+deleted lines."
    )
    parser.add_argument(
        "--max-loc",
        type=int,
        default=500,
        help="Maximum allowed LOC change (added+deleted) before failing.",
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Check staged changes (git diff --cached).",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Exclude glob (can be repeated). Defaults exclude docs/tests/media/locks.",
    )
    args = parser.parse_args(argv)

    exclude_globs = DEFAULT_EXCLUDE_GLOBS + list(args.exclude)

    diff_args = ["diff", "--numstat"]
    if args.staged:
        diff_args.append("--cached")

    result = _run_git(diff_args)
    if result.returncode != 0:
        print(result.stderr.strip() or "git diff failed", file=sys.stderr)
        return 2

    stats = [s for s in _parse_numstat(result.stdout) if not _matches_any(s.path, exclude_globs)]
    total = sum(s.added + s.deleted for s in stats)

    if total <= args.max_loc:
        return 0

    print(
        f"PR size check failed: {total} LOC changed (added+deleted) > {args.max_loc}.",
        file=sys.stderr,
    )
    for s in sorted(stats, key=lambda x: (x.added + x.deleted), reverse=True)[:10]:
        print(f"- {s.path}: +{s.added} -{s.deleted}", file=sys.stderr)
    print(
        "Tip: split into smaller PRs or exclude docs/tests-only changes (see --exclude).",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
