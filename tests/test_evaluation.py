import json
from pathlib import Path

import pytest

from fake_responses import COMPONENT_YAML, CONTAINER_YAML, CONTEXT_YAML
from masc4 import judge as J
from masc4.llm import FakeLLM
from masc4.structural import (abstraction_adherence, compilation, completeness, cross_level, evaluate_structure,
                              reference_validity, size)

BRIEF = """title: Test System
constraints:
  - "GDPR compliance"
functional_requirements:
  - id: R-01
    desc: "Register patients"
nonfunctional_requirements:
  - id: R-02
    quality: Performance
    desc: "Page load < 1 s"
"""

SCENARIOS = [{"id": "PERF-01", "quality_attribute": "Performance", "stimulus": "peak load", "response": "serve",
              "response_measure": "P95 < 1 s"},
             {"id": "SEC-01", "quality_attribute": "Security", "stimulus": "attack", "response": "block",
              "response_measure": "no breach"}]


def model(context=CONTEXT_YAML, container=CONTAINER_YAML, components=("Web App", "Database")):
    diag = {"context": '@startuml\nPerson(a, "A")\nSystem(s, "S")\n@enduml',
            "container": '@startuml\nSystem_Boundary(b, "B") {\nContainer(c, "C", "T")\n}\n@enduml',
            "component": '@startuml\nContainer_Boundary(b, "B") {\nComponent(c, "C", "T")\n}\n@enduml'}
    return {"context": {"analysis": "a", "yaml_definition": context, "diagram": diag["context"]},
            "containers": {"analysis": "a", "yaml_definition": container, "diagram": diag["container"]},
            "components": {n: {"analysis": "a", "yaml_definition": COMPONENT_YAML.format(parent=n),
                               "diagram": diag["component"]} for n in components}}


def test_complete_and_consistent_model_scores_perfectly():
    c4 = model()
    assert completeness(c4)["score"] == 1.0
    assert abstraction_adherence(c4)["score"] == 1.0
    rv = reference_validity(c4)
    # context: 1 rel to the system (defined); container: 2 rels; components: 1 rel each
    assert (rv["valid"], rv["total"], rv["score"], rv["c4_sc"]) == (5, 5, 1.0, 5.0)
    cl = cross_level(c4)
    assert cl["l1_l2_jaccard"] == 1.0 and cl["l2_l3_consistency"] == 1.0
    s = size(c4)
    assert s["elements"] == {"context": 2, "container": 4, "component": 4} and s["n_containers"] == 2


def test_missing_component_diagram_and_dangling_reference_are_counted():
    c4 = model(components=("Web App",))                      # L2 defines two containers, only one L3 diagram
    comp = completeness(c4)
    assert comp["score"] == pytest.approx(9 / 12) and "component 'Database':diagram" in comp["missing"]
    dangling = CONTAINER_YAML.replace('destination: "Database"', 'destination: "Cache"')
    rv = reference_validity(model(container=dangling))
    assert rv["valid"] == rv["total"] - 1 and any("Cache" in i for i in rv["dangling"])


def test_reference_to_a_container_from_a_component_diagram_is_valid_but_not_strict():
    c4 = model()
    c4["components"]["Web App"]["yaml_definition"] += (
        '  - source: "Web App Service"\n    destination: "Database"\n    description: "Reads"\n')
    rv = reference_validity(c4)
    assert rv["score"] == 1.0 and rv["cross_level_references"] == 1 and rv["strict_score"] == pytest.approx(5 / 6)
    c4["components"]["Web App"]["yaml_definition"] += (
        '  - source: "Web App Service"\n    destination: "Payroll Service"\n    description: "x"\n')
    rv = reference_validity(c4)
    assert rv["dangling"] == ["component:Web App: Web App Service -> Payroll Service"]


def test_no_relationships_gives_none_not_a_perfect_score():
    no_rels = {"context": {"yaml_definition": "level: context\nelements:\n  - {type: person, name: A}\n"},
               "containers": {}, "components": {}}
    assert reference_validity(no_rels)["score"] is None


def test_abstraction_rules_flag_level_inappropriate_elements():
    c4 = model()
    c4["context"]["diagram"] = '@startuml\nSystem(s, "S")\nContainer(c, "C", "T")\n@enduml'
    res = abstraction_adherence(c4)
    assert res["details"]["context:context"] is False and res["score"] == pytest.approx(3 / 4)


def test_cross_level_detects_changed_actors_and_wrong_parent():
    c4 = model()
    c4["containers"]["yaml_definition"] = CONTAINER_YAML.replace('name: "Lab System"', 'name: "Laboratory"')
    c4["components"]["Web App"]["yaml_definition"] = COMPONENT_YAML.format(parent="Frontend")
    cl = cross_level(c4)
    assert cl["l1_l2_jaccard"] == pytest.approx(1 / 3) and cl["l2_l3_consistency"] == 0.5
    assert "L2 adds Laboratory" in cl["issues"]


