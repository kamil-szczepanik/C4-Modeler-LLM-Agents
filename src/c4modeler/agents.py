# src/agents.py
from __future__ import annotations

import copy
import functools
import re
from collections import deque
from typing import Annotated, Dict, List, Optional, Sequence, TypedDict, Any

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
# Utility functions for output cleaning
# ============================================================================

def strip_markdown_code_fences(text: str) -> str:
    """
    Remove markdown code fences from LLM output.
    
    Many LLMs (especially Gemini) wrap their output in markdown code fences like:
    ```yaml
    content here
    ```
    
    This function strips those fences to get the raw content.
    """
    if not text:
        return text
    
    text = text.strip()
    
    # Check for code fence at start
    if text.startswith("```"):
        lines = text.split("\n")
        # Remove first line (```yaml, ```plantuml, etc.)
        lines = lines[1:]
        
        # Remove last line if it's ```
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        
        text = "\n".join(lines)
    
    return text.strip()

# ============================================================================
# Helpers to build teams from roles (enhanced for experiments)
# ============================================================================

def build_experimental_team(level: str, experiment_condition: Dict[str, Any]) -> List[Agent]:
    """Build team using experimental configuration."""
    try:
        from .agent_factory import ExperimentalAgentFactory
        factory = ExperimentalAgentFactory()
        return factory.create_team_for_experiment(experiment_condition, level)
    except ImportError:
        print("⚠️ ExperimentalAgentFactory not available, falling back to default teams")
        # Fallback to default teams
        if level == "context":
            return build_context_team()
        elif level == "container":
            return build_container_team()
        else:
            return build_component_team()

def build_context_team(experiment_condition: Optional[Dict] = None) -> List[Agent]:
    """Build context team with optional experimental configuration."""
    if experiment_condition:
        from .agent_factory import ExperimentalAgentFactory
        factory = ExperimentalAgentFactory()
        return factory.create_team_for_experiment(experiment_condition, "context")
    return [Agent(name=role, persona=PERSONA_BY_ROLE[role]) for role in CONTEXT_TEAM_ROLES]

def build_container_team(experiment_condition: Optional[Dict] = None) -> List[Agent]:
    """Build container team with optional experimental configuration."""
    if experiment_condition:
        from .agent_factory import ExperimentalAgentFactory
        factory = ExperimentalAgentFactory()
        return factory.create_team_for_experiment(experiment_condition, "containers")
    return [Agent(name=role, persona=PERSONA_BY_ROLE[role]) for role in CONTAINER_TEAM_ROLES]

def build_component_team(experiment_condition: Optional[Dict] = None) -> List[Agent]:
    """Build component team with optional experimental configuration."""
    if experiment_condition:
        from .agent_factory import ExperimentalAgentFactory
        factory = ExperimentalAgentFactory()
        return factory.create_team_for_experiment(experiment_condition, "components")
    
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

def _extract_key_context(c4_model: Dict, current_level: str) -> str:
    """
    Extract only key decisions from previous C4 levels to provide minimal context.
    This prevents token explosion by avoiding full analysis text repetition.
    """
    context_parts = []
    
    if current_level in ["container", "component"]:
        # For container/component level, extract key info from context level
        context_analysis = c4_model.get("context", {}).get("analysis", "")
        if context_analysis:
            # Extract only essential elements - try to parse YAML if available
            context_yaml = c4_model.get("context", {}).get("yaml_definition", "")
            if context_yaml:
                try:
                    parsed = yaml.safe_load(context_yaml)
                    system_name = parsed.get("system", {}).get("name", "Unknown System")
                    elements = parsed.get("elements", [])
                    people = [e["name"] for e in elements if e.get("type") == "person"]
                    external = [e["name"] for e in elements if e.get("type") == "externalSystem"]
                    
                    context_parts.append(f"- System: {system_name}")
                    if people:
                        context_parts.append(f"- Users: {', '.join(people)}")
                    if external:
                        context_parts.append(f"- External Systems: {', '.join(external)}")
                except:
                    # Fallback: just mention that context exists
                    context_parts.append("- System context defined in previous level")
    
    if current_level == "component":
        # For component level, extract container info
        container_yaml = c4_model.get("containers", {}).get("yaml_definition", "")
        if container_yaml:
            try:
                parsed = yaml.safe_load(container_yaml)
                elements = parsed.get("elements", [])
                containers = [
                    f"{e['name']} ({e.get('technology', 'N/A')})" 
                    for e in elements if e.get("type") == "container"
                ]
                if containers:
                    context_parts.append(f"- Containers: {', '.join(containers)}")
            except:
                context_parts.append("- Container architecture defined in previous level")
    
    return "\n".join(context_parts) if context_parts else ""

