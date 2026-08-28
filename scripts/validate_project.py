#!/usr/bin/env python3
"""Validate that an econometric research project has the required contract files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List

REQUIRED_FILES = [
    "research_config.yaml",
    "PROJECT_STATE.yaml",
    "RESEARCH_PROTOCOL.md",
    "VARIABLE_REGISTRY.yaml",
]

REQUIRED_DIRS = [
    "research_system/registry",
    "research_system/staging",
    "research_system/results_db",
    "research_system/reviews/human_decisions",
    "research_system/logs/agent_decisions",
]

CONFIG_MARKERS = [
    "preserve_all_results:",
    "stop_on_significance:",
    "staging_only:",
    "require_human_candidate_approval:",
    "require_human_final_approval:",
]


def validate_project(root: Path | str) -> Dict[str, object]:
    root = Path(root).expanduser().resolve()
    missing_files: List[str] = [p for p in REQUIRED_FILES if not (root / p).is_file()]
    missing_dirs: List[str] = [p for p in REQUIRED_DIRS if not (root / p).is_dir()]
    config_missing_markers: List[str] = []

    config = root / "research_config.yaml"
    if config.is_file():
        text = config.read_text(encoding="utf-8")
        config_missing_markers = [m for m in CONFIG_MARKERS if m not in text]

    ok = not missing_files and not missing_dirs and not config_missing_markers
    return {
        "ok": ok,
        "missing_files": missing_files,
        "missing_dirs": missing_dirs,
        "config_missing_markers": config_missing_markers,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate econometric research project contract.")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    report = validate_project(args.root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
