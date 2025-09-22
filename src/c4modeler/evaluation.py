# src/evaluation.py
from __future__ import annotations

import json
import re
from collections import Counter, deque
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import yaml
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from .types import C4Model
from .llm import get_llm
from .utils import setup_plantuml, compile_plantuml_java, PLANTUML_JAR_PATH

# ==============================================================================
# 0. Small shared helpers
# ==============================================================================

def _parse_yaml_safe(yaml_string: Optional[str]) -> Dict:
    """Safely parses a YAML string, returning an empty dict on error."""
    if not yaml_string or not isinstance(yaml_string, str) or not yaml_string.strip():
        return {}
    try:
        return yaml.safe_load(yaml_string) or {}
    except yaml.YAMLError:
        return {}

def _extract_element_names(parsed_yaml: Dict, element_types: List[str]) -> Set[str]:
    """Extract a set of names from 'elements' list, filtering by type."""
    names: Set[str] = set()
    for element in parsed_yaml.get("elements", []) or []:
        if element.get("type") in element_types:
            if "name" in element and isinstance(element["name"], str):
                names.add(element["name"])
    return names

# ==============================================================================
# 1) PlantUML compilation success (using your utils helpers)
# ==============================================================================

def evaluate_compilation_success(c4_model: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculates the percentage of diagrams that compile and captures detailed diagnostics.
    Uses `java -jar <PLANTUML_JAR_PATH> -failfast2 -tsvg ...` via utils.compile_plantuml_java.
    """
    print("🤖 Evaluating Metric: PlantUML Compilation Success...")
    ready = setup_plantuml()
    if not ready:
        return {"error": "PlantUML runner not available (download/setup failed)."}

    jar_path = str(PLANTUML_JAR_PATH)

    # Collect diagrams
    diagrams: List[Dict[str, str]] = []
    ctx = c4_model.get("context", {}) or {}
    cnt = c4_model.get("containers", {}) or {}
    comps = c4_model.get("components", {}) or {}

    if ctx.get("diagram"):
        diagrams.append({"source": "1_Context", "code": ctx["diagram"]})
    if cnt.get("diagram"):
        diagrams.append({"source": "2_Containers", "code": cnt["diagram"]})
    for name, comp in comps.items():
        if isinstance(comp, dict) and comp.get("diagram"):
            diagrams.append({"source": f"3_Component_{name}", "code": comp["diagram"]})

    if not diagrams:
        return {"metric": "Compilation Success Rate", "score": 0, "successful": 0, "total": 0, "details": []}

    successful = 0
    details: List[Dict[str, Any]] = []

    for d in diagrams:
        code = (d["code"] or "").strip()
        if not code:
            details.append({"source": d["source"], "status": "Failed - Empty", "error": "Diagram content empty."})
            continue

        ok, log, _ = compile_plantuml_java(code, jar_path, out_format="svg")
        if ok:
            successful += 1
            details.append({"source": d["source"], "status": "Compiled", "error": None})
        else:
            details.append({"source": d["source"], "status": "Failed - Syntax Error", "error": (log or "").strip()})

    total = len(diagrams)
    score = round((successful / total) * 100, 2) if total else 0.0
    return {
        "metric": "Compilation Success Rate",
        "score": score,
        "successful": successful,
        "total": total,
        "details": details,
    }

# ==============================================================================
# 2) Abstraction adherence (your dedicated rule checkers)
# ==============================================================================

def _check_context_rules(code: str) -> Tuple[bool, str]:
    """Checks rules for a C4 Context Diagram."""
    if re.search(r'Container\s*\(', code, re.IGNORECASE):
        return (False, "Illegal 'Container' element found in a Context diagram.")
    if re.search(r'Component\s*\(', code, re.IGNORECASE):
        return (False, "Illegal 'Component' element found in a Context diagram.")
    # A context diagram should generally define the main system
    if not (re.search(r'System\s*\(', code, re.IGNORECASE) or
            re.search(r'SystemDb\s*\(', code, re.IGNORECASE) or
            re.search(r'System_Ext\s*\(', code, re.IGNORECASE)):
        return (False, "Required 'System', 'SystemDb', or 'System_Ext' element appears to be missing.")
    return (True, "Adheres to abstraction level.")

def _check_container_rules(code: str) -> Tuple[bool, str]:
    """Checks rules for a C4 Container Diagram."""
    if re.search(r'Component\s*\(', code, re.IGNORECASE):
        return (False, "Illegal 'Component' element found in a Container diagram.")
    if not re.search(r'Container\s*\(', code, re.IGNORECASE):
        return (False, "Required 'Container' element appears to be missing.")
    if not re.search(r'System_Boundary\s*\(', code, re.IGNORECASE):
        return (False, "Required 'System_Boundary' element appears to be missing.")
    return (True, "Adheres to abstraction level.")

def _check_component_rules(code: str) -> Tuple[bool, str]:
    """Checks rules for a C4 Component Diagram."""
    if not re.search(r'Component\s*\(', code, re.IGNORECASE):
        return (False, "Required 'Component' element appears to be missing.")
    if not re.search(r'Container_Boundary\s*\(', code, re.IGNORECASE):
        return (False, "Required 'Container_Boundary' element appears to be missing.")
    return (True, "Adheres to abstraction level.")

def evaluate_abstraction_adherence(c4_model: Dict[str, Any]) -> Dict[str, Any]:
    """Checks if each diagram uses PlantUML elements appropriate for its C4 level."""
    print("🤖 Evaluating Metric: C4 Abstraction Adherence...")

    RULE_CHECKERS = {
        'Context': _check_context_rules,
        'Containers': _check_container_rules,
        'Component': _check_component_rules,
    }

    diagrams_to_check = []
    if c4_model.get("context", {}).get("diagram"):
        diagrams_to_check.append({"type": "Context", "name": "Context", "code": c4_model["context"]["diagram"]})
    if c4_model.get("containers", {}).get("diagram"):
        diagrams_to_check.append({"type": "Containers", "name": "Containers", "code": c4_model["containers"]["diagram"]})
    for name, comp_data in (c4_model.get("components") or {}).items():
        if comp_data.get("diagram"):
            diagrams_to_check.append({"type": "Component", "name": f"Component: {name}", "code": comp_data["diagram"]})

    total = len(diagrams_to_check)
    if total == 0:
        return {"metric": "Abstraction Adherence", "score": 0, "details": {}}

    passes = 0
    details: Dict[str, Any] = {}

    for item in diagrams_to_check:
        checker = RULE_CHECKERS.get(item["type"])
        if not checker:
            details[item["name"]] = {"status": "Unknown", "reason": "No rule checker found for this diagram type."}
            continue

        ok, reason = checker(item["code"])
        if ok:
            passes += 1
        details[item["name"]] = {"status": "Pass" if ok else "Fail", "reason": reason}

    score = (passes / total) * 100 if total else 0
    return {"metric": "Abstraction Adherence", "score": round(score, 2), "details": details}

# ==============================================================================
# 3) Semantic consistency (LLM judge; your prompt kept intact)
# ==============================================================================

def evaluate_semantic_consistency(system_brief: str, c4_model: Dict[str, Any], judge_llm) -> Dict[str, Any]:
    """Evaluates how well the diagrams capture entities from the input brief."""
    print("⚖️ Evaluating Metric 3: Semantic Consistency...")
    context_diag = c4_model.get("context", {}).get("diagram")
    if not context_diag:
        return {"error": "Context diagram not found."}

    extraction_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a requirements analyst. Your task is to extract key entities from a system description. List all people (user roles), external systems, and the main system itself."),
        ("human", "Please extract the entities from the following brief:\n\n{brief}")
    ])
    extraction_chain = extraction_prompt | judge_llm | StrOutputParser()
    extracted_items_str = extraction_chain.invoke({"brief": system_brief})

    extracted_items = [item.strip() for item in extracted_items_str.split('\n') if item.strip()]

    verification_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a meticulous verifier. For each item in the checklist, check if it is clearly represented in the provided PlantUML diagram. Respond with only 'YES' or 'NO' for each item."),
        ("human", """**Checklist:**
                   {checklist}

                   **PlantUML Diagram:**
                   ```puml
                   {diagram}
                   ```""")
    ])
    verification_chain = verification_prompt | judge_llm | StrOutputParser()
    verification_results_str = verification_chain.invoke({
        "checklist": "\n".join(f"- {item}" for item in extracted_items),
        "diagram": context_diag
    })

    verified_count = verification_results_str.upper().count("YES")
    total_items = len(extracted_items)
    score = (verified_count / total_items) * 100 if total_items > 0 else 0

    return {
        "metric": "Semantic Consistency",
        "score": round(score, 2),
        "verified_items": verified_count,
        "total_items": total_items
    }

# ==============================================================================
# 4) Definitional consistency (YAML vs diagram) — robust to both YAML shapes
# ==============================================================================

def evaluate_definitional_consistency(
    yaml_definition_str: str,
    diagram_code_str: str,
    element_type: str  # e.g., 'containers' or 'components'
) -> Dict[str, Any]:
    """
    Checks if all elements defined in a YAML spec are present in a PlantUML diagram.
    Accepts two YAML shapes:
      A) Explicit lists under keys: {'containers': [...]} / {'components': [...]}
      B) Single 'elements' list with 'type' fields ('container' / 'component')
    """
    if not yaml_definition_str or not diagram_code_str:
        return {"score": 0, "details": {"error": f"Missing YAML definition or diagram for {element_type}."}}

    try:
        definition_data = yaml.safe_load(yaml_definition_str) or {}

        # Try explicit keyed list first
        items = definition_data.get(element_type)
        defined_names: List[str] = []
        if isinstance(items, list):
            defined_names = [item.get("name") for item in items if isinstance(item, dict) and "name" in item]

        # Fallback to 'elements' list filtered by type
        if not defined_names:
            filter_type = "container" if element_type == "containers" else "component"
            for elem in definition_data.get("elements", []) or []:
                if isinstance(elem, dict) and elem.get("type") == filter_type and "name" in elem:
                    defined_names.append(elem["name"])

        if not defined_names:
            return {
                "metric": f"{element_type.capitalize()} Definitional Consistency",
                "score": 100,
                "found_count": 0,
                "total_defined": 0,
                "details": {"message": f"No {element_type} with a 'name' key found in the YAML."}
            }

        found_count = 0
        verification_details = []
        for name in defined_names:
            # Look for name inside PlantUML element parentheses (with or without quotes)
            if re.search(fr'\(\s*"{re.escape(name)}"\s*,', diagram_code_str) or re.search(fr'\(\s*{re.escape(name)}\s*,', diagram_code_str):
                found_count += 1
                verification_details.append({"element_name": name, "status": "Found"})
            else:
                verification_details.append({"element_name": name, "status": "Missing"})

        total_defined = len(defined_names)
        score = (found_count / total_defined) * 100 if total_defined > 0 else 100

        return {
            "metric": f"{element_type.capitalize()} Definitional Consistency",
            "score": round(score, 2),
            "found_count": found_count,
            "total_defined": total_defined,
            "details": verification_details
        }

    except Exception as e:
        return {"error": f"Failed to process definitional consistency check: {e}"}

# ==============================================================================
# 5) Qualitative rubric (LLM judge; prompt preserved)
# ==============================================================================

def evaluate_qualitative_rubric(
    diagram_code: str,
    diagram_name: str,
    system_brief: str,
    judge_llm
) -> Dict[str, Any]:
    """
    Scores a single diagram based on a qualitative rubric using an LLM-as-a-Judge,
    providing the judge with the system brief for context.
    """
    print(f"⚖️ Evaluating Metric: Qualitative Rubric for {diagram_name}...")

    rubric_schema = {
        "title": "QualitativeRubricEvaluation",
        "type": "object",
        "additionalProperties": True  # keep flexible; your schema comment said "identical"
    }

    rubric_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert software architect acting as a judge. Your task is to evaluate the provided C4 diagram against the requirements of the original system brief. Provide a score from 1 (poor) to 5 (excellent) for each criterion, along with a brief justification. You must format your response as a JSON object that adheres to the provided schema."),
        ("human", """
        **System Brief to Reference:**
        ---
        {system_brief}
        ---

        **Rubric:**
        | Criterion         | 1 (Poor)                                                    | 3 (Average)                                                    | 5 (Excellent)                                                                      |
        |-------------------|-------------------------------------------------------------|----------------------------------------------------------------|------------------------------------------------------------------------------------|
        | **Completeness** | The diagram is missing core elements from the system brief. | The diagram includes most major elements but misses minor details. | All key entities and relationships required by the system brief are present.       |
        | **Correctness** | Relationships are illogical or incorrectly depicted.        | Relationships are mostly correct but have minor inaccuracies.    | All relationships are logical, well-defined, and correctly directed.               |
        | **Plausibility** | The architecture is unrealistic for the system's goals.     | The architecture is plausible but might be suboptimal.           | The architecture is highly plausible and follows common industry patterns.         |
        | **Clarity & Naming**| Element names are vague, inconsistent, or use jargon poorly.| Names are understandable but could be clearer.                 | Names are clear, concise, and follow standard naming conventions.                  |

        **Diagram to Evaluate:**
        ```puml
        {diagram}
        ```

        Please provide your JSON response now.
        """)
    ])

    structured_judge_llm = judge_llm.with_structured_output(rubric_schema)
    rubric_chain = rubric_prompt | structured_judge_llm

    try:
        results = rubric_chain.invoke({
            "diagram": diagram_code,
            "system_brief": system_brief
        })
        try:
            scores = [v['score'] for v in results.values() if isinstance(v, dict) and 'score' in v]
            average_score = sum(scores) / len(scores) if scores else 0.0
        except Exception:
            average_score = 0.0
        return {
            "diagram_name": diagram_name,
            "average_score": round(average_score, 2),
            "details": results
        }
    except Exception as e:
        return {"error": f"Failed to get rubric score: {e}"}

# ==============================================================================
# 6) Cross-level consistency (Context -> Container; Container -> Component)
# ==============================================================================

def _check_context_to_container(context_data: Dict, container_data: Dict) -> Tuple[bool, str]:
    """Two-way consistency check between Context and Container levels."""
    context_externals = _extract_element_names(context_data, ["person", "externalSystem"])
    container_externals = _extract_element_names(container_data, ["person", "externalSystem"])

    added = container_externals - context_externals
    missing = context_externals - container_externals

    errors = []
    if added:
        errors.append(f"Illegally added elements not found in Context: {sorted(added)}")
    if missing:
        errors.append(f"Elements from Context missing from diagram: {sorted(missing)}")

    if not errors:
        return (True, "External elements are consistent with the Context level.")
    else:
        return (False, " ".join(errors))

def _check_container_to_components(container_data: Dict, component_data_map: Dict) -> Dict:
    """Check each component diagram for consistency with the Container level."""
    results = {}
    container_known = _extract_element_names(container_data, ["container", "person", "externalSystem", "database"])

    for comp_name, comp_data in component_data_map.items():
        if not comp_data:
            continue
        comp_refs = _extract_element_names(comp_data, ["container", "person", "externalSystem", "database", "component"])
        mismatched = comp_refs - container_known
        key = f"Container->Component ({comp_name})"
        if not mismatched:
            results[key] = {"status": "Pass", "reason": "All references are consistent with the Container level."}
        else:
            results[key] = {"status": "Fail", "reason": f"References not found in Container scope: {sorted(mismatched)}"}
    return results

def evaluate_cross_level_consistency(c4_model: Dict[str, Any]) -> Dict[str, Any]:
    """Measures two-way consistency of elements across C4 levels."""
    print("🤖 Evaluating Metric: Cross-Level Consistency Check...")

    context_data = _parse_yaml_safe(c4_model.get("context", {}).get("yaml_definition"))
    container_data = _parse_yaml_safe(c4_model.get("containers", {}).get("yaml_definition"))
    component_data_map = {
        name: _parse_yaml_safe(data.get("yaml_definition", ""))
        for name, data in (c4_model.get("components") or {}).items()
    }

    details: Dict[str, Any] = {}

    if context_data and container_data:
        ok, reason = _check_context_to_container(context_data, container_data)
        details["Context->Container"] = {"status": "Pass" if ok else "Fail", "reason": reason}

    if container_data and component_data_map:
        comp_results = _check_container_to_components(container_data, component_data_map)
        details.update(comp_results)

    total = len(details)
    passed = sum(1 for v in details.values() if v["status"] == "Pass")
    score = (passed / total) * 100 if total > 0 else 100.0

    return {"metric": "Cross-Level Consistency", "score": round(score, 2), "passed": passed, "total": total, "details": details}

# ==============================================================================
# 7) Emergent naming consistency (detect dominant convention; flag outliers)
# ==============================================================================

def evaluate_emergent_naming_consistency(c4_model: Dict[str, Any]) -> Dict[str, Any]:
    """
    Detect dominant naming convention across elements and identify outliers.
    """
    print("🤖 Evaluating Metric 6 (New): Emergent Naming Consistency...")

    PATTERNS = {
        "PascalCase": r'^(?:[A-Z][a-z0-9]+)+$',
        "camelCase": r'^[a-z]+(?:[A-Z][a-z0-9]+)*$',
        "snake_case": r'^[a-z0-9]+(?:_[a-z0-9]+)*$',
        "kebab-case": r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
    }

    def classify(name: str) -> str:
        if not name:
            return "missing"
        for conv, pat in PATTERNS.items():
            if re.match(pat, name):
                return conv
        return "other"

    elements: List[Dict[str, str]] = []

    ctx = _parse_yaml_safe(c4_model.get("context", {}).get("yaml_definition"))
    if ctx.get("system"):
        elements.append({"type": "system", "name": ctx["system"].get("name", "")})

    cnt = _parse_yaml_safe(c4_model.get("containers", {}).get("yaml_definition"))
    for e in cnt.get("elements", []) or []:
        if e.get("type") == "container":
            elements.append({"type": "container", "name": e.get("name", "")})

    for comp_name, comp in (c4_model.get("components") or {}).items():
        comp_yaml = _parse_yaml_safe(comp.get("yaml_definition"))
        for e in comp_yaml.get("elements", []) or []:
            if e.get("type") == "component":
                elements.append({"type": f"component (in {comp_name})", "name": e.get("name", "")})

    total = len(elements)
    if total == 0:
        return {"metric": "Emergent Naming Consistency", "score": 100.0, "details": "No elements found to evaluate."}

    classes = [classify(e["name"]) for e in elements]
    counts = Counter(classes)

    dom = "none"
    top = [item for item in counts.most_common() if item[0] not in ["other", "missing"]]
    if top:
        dom = top[0][0]
    else:
        dom = counts.most_common(1)[0][0]

    outliers = []
    consistent = 0
    for idx, e in enumerate(elements):
        if classes[idx] == dom:
            consistent += 1
        else:
            outliers.append({
                "name": e.get("name", "[MISSING NAME]"),
                "type": e["type"],
                "detected_convention": classes[idx],
                "reason": f"Deviates from the dominant convention: '{dom}'"
            })

    score = (consistent / total) * 100
    return {
        "metric": "Emergent Naming Consistency",
        "score": round(score, 2),
        "dominantConvention": {
            "name": dom,
            "count": counts.get(dom, 0),
            "total": total
        },
        "allConventionCounts": dict(counts),
        "details": {"outliers": outliers} if outliers else "All names are internally consistent."
    }

# ==============================================================================
# 8) Principal architect critique (LLM judge; prompt preserved)
# ==============================================================================

def evaluate_architect_critique(system_brief: str, c4_model: Dict[str, Any], judge_llm) -> Dict[str, Any]:
    """
    Structured, qualitative critique of the entire C4 model from a Principal Architect.
    """
    print("⚖️ Evaluating Metric 7: Principal Architect's Critique...")

    architect_critique_schema = {
        "title": "PrincipalArchitectCritique",
        "description": "A senior-level review of a software architecture, providing both quantitative ratings and qualitative, narrative feedback.",
        "type": "object",
        "properties": {
            "executiveSummary": {"type": "string"},
            "feasibilityAndSoundness": {
                "type": "object",
                "properties": {
                    "rating": {"type": "integer"},
                    "critique": {"type": "string"},
                    "identifiedRisks": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["rating", "critique", "identifiedRisks"]
            },
            "clarityAndCommunication": {
                "type": "object",
                "properties": {
                    "rating": {"type": "integer"},
                    "critique": {"type": "string"}
                },
                "required": ["rating", "critique"]
            },
            "actionableRecommendation": {
                "type": "object",
                "properties": {
                    "recommendation": {"type": "string"},
                    "justification": {"type": "string"},
                    "priority": {"type": "string", "enum": ["Critical", "High", "Medium"]}
                },
                "required": ["recommendation", "justification", "priority"]
            }
        },
        "required": ["executiveSummary", "feasibilityAndSoundness", "clarityAndCommunication", "actionableRecommendation"]
    }

    docs: List[str] = []
    # Context
    docs.append("## Context Level Definition (YAML)\n```yaml\n" + (c4_model.get("context", {}).get("yaml_definition", "Not available") or "Not available") + "\n```")
    docs.append("\n## Context Level Diagram (PlantUML)\n```puml\n" + (c4_model.get("context", {}).get("diagram", "Not available") or "Not available") + "\n```")
    # Container
    docs.append("\n\n## Container Level Definition (YAML)\n```yaml\n" + (c4_model.get("containers", {}).get("yaml_definition", "Not available") or "Not available") + "\n```")
    docs.append("\n## Container Level Diagram (PlantUML)\n```puml\n" + (c4_model.get("containers", {}).get("diagram", "Not available") or "Not available") + "\n```")
    # Components (up to 2)
    cnt = 0
    for name, data in (c4_model.get("components") or {}).items():
        if cnt >= 2:
            break
        docs.append(f"\n\n## Component Level: {name} (YAML)\n```yaml\n" + (data.get("yaml_definition", "Not available") or "Not available") + "\n```")
        docs.append(f"\n## Component Level: {name} (PlantUML)\n```puml\n" + (data.get("diagram", "Not available") or "Not available") + "\n```")
        cnt += 1

    full_context = "\n".join(docs)

    critique_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a pragmatic Principal Software Architect... (persona is unchanged)"""),
        ("human", """Please review the following architecture.

        **Guiding Questions for Your Analysis:**
        1.  **Feasibility & Soundness:** Based on the brief and the YAML definitions, are the technology choices realistic? Does the decomposition make sense for scalability and performance? Identify the biggest architectural risk.
        2.  **Clarity & Communication:** Does this set of diagrams AND definitions effectively communicate the architecture? Is there a clear link between the definitions and the diagrams?
        3.  **Actionable Recommendation:** What is the single most important change you would recommend to this design and why?

        **System Design Brief:**
        ```
        {brief}
        ```

        **Generated C4 Architecture (Definitions & Diagrams):**
        {architecture_docs}

        Provide your structured JSON response now.
        """)
    ])

    structured_judge_llm = judge_llm.with_structured_output(architect_critique_schema)
    chain = critique_prompt | structured_judge_llm

    try:
        critique = chain.invoke({
            "brief": system_brief,
            "architecture_docs": full_context
        })
        return {"metric": "Principal Architect's Critique", "critique": critique}
    except Exception as e:
        return {"error": f"Failed to get architect's critique: {e}"}

