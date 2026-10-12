"""Explicit experimental conditions: team (in speaking order), personas and memory."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import yaml

from .prompts import PERSONAS

MEMORY_TYPES = {"none", "glossary"}
CONDITION_FIELDS = {"id", "studies", "description", "team", "memory"}


@dataclass(frozen=True)
class AgentSpec:
    persona_key: str
    display_name: str     # unique within the team, e.g. "Software Architect #2"
    role_name: str        # name used in the turn prompt, e.g. "Software Architect"
    persona: str


@dataclass(frozen=True)
class Condition:
    id: str
    studies: Tuple[str, ...]
    description: str
    team: Tuple[AgentSpec, ...]
    memory: str

    @property
    def team_keys(self) -> List[str]:
        return [a.persona_key for a in self.team]


@dataclass(frozen=True)
class GenerationSettings:
    model: str
    temperature: float
    rounds: int


def build_team(persona_keys: List[str]) -> Tuple[AgentSpec, ...]:
    counts = Counter(persona_keys)
    seen: Counter = Counter()
    team = []
    for key in persona_keys:
        if key not in PERSONAS:
            raise ValueError(f"unknown persona '{key}'")
        role_name, persona = PERSONAS[key]
        if not persona.strip():
            raise ValueError(f"empty persona text for '{key}'")
        seen[key] += 1
        display = f"{role_name} #{seen[key]}" if counts[key] > 1 else role_name
        team.append(AgentSpec(key, display, role_name, persona))
    return tuple(team)


def load_conditions(path: Path) -> Tuple[GenerationSettings, List[Condition]]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    gen = data["generation"]
    settings = GenerationSettings(model=gen["model"], temperature=float(gen["temperature"]), rounds=int(gen["rounds"]))
    conditions = []
    for raw in data["conditions"]:
        unknown = set(raw) - CONDITION_FIELDS
        if unknown:
            raise ValueError(f"{raw.get('id')}: unknown fields {sorted(unknown)}")
        if raw["memory"] not in MEMORY_TYPES:
            raise ValueError(f"{raw['id']}: memory must be one of {sorted(MEMORY_TYPES)}")
        if not raw["team"]:
            raise ValueError(f"{raw['id']}: empty team")
        conditions.append(Condition(id=raw["id"], studies=tuple(raw["studies"]), description=raw["description"],
                                    team=build_team(list(raw["team"])), memory=raw["memory"]))
    ids = [c.id for c in conditions]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate condition ids")
    return settings, conditions
