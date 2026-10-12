from __future__ import annotations

from collections import deque
from typing import TypedDict, Dict, Sequence, Optional, Any, List
from langchain_core.messages import BaseMessage

# Artifacts for a single C4 level/diagram
class LevelOutput(TypedDict, total=False):
    analysis: str             # textual analysis
    yaml_definition: str      # structured YAML
    diagram: str              # PlantUML diagram code

# Complete C4 model across levels
class C4Model(TypedDict):
    context: LevelOutput
    containers: LevelOutput
    # Components keyed by container name
    components: Dict[str, LevelOutput]

# Global state carried through your LangGraph app
class State(TypedDict):
    messages: Sequence[BaseMessage]
    system_brief: str
    c4_model: C4Model
    component_queue: Optional[deque[str]]  # None until populated after container diagram
    # Enhanced experimental state
    experiment_condition: Optional[Dict[str, Any]]
    memory_system: Optional[Any]  # SharedMemorySystem (avoiding circular import)
    speaking_order: Optional[List[str]]
    current_speaker_index: int
    experimental_metadata: Optional[Dict[str, Any]]
