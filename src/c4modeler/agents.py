# src/agents.py
from __future__ import annotations

import copy
import functools
import re
from collections import deque
from typing import Annotated, Dict, List, Optional, Sequence, TypedDict

import yaml
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

from .models import Agent
from .types import State
from .prompts import (
    # persona strings
    PERSONA_BY_ROLE,
    CONTEXT_TEAM_ROLES,
    CONTAINER_TEAM_ROLES,
    COMPONENT_TEAM_ROLES,
    # system prompts / templates
    REPORT_GENERATOR_SYSTEM_PROMPT,
    ANALYSIS_PERSONA_PROMPT,
    ANALYSIS_HUMAN_MESSAGE_PROMPT,
    YAML_PERSONA_PROMPT,
    YAML_HUMAN_MESSAGE_PROMPT,
    PLANTUML_PERSONA_PROMPT,
    PLANTUML_HUMAN_MESSAGE_PROMPT,
    CONTEXT_YAML_TEMPLATE,
    CONTAINER_YAML_TEMPLATE,
    COMPONENT_YAML_TEMPLATE,
    PLANTUML_SYNTAX_GUIDE,
)

# ============================================================================
# Helpers to build teams from roles (uses unchanged persona texts)
# ============================================================================

def build_context_team() -> List[Agent]:
    return [Agent(name=role, persona=PERSONA_BY_ROLE[role]) for role in CONTEXT_TEAM_ROLES]

def build_container_team() -> List[Agent]:
    return [Agent(name=role, persona=PERSONA_BY_ROLE[role]) for role in CONTAINER_TEAM_ROLES]

def build_component_team() -> List[Agent]:
    def persona_for(role: str) -> str:
        # Prefer L3-specific when present
        return (
            PERSONA_BY_ROLE.get(f"L3_{role}")
            or PERSONA_BY_ROLE.get(role, "")
        )
    return [Agent(name=role, persona=persona_for(role)) for role in COMPONENT_TEAM_ROLES]

# ============================================================================
# Collaborative analysis subgraph (multi-agent round-robin)
# ============================================================================

class CollaborativeAnalysisState(TypedDict):
    """Internal state for the collaborative analysis subgraph."""
    messages: Annotated[List[BaseMessage], add_messages]
    system_brief: str
    context: str
    level: str
    max_rounds: int
    final_analysis: str
    team: List[Agent]

def agent_node(state: CollaborativeAnalysisState, agent: Agent, llm: BaseChatModel) -> Dict:
    print(f"--- 🗣️  Turn: {agent.name} on C4 Level: '{state['level']}' ---")
    system_prompt = (
        "You are a member of an expert team collaboratively creating the analysis for a C4 model diagram.\n"
        f"Your current task is to analyze the provided system brief for the **C4 {state['level']} level**.\n"
        f"{state['context']}\n"
        "Your specific role is as follows:\n---\n"
        f"{agent.persona}\n---\n"
        "Read the conversation history and add your next insight based on your specific role. "
        "Provide your analysis directly and concisely."
    )
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
    ])
    chain = prompt_template | llm
    response = chain.invoke({"messages": state["messages"]})
    sanitized_name = re.sub(r"[^a-zA-Z0-9_-]", "_", agent.name)
    named_message = AIMessage(content=response.content, name=sanitized_name)
    return {"messages": [named_message]}

def report_generator_node(state: CollaborativeAnalysisState, llm: BaseChatModel) -> Dict:
    print("--- 🔬 Generating Final Analysis Report ---")
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", REPORT_GENERATOR_SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="messages"),
    ])
    chain = prompt_template | llm
    final_report = chain.invoke({
        "system_brief": state["system_brief"],
        "messages": state["messages"],
    }).content
    return {"final_analysis": final_report}

def collaboration_router(state: CollaborativeAnalysisState) -> str:
    """Routes based on rounds completed."""
    active_team = state["team"]
    num_ai_turns = len(state["messages"]) - 1  # minus initial human
    rounds_completed = num_ai_turns // len(active_team)
    if rounds_completed >= state["max_rounds"]:
        print(f"--- ✅ Collaboration Complete: Max rounds ({state['max_rounds']}) reached. ---")
        return "generate_report"
    else:
        return active_team[0].name  # loop back