def _extract_yaml_context_for_generation(c4_model: Dict, target_level: str) -> str:
    """
    Extract minimal YAML context needed for generating the next level.
    For YAML generation, we need structure references from previous levels.
    """
    if target_level == "container":
        # For container YAML, include the context YAML (it's small and needed for structure)
        context_yaml = c4_model.get("context", {}).get("yaml_definition", "")
        if context_yaml:
            return f"**Context Level YAML (for reference on system name and external entities):**\n```yaml\n{context_yaml}\n```"
        return ""
    
    elif target_level == "component":
        # For component YAML, only include the container names list, not full YAML
        container_yaml = c4_model.get("containers", {}).get("yaml_definition", "")
        if container_yaml:
            try:
                parsed = yaml.safe_load(container_yaml)
                system_name = parsed.get("system", {}).get("name", "System")
                elements = parsed.get("elements", [])
                containers = [e["name"] for e in elements if e.get("type") == "container"]
                
                return f"**Reference Info:**\n- System: {system_name}\n- Containers defined: {', '.join(containers)}"
            except:
                pass
        return ""
    
    return ""

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
    
    # Highly optimized prompt: forces agents to be concise and avoid repetition
    system_prompt = (
        "You are {persona_short} contributing to a C4 model analysis for **{level}**.\n"
        "\n"
        "ROLE:\n{persona}\n"
        "\n"
        "RULES - READ CAREFULLY:\n"
        "• Write 2-3 SHORT paragraphs ONLY from YOUR role's perspective\n"
        "• DO NOT repeat, summarize, or acknowledge what others already said\n"
        "• DO NOT use phrases like 'As mentioned', 'Building on', 'The X said', 'I agree with'\n"
        "• If others already covered a point, SKIP it - only add NEW insights\n"
        "• Be direct and specific - state YOUR concerns or recommendations\n"
        "• Maximum 150 words\n"
        "\n"
        "Write your analysis now:"
    )
    
    # Limit message history to reduce token usage and prevent overwhelming context
    # Only include: initial message + last 4 agent messages (not all history)
    messages = state["messages"]
    
    if len(messages) > 6:  # Initial HumanMessage + 5+ agent messages
        # Keep the first message (system brief) and last 4 agent responses
        limited_messages = [messages[0]] + messages[-4:]
    else:
        limited_messages = messages
    
    # Extract short persona identifier for the prompt
    persona_short = agent.name.replace("_", " ")
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
    ])
    chain = prompt_template | llm
    response = chain.invoke({
        "messages": limited_messages,
        "level": state["level"],
        "persona": agent.persona,
        "persona_short": persona_short
    })
    
    # Create sanitized name for the agent
    sanitized_name = re.sub(r"[^a-zA-Z0-9_-]", "_", agent.name)
    
    # Store as HumanMessage with agent's name so other agents see it as peer input
    # This creates natural multi-agent dialogue where agents respond to each other as collaborators
    named_message = HumanMessage(content=response.content, name=sanitized_name)
    
    return {"messages": [named_message]}

