"""Generation of one C4 model (L1 Context -> L2 Container -> L3 Component per container).

Each level runs the divergence-convergence cycle of the paper:
  discussion (round-robin turns of the team) -> Technical Writer -> YAML Agent -> Diagram Agent.
With memory == "glossary", the Glossary Agent builds the shared knowledge context K
after L1 and after L2, and K is injected into the L2 and L3 discussions and YAML prompts.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from . import prompts as P
from .conditions import AgentSpec, Condition
from .llm import LLMClient

GLOSSARY_TEMPERATURE = 0.0


class PipelineError(RuntimeError):
    """The run cannot continue (e.g. no valid YAML after the allowed retry)."""


def strip_code_fences(text: str) -> str:
    text = (text or "").strip()
    if text.startswith("```"):
        lines = text.split("\n")[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines)
    return text.strip()


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") or "unnamed"


def parse_yaml_definition(text: str, level: str) -> Optional[dict]:
    """Parsed YAML if it has the structure required for `level`, else None."""
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError:
        return None
    if not isinstance(data, dict) or not isinstance(data.get("elements"), list):
        return None
    if not all(isinstance(e, dict) and e.get("name") for e in data["elements"]):
        return None
    if level == "container" and not any(e.get("type") == "container" for e in data["elements"]):
        return None
    if level == "component" and not any(e.get("type") == "component" for e in data["elements"]):
        return None
    return data


@dataclass
class Turn:
    level: str
    scope: str
    round: int
    speaker: str
    persona_key: str
    text: str


@dataclass
class RunRecord:
    """Everything produced by one run; written to disk by the runner."""
    transcript: List[Turn] = field(default_factory=list)
    c4_model: Dict = field(default_factory=lambda: {"context": {}, "containers": {}, "components": {}})
    glossary_snapshots: Dict[str, dict] = field(default_factory=dict)
    yaml_retries: int = 0


def render_discussion(opening: str, turns: List[Turn]) -> str:
    if not turns:
        return opening
    lines = [opening.rstrip(), "", "**Discussion so far:**"]
    for t in turns:
        lines += ["", f"[{t.speaker}]:", t.text.strip()]
    return "\n".join(lines)


def format_glossary(glossary: dict) -> str:
    lines = ["- Entities:"]
    for e in glossary.get("entities", []):
        tech = f" ({e['technology']})" if e.get("technology") else ""
        desc = f": {e['description']}" if e.get("description") else ""
        lines.append(f"  - {e['name']} [{e.get('type', '?')}, {e.get('level', '?')}]{tech}{desc}")
    lines.append("- Interfaces:")
    for i in glossary.get("interfaces", []):
        proto = f" ({i['protocol']})" if i.get("protocol") else ""
        lines.append(f"  - {i['source']} -> {i['destination']}{proto}")
    if glossary.get("naming_conventions"):
        lines.append("- Naming conventions: " + "; ".join(glossary["naming_conventions"]))
    return P.GLOSSARY_INJECTION_HEADER + "\n".join(lines) + "\n"


def prior_decisions(c4_model: dict, level: str, parent: Optional[str] = None) -> str:
    """Condensed context from earlier levels (v1 logic, plus the parent container's definition at L3)."""
    parts: List[str] = []
    ctx = parse_yaml_definition(c4_model["context"].get("yaml_definition", ""), "context") or {}
    if ctx:
        parts.append(f"- System: {(ctx.get('system') or {}).get('name', 'Unknown System')}")
        people = [e["name"] for e in ctx["elements"] if e.get("type") == "person"]
        external = [e["name"] for e in ctx["elements"] if e.get("type") == "externalSystem"]
        if people:
            parts.append(f"- Users: {', '.join(people)}")
        if external:
            parts.append(f"- External Systems: {', '.join(external)}")
    if level == "component":
        cont = parse_yaml_definition(c4_model["containers"].get("yaml_definition", ""), "container") or {}
        containers = [e for e in cont.get("elements", []) if e.get("type") == "container"]
        if containers:
            parts.append("- Containers: " + ", ".join(f"{e['name']} ({e.get('technology', 'N/A')})" for e in containers))
        target = next((e for e in containers if e["name"] == parent), None)
        if target:  # v2: the paper states that the parent container definition is part of the L3 context
            parts.append(f"- Parent container: {target['name']} ({target.get('technology', 'N/A')}): {target.get('description', '')}")
            for r in cont.get("relationships", []) or []:
                if isinstance(r, dict) and parent in (r.get("source"), r.get("destination")):
                    tech = f" [{r['technology']}]" if r.get("technology") else ""
                    parts.append(f"  - {r.get('source')} -> {r.get('destination')}: {r.get('description', '')}{tech}")
    return "\n".join(parts)


class C4Generator:
    def __init__(self, llm: LLMClient, condition: Condition, *, temperature: float, rounds: int):
        self.llm = llm
        self.condition = condition
        self.temperature = temperature
        self.rounds = rounds

    # -- building blocks ---------------------------------------------------
    def _discussion(self, record: RunRecord, level: str, scope: str, opening: str) -> List[Turn]:
        turns: List[Turn] = []
        for rnd in range(1, self.rounds + 1):
            for agent in self.condition.team:
                system = P.TURN_SYSTEM_PROMPT.format(persona_short=agent.role_name, level=scope, persona=agent.persona)
                resp = self.llm.generate(system=system, user=render_discussion(opening, turns),
                                         temperature=self.temperature, purpose=f"turn|{scope}|{agent.display_name}")
                turns.append(Turn(level, scope, rnd, agent.display_name, agent.persona_key, resp.text.strip()))
        record.transcript.extend(turns)
        return turns

    def _writer(self, brief: str, opening: str, turns: List[Turn], scope: str) -> str:
        user = P.WRITER_TASK_PROMPT.format(system_brief=brief) + "\n\n**Discussion:**\n" + render_discussion(opening, turns)
        return self.llm.generate(system=P.WRITER_SYSTEM_PROMPT, user=user, temperature=self.temperature,
                                 purpose=f"writer|{scope}").text.strip()

    def _yaml(self, record: RunRecord, analysis: str, level: str, template: str, context: str, scope: str) -> str:
        user = P.YAML_HUMAN_MESSAGE_PROMPT.format(analysis=analysis, context=context, template=template)
        for attempt in (1, 2):  # one retry if the YAML is unusable
            text = strip_code_fences(self.llm.generate(system=P.YAML_PERSONA_PROMPT, user=user,
                                                       temperature=self.temperature,
                                                       purpose=f"yaml|{scope}|attempt{attempt}").text)
            if parse_yaml_definition(text, level) is not None:
                return text
            record.yaml_retries += 1
        raise PipelineError(f"no valid {level} YAML for {scope} after 2 attempts")

    def _diagram(self, yaml_def: str, analysis: str, scope: str) -> str:
        user = P.PLANTUML_HUMAN_MESSAGE_PROMPT.format(syntax_guide=P.PLANTUML_SYNTAX_GUIDE, yaml_def=yaml_def,
                                                      analysis=analysis)
        return strip_code_fences(self.llm.generate(system=P.PLANTUML_PERSONA_PROMPT, user=user,
                                                   temperature=self.temperature, purpose=f"diagram|{scope}").text)

    def _update_glossary(self, glossary: dict, yaml_def: str, level: str) -> dict:
        user = P.GLOSSARY_TASK_PROMPT.format(glossary=json.dumps(glossary, indent=1), level=level, yaml_def=yaml_def)
        last = ""
        for attempt in (1, 2):
            text = self.llm.generate(system=P.GLOSSARY_AGENT_PERSONA, user=user, temperature=GLOSSARY_TEMPERATURE,
                                     purpose=f"glossary|{level}|attempt{attempt}",
                                     json_schema=P.GLOSSARY_SCHEMA).text
            try:
                data = json.loads(strip_code_fences(text))
                if isinstance(data, dict) and isinstance(data.get("entities"), list):
                    data.setdefault("interfaces", [])
                    data.setdefault("naming_conventions", [])
                    return data
            except json.JSONDecodeError as err:
                last = str(err)
        raise PipelineError(f"Glossary Agent returned no valid JSON at {level} ({last})")

    def _level(self, record: RunRecord, brief: str, level: str, scope: str, template: str,
               prior: str, yaml_context: str, glossary: Optional[dict]) -> Dict[str, str]:
        opening = P.OPENING_MESSAGE.format(level=scope, brief=brief)
        if prior:
            opening += P.PRIOR_DECISIONS_HEADER + prior + "\n\n"
        if glossary is not None:
            opening += format_glossary(glossary) + "\n"
            yaml_context = (yaml_context + "\n\n" + format_glossary(glossary)).strip()
        turns = self._discussion(record, level, scope, opening)
        analysis = self._writer(brief, opening, turns, scope)
        yaml_def = self._yaml(record, analysis, level, template, yaml_context, scope)
        diagram = self._diagram(yaml_def, analysis, scope)
        return {"analysis": analysis, "yaml_definition": yaml_def, "diagram": diagram}

    # -- full run --------------------------------------------------------------
    def generate(self, brief: str, record: Optional[RunRecord] = None) -> RunRecord:
        """Fill `record` (created if None) so that partial output survives a failure."""
        record = record if record is not None else RunRecord()
        use_memory = self.condition.memory == "glossary"
        glossary: Optional[dict] = {"entities": [], "interfaces": [], "naming_conventions": []} if use_memory else None

        record.c4_model["context"] = self._level(record, brief, "context", "context", P.CONTEXT_YAML_TEMPLATE,
                                                 prior="", yaml_context="", glossary=None)
        if use_memory:
            glossary = self._update_glossary(glossary, record.c4_model["context"]["yaml_definition"], "context")
            record.glossary_snapshots["after_L1"] = glossary

        context_yaml = record.c4_model["context"]["yaml_definition"]
        record.c4_model["containers"] = self._level(
            record, brief, "container", "container", P.CONTAINER_YAML_TEMPLATE,
            prior=prior_decisions(record.c4_model, "container"),
            yaml_context=("**Context Level YAML (for reference on system name and external entities):**\n"
                          f"```yaml\n{context_yaml}\n```"),
            glossary=glossary)
        if use_memory:
            glossary = self._update_glossary(glossary, record.c4_model["containers"]["yaml_definition"], "container")
            record.glossary_snapshots["after_L2"] = glossary

        cont = parse_yaml_definition(record.c4_model["containers"]["yaml_definition"], "container")
        system_name = (cont.get("system") or {}).get("name", "System")
        names = list(dict.fromkeys(e["name"] for e in cont["elements"] if e.get("type") == "container"))
        for name in names:
            record.c4_model["components"][name] = self._level(
                record, brief, "component", f"component '{name}'", P.COMPONENT_YAML_TEMPLATE,
                prior=prior_decisions(record.c4_model, "component", parent=name),
                yaml_context=(f"Parent container: {name}\n**Reference Info:**\n- System: {system_name}\n"
                              f"- Containers defined: {', '.join(names)}"),
                glossary=glossary)
        return record


def save_record(record: RunRecord, run_dir: Path) -> None:
    """Write artifacts in the v1 file layout plus transcript and the combined model."""
    run_dir.mkdir(parents=True, exist_ok=True)
    c4 = record.c4_model
    for prefix, key in (("1_context", "context"), ("2_container", "containers")):
        level = c4.get(key) or {}
        for suffix, field_name in (("analysis.md", "analysis"), ("definition.yaml", "yaml_definition"),
                                   ("diagram.puml", "diagram")):
            if level.get(field_name):
                (run_dir / f"{prefix}_{suffix}").write_text(level[field_name], encoding="utf-8")
    comp_dir = run_dir / "3_components"
    for name, level in (c4.get("components") or {}).items():
        comp_dir.mkdir(exist_ok=True)
        for suffix, field_name in (("analysis.md", "analysis"), ("definition.yaml", "yaml_definition"),
                                   ("diagram.puml", "diagram")):
            if level.get(field_name):
                (comp_dir / f"{slugify(name)}_{suffix}").write_text(level[field_name], encoding="utf-8")
    with open(run_dir / "transcript.jsonl", "w", encoding="utf-8") as fh:
        for t in record.transcript:
            fh.write(json.dumps(t.__dict__, ensure_ascii=False) + "\n")
    (run_dir / "c4_model.json").write_text(json.dumps(c4, indent=1, ensure_ascii=False), encoding="utf-8")
    for name, glossary in record.glossary_snapshots.items():
        (run_dir / f"glossary_{name}.json").write_text(json.dumps(glossary, indent=1, ensure_ascii=False),
                                                       encoding="utf-8")