# ==============================================================================
# 9) Security "Red Team" assessment (LLM judge; prompt preserved)
# ==============================================================================

def evaluate_security_assessment(system_brief: str, c4_model: Dict[str, Any], judge_llm) -> Dict[str, Any]:
    """
    Performs a threat modeling assessment on the container diagram from the
    perspective of a cybersecurity expert.
    """
    print("🛡️  Evaluating Metric 8: Security 'Red Team' Assessment...")

    container_diag = c4_model.get("containers", {}).get("diagram")
    if not container_diag:
        return {"error": "Container diagram not found, cannot perform security assessment."}

    security_assessment_schema = {
        "title": "SecurityThreatModel",
        "description": "A threat model report identifying potential security vulnerabilities in a software architecture.",
        "type": "object",
        "properties": {
            "executiveSummary": {"type": "string"},
            "vulnerabilities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "description": {"type": "string"},
                        "category": {
                            "type": "string",
                            "enum": ["Information Disclosure", "Insecure Data Flow", "Authentication Bypass", "Elevation of Privilege", "Denial of Service", "Missing Security Control"]
                        },
                        "severity": {"type": "string", "enum": ["Critical", "High", "Medium", "Low"]},
                        "recommendation": {"type": "string"}
                    },
                    "required": ["description", "category", "severity", "recommendation"]
                }
            }
        },
        "required": ["executiveSummary", "vulnerabilities"]
    }

    security_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a cybersecurity expert specializing in threat modeling and architectural security reviews. Your call sign is 'Red Specter'. Your job is to think like an attacker and identify potential weaknesses in the proposed design.