def create_collaboration_graph(llm: BaseChatModel, team: List[Agent], max_rounds: int = 2):
    """Builds and returns a compiled collaborative analysis subgraph for the GIVEN TEAM."""
    builder = StateGraph(CollaborativeAnalysisState)

    for agent in team:
        node_name = re.sub(r"[^a-zA-Z0-9_-]", "_", agent.name)
        builder.add_node(node_name, functools.partial(agent_node, agent=agent, llm=llm))

    builder.add_node("generate_report", functools.partial(report_generator_node, llm=llm))

    entry_point = re.sub(r"[^a-zA-Z0-9_-]", "_", team[0].name)
    builder.set_entry_point(entry_point)

    for i in range(len(team) - 1):
        src = re.sub(r"[^a-zA-Z0-9_-]", "_", team[i].name)
        dst = re.sub(r"[^a-zA-Z0-9_-]", "_", team[i + 1].name)
        builder.add_edge(src, dst)

    last_agent = re.sub(r"[^a-zA-Z0-9_-]", "_", team[-1].name)
    first_agent = entry_point

    builder.add_conditional_edges(
        last_agent,
        collaboration_router,
        {
            "generate_report": "generate_report",
            first_agent: first_agent,
        },
    )

    builder.add_edge("generate_report", END)
    return builder.compile()


# ============================================================================
# Single-agent nodes used in the main pipeline
# ============================================================================


def analysis_agent_node(state: State, llm: BaseChatModel) -> Dict:
    """
    Generates the textual analysis for the next required C4 level,
    exactly like in your notebook (prompts unchanged).
    """
    system_brief = state["system_brief"]
    c4_model = state["c4_model"]
    component_target: Optional[str] = None

    if not c4_model.get("context"):
        level = "context"
        print("--- ✍️ Generating Context Level Analysis ---")
        context_blob = ""
    elif not c4_model.get("containers"):
        level = "container"
        print("--- ✍️ Generating Container Level Analysis ---")
        context_blob = f"**Context Level Analysis (for context):**\n{c4_model['context']['analysis']}"
    else:
        component_queue: deque[str] = state.get("component_queue", deque())
        if component_queue:
            component_target = component_queue[0]
            level = "component"
            print(f"--- ✍️ Generating Component Level Analysis for '{component_target}' ---")
            context_blob = f"**Container Level Analysis (for context):**\n{c4_model['containers']['analysis']}"
        else:
            return {}
        
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", ANALYSIS_PERSONA_PROMPT),
        ("human", ANALYSIS_HUMAN_MESSAGE_PROMPT),
    ])

    analysis_chain = prompt_template | llm | StrOutputParser()

    analysis = analysis_chain.invoke({
        "level": level,
        "brief": system_brief,
        "context": context_blob,
        "component_target": component_target or "",
    })

    updated_model = copy.deepcopy(c4_model)
    if level == "context":
        updated_model["context"] = {"analysis": analysis}
    elif level == "container":
        updated_model["containers"] = {"analysis": analysis}
    elif level == "component" and component_target:
        if "components" not in updated_model:
            updated_model["components"] = {}
        updated_model["components"][component_target] = {"analysis": analysis}

    return {"c4_model": updated_model}