def report_generator_node(state: CollaborativeAnalysisState, llm: BaseChatModel) -> Dict:
    print("--- 🔬 Generating Final Analysis Report ---")
    
    # Extremely concise prompt
    report_system_prompt = (
        "Extract architectural decisions from the discussion into a structured summary.\n"
        "\n"
        "CRITICAL REQUIREMENTS:\n"
        "• Use EXACTLY the format provided in the template\n"
        "• Maximum 300 words total\n"
        "• Use bullet points, NOT paragraphs\n"
        "• Include specific names, technologies, and protocols\n"
        "• NO explanations of the discussion process\n"
        "• Extract ONLY final decisions\n"
    )
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", report_system_prompt),
        ("human", REPORT_GENERATOR_SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="messages"),
    ])
    chain = prompt_template | llm
    final_report = chain.invoke({
        "system_brief": state["system_brief"],
        "messages": state["messages"],
    }).content
    return {"final_analysis": final_report}

def collaboration_router(state: CollaborativeAnalysisState) -> str:
    """Routes based on rounds completed. Returns either 'generate_report' or first agent name."""
    import re
    active_team = state["team"]
    num_ai_turns = len(state["messages"]) - 1  # minus initial human
    rounds_completed = num_ai_turns // len(active_team)
    
    if rounds_completed >= state["max_rounds"]:
        print(f"--- ✅ Collaboration Complete: Max rounds ({state['max_rounds']}) reached. ---")
        return "generate_report"
    else:
        # Return first agent's unique name to start next round
        # This works because edges already handle the sequential flow through all agents
        first_agent_base = re.sub(r"[^a-zA-Z0-9_-]", "_", active_team[0].name)
        
        # The first agent always uses the base name (no suffix)
        return first_agent_base

def create_collaboration_graph(llm: BaseChatModel, team: List[Agent], max_rounds: int = 2):
    """Builds and returns a compiled collaborative analysis subgraph for the GIVEN TEAM."""
    builder = StateGraph(CollaborativeAnalysisState)

    # Create unique node names by adding indices for duplicate roles
    # This handles cases like ["Architect", "Architect", "Architect", "Architect"]
    node_names = []
    name_counts = {}
    
    for agent in team:
        base_name = re.sub(r"[^a-zA-Z0-9_-]", "_", agent.name)
        
        # Track how many times we've seen this name
        if base_name in name_counts:
            name_counts[base_name] += 1
            # Add index to make it unique: "Lead_Software_Architect_2", "Lead_Software_Architect_3", etc.
            unique_name = f"{base_name}_{name_counts[base_name]}"
        else:
            name_counts[base_name] = 1
            unique_name = base_name
        
        node_names.append(unique_name)
    
    # Add nodes with unique names
    for i, (agent, node_name) in enumerate(zip(team, node_names)):
        builder.add_node(node_name, functools.partial(agent_node, agent=agent, llm=llm))

    builder.add_node("generate_report", functools.partial(report_generator_node, llm=llm))

    # Use the unique node names for routing
    entry_point = node_names[0]
    builder.set_entry_point(entry_point)

    for i in range(len(node_names) - 1):
        builder.add_edge(node_names[i], node_names[i + 1])

    # Last agent node (with proper unique name)
    last_agent_node = node_names[-1]

    builder.add_conditional_edges(
        last_agent_node,
        collaboration_router,
        {
            "generate_report": "generate_report",
            entry_point: entry_point,  # Loop back to first agent for next round
        },
    )

    builder.add_edge("generate_report", END)
    return builder.compile()


# ============================================================================
# Single-agent nodes used in the main pipeline
# ============================================================================