def test_compilation_is_none_without_java(tmp_path):
    res = compilation(model(), tmp_path / "plantuml.jar", java="definitely-not-java")
    assert res["score"] is None and "java" in res["reason"]
    stub = tmp_path / "java"                       # like the macOS stub: exists but fails
    stub.write_text("#!/bin/sh\necho 'Unable to locate a Java Runtime' >&2\nexit 1\n")
    stub.chmod(0o755)
    assert compilation(model(), tmp_path / "plantuml.jar", java=str(stub))["score"] is None
    assert evaluate_structure(model())["compilation"]["score"] is None


def judge_answers(iso_score=4, bad_first=False):
    calls = {"n": 0}

    def responder(purpose, system, user):
        calls["n"] += 1
        assert "Product Owner" not in user and "condition" not in user.lower()   # blind evaluation
        if purpose.startswith("judge_iso"):
            if bad_first and purpose.endswith("attempt1"):
                return '{"functional_suitability": {"score": 7, "justification": "x"}}'
            return json.dumps({k: {"score": iso_score, "justification": "ok"} for k in J.ISO_CHARACTERISTICS})
        if purpose.startswith("judge_atam"):
            return json.dumps({"scenarios": [{"id": "PERF-01", "score": 5, "justification": "j"},
                                             {"id": "SEC-01", "score": 1, "justification": "j"}]})
        return "```json\n" + json.dumps({"requirements": [
            {"id": "C-01", "status": "full"}, {"id": "R-01", "status": "partial"},
            {"id": "R-02", "status": "none"}]}) + "\n```"
    return FakeLLM(responder, model="judge-fake"), calls


def test_judge_run_scores_and_aggregates():
    llm, _ = judge_answers()
    res = J.judge_run(llm, BRIEF, model(), SCENARIOS)
    assert res["iso"]["mean"] == 4 and set(res["iso"]["scores"]) == set(J.ISO_CHARACTERISTICS)
    assert res["atam"]["responsiveness_index"] == 0.5 and res["atam"]["by_quality_attribute"] == {"Performance": 5, "Security": 1}
    assert res["requirements"]["coverage"] == pytest.approx(0.5)  # (1 + 0.5 + 0) / 3


def test_invalid_judge_answer_is_retried_then_rejected():
    llm, calls = judge_answers(bad_first=True)
    assert J.judge_iso(llm, BRIEF, model())["mean"] == 4 and calls["n"] == 2
    always_bad = FakeLLM(lambda p, s, u: '{"functional_suitability": {"score": 0}}')
    with pytest.raises(J.JudgeError):
        J.judge_iso(always_bad, BRIEF, model())


def test_brief_requirements_include_constraints_and_quality():
    reqs = J.brief_requirements(BRIEF)
    assert [r["id"] for r in reqs] == ["C-01", "R-01", "R-02"] and reqs[2]["text"] == "Page load < 1 s (Performance)"


def test_architecture_rendering_contains_all_levels():
    text = J.render_architecture(model())
    assert "Level 1 - System Context" in text and "Level 3 - Components of 'Database'" in text


ROOT = Path(__file__).resolve().parents[1]


def test_every_brief_has_complete_scenarios_and_parsable_requirements():
    briefs = sorted((ROOT / "data/briefs").glob("*.yaml"))
    assert len(briefs) == 6
    for brief in briefs:
        reqs = J.brief_requirements(brief.read_text(encoding="utf-8"))
        assert reqs, brief.name
        scenarios = J.load_scenarios(ROOT / "configs/scenarios" / brief.name)
        assert len(scenarios) == 8 and len({s["id"] for s in scenarios}) == 8, brief.name
        for s in scenarios:
            assert all(s.get(f) for f in ("id", "quality_attribute", "stimulus", "environment", "response",
                                          "response_measure")), (brief.name, s.get("id"))
        assert {s["quality_attribute"] for s in scenarios} == {"Performance", "Availability", "Modifiability",
                                                               "Security"}



def test_judge_keeps_successful_tasks_and_repeats_only_failed_ones():
    good, _ = judge_answers()
    state = {"fail": True}

    def flaky(purpose, system, user):
        if purpose.startswith("judge_requirements") and state["fail"]:
            raise J.JudgeError("simulated overload")
        return good.responder(purpose, system, user)

    llm = FakeLLM(flaky, model="judge-fake")
    first = J.judge_run(llm, BRIEF, model(), SCENARIOS)
    assert "iso" in first and "atam" in first and set(first["errors"]) == {"requirements"}
    state["fail"] = False
    n_before = len(llm.calls)
    second = J.judge_run(llm, BRIEF, model(), SCENARIOS, previous=first)
    assert "errors" not in second and second["iso"] == first["iso"]
    assert [c["purpose"] for c in llm.calls[n_before:]] == ["judge_requirements|attempt1"]


def test_judge_prompt_hashes_are_stable_and_complete():
    a, b = J.judge_prompt_hashes(), J.judge_prompt_hashes()
    assert a == b and set(a) == {"JUDGE_SYSTEM_PROMPT", "ISO_TASK_PROMPT", "ATAM_TASK_PROMPT",
                                 "REQUIREMENTS_TASK_PROMPT", "ISO_CHARACTERISTICS"}
