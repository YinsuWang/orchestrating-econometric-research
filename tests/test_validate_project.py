from pathlib import Path
import importlib.util

SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "validate_project.py"


def load_module():
    spec = importlib.util.spec_from_file_location("validate_project", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_validator_reports_missing_contract(tmp_path):
    module = load_module()
    report = module.validate_project(tmp_path)
    assert report["ok"] is False
    assert "research_config.yaml" in report["missing_files"]


def test_validator_accepts_initialized_project(tmp_path):
    init_spec = importlib.util.spec_from_file_location(
        "init_project", SKILL_ROOT / "scripts" / "init_project.py"
    )
    init_module = importlib.util.module_from_spec(init_spec)
    init_spec.loader.exec_module(init_module)
    init_module.initialize_project(tmp_path)

    module = load_module()
    report = module.validate_project(tmp_path)
    assert report["ok"] is True
    assert report["missing_files"] == []
