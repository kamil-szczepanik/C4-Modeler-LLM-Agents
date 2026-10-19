import importlib.util
from pathlib import Path

import pytest

from masc4 import prompts as P
from masc4.conditions import build_team, load_conditions

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs/conditions_v2.yaml"

EXPECTED_TEAMS = {
    "C0_baseline": ["product_owner", "software_architect", "devops", "security"],
    "C1_no_product_owner": ["software_architect", "devops", "security"],
    "C2_no_architect": ["product_owner", "devops", "security"],
    "C3_no_devops": ["product_owner", "software_architect", "security"],
    "C4_no_security": ["product_owner", "software_architect", "devops"],
    "C5_single_architect": ["software_architect"],
    "C6_four_architects": ["software_architect"] * 4,
    "C7_architect_first": ["software_architect", "devops", "security", "product_owner"],
    "C9_security_first": ["security", "product_owner", "software_architect", "devops"],
    "C10_generic_team": ["generic_engineer"] * 4,
    "C12_glossary_memory": ["product_owner", "software_architect", "devops", "security"],
}


def test_every_condition_has_the_intended_team_and_memory():
    settings, conditions = load_conditions(CONFIG)
    assert settings.model == "gemini-3.5-flash-lite" and settings.rounds == 2
    assert {c.id: c.team_keys for c in conditions} == EXPECTED_TEAMS
    assert {c.id for c in conditions if c.memory == "glossary"} == {"C12_glossary_memory"}
    for c in conditions:
        assert all(a.persona.strip() for a in c.team), f"{c.id} has an agent without persona text"


def test_order_conditions_are_rotations_of_the_baseline():
    _, conditions = load_conditions(CONFIG)
    base = {c.id: c.team_keys for c in conditions}["C0_baseline"]
    rotations = [base[i:] + base[:i] for i in range(len(base))]
    for cid in ("C7_architect_first", "C9_security_first"):
        assert {c.id: c.team_keys for c in conditions}[cid] in rotations


def test_duplicate_roles_get_distinct_display_names():
    team = build_team(["software_architect", "software_architect", "product_owner"])
    assert [a.display_name for a in team] == ["Software Architect #1", "Software Architect #2", "Product Owner"]
    assert team[0].role_name == "Software Architect"


def test_unknown_persona_and_unknown_field_are_rejected(tmp_path):
    with pytest.raises(ValueError):
        build_team(["domain_expert"])
    bad = tmp_path / "bad.yaml"
    bad.write_text("generation: {model: m, temperature: 0.5, rounds: 2}\nconditions:\n"
                   "  - {id: X, studies: [a], description: d, team: [product_owner], memory: none, persona_type: generic}\n")
    with pytest.raises(ValueError):
        load_conditions(bad)


def test_v1_prompt_texts_are_copied_verbatim():
    spec = importlib.util.spec_from_file_location("v1_prompts", ROOT / "src/c4modeler/prompts.py")
    v1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v1)
    same = ["PRODUCT_OWNER_PERSONA", "DEVOPS_SPECIALIST_PERSONA", "SECURITY_SPECIALIST_PERSONA",
            "GENERIC_SOFTWARE_ENGINEER_PERSONA", "YAML_PERSONA_PROMPT", "YAML_HUMAN_MESSAGE_PROMPT",
            "CONTEXT_YAML_TEMPLATE", "CONTAINER_YAML_TEMPLATE", "COMPONENT_YAML_TEMPLATE",
            "PLANTUML_PERSONA_PROMPT", "PLANTUML_HUMAN_MESSAGE_PROMPT", "PLANTUML_SYNTAX_GUIDE",
            "GLOSSARY_AGENT_PERSONA"]
    for name in same:
        assert getattr(P, name) == getattr(v1, name), name
    assert P.WRITER_TASK_PROMPT == v1.REPORT_GENERATOR_SYSTEM_PROMPT


def test_v2_turn_prompt_makes_agents_engage_with_earlier_contributions():
    prompt = P.TURN_SYSTEM_PROMPT
    assert "{persona_short}" in prompt and "{level}" in prompt and "{persona}" in prompt
    assert "support, refine or challenge" in prompt and "Maximum 150 words" in prompt
    assert "DO NOT repeat, summarize, or acknowledge" not in prompt      # the v1 rule that blocked dialogue


def test_turn_v1_and_writer_prompts_match_v1_agents_source():
    source = (ROOT / "src/c4modeler/agents.py").read_text(encoding="utf-8")
    for prompt in (P.TURN_SYSTEM_PROMPT_V1, P.WRITER_SYSTEM_PROMPT):
        for line in prompt.split("\n"):
            if line.strip():
                assert line.replace("'", "\\'") in source or line in source, line
