# src/orchestrator.py
"""
Experimental Orchestrator for Multi-Agent C4 Architecture Design

This module controls conversation flow and collaboration dynamics based on
experimental conditions, supporting all five experimental configurations.
"""

from __future__ import annotations

import copy
import random
from typing import Dict, List, Optional, Any
from langchain_core.messages import BaseMessage, AIMessage

from .models import Agent
from .types import State
from .memory import SharedMemorySystem, GlossaryAgent


class ExperimentalOrchestrator:
    """
    Orchestrates multi-agent collaboration based on experimental conditions.
    Handles speaking order, memory integration, and experimental modifications.
    """
    
    def __init__(self, condition: Optional[Dict[str, Any]] = None, 
                 memory_system: Optional[SharedMemorySystem] = None):
        self.condition = condition or {}
        self.memory_system = memory_system
        self.glossary_agent = GlossaryAgent(memory_system) if memory_system else None
        self.conversation_history = []
        self.current_round = 0
        
    def determine_speaking_order(self, agents: List[Agent]) -> List[Agent]:
        """
        Determine the speaking order based on experimental condition.
        
        Args:
            agents: List of agents to order
            
        Returns:
            Ordered list of agents
        """
        if not self.condition:
            return agents
        
        # Check for explicit speaking order (Experiment 2)
        speaking_order = self.condition.get("speaking_order", [])
        if speaking_order:
            return self._apply_speaking_order(agents, speaking_order)
        
        # Check for other ordering preferences
        experiment_type = self._detect_experiment_type()
        
        if experiment_type == "role_ablation":
            # For ablation, maintain natural order but filter agents
            return agents
        
        elif experiment_type == "role_specialization":
            # For specialization experiments, might want to randomize to avoid bias
            persona_type = self.condition.get("persona_type", "specialized")
            if persona_type == "generic":
                # Generic agents - random order to avoid first-speaker bias
                ordered_agents = agents.copy()
                random.shuffle(ordered_agents)
                return ordered_agents
        
        elif experiment_type == "shared_memory":
            # Memory experiments - glossary agent might speak first or last
            if self.glossary_agent and any(agent.name == "Glossary_Agent" for agent in agents):
                return self._prioritize_glossary_agent(agents)
        
        elif experiment_type == "role_diversity":
            # Diversity experiments - order by expertise breadth
            return self._order_by_diversity(agents)
        
        return agents
    
    def manage_turn_rotation(self, agents: List[Agent], round_num: int) -> Agent:
        """
        Select the next agent to speak based on experimental condition.
        
        Args:
            agents: Available agents
            round_num: Current round number
            
        Returns:
            Next agent to speak
        """
        if not agents:
            raise ValueError("No agents available for turn rotation")
        
        # Standard round-robin if no experimental modifications
        if not self.condition:
            return agents[round_num % len(agents)]
        
        experiment_type = self._detect_experiment_type()
        
        if experiment_type == "interaction_order":
            # Strict adherence to speaking order
            speaking_order = self.condition.get("speaking_order", [])
            if speaking_order:
                # Cycle through the predefined order
                next_role = speaking_order[round_num % len(speaking_order)]
                next_agent = next((agent for agent in agents if agent.name == next_role), None)
                if next_agent:
                    return next_agent
        
        elif experiment_type == "shared_memory" and self.glossary_agent:
            # Glossary agent speaks at specific intervals
            memory_type = self.condition.get("memory_type", "none")
            if memory_type == "glossary":
                # Glossary agent speaks every 3rd turn
                if round_num % 3 == 2:
                    glossary_agent = next((agent for agent in agents if agent.name == "Glossary_Agent"), None)
                    if glossary_agent:
                        return glossary_agent
        
        # Default round-robin
        return agents[round_num % len(agents)]
    
    def integrate_memory_updates(self, state: State, agent_output: Dict[str, Any]) -> State:
        """
        Integrate memory system updates after an agent's turn.
        
        Args:
            state: Current conversation state
            agent_output: Output from the agent's turn
            
        Returns:
            Updated state with memory integration
        """
        if not self.memory_system:
            return state
        
        # Extract information from agent output
        agent_message = agent_output.get("messages", [])
        if agent_message and isinstance(agent_message[0], AIMessage):
            message_content = agent_message[0].content
            agent_name = getattr(agent_message[0], 'name', 'unknown')
            
            # Add conversation turn to memory
            current_level = self._determine_current_level(state)
            self.memory_system.add_conversation_turn(agent_name, message_content, current_level)
            
            # Update entities if this is a YAML or structured output
            if "yaml_definition" in str(agent_output) or "elements:" in message_content:
                self._extract_and_update_entities(message_content, current_level)
        
        # Update state with memory context
        updated_state = copy.deepcopy(state)
        if hasattr(updated_state, 'memory_system'):
            updated_state['memory_system'] = self.memory_system
        
        return updated_state
    
    def prepare_agent_context(self, agent: Agent, state: State) -> Dict[str, Any]:
        """
        Prepare context for an agent based on experimental condition and memory.
        
        Args:
            agent: Agent about to speak
            state: Current conversation state
            
        Returns:
            Enhanced context dictionary
        """
        context = {
            "experimental_condition": self.condition,
            "agent_metadata": {
                "role": agent.name,
                "speaking_order": getattr(agent, 'speaking_order', 0),
                "memory_type": getattr(agent, 'memory_type', 'none')
            }
        }
        
        # Add memory context if available
        if self.memory_system:
            current_level = self._determine_current_level(state)
            memory_context = self.memory_system.get_context_for_level(current_level)
            context["memory_context"] = memory_context
            
            # Add glossary if relevant
            if self.memory_system.memory_type in ["glossary", "persistent", "hierarchical"]:
                context["glossary"] = self.memory_system.get_glossary()
        
        # Add experimental modifications
        experiment_type = self._detect_experiment_type()
        
        if experiment_type == "role_specialization":
            context["specialization_level"] = self.condition.get("persona_type", "specialized")
        
        elif experiment_type == "shared_memory":
            context["memory_instructions"] = self._get_memory_instructions()
        
        elif experiment_type == "interaction_order":
            context["speaking_instructions"] = self._get_speaking_instructions(agent)
        
        return context
    
    def _apply_speaking_order(self, agents: List[Agent], speaking_order: List[str]) -> List[Agent]:
        """Apply explicit speaking order to agents."""
        ordered_agents = []
        
        # First, add agents in the specified order
        for role_name in speaking_order:
            agent = next((a for a in agents if a.name == role_name), None)
            if agent:
                ordered_agents.append(agent)
        
        # Add any remaining agents not in the speaking order
        for agent in agents:
            if agent not in ordered_agents:
                ordered_agents.append(agent)
        
        return ordered_agents
    
    def _prioritize_glossary_agent(self, agents: List[Agent]) -> List[Agent]:
        """Move glossary agent to first or last position."""
        glossary_agent = None
        other_agents = []
        
        for agent in agents:
            if agent.name == "Glossary_Agent":
                glossary_agent = agent
            else:
                other_agents.append(agent)
        
        if glossary_agent:
            # Put glossary agent first for initial setup
            return [glossary_agent] + other_agents
        
        return agents
    
    def _order_by_diversity(self, agents: List[Agent]) -> List[Agent]:
        """Order agents by role diversity (domain-focused first)."""
        diversity_level = self.condition.get("diversity_level", "high")
        
        if diversity_level == "domain":
            # Prioritize business-focused roles
            domain_priority = ["Product_Owner", "Business_Analyst", "Domain_Expert"]
            tech_roles = []
            domain_roles = []
            
            for agent in agents:
                if agent.name in domain_priority:
                    domain_roles.append(agent)
                else:
                    tech_roles.append(agent)
            
            return domain_roles + tech_roles
        
        # Default ordering
        return agents
    
    def _detect_experiment_type(self) -> str:
        """Detect experiment type from condition."""
        if "removed_roles" in self.condition or self.condition.get("id") == "architect_only":
            return "role_ablation"
        elif "speaking_order" in self.condition:
            return "interaction_order"
        elif "persona_type" in self.condition:
            return "role_specialization"
        elif "memory_type" in self.condition:
            return "shared_memory"
        elif "diversity_level" in self.condition:
            return "role_diversity"
        else:
            return "standard"
    
    def _determine_current_level(self, state: State) -> str:
        """Determine current C4 level from state."""
        c4_model = state.get("c4_model", {})
        
        if not c4_model.get("context"):
            return "context"
        elif not c4_model.get("containers"):
            return "containers"
        else:
            return "components"
    
    def _extract_and_update_entities(self, message_content: str, level: str) -> None:
        """Extract entities from message content and update memory."""
        if not self.memory_system:
            return
        
        # Simple YAML parsing to extract elements
        try:
            import yaml
            
            # Look for YAML-like content in the message
            yaml_sections = []
            lines = message_content.split('\n')
            yaml_content = []
            in_yaml = False
            
            for line in lines:
                if line.strip().startswith('elements:') or line.strip().startswith('- type:'):
                    in_yaml = True
                    yaml_content.append(line)
                elif in_yaml and (line.startswith('  ') or line.startswith('- ')):
                    yaml_content.append(line)
                elif in_yaml and line.strip() == '':
                    yaml_content.append(line)
                elif in_yaml:
                    # End of YAML section
                    if yaml_content:
                        yaml_sections.append('\n'.join(yaml_content))
                    yaml_content = []
                    in_yaml = False
            
            # Process final section
            if yaml_content:
                yaml_sections.append('\n'.join(yaml_content))
            
            # Parse and update entities
            for yaml_section in yaml_sections:
                try:
                    if yaml_section.strip().startswith('elements:'):
                        parsed = yaml.safe_load(yaml_section)
                        if parsed and 'elements' in parsed:
                            self.memory_system.update_cross_level_mapping(level, parsed['elements'])
                except:
                    continue  # Skip unparseable sections
                    
        except Exception:
            # Fallback to simple text extraction
            pass
    
    def _get_memory_instructions(self) -> str:
        """Get memory-specific instructions for agents."""
        memory_type = self.condition.get("memory_type", "none")
        
        if memory_type == "glossary":
            return "Consult the shared glossary for naming consistency. Use established entity names when available."
        elif memory_type == "persistent":
            return "You have access to full conversation history and decisions. Build upon previous discussions."
        elif memory_type == "hierarchical":
            return "Memory is organized by C4 levels. Focus on information relevant to the current level."
        else:
            return ""
    
    def _get_speaking_instructions(self, agent: Agent) -> str:
        """Get speaking order specific instructions."""
        speaking_order = self.condition.get("speaking_order", [])
        
        if not speaking_order:
            return ""
        
        agent_position = -1
        try:
            agent_position = speaking_order.index(agent.name)
        except ValueError:
            pass
        
        if agent_position == 0:
            return "You are speaking first. Set the direction and foundation for the discussion."
        elif agent_position == len(speaking_order) - 1:
            return "You are speaking last. Synthesize and build upon all previous contributions."
        else:
            return f"You are speaking in position {agent_position + 1}. Build upon previous speakers' insights."