def analysis_agent_node(state: State, llm: BaseChatModel) -> Dict:
    """
    Generates the textual analysis for the next required C4 level.
    Uses condensed context to minimize token usage.
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
        # Use condensed context instead of full analysis
        context_blob = f"**Prior Decisions:**\n{_extract_key_context(c4_model, 'container')}"
    else:
        component_queue = state.get("component_queue")  # Don't default to deque()!
        if component_queue:
            component_target = component_queue[0]
            level = "component"
            print(f"--- ✍️ Generating Component Level Analysis for '{component_target}' ---")
            # Use condensed context instead of full analysis
            context_blob = f"**Prior Decisions:**\n{_extract_key_context(c4_model, 'component')}"
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
        # Include context YAML for structure reference (it's small, ~200-400 tokens)
        ctx = _extract_yaml_context_for_generation(c4_model, 'container')
    else:
        component_queue = state.get("component_queue")  # Don't default to deque()!
        if component_queue:
            component_target = component_queue[0]
            if c4_model.get("components", {}).get(component_target, {}).get("analysis") and not c4_model.get("components", {}).get(component_target, {}).get("yaml_definition"):
                level = "component"
                print(f"--- 📝 Generating Component Level YAML for '{component_target}' ---")
                analysis = c4_model["components"][component_target]["analysis"]
                template = COMPONENT_YAML_TEMPLATE
                # Include minimal container reference
                ctx = f"Parent container: {component_target}\n{_extract_yaml_context_for_generation(c4_model, 'component')}"
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
    
    # Clean markdown code fences that LLMs (especially Gemini) often add
    yaml_output = strip_markdown_code_fences(yaml_output)

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
        component_queue = state.get("component_queue")  # Don't default to deque()!
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
    
    # Clean markdown code fences that LLMs (especially Gemini) often add
    diagram_code = strip_markdown_code_fences(diagram_code)

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
    Enhanced version with robust YAML parsing and multiple extraction strategies.
    """
    print("--- Populating Component Queue ---")
    
    try:
        container_yaml = state["c4_model"]["containers"]["yaml_definition"]
        print(f"Container YAML length: {len(container_yaml)} chars")
        
        data = yaml.safe_load(container_yaml) or {}
        print(f"Parsed YAML keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}")
        
        names = []
        
        # Strategy 1: elements array with type=container (ACTUAL STRUCTURE!)
        if isinstance(data, dict) and 'elements' in data:
            elements = data['elements']
            if isinstance(elements, list):
                # Filter for elements with type="container"
                containers = [e for e in elements if isinstance(e, dict) and e.get("type") == "container"]
                names = [c.get("name") for c in containers if c.get("name")]
                print(f"Strategy 1 (elements with type=container): Found {len(names)} containers: {names}")
        
        # Strategy 2: direct containers array/dict (fallback)
        elif isinstance(data, dict) and 'containers' in data:
            containers = data['containers']
            if isinstance(containers, list):
                names = [c.get("name", str(c)) for c in containers if c]
            elif isinstance(containers, dict):
                names = list(containers.keys())
            print(f"Strategy 2 (containers): Found {len(names)} containers: {names}")
        
        # Strategy 3: assume top-level keys are containers (fallback)
        elif isinstance(data, dict) and data:
            # Filter out metadata keys that aren't containers
            metadata_keys = {'name', 'description', 'version', 'type', 'technology_stack', 'overview', 'level', 'scope', 'system'}
            potential_containers = {}
            for k, v in data.items():
                if k not in metadata_keys and isinstance(v, dict):
                    potential_containers[k] = v
            names = list(potential_containers.keys())
            print(f"Strategy 3 (top-level): Found {len(names)} containers: {names}")
        
        if names:
            print(f"Successfully found {len(names)} containers to process: {names}")
            return {"component_queue": deque(names)}
        else:
            print("No containers found in YAML - skipping component generation")
            print(f"Container YAML preview: {container_yaml[:500]}...")
            return {"component_queue": deque()}  # Empty queue to prevent crash
            
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        print(f"Raw YAML: {container_yaml[:300]}...")
        return {"component_queue": deque()}
    except Exception as e:
        print(f"Unexpected error in component queue population: {e}")
        return {"component_queue": deque()}

