# src/graph.py
from __future__ import annotations

from typing import Literal, Type, List, Optional, Dict, Any
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
    checkpointer=None,
    model_name: ModelName = "gemini-2.5-flash",
    analysis_method: Literal["simple", "collaborative"] = "collaborative",
    collab_rounds: int = 2,
    experiment_condition: Optional[Dict[str, Any]] = None,
    memory_config: Optional[Dict[str, Any]] = None,
    temperature: float = 0.5,
) -> Type[StateGraph]:
    """
    Factory function to build the C4 Modeler workflow with experimental support.
    
    Args:
        checkpointer: LangGraph checkpointer (optional)
        model_name: LLM model to use
        analysis_method: Simple or collaborative analysis
        collab_rounds: Number of collaboration rounds
        experiment_condition: Experimental condition configuration
        memory_config: Memory system configuration
        temperature: LLM temperature (0.0 = deterministic, 1.0 = creative)
    """
    print(f"--- 🏗️ Building graph with model: '{model_name}' and analysis: '{analysis_method}' ---")
    
    if experiment_condition:
        print(f"🧪 Experimental condition: {experiment_condition.get('name', 'Unknown')}")
    
    if memory_config:
        print(f"🧠 Memory configuration: {memory_config.get('type', 'none')}")

    llm = get_llm(model_name=model_name, temperature=temperature)

    workflow = StateGraph(State)

    if analysis_method == "simple":
        bound_analysis_agent_node = functools.partial(analysis_agent_node, llm=llm)
        workflow.add_node("analysis", bound_analysis_agent_node)
    else:
        # Enhanced collaborative analysis with experimental support
        def experimental_collaborative_analysis(state):
            return collaborative_analysis_node(
                state, 
                llm=llm, 
                collab_rounds=collab_rounds,
                experiment_condition=experiment_condition,
                memory_config=memory_config
            )
        workflow.add_node("analysis", experimental_collaborative_analysis)

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
    if checkpointer:
        print("✅ LangGraph C4 Modeler compiled successfully with checkpointer!")
    else:
        print("✅ LangGraph C4 Modeler compiled successfully without checkpointer!")
    return app
