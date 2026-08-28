#!/usr/bin/env python3
"""Initialize a project for the orchestrating-econometric-research skill.

Non-destructive by design: existing files are never overwritten.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from typing import Dict, List

SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = SKILL_ROOT / "templates"

TEMPLATE_MAP = {
    "research_config.yaml": "research_config.yaml",
    "PROJECT_STATE.yaml": "project_state.yaml",
    "RESEARCH_PROTOCOL.md": "research_protocol.md",
    "VARIABLE_REGISTRY.yaml": "variable_registry.yaml",
}

DIRECTORIES = [
    "research_system/registry",
    "research_system/staging",
    "research_system/specs/pending",
    "research_system/specs/running",
    "research_system/specs/completed",
    "research_system/specs/failed",
    "research_system/results_db",
    "research_system/reviews/staging_data_review",
    "research_system/reviews/iv_statistical_review",
    "research_system/reviews/iv_theory_review",
    "research_system/reviews/human_decisions",
    "research_system/discovery/literature",
    "research_system/discovery/datasets",
    "research_system/discovery/search_logs",
    "research_system/logs/agent_decisions",
    "research_system/logs/stata",
    "research_system/logs/python",
    "research_system/logs/web_discovery",
    "research_system/reports/iv_cards",
    "research_system/reports/data_discovery",
    "research_system/reports/mechanism_evidence",
    "research_system/reports/research_summary",
]


def initialize_project(root: Path | str, dry_run: bool = False) -> Dict[str, List[str]]:
    root = Path(root).expanduser().resolve()
    created: List[str] = []
    skipped: List[str] = []

    if not dry_run:
        root.mkdir(parents=True, exist_ok=True)

    for rel in DIRECTORIES:
        path = root / rel
        if path.exists():
            skipped.append(rel + "/")
        else:
            created.append(rel + "/")
            if not dry_run:
                path.mkdir(parents=True, exist_ok=True)

    for destination, template in TEMPLATE_MAP.items():
        dest = root / destination
        src = TEMPLATE_DIR / template
        if dest.exists():
            skipped.append(destination)
            continue
        created.append(destination)
        if not dry_run:
            shutil.copyfile(src, dest)

    return {"created": created, "skipped": skipped}


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize an econometric research project non-destructively.")
    parser.add_argument("root", nargs="?", default=".", help="Project root (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing files")
    args = parser.parse_args()

    result = initialize_project(args.root, dry_run=args.dry_run)
    print("Created:")
    for item in result["created"]:
        print(f"  + {item}")
    print("Skipped (already exists):")
    for item in result["skipped"]:
        print(f"  = {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
