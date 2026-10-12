"""Deterministic (LLM-free) evaluation of a generated C4 model.

Every metric is computed from the stored artifacts; a metric that cannot be
computed is reported as None with a reason, never replaced by a default value.

Metrics
- completeness: share of expected artifacts (analysis, YAML, diagram for L1, L2 and
  one L3 diagram per L2 container) that are present and non-empty
- yaml_validity: share of YAML definitions with the structure required for their level
- abstraction_adherence: share of diagrams passing the v1 regular-expression rules
- compilation: share of diagrams that PlantUML compiles (None if Java is unavailable)
- reference_validity: share of relationships whose source and destination are defined
  in the same YAML definition (elements, the system at L1/L2, the parent container at
  L3), pooled over all diagrams of the run; c4_sc = 5 * reference_validity
- cross_level: L1->L2 agreement of people and external systems (Jaccard) and the share
  of L3 diagrams whose parent container and non-component references exist at L2
- size: numbers of elements and relationships per level
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from .pipeline import parse_yaml_definition

C4_INCLUDE = re.compile(r"!include\s+https://raw\.githubusercontent\.com/plantuml-stdlib/C4-PlantUML/[^/\s]+/(C4_\w+)\.puml")


# --- abstraction rules (as in v1, src/c4modeler/evaluation.py) ---------------
def check_context_rules(code: str) -> Tuple[bool, str]:
    if re.search(r"Container\s*\(", code, re.IGNORECASE):
        return False, "Illegal 'Container' element found in a Context diagram."
    if re.search(r"Component\s*\(", code, re.IGNORECASE):
        return False, "Illegal 'Component' element found in a Context diagram."
    if not (re.search(r"System\s*\(", code, re.IGNORECASE) or re.search(r"SystemDb\s*\(", code, re.IGNORECASE)
            or re.search(r"System_Ext\s*\(", code, re.IGNORECASE)):
        return False, "Required 'System', 'SystemDb', or 'System_Ext' element appears to be missing."
    return True, "Adheres to abstraction level."


def check_container_rules(code: str) -> Tuple[bool, str]:
    if re.search(r"Component\s*\(", code, re.IGNORECASE):
        return False, "Illegal 'Component' element found in a Container diagram."
    if not re.search(r"Container\s*\(", code, re.IGNORECASE):
        return False, "Required 'Container' element appears to be missing."
    if not re.search(r"System_Boundary\s*\(", code, re.IGNORECASE):
        return False, "Required 'System_Boundary' element appears to be missing."
    return True, "Adheres to abstraction level."


def check_component_rules(code: str) -> Tuple[bool, str]:
    if not re.search(r"Component\s*\(", code, re.IGNORECASE):
        return False, "Required 'Component' element appears to be missing."
    if not re.search(r"Container_Boundary\s*\(", code, re.IGNORECASE):
        return False, "Required 'Container_Boundary' element appears to be missing."
    return True, "Adheres to abstraction level."


RULES = {"context": check_context_rules, "container": check_container_rules, "component": check_component_rules}


# --- helpers -----------------------------------------------------------------
def diagrams_of(c4: dict) -> List[Tuple[str, str, dict]]:
    """(level, scope name, artifacts) for every diagram of the model, in a fixed order."""
    items = [("context", "context", c4.get("context") or {}), ("container", "container", c4.get("containers") or {})]
    items += [("component", name, art or {}) for name, art in (c4.get("components") or {}).items()]
    return items


def _ratio(num: int, den: int) -> Optional[float]:
    return num / den if den else None


_JAVA_OK: Dict[str, bool] = {}


def java_works(java: str = "java") -> bool:
    """True only if a Java runtime actually runs (macOS ships a /usr/bin/java stub without a JRE)."""
    if java not in _JAVA_OK:
        try:
            ok = bool(shutil.which(java)) and subprocess.run([java, "-version"], capture_output=True,
                                                             timeout=30).returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            ok = False
        _JAVA_OK[java] = ok
    return _JAVA_OK[java]


JAVA_CANDIDATES = ("java", "/opt/homebrew/opt/openjdk/bin/java", "/usr/local/opt/openjdk/bin/java")


def find_java() -> str:
    """First Java command that actually runs (Homebrew's keg-only openjdk included); "java" if none."""
    return next((j for j in JAVA_CANDIDATES if java_works(j)), "java")


def compile_plantuml(code: str, jar: Path, java: str = "java", timeout: int = 120) -> Tuple[Optional[bool], str]:
    """(True/False, log) after compiling with PlantUML; (None, reason) if it cannot be run."""
    if not java_works(java):
        return None, "java not available"
    if not Path(jar).exists():
        return None, f"PlantUML jar not found: {jar}"
    source = C4_INCLUDE.sub(r"!include <C4/\1>", code)  # use the C4 library bundled with PlantUML (offline)
    try:
        proc = subprocess.run([java, "-Djava.awt.headless=true", "-jar", str(jar), "-failfast2", "-tsvg", "-pipe"],
                              input=source.encode("utf-8"), capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    return proc.returncode == 0, proc.stderr.decode("utf-8", "replace")[-500:]


# --- metrics -----------------------------------------------------------------
def completeness(c4: dict) -> Dict:
    expected = present = 0
    missing = []
    cont = parse_yaml_definition((c4.get("containers") or {}).get("yaml_definition", ""), "container")
    expected_components = [e["name"] for e in cont["elements"] if e.get("type") == "container"] if cont else []
    levels = [("context", c4.get("context") or {}), ("container", c4.get("containers") or {})]
    levels += [(f"component '{n}'", (c4.get("components") or {}).get(n) or {}) for n in expected_components]
    for scope, art in levels:
        for key in ("analysis", "yaml_definition", "diagram"):
            expected += 1
            if (art.get(key) or "").strip():
                present += 1
            else:
                missing.append(f"{scope}:{key}")
    return {"score": _ratio(present, expected), "missing": missing, "expected_components": len(expected_components)}


def yaml_validity(c4: dict) -> Dict:
    results = {f"{lvl}:{name}": parse_yaml_definition(art.get("yaml_definition", ""), lvl) is not None
               for lvl, name, art in diagrams_of(c4)}
    return {"score": _ratio(sum(results.values()), len(results)), "details": results}


def abstraction_adherence(c4: dict) -> Dict:
    details = {}
    for lvl, name, art in diagrams_of(c4):
        code = art.get("diagram") or ""
        details[f"{lvl}:{name}"] = RULES[lvl](code)[0] if code.strip() else False
    return {"score": _ratio(sum(details.values()), len(details)), "details": details}


def compilation(c4: dict, jar: Path, java: str = "java") -> Dict:
    details, reasons = {}, {}
    for lvl, name, art in diagrams_of(c4):
        ok, log = compile_plantuml(art.get("diagram") or "", jar, java)
        if ok is None:
            return {"score": None, "reason": log}
        details[f"{lvl}:{name}"] = ok
        if not ok:
            reasons[f"{lvl}:{name}"] = log
    return {"score": _ratio(sum(details.values()), len(details)), "details": details, "errors": reasons}


def _defined_names(data: dict, level: str) -> set:
    names = {e["name"] for e in data.get("elements", []) if isinstance(e, dict) and e.get("name")}
    if level in ("context", "container") and isinstance(data.get("system"), dict) and data["system"].get("name"):
        names.add(data["system"]["name"])
    if level == "component" and isinstance(data.get("parentContainer"), dict) and data["parentContainer"].get("name"):
        names.add(data["parentContainer"]["name"])
    return names


def reference_validity(c4: dict) -> Dict:
    per_level = {"context": [0, 0], "container": [0, 0], "component": [0, 0]}
    invalid = []
    for lvl, name, art in diagrams_of(c4):
        data = parse_yaml_definition(art.get("yaml_definition", ""), lvl)
        if data is None:
            continue
        defined = _defined_names(data, lvl)
        for rel in data.get("relationships") or []:
            if not isinstance(rel, dict):
                continue
            per_level[lvl][1] += 1
            if rel.get("source") in defined and rel.get("destination") in defined:
                per_level[lvl][0] += 1
            else:
                invalid.append(f"{lvl}:{name}: {rel.get('source')} -> {rel.get('destination')}")
    valid = sum(v for v, _ in per_level.values())
    total = sum(t for _, t in per_level.values())
    score = _ratio(valid, total)
    return {"score": score, "c4_sc": None if score is None else 5 * score, "valid": valid, "total": total,
            "per_level": {k: _ratio(v, t) for k, (v, t) in per_level.items()}, "invalid": invalid[:50]}


def cross_level(c4: dict) -> Dict:
    ctx = parse_yaml_definition((c4.get("context") or {}).get("yaml_definition", ""), "context")
    cont = parse_yaml_definition((c4.get("containers") or {}).get("yaml_definition", ""), "container")
    result: Dict = {"l1_l2_jaccard": None, "l2_l3_consistency": None, "issues": []}
    if ctx and cont:
        def actors(d):
            return {e["name"] for e in d["elements"] if e.get("type") in ("person", "externalSystem")}
        a, b = actors(ctx), actors(cont)
        result["l1_l2_jaccard"] = len(a & b) / len(a | b) if a | b else None
        result["issues"] += [f"L2 adds {n}" for n in sorted(b - a)] + [f"L2 drops {n}" for n in sorted(a - b)]
    if cont:
        l2_names = {e["name"] for e in cont["elements"]}
        checks = []
        for name, art in (c4.get("components") or {}).items():
            data = parse_yaml_definition((art or {}).get("yaml_definition", ""), "component")
            if data is None:
                checks.append(False)
                continue
            parent_ok = (data.get("parentContainer") or {}).get("name") == name
            outside = [e["name"] for e in data["elements"] if e.get("type") != "component"]
            refs_ok = all(n in l2_names for n in outside)
            checks.append(parent_ok and refs_ok)
            if not parent_ok:
                result["issues"].append(f"L3 '{name}': parentContainer is {(data.get('parentContainer') or {}).get('name')!r}")
            result["issues"] += [f"L3 '{name}': unknown reference {n}" for n in outside if n not in l2_names]
        result["l2_l3_consistency"] = _ratio(sum(checks), len(checks))
    return result


def size(c4: dict) -> Dict:
    out = {"elements": {}, "relationships": {}}
    for lvl in ("context", "container", "component"):
        out["elements"][lvl] = out["relationships"][lvl] = 0
    for lvl, name, art in diagrams_of(c4):
        try:
            data = yaml.safe_load(art.get("yaml_definition") or "") or {}
        except yaml.YAMLError:
            data = {}
        if isinstance(data, dict):
            out["elements"][lvl] += len(data.get("elements") or [])
            out["relationships"][lvl] += len(data.get("relationships") or [])
    out["n_containers"] = len(c4.get("components") or {})
    out["total_elements"] = sum(out["elements"].values())
    out["total_relationships"] = sum(out["relationships"].values())
    return out


def evaluate_structure(c4: dict, jar: Optional[Path] = None, java: str = "java") -> Dict:
    return {
        "completeness": completeness(c4),
        "yaml_validity": yaml_validity(c4),
        "abstraction_adherence": abstraction_adherence(c4),
        "compilation": compilation(c4, jar, java) if jar else {"score": None, "reason": "no PlantUML jar given"},
        "reference_validity": reference_validity(c4),
        "cross_level": cross_level(c4),
        "size": size(c4),
    }