Your analysis should be based on the provided system brief and C4 Container diagram. You must format your entire response as a single JSON object that strictly adheres to the provided schema. Do not add any text outside the JSON object."""),
        ("human", """Please perform a security review of the following architecture.

        **Guiding Questions for Your Analysis:**
        1.  **Attack Surface Analysis:** Based on the diagram, what are the primary entry points for an external attacker? Which containers are most exposed?
        2.  **Data Flow Risks:** Where is sensitive patron data likely to be stored or processed? Are there any risky relationships shown, such as a public-facing container having direct access to the main database?
        3.  **Missing Controls:** What critical security components or considerations (e.g., an API Gateway, a dedicated authentication service, firewalls, rate limiting) appear to be missing from this architecture?

        **System Design Brief:**
        ```yaml
        {brief}
        ```

        **C4 Container Diagram:**
        ```puml
        {diagram}
        ```

        Provide your structured JSON threat model now.
        """)
    ])

    structured_judge_llm = judge_llm.with_structured_output(security_assessment_schema)
    chain = security_prompt | structured_judge_llm

    try:
        assessment = chain.invoke({
            "brief": system_brief,
            "diagram": container_diag
        })

        # Derive a simple risk score (lower is better)
        risk_weights = {"Critical": 10, "High": 5, "Medium": 2, "Low": 1}
        total_risk = 0
        for vuln in assessment.get("vulnerabilities", []):
            total_risk += risk_weights.get(vuln.get("severity"), 0)
        assessment["overallRiskScore"] = total_risk

        return {"metric": "Security 'Red Team' Assessment", "assessment": assessment}
    except Exception as e:
        return {"error": f"Failed to get security assessment: {e}"}

# ==============================================================================
# 10) Sequential completeness (your refined version)
# ==============================================================================

def check_c4_completeness(c4_model: Dict[str, Any]) -> Dict[str, Any]:
    """
    Checks for missing or empty C4 artifacts, respecting the sequential
    dependency between C4 levels.
    """
    print("🤖 Evaluating Metric: C4 Model Completeness...")

    def is_missing(value: Optional[str]) -> bool:
        return not value or not isinstance(value, str) or not value.strip()

    results: Dict[str, Any] = {}
    missing_count = 0
    total_expected = 0
    artifacts = ["analysis", "yaml_definition", "diagram"]

    # Context (always expected)
    total_expected += 3
    ctx = c4_model.get("context", {}) or {}
    ctx_status = {k: "Present" if not is_missing(ctx.get(k)) else "Missing" for k in artifacts}
    missing_count += list(ctx_status.values()).count("Missing")
    results["Context"] = ctx_status

    # Containers (only if context YAML exists)
    if not is_missing(ctx.get("yaml_definition")):
        total_expected += 3
        cnt = c4_model.get("containers", {}) or {}
        cnt_status = {k: "Present" if not is_missing(cnt.get(k)) else "Missing" for k in artifacts}
        missing_count += list(cnt_status.values()).count("Missing")
        results["Containers"] = cnt_status
    else:
        results["Containers"] = {k: "Not Expected" for k in artifacts}

    # Components
    results["Components"] = {}
    comps = c4_model.get("components", {}) or {}
    for comp_name, comp in comps.items():
        comp_status: Dict[str, str] = {}
        total_expected += 1  # analysis expected if the component key exists
        if is_missing(comp.get("analysis")):
            comp_status["analysis"] = "Missing"
            comp_status["yaml_definition"] = "Not Expected"
            comp_status["diagram"] = "Not Expected"
            missing_count += 1
        else:
            comp_status["analysis"] = "Present"
            total_expected += 2
            for k in ["yaml_definition", "diagram"]:
                if is_missing(comp.get(k)):
                    comp_status[k] = "Missing"
                    missing_count += 1
                else:
                    comp_status[k] = "Present"
        results["Components"][comp_name] = comp_status

    score = ((total_expected - missing_count) / total_expected) * 100 if total_expected > 0 else 100.0
    return {
        "metric": "C4 Model Completeness",
        "score": round(score, 2),
        "missing_count": missing_count,
        "total_expected_artifacts": total_expected,
        "details": results
    }

# ==============================================================================
# 11) Full evaluation runner (your layering; unchanged prompts and flow)
# ==============================================================================

def run_full_evaluation(
    system_brief: str,
    c4_model: Dict[str, Any],
    judge_model_name: Any,   # keep Any to align with your original usage
    temperature: float = 0.0
) -> Dict[str, Any]:
    """
    Runs a structured, level-aware evaluation of a C4 model, providing the
    correct context and source of truth to each metric.
    """
    print("\n" + "="*50)
    print(f"🏁 STARTING FULL C4 MODEL EVALUATION (Judge: {judge_model_name}) 🏁")
    print("="*50 + "\n")

    judge_llm = get_llm(model_name=judge_model_name, temperature=temperature)
    report: Dict[str, Any] = {
        "evaluationMetadata": {
            "judgeModel": judge_model_name,
            "judgeModelTemperature": temperature,
            "evaluationTimestamp": datetime.now().isoformat()
        }
    }

    # Layer 1: Holistic structural checks
    print("--- Running Holistic Structural Checks ---")
    report["compilationSuccess"] = evaluate_compilation_success(c4_model)
    report["abstractionAdherence"] = evaluate_abstraction_adherence(c4_model)
    report["missingInformation"] = check_c4_completeness(c4_model)
    report["emergentNamingConsistency"] = evaluate_emergent_naming_consistency(c4_model)

    # Layer 2: Level-specific semantic & qualitative
    print("\n--- Running Level-Specific Evaluations ---")

    if "context" in c4_model:
        print("  - Evaluating Context Level...")
        context_eval: Dict[str, Any] = {}
        context_diag = c4_model["context"].get("diagram")
        if context_diag:
            context_eval["semanticConsistency"] = evaluate_semantic_consistency(system_brief, c4_model, judge_llm)
            context_eval["qualitativeRubric"] = evaluate_qualitative_rubric(context_diag, "Context Diagram", system_brief, judge_llm)
        report["contextEvaluation"] = context_eval

    if "containers" in c4_model:
        print("  - Evaluating Container Level...")
        container_eval: Dict[str, Any] = {}
        container_diag = c4_model["containers"].get("diagram")
        container_yaml = c4_model["containers"].get("yaml_definition")
        if container_diag and container_yaml:
            container_eval["definitionalConsistency"] = evaluate_definitional_consistency(container_yaml, container_diag, "containers")
            container_eval["qualitativeRubric"] = evaluate_qualitative_rubric(container_diag, "Container Diagram", system_brief, judge_llm)
        report["containerEvaluation"] = container_eval

    if "components" in c4_model:
        print("  - Evaluating Component Level(s)...")
        component_evals: Dict[str, Any] = {}
        for comp_name, comp in c4_model["components"].items():
            comp_diag = comp.get("diagram")
            comp_yaml = comp.get("yaml_definition")
            if comp_diag and comp_yaml:
                component_evals[comp_name] = {
                    "definitionalConsistency": evaluate_definitional_consistency(comp_yaml, comp_diag, "components"),
                    "qualitativeRubric": evaluate_qualitative_rubric(comp_diag, f"Component: {comp_name}", system_brief, judge_llm),
                }
        report["componentEvaluations"] = component_evals

    # Layer 3: Holistic critiques
    print("\n--- Running Holistic Expert Critiques ---")
    report["architectCritique"] = evaluate_architect_critique(system_brief, c4_model, judge_llm)
    report["securityAssessment"] = evaluate_security_assessment(system_brief, c4_model, judge_llm)

    print("\n\n" + "="*50)
    print(f"📋 FINAL EVALUATION REPORT (Judge: {judge_model_name}) 📋")
    print("="*50 + "\n")
    print(json.dumps(report, indent=2))

    return report