class CollaborationManager:
    """
    High-level manager for experimental collaboration sessions.
    Coordinates orchestrator, memory, and evaluation.
    """
    
    def __init__(self, experiment_condition: Optional[Dict[str, Any]] = None):
        self.condition = experiment_condition
        self.memory_system = None
        self.orchestrator = None
        self.session_metadata = {
            "experiment_type": self._detect_experiment_type(),
            "start_time": None,
            "agents_involved": [],
            "conversation_turns": 0
        }
        
        # Initialize memory system if needed
        if self.condition and self.condition.get("memory_type", "none") != "none":
            self.memory_system = SharedMemorySystem(self.condition["memory_type"])
            
        # Initialize orchestrator
        self.orchestrator = ExperimentalOrchestrator(
            condition=self.condition,
            memory_system=self.memory_system
        )
    
    def prepare_collaboration_session(self, agents: List[Agent]) -> Dict[str, Any]:
        """Prepare a collaboration session with experimental configuration."""
        
        # Apply experimental modifications to agents
        if self.orchestrator:
            ordered_agents = self.orchestrator.determine_speaking_order(agents)
        else:
            ordered_agents = agents
        
        # Update session metadata
        self.session_metadata["agents_involved"] = [agent.name for agent in ordered_agents]
        
        session_config = {
            "agents": ordered_agents,
            "orchestrator": self.orchestrator,
            "memory_system": self.memory_system,
            "condition": self.condition,
            "metadata": self.session_metadata
        }
        
        return session_config
    
    def finalize_collaboration_session(self) -> Dict[str, Any]:
        """Finalize collaboration session and gather experimental data."""
        
        session_summary = {
            "metadata": self.session_metadata,
            "condition": self.condition,
            "memory_state": None,
            "conversation_analysis": {}
        }
        
        # Gather memory system data
        if self.memory_system:
            session_summary["memory_state"] = {
                "total_entities": len(self.memory_system.entities),
                "cross_level_mappings": self.memory_system.cross_level_mappings,
                "conversation_turns": len(self.memory_system.conversation_history),
                "design_decisions": len(self.memory_system.decisions)
            }
            
            # Generate naming report if glossary agent was used
            if self.orchestrator and self.orchestrator.glossary_agent:
                session_summary["naming_report"] = self.orchestrator.glossary_agent.generate_naming_report()
        
        return session_summary
    
    def _detect_experiment_type(self) -> str:
        """Detect experiment type from condition."""
        if not self.condition:
            return "standard"
            
        if "removed_roles" in self.condition or self.condition.get("id") == "architect_only":
            return "role_ablation"
        elif "speaking_order" in self.condition:
            return "interaction_order"
        elif "persona_type" in self.condition:
            return "role_specialization"
        elif "memory_type" in self.condition:
            return "shared_memory"
        elif "diversity_level" in self.condition:
            return "role_diversity"
        else:
            return "standard"