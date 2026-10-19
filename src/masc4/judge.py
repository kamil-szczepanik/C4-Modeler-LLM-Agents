"""LLM-as-a-judge evaluation (v2): ISO/IEC 25010:2011 characteristics, ATAM-style
scenarios and requirement coverage.

The judge sees only the system brief and the YAML definitions of the generated model;
it never sees the condition, the team or the discussion (blind evaluation). Invalid
answers are retried once and otherwise recorded as errors; no score is ever defaulted.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from .llm import LLMClient
from .pipeline import strip_code_fences
from .structural import diagrams_of

JUDGE_TEMPERATURE = 0.0

ISO_CHARACTERISTICS = {
    "functional_suitability": "the architecture provides elements for every functional requirement of the brief",
    "performance_efficiency": "the architecture contains mechanisms that make the stated performance and scalability "
                              "targets achievable (e.g. caching, asynchronous processing, scaling, efficient data access)",
    "compatibility": "interoperability with the external systems and standards named in the brief, and coexistence with them",
    "usability": "every user group of the brief is served by elements with appropriate interfaces and channels",
    "reliability": "availability, fault tolerance and recoverability mechanisms appropriate to the stated targets",
    "security": "confidentiality, integrity, authentication, authorization and accountability (audit) mechanisms "
                "appropriate to the brief",
    "maintainability": "modular decomposition with clear responsibilities, low coupling and replaceable parts",
    "portability": "adaptability to the deployment environments named in the brief and replaceability of infrastructure",
}

JUDGE_SYSTEM_PROMPT = """You are an experienced software architect acting as an independent evaluator of C4 architecture models.
Assess only the architecture described in the YAML definitions against the system brief.
Be strict and consistent: reward explicit mechanisms that address the brief; do not reward length, buzzwords or
elements unrelated to the brief; penalize the absence of elements or mechanisms that the brief requires.
Return only the requested JSON."""

ISO_TASK_PROMPT = """Evaluate the architecture against the eight product quality characteristics of ISO/IEC 25010:2011.

**System brief:**
```yaml
{brief}
```

**Architecture (C4 model, YAML definitions of all levels):**
{architecture}

For each characteristic give an integer score from 1 to 5 and a justification of at most 50 words that cites element names.
{characteristics}

Scale for every characteristic:
1 = not addressed, or contradicted by the architecture
2 = addressed superficially (mentioned without a concrete mechanism)
3 = addressed with concrete mechanisms but with important gaps
4 = addressed well, with minor gaps
5 = addressed thoroughly, with mechanisms that explicitly match the targets of the brief"""

ATAM_TASK_PROMPT = """Analyse how the architecture responds to the quality-attribute scenarios below, following the
scenario analysis of the Architecture Tradeoff Analysis Method (ATAM).

**System brief:**
```yaml
{brief}
```

**Architecture (C4 model, YAML definitions of all levels):**
{architecture}

**Scenarios:**
{scenarios}

For every scenario give:
- score: integer from 1 to 5 (1 = the architecture cannot achieve the response; 3 = it can, but only with significant
  changes or with unaddressed risks; 5 = it achieves the response measure with the mechanisms it already contains)
- elements: names of the architectural elements involved
- sensitivity_points and tradeoffs: short phrases (at most 15 words each)
- justification: at most 50 words"""

REQUIREMENTS_TASK_PROMPT = """Decide for every requirement of the brief whether the architecture addresses it.

**System brief:**
```yaml
{brief}
```

**Architecture (C4 model, YAML definitions of all levels):**
{architecture}

**Requirements:**
{requirements}

