# src/graph.py
from __future__ import annotations

from typing import Literal, Type, List
from collections import deque
import copy
import functools

from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage

from .llm import get_llm, ModelName
from .types import State
from .models import Agent
from .agents import (
    analysis_agent_node,
    yaml_structure_node,
    plantuml_diagram_node,
    populate_component_queue_node,
    complete_component_node,
    should_process_components,
    post_diagram_router,
    create_collaboration_graph,
    # team builders use your exact personas from prompts.py
    build_context_team,
    build_container_team,
    build_component_team,
    collaborative_analysis_node,
)

def create_c4_modeler_graph(
    checkpointer,
    model_name: ModelName = "gemini-1.5-flash-latest",
    analysis_method: Literal["simple", "collaborative"] = "collaborative",
    collab_rounds: int = 2,
) -> Type[StateGraph]:
    """
    Factory function to build the C4 Modeler workflow.
    """
    print(f"--- 🏗️ Building graph with model: '{model_name}' and analysis: '{analysis_method}' ---")

    llm = get_llm(model_name=model_name)

    workflow = StateGraph(State)

    if analysis_method == "simple":
        bound_analysis_agent_node = functools.partial(analysis_agent_node, llm=llm)
        workflow.add_node("analysis", bound_analysis_agent_node)
    else:
        workflow.add_node("analysis", 
                          lambda s: collaborative_analysis_node(s, llm=llm, collab_rounds=collab_rounds))

    # --- Remaining nodes & edges (unchanged) ---
    bound_yaml_structure_node = functools.partial(yaml_structure_node, llm=llm)
    bound_plantuml_diagram_node = functools.partial(plantuml_diagram_node, llm=llm)

    workflow.add_node("yaml", bound_yaml_structure_node)
    workflow.add_node("diagram", bound_plantuml_diagram_node)
    workflow.add_node("populate_queue", populate_component_queue_node)
    workflow.add_node("complete_component", complete_component_node)

    workflow.set_entry_point("analysis")
    workflow.add_edge("analysis", "yaml")
    workflow.add_edge("yaml", "diagram")

    workflow.add_conditional_edges("diagram", post_diagram_router, {
        "analysis": "analysis",
        "populate_queue": "populate_queue",
        "complete_component": "complete_component",
    })
    workflow.add_conditional_edges(
        "populate_queue", should_process_components,
        {"process_component": "analysis", "end_workflow": END},
    )
    workflow.add_conditional_edges(
        "complete_component", should_process_components,
        {"process_component": "analysis", "end_workflow": END},
    )

    app = workflow.compile(checkpointer=checkpointer)
    print("✅ LangGraph C4 Modeler compiled successfully with checkpointer!")
    return app