def yaml_structure_node(state: State, llm: BaseChatModel) -> Dict:
    """
    Converts textual analysis to YAML using your templates (unchanged).
    """
    c4_model = state["c4_model"]
    component_target: Optional[str] = None

    if c4_model.get("context", {}).get("analysis") and not c4_model.get("context", {}).get("yaml_definition"):
        level = "context"
        print("--- 📝 Generating Context Level YAML ---")
        analysis = c4_model["context"]["analysis"]
        template = CONTEXT_YAML_TEMPLATE
        ctx = ""
    elif c4_model.get("containers", {}).get("analysis") and not c4_model.get("containers", {}).get("yaml_definition"):
        level = "container"
        print("--- 📝 Generating Container Level YAML ---")
        analysis = c4_model["containers"]["analysis"]
        template = CONTAINER_YAML_TEMPLATE
        ctx = f"Context Level YAML (for reference):\n{c4_model['context']['yaml_definition']}"
    else:
        component_queue: deque[str] = state.get("component_queue", deque())
        if component_queue:
            component_target = component_queue[0]
            if c4_model.get("components", {}).get(component_target, {}).get("analysis") and not c4_model.get("components", {}).get(component_target, {}).get("yaml_definition"):
                level = "component"
                print(f"--- 📝 Generating Component Level YAML for '{component_target}' ---")
                analysis = c4_model["components"][component_target]["analysis"]
                template = COMPONENT_YAML_TEMPLATE
                ctx = f"Container Level YAML (for reference):\n{c4_model['containers']['yaml_definition']}"
            else:
                return {}
        else:
            return {}

    prompt = ChatPromptTemplate.from_messages([
        ("system", YAML_PERSONA_PROMPT),
        ("human", YAML_HUMAN_MESSAGE_PROMPT),
    ])
    chain = prompt | llm | StrOutputParser()

    yaml_output = chain.invoke({
        "analysis": analysis,
        "template": template,
        "context": ctx,
    })

    updated_model = copy.deepcopy(c4_model)
    if level == "context":
        updated_model["context"]["yaml_definition"] = yaml_output
    elif level == "container":
        updated_model["containers"]["yaml_definition"] = yaml_output
    elif level == "component" and component_target:
        if component_target not in updated_model.get("components", {}):
            updated_model.setdefault("components", {})
            updated_model["components"][component_target] = {}
        updated_model["components"][component_target]["yaml_definition"] = yaml_output

    return {"c4_model": updated_model}

def plantuml_diagram_node(state: State, llm: BaseChatModel) -> Dict:
    """
    Generates PlantUML code from YAML + analysis using your syntax guide (unchanged).
    """
    c4_model = state["c4_model"]
    component_target: Optional[str] = None

    if c4_model.get("context", {}).get("yaml_definition") and not c4_model.get("context", {}).get("diagram"):
        level = "context"
        print(f"--- 🎨 Generating {level.capitalize()} Level Diagram ---")
        analysis = c4_model["context"]["analysis"]
        yaml_def = c4_model["context"]["yaml_definition"]
    elif c4_model.get("containers", {}).get("yaml_definition") and not c4_model.get("containers", {}).get("diagram"):
        level = "container"
        print(f"--- 🎨 Generating {level.capitalize()} Level Diagram ---")
        analysis = c4_model["containers"]["analysis"]
        yaml_def = c4_model["containers"]["yaml_definition"]
    else:
        component_queue: deque[str] = state.get("component_queue", deque())
        if component_queue:
            component_target = component_queue[0]
            comp = c4_model.get("components", {}).get(component_target, {})
            if comp.get("yaml_definition") and not comp.get("diagram"):
                level = "component"
                print(f"--- 🎨 Generating {level.capitalize()} Level Diagram for '{component_target}' ---")
                analysis = comp["analysis"]
                yaml_def = comp["yaml_definition"]
            else:
                return {}
        else:
            return {}

    prompt = ChatPromptTemplate.from_messages([
        ("system", PLANTUML_PERSONA_PROMPT),
        ("human", PLANTUML_HUMAN_MESSAGE_PROMPT),
    ])
    chain = prompt | llm | StrOutputParser()

    diagram_code = chain.invoke({
        "syntax_guide": PLANTUML_SYNTAX_GUIDE,
        "yaml_def": yaml_def,
        "analysis": analysis,
    })

    updated_model = copy.deepcopy(c4_model)
    if level == "context":
        updated_model["context"]["diagram"] = diagram_code
    elif level == "container":
        updated_model["containers"]["diagram"] = diagram_code
    elif level == "component" and component_target:
        updated_model.setdefault("components", {})
        updated_model["components"].setdefault(component_target, {})
        updated_model["components"][component_target]["diagram"] = diagram_code

    return {"c4_model": updated_model}


# ============================================================================
# Queue management & routers for components
# ============================================================================