def complete_component_node(state: State) -> Dict:
    """
    Pops the completed component from the front of the queue.
    """
    print("--- Completing Component Task ---")
    queue = state["component_queue"]
    if queue:
        finished = queue.popleft()
        print(f"Finished processing: {finished}")
    return {"component_queue": queue}

def should_process_components(state: State) -> str:
    """
    Router that checks the component queue to decide whether to continue or end.
    """
    print("--- Checking Component Queue ---")
    if state["component_queue"]:
        print("Queue is not empty. Processing next component.")
        return "process_component"
    else:
        print("Queue is empty. Finishing workflow.")
        return "end_workflow"

def post_diagram_router(state: State) -> str:
    """
    Decide next step after any diagram is generated.
    Fixed to handle both None and empty deque for component_queue.
    """
    model = state["c4_model"]
    component_queue = state.get("component_queue")
    
    # After context diagram -> continue to containers
    if model.get("context", {}).get("diagram") and not model.get("containers"):
        print("Router: Context done -> Continue to Container analysis")
        return "analysis"
    
    # After container diagram -> populate component queue (if not done yet)
    # Check if queue is None (not yet populated) - don't check if it's just empty!
    elif model.get("containers", {}).get("diagram") and component_queue is None:
        print("Router: Container done -> Populate component queue")
        # print(f"DEBUG: component_queue value = {component_queue}, type = {type(component_queue)}")
        return "populate_queue"
    
    # After component diagram -> complete current component (which will check queue and route appropriately)
    else:
        print("Router: Component diagram done -> Complete current component")
        # print(f"DEBUG: component_queue value = {component_queue}, type = {type(component_queue)}")
        return "complete_component"
    

def collaborative_analysis_node(
    state: State, 
    llm: BaseChatModel, 
    collab_rounds: int = 2,
    experiment_condition: Optional[Dict[str, Any]] = None,
    memory_config: Optional[Dict[str, Any]] = None
) -> Dict:
    """
    This node acts as a smart orchestrator. It determines the C4 level,
    selects the correct expert team, and invokes the appropriate subgraph.
    Enhanced with experimental configuration support.
    """
    print("--- 🚀 Orchestrating Collaborative Analysis ---")
    
    if experiment_condition:
        print(f"🧪 Using experimental condition: {experiment_condition}")
    if memory_config:
        print(f"🧠 Memory configuration: {memory_config}")

    # 1. Determine the current C4 level and select the appropriate team
    level = ""
    component_target = None
    active_team: List[Agent] = [] # The team we will use for the subgraph

    if not state["c4_model"].get("context"):
        level = "context"
        if experiment_condition:
            # Use experimental team configuration
            active_team = build_experimental_team(level, experiment_condition)
        else:
            active_team = build_context_team()
        print("--- Selecting Team: Context Level ---")
    elif not state["c4_model"].get("containers"):
        level = "container"
        if experiment_condition:
            # Use experimental team configuration
            active_team = build_experimental_team(level, experiment_condition)
        else:
            active_team = build_container_team()
        print("--- Selecting Team: Container Level ---")
    else:
        level = "component"
        if experiment_condition:
            # Use experimental team configuration
            active_team = build_experimental_team(level, experiment_condition)
        else:
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
    
    # Build context-aware initial message
    initial_message_content = f"Let's begin the C4 analysis for the {subgraph_level_description}.\n\n"
    initial_message_content += f"**System Brief:**\n{state['system_brief']}\n\n"
    
    # Add condensed context from previous levels (if any)
    previous_context = _extract_key_context(state['c4_model'], level)
    if previous_context:
        initial_message_content += f"**Prior Decisions:**\n{previous_context}\n\n"
    
    subgraph_input = {
        "messages": [HumanMessage(content=initial_message_content)],
        "system_brief": state['system_brief'],
        "context": "",  # No longer needed - context is in the initial message
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
