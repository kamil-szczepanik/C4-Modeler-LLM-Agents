from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Agent:
    """Lightweight holder for a role name and its persona text."""
    name: str
    persona: str
