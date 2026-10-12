"""Scripted answers for the fake model: valid output for every pipeline step."""
from __future__ import annotations

import json
import re
from typing import Optional, Set

from masc4.llm import CallLog, FakeLLM

CONTEXT_YAML = """level: context
scope: "System Context diagram for Test System"
system:
  name: "Test System"
  description: "A system used in tests."
elements:
  - type: "person"
    name: "Clinician"
    description: "Uses the system."
  - type: "externalSystem"
    name: "Lab System"
    description: "Receives orders."
relationships:
  - source: "Clinician"
    destination: "Test System"
    description: "Uses"
    technology: "HTTPS"
"""

CONTAINER_YAML = """level: container
scope: "Container diagram for Test System"
system:
  name: "Test System"
elements:
  - type: "person"
    name: "Clinician"
    description: "Uses the system."
  - type: "externalSystem"
    name: "Lab System"
    description: "Receives orders."
  - type: "container"
    name: "Web App"
    technology: "React"
    description: "User interface."
  - type: "container"
    name: "Database"
    technology: "PostgreSQL"
    description: "Stores records."
relationships:
  - source: "Clinician"
    destination: "Web App"
    description: "Uses"
    technology: "HTTPS"
  - source: "Web App"
    destination: "Database"
    description: "Reads and writes"
    technology: "JDBC"
"""

COMPONENT_YAML = """level: component
scope: "Component diagram for the {parent} container"
parentContainer:
  name: "{parent}"
elements:
  - type: "component"
    name: "{parent} Controller"
    technology: "Spring MVC"
    description: "Handles requests."
  - type: "component"
    name: "{parent} Service"
    technology: "Spring"
    description: "Business logic."
relationships:
  - source: "{parent} Controller"
    destination: "{parent} Service"
    description: "Invokes"
"""

GLOSSARY = {"entities": [{"name": "Test System", "type": "software_system", "level": "context"}],
            "interfaces": [{"source": "Clinician", "destination": "Test System", "protocol": "HTTPS"}],
            "naming_conventions": ["Title Case names"]}


def respond(purpose: str, system: str, user: str, invalid_yaml_first: Set[str]) -> str:
    kind, scope = purpose.split("|")[:2]
    if kind == "turn":
        return f"{purpose.split('|')[2]} adds a point about {scope}."
    if kind == "writer":
        return f"## Overview\nDecisions for {scope}."
    if kind == "yaml":
        if scope in invalid_yaml_first and purpose.endswith("attempt1"):
            return "this is: not: valid: yaml: ["
        if scope == "context":
            return CONTEXT_YAML
        if scope == "container":
            return "```yaml\n" + CONTAINER_YAML + "```"   # fenced on purpose: must be stripped
        parent = re.match(r"component '(.*)'", scope).group(1)
        return COMPONENT_YAML.format(parent=parent)
    if kind == "diagram":
        macro = {"context": "System", "container": "Container"}.get(scope, "Component")
        return f"@startuml\n{macro}(x, \"X\", \"desc\")\n@enduml"
    if kind == "glossary":
        return json.dumps(GLOSSARY)
    raise AssertionError(f"unexpected purpose {purpose}")


def make_fake_llm(call_log: Optional[CallLog] = None, invalid_yaml_first: Optional[Set[str]] = None,
                  fail_on: Optional[str] = None) -> FakeLLM:
    bad = set(invalid_yaml_first or ())

    def responder(purpose: str, system: str, user: str) -> str:
        if fail_on and purpose.startswith(fail_on):
            raise RuntimeError(f"simulated API failure at {purpose}")
        return respond(purpose, system, user, bad)

    return FakeLLM(responder, call_log=call_log)