def populate_component_queue_node(state: State) -> Dict:
    """
    Parses the container YAML to find container names and adds them to the queue.
    """
    print("--- ⚙️ Populating Component Queue ---")
    container_yaml = state["c4_model"]["containers"]["yaml_definition"]
    try:
        data = yaml.safe_load(container_yaml) or {}
        names = [e["name"] for e in data.get("elements", []) if e.get("type") == "container"]
        print(f"Found containers to process: {names}")
        return {"component_queue": deque(names)}
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return {}

def complete_component_node(state: State) -> Dict:
    """
    Pops the completed component from the front of the queue.
    """
    print("--- ✅ Completing Component Task ---")
    queue = state["component_queue"]
    if queue:
        finished = queue.popleft()
        print(f"Finished processing: {finished}")
    return {"component_queue": queue}

def should_process_components(state: State) -> str:
    """
    Router that checks the component queue to decide whether to continue or end.
    """
    print("--- 🤔 Checking Component Queue ---")
    if state["component_queue"]:
        print("Queue is not empty. Processing next component.")
        return "process_component"
    else:
        print("Queue is empty. Finishing workflow.")
        return "end_workflow"

def post_diagram_router(state: State) -> str:
    """
    Decide next step after any diagram is generated.
    """
    model = state["c4_model"]
    if model.get("context", {}).get("diagram") and not model.get("containers"):
        return "analysis"
    elif model.get("containers", {}).get("diagram") and state.get("component_queue") is None:
        return "populate_queue"
    else:
        return "complete_component"
    

def collaborative_analysis_node(state: State, llm: BaseChatModel, collab_rounds: int = 2) -> Dict:
    """
    This node acts as a smart orchestrator. It determines the C4 level,
    selects the correct expert team, and invokes the appropriate subgraph.
    """
    print("--- 🚀 Orchestrating Collaborative Analysis ---")

    # 1. Determine the current C4 level and select the appropriate team
    level = ""
    component_target = None
    active_team: List[Agent] = [] # The team we will use for the subgraph

    if not state["c4_model"].get("context"):
        level = "context"
        active_team = build_context_team()
        print("--- Selecting Team: Context Level ---")
    elif not state["c4_model"].get("containers"):
        level = "container"
        active_team = build_container_team()
        print("--- Selecting Team: Container Level ---")
    else:
        level = "component"
        active_team = build_component_team()
        if state.get("component_queue"):
            component_target = state["component_queue"][0]
        print(f"--- Selecting Team: Component Level for '{component_target}' ---")

    # 2. Create the specialized subgraph using the selected team
    # <<< CHANGED: Pass the active_team to the factory >>>
    analysis_subgraph = create_collaboration_graph(
        llm=llm,
        team=active_team,
        max_rounds=collab_rounds
    )

    # 3. Prepare the input for the subgraph
    subgraph_level_description = f"component '{component_target}'" if component_target else level
    subgraph_input = {
        "messages": [HumanMessage(content=f"Let's begin the C4 analysis for the {subgraph_level_description}:\n\n{state['system_brief']}")],
        "system_brief": state['system_brief'],
        "context": state['c4_model'].get('context', {}).get('analysis', ''),
        "level": subgraph_level_description,
        "max_rounds": collab_rounds,
        "team": active_team, # <<< CRITICAL: Pass the team into the subgraph's state
    }

    # 4. Invoke the subgraph
    print(f"--- Invoking subgraph for: {subgraph_level_description} ---")
    subgraph_output = analysis_subgraph.invoke(subgraph_input)
    final_analysis = subgraph_output['final_analysis']

    # 5. Update the main graph's state with the result
    print(f"--- ✅ Subgraph complete. Updating main C4 model for: {subgraph_level_description} ---")
    updated_model = copy.deepcopy(state['c4_model'])

    if level == "context":
        updated_model["context"] = {"analysis": final_analysis}
    elif level == "container":
        updated_model["containers"] = {"analysis": final_analysis}
    elif level == "component" and component_target:
        if "components" not in updated_model:
            updated_model["components"] = {}
        if component_target not in updated_model["components"]:
            updated_model["components"][component_target] = {}
        updated_model["components"][component_target]["analysis"] = final_analysis
        print(f"--- Successfully updated analysis for component: '{component_target}' ---")

    return {"c4_model": updated_model}
