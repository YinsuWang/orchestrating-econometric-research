from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_skill_has_valid_frontmatter_and_core_contract():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---\n")
    assert "name: orchestrating-econometric-research" in text
    assert "description: Use when" in text
    for phrase in [
        "preserve every attempted specification",
        "Human Gate",
        "PROJECT_STATE.yaml",
        "research_config.yaml",
    ]:
        assert phrase in text


def test_required_references_exist():
    required = [
        "research-workflow.md",
        "project-contract.md",
        "data-discovery.md",
        "iv-protocol.md",
        "econometric-chain.md",
        "specification-search.md",
        "stata-protocol.md",
        "human-gates.md",
        "reporting.md",
    ]
    for name in required:
        assert (ROOT / "references" / name).is_file(), name


def test_required_templates_exist():
    required = [
        "research_config.yaml",
        "project_state.yaml",
        "research_protocol.md",
        "variable_registry.yaml",
        "iv_candidate.yaml",
        "iv_card.md",
        "data_review.md",
        "human_decision.yaml",
        "spec_record.json",
    ]
    for name in required:
        assert (ROOT / "templates" / name).is_file(), name
