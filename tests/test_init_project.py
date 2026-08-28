from pathlib import Path
import importlib.util

SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "init_project.py"


def load_module():
    spec = importlib.util.spec_from_file_location("init_project", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_initializer_creates_contract_without_overwriting(tmp_path):
    module = load_module()
    existing = tmp_path / "research_config.yaml"
    existing.write_text("existing: true\n", encoding="utf-8")

    result = module.initialize_project(tmp_path)

    assert existing.read_text(encoding="utf-8") == "existing: true\n"
    assert (tmp_path / "PROJECT_STATE.yaml").exists()
    assert (tmp_path / "RESEARCH_PROTOCOL.md").exists()
    assert (tmp_path / "research_system" / "registry").is_dir()
    assert (tmp_path / "research_system" / "results_db").is_dir()
    assert "research_config.yaml" in result["skipped"]


def test_initializer_is_idempotent(tmp_path):
    module = load_module()
    first = module.initialize_project(tmp_path)
    second = module.initialize_project(tmp_path)

    assert first["created"]
    assert not second["created"]
    assert second["skipped"]
