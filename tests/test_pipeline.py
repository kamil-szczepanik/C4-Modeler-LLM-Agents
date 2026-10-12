import json
from pathlib import Path

import pytest

from fake_responses import make_fake_llm
from masc4 import prompts as P
from masc4.conditions import load_conditions
from masc4.pipeline import C4Generator, PipelineError, RunRecord, save_record

ROOT = Path(__file__).resolve().parents[1]
BRIEF = "title: Test System\ndescription: A system used in tests.\n"


def conditions():
    _, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    return {c.id: c for c in conds}


def generate(cid, **fake_kwargs):
    llm = make_fake_llm(**fake_kwargs)
    record = C4Generator(llm, conditions()[cid], temperature=0.5, rounds=2).generate(BRIEF)
    return record, llm


def openings(llm, kind):
    return [c for c in llm.calls if c["purpose"].startswith(kind)]


def test_baseline_produces_all_levels_with_round_robin_turns():
    record, llm = generate("C0_baseline")
    model = record.c4_model
    assert set(model["components"]) == {"Web App", "Database"}
    for level in [model["context"], model["containers"], *model["components"].values()]:
        assert level["analysis"] and level["yaml_definition"] and level["diagram"].startswith("@startuml")
    assert not model["containers"]["yaml_definition"].startswith("```")  # fences stripped
    team = [a.display_name for a in conditions()["C0_baseline"].team]
    assert len(record.transcript) == 2 * 4 * (2 + 2)          # rounds x agents x (L1, L2, two containers)
    first_level = [t.speaker for t in record.transcript if t.scope == "context"]
    assert first_level == team + team                          # speaking order, two rounds
    assert not openings(llm, "glossary")


def test_turn_prompt_carries_role_and_persona_and_full_history():
    record, llm = generate("C10_generic_team")
    turns = [c for c in llm.calls if c["purpose"].startswith("turn|context")]
    assert all(P.GENERIC_SOFTWARE_ENGINEER_PERSONA in c["system"] for c in turns)
    assert "You are Software Engineer contributing" in turns[0]["system"]
    last = turns[-1]["user"]
    assert last.count("[Software Engineer #") == 7            # all earlier turns are visible
    assert "**System Brief:**" in last


def test_component_level_gets_parent_container_definition():
    _, llm = generate("C0_baseline")
    opening = next(c for c in llm.calls if c["purpose"].startswith("turn|component 'Web App'"))["user"]
    assert "- Parent container: Web App (React): User interface." in opening
    assert "Web App -> Database" in opening
    yaml_ctx = next(c for c in llm.calls if c["purpose"].startswith("yaml|component 'Web App'"))["user"]
    assert "Parent container: Web App" in yaml_ctx and "Containers defined: Web App, Database" in yaml_ctx


def test_glossary_memory_is_built_after_L1_and_L2_and_injected_into_L2_and_L3():
    record, llm = generate("C12_glossary_memory")
    assert [c["purpose"] for c in openings(llm, "glossary")] == ["glossary|context|attempt1",
                                                                  "glossary|container|attempt1"]
    assert set(record.glossary_snapshots) == {"after_L1", "after_L2"}
    header = P.GLOSSARY_INJECTION_HEADER
    for c in llm.calls:
        kind, scope = c["purpose"].split("|")[:2]
        if kind in ("turn", "yaml"):
            assert (header in c["user"]) == (scope != "context"), c["purpose"]


def test_baseline_never_sees_the_glossary():
    _, llm = generate("C0_baseline")
    assert all(P.GLOSSARY_INJECTION_HEADER not in c["user"] for c in llm.calls)


def test_single_agent_condition():
    record, _ = generate("C5_single_architect")
    assert {t.speaker for t in record.transcript} == {"Software Architect"}
    assert len([t for t in record.transcript if t.scope == "container"]) == 2


def test_invalid_yaml_is_retried_once_then_fails():
    record, _ = generate("C0_baseline", invalid_yaml_first={"container"})
    assert record.yaml_retries == 1
    llm = make_fake_llm(invalid_yaml_first={"context"})
    llm.responder = lambda p, s, u: "not: [valid" if p.startswith("yaml|context") else make_fake_llm().responder(p, s, u)
    record = RunRecord()
    with pytest.raises(PipelineError):
        C4Generator(llm, conditions()["C0_baseline"], temperature=0.5, rounds=2).generate(BRIEF, record)
    assert record.yaml_retries == 2 and record.transcript      # partial output is kept


def test_save_record_writes_artifacts_and_transcript(tmp_path):
    record, _ = generate("C12_glossary_memory")
    save_record(record, tmp_path)
    for name in ["1_context_definition.yaml", "2_container_diagram.puml", "3_components/web_app_analysis.md",
                 "transcript.jsonl", "c4_model.json", "glossary_after_L2.json"]:
        assert (tmp_path / name).exists(), name
    lines = (tmp_path / "transcript.jsonl").read_text().splitlines()
    assert len(lines) == len(record.transcript) and json.loads(lines[0])["speaker"] == "Product Owner"