Status values: "full" = dedicated elements or mechanisms clearly realize the requirement; "partial" = it is realized
only partly or only implicitly; "none" = nothing in the architecture realizes it.
For every requirement give its id, the status and the names of the elements that realize it."""

ISO_SCHEMA = {"type": "OBJECT", "properties": {
    name: {"type": "OBJECT", "properties": {"score": {"type": "INTEGER"}, "justification": {"type": "STRING"}},
           "required": ["score", "justification"]} for name in ISO_CHARACTERISTICS},
    "required": list(ISO_CHARACTERISTICS)}

ATAM_SCHEMA = {"type": "OBJECT", "properties": {"scenarios": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {
    "id": {"type": "STRING"}, "score": {"type": "INTEGER"},
    "elements": {"type": "ARRAY", "items": {"type": "STRING"}},
    "sensitivity_points": {"type": "ARRAY", "items": {"type": "STRING"}},
    "tradeoffs": {"type": "ARRAY", "items": {"type": "STRING"}},
    "justification": {"type": "STRING"}}, "required": ["id", "score", "justification"]}}},
    "required": ["scenarios"]}

REQUIREMENTS_SCHEMA = {"type": "OBJECT", "properties": {"requirements": {"type": "ARRAY", "items": {
    "type": "OBJECT", "properties": {"id": {"type": "STRING"},
                                     "status": {"type": "STRING", "enum": ["full", "partial", "none"]},
                                     "elements": {"type": "ARRAY", "items": {"type": "STRING"}}},
    "required": ["id", "status"]}}}, "required": ["requirements"]}


def judge_prompt_hashes() -> Dict[str, str]:
    """Short hashes of the judge prompts and rubric, stored with every evaluation."""
    import hashlib
    items = {"JUDGE_SYSTEM_PROMPT": JUDGE_SYSTEM_PROMPT, "ISO_TASK_PROMPT": ISO_TASK_PROMPT,
             "ATAM_TASK_PROMPT": ATAM_TASK_PROMPT, "REQUIREMENTS_TASK_PROMPT": REQUIREMENTS_TASK_PROMPT,
             "ISO_CHARACTERISTICS": json.dumps(ISO_CHARACTERISTICS, sort_keys=True)}
    return {k: hashlib.sha256(v.encode("utf-8")).hexdigest()[:12] for k, v in items.items()}


class JudgeError(RuntimeError):
    pass


def render_architecture(c4: dict) -> str:
    titles = {"context": "Level 1 - System Context", "container": "Level 2 - Containers"}
    parts = []
    for lvl, name, art in diagrams_of(c4):
        title = titles.get(lvl, f"Level 3 - Components of '{name}'")
        parts.append(f"### {title}\n```yaml\n{(art.get('yaml_definition') or '(missing)').strip()}\n```")
    return "\n\n".join(parts)


def brief_requirements(brief_text: str) -> List[Dict[str, str]]:
    data = yaml.safe_load(brief_text) or {}
    reqs = []
    for i, c in enumerate(data.get("constraints") or [], 1):
        reqs.append({"id": f"C-{i:02d}", "text": str(c)})
    for r in (data.get("functional_requirements") or []) + (data.get("nonfunctional_requirements") or []):
        quality = f" ({r['quality']})" if r.get("quality") else ""
        reqs.append({"id": str(r["id"]), "text": f"{r.get('desc', '')}{quality}"})
    ids = [r["id"] for r in reqs]
    if len(ids) != len(set(ids)):
        raise JudgeError("duplicate requirement ids in brief")
    return reqs


def load_scenarios(path: Path) -> List[Dict[str, str]]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return data["scenarios"]


def parse_json_answer(text: str) -> dict:
    text = strip_code_fences(text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start:end + 1])
        raise


def _ask(llm: LLMClient, user: str, schema: dict, purpose: str, validate) -> dict:
    last = ""
    for attempt in (1, 2):
        text = llm.generate(system=JUDGE_SYSTEM_PROMPT, user=user, temperature=JUDGE_TEMPERATURE,
                            purpose=f"{purpose}|attempt{attempt}", json_schema=schema).text
        try:
            data = parse_json_answer(text)
            problem = validate(data)
            if not problem:
                return data
            last = problem
        except (json.JSONDecodeError, TypeError, KeyError, AttributeError) as err:
            last = f"{type(err).__name__}: {err}"
    raise JudgeError(f"{purpose}: no valid answer after 2 attempts ({last})")


def _score_ok(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and 1 <= value <= 5


def judge_iso(llm: LLMClient, brief: str, c4: dict) -> Dict:
    chars = "\n".join(f"- {k}: {v}" for k, v in ISO_CHARACTERISTICS.items())
    user = ISO_TASK_PROMPT.format(brief=brief.strip(), architecture=render_architecture(c4), characteristics=chars)

    def validate(d):
        bad = [k for k in ISO_CHARACTERISTICS if not (isinstance(d.get(k), dict) and _score_ok(d[k].get("score")))]
        return f"invalid or missing scores: {bad}" if bad else ""

    data = _ask(llm, user, ISO_SCHEMA, "judge_iso", validate)
    scores = {k: data[k]["score"] for k in ISO_CHARACTERISTICS}
    return {"scores": scores, "mean": sum(scores.values()) / len(scores),
            "justifications": {k: data[k]["justification"] for k in ISO_CHARACTERISTICS}}


def judge_atam(llm: LLMClient, brief: str, c4: dict, scenarios: List[Dict[str, str]]) -> Dict:
    fields = ("quality_attribute", "stimulus", "environment", "response", "response_measure")
    text = "\n".join(f"- {s['id']}: " + "; ".join(f"{f.replace('_', ' ')}: {s[f]}" for f in fields if s.get(f))
                     for s in scenarios)
    user = ATAM_TASK_PROMPT.format(brief=brief.strip(), architecture=render_architecture(c4), scenarios=text)
    expected = {s["id"] for s in scenarios}

    def validate(d):
        got = {x.get("id"): x for x in d.get("scenarios", []) if isinstance(x, dict)}
        if set(got) != expected:
            return f"scenario ids {sorted(got)} != {sorted(expected)}"
        bad = [i for i, x in got.items() if not _score_ok(x.get("score"))]
        return f"invalid scores for {bad}" if bad else ""

    data = _ask(llm, user, ATAM_SCHEMA, "judge_atam", validate)
    per = {x["id"]: x for x in data["scenarios"]}
    scores = {i: per[i]["score"] for i in sorted(expected)}
    by_attr: Dict[str, List[int]] = {}
    for s in scenarios:
        by_attr.setdefault(s["quality_attribute"], []).append(scores[s["id"]])
    return {"scores": scores, "responsiveness_index": sum((v - 1) / 4 for v in scores.values()) / len(scores),
            "by_quality_attribute": {k: sum(v) / len(v) for k, v in by_attr.items()}, "details": per}


def judge_requirements(llm: LLMClient, brief: str, c4: dict) -> Dict:
    reqs = brief_requirements(brief)
    user = REQUIREMENTS_TASK_PROMPT.format(brief=brief.strip(), architecture=render_architecture(c4),
                                           requirements="\n".join(f"- {r['id']}: {r['text']}" for r in reqs))
    expected = {r["id"] for r in reqs}

    def validate(d):
        got = {x.get("id"): x.get("status") for x in d.get("requirements", []) if isinstance(x, dict)}
        if set(got) != expected:
            return f"requirement ids {sorted(got)} != {sorted(expected)}"
        bad = [i for i, s in got.items() if s not in ("full", "partial", "none")]
        return f"invalid status for {bad}" if bad else ""

    data = _ask(llm, user, REQUIREMENTS_SCHEMA, "judge_requirements", validate)
    status = {x["id"]: x["status"] for x in data["requirements"]}
    full = sum(s == "full" for s in status.values())
    partial = sum(s == "partial" for s in status.values())
    return {"status": status, "coverage": (full + 0.5 * partial) / len(status),
            "details": {x["id"]: x for x in data["requirements"]}}


JUDGE_TASKS = ("iso", "atam", "requirements")


def judge_run(llm: LLMClient, brief: str, c4: dict, scenarios: List[Dict[str, str]],
              previous: Optional[Dict] = None) -> Dict:
    """Run the three judge tasks, keeping results of tasks that already succeeded in `previous`.

    A failed task is stored under "errors" and the others are kept, so a later call
    repeats only what is missing.
    """
    result = {"model": llm.model}
    result.update({t: previous[t] for t in JUDGE_TASKS if previous and t in previous})
    tasks = {"iso": lambda: judge_iso(llm, brief, c4), "atam": lambda: judge_atam(llm, brief, c4, scenarios),
             "requirements": lambda: judge_requirements(llm, brief, c4)}
    errors = {}
    for name in JUDGE_TASKS:
        if name in result:
            continue
        try:
            result[name] = tasks[name]()
        except Exception as err:  # JudgeError or LLMError after all retries
            errors[name] = f"{type(err).__name__}: {err}"
    if errors:
        result["errors"] = errors
    return result
