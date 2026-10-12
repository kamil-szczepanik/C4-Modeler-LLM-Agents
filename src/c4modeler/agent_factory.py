# src/agent_factory.py
"""
Experimental Agent Factory for Multi-Agent C4 Architecture Design

This module provides flexible agent creation based on experimental conditions,
supporting role ablation, interaction order, specialization, and memory configurations.
"""

from __future__ import annotations

import copy
from typing import Dict, List, Optional, Any

from .models import Agent
from .prompts import PERSONA_BY_ROLE, GENERIC_PERSONA_BY_ROLE


class ExperimentalAgentFactory:
    """
    Factory class for creating agent teams based on experimental conditions.
    Supports all five experimental configurations defined in the research.
    """
    
    def __init__(self):
        # Standard role mappings for each C4 level
        self.standard_roles = {
            "context": ["Product_Owner", "Business_Analyst", "Lead_Software_Architect"],
            "containers": ["Software_Architect", "Lead_Developer", "DevOps_Specialist", "Security_Specialist"],
            "components": ["Lead_Developer", "Senior_Developer", "Database_Administrator", "Security_Specialist"]
        }
        
        # Role name mapping from experiment configs to internal persona keys
        self.role_name_mapping = {
            "Product Owner": "Product_Owner",
            "Business Analyst": "Business_Analyst", 
            "Architect": "Lead_Software_Architect",
            "Software Architect": "Software_Architect",
            "Lead Developer": "Lead_Developer",
            "DevOps Engineer": "DevOps_Specialist",
            "DevOps Specialist": "DevOps_Specialist",
            "Security Expert": "Security_Specialist",
            "Security Specialist": "Security_Specialist",
            "Senior Developer": "Senior_Developer",
            "Database Administrator": "Database_Administrator",
            "Lead Software Architect": "Lead_Software_Architect",
            "Generic Engineer": "Software_Engineer",
            "Software Engineer": "Software_Engineer",
            # Also support the internal names directly
            "Product_Owner": "Product_Owner",
            "Business_Analyst": "Business_Analyst",
            "Lead_Software_Architect": "Lead_Software_Architect",
            "Software_Architect": "Software_Architect",
            "Lead_Developer": "Lead_Developer",
            "DevOps_Specialist": "DevOps_Specialist",
            "Security_Specialist": "Security_Specialist",
            "Senior_Developer": "Senior_Developer",
            "Database_Administrator": "Database_Administrator",
        }
    
    def _normalize_role_name(self, role_name: str) -> str:
        """Convert experiment config role names to internal persona keys."""
        return self.role_name_mapping.get(role_name, role_name)
    
    def _normalize_role_list(self, roles: List[str]) -> List[str]:
        """Convert a list of experiment config role names to internal persona keys."""
        return [self._normalize_role_name(role) for role in roles]
    
    def create_team_for_experiment(self, condition: Dict[str, Any], level: str) -> List[Agent]:
        """
        Create agent team based on experimental condition and C4 level.
        
        Args:
            condition: Experimental condition configuration
            level: C4 level ("context", "containers", "components")
            
        Returns:
            List of Agent objects configured for the experiment
        """
        base_roles = self.standard_roles.get(level, self.standard_roles["containers"])
        
        # Normalize any role names in the condition
        if "roles" in condition:
            condition = dict(condition)  # Make a copy
            condition["roles"] = self._normalize_role_list(condition["roles"])
        if "removed_roles" in condition:
            condition["removed_roles"] = self._normalize_role_list(condition["removed_roles"])
        if "speaking_order" in condition:
            condition["speaking_order"] = self._normalize_role_list(condition["speaking_order"])
        
        # Apply experimental modifications based on condition type
        experiment_type = self._detect_experiment_type(condition)
        
        if experiment_type == "role_ablation":
            return self._create_ablation_team(condition, base_roles)
        elif experiment_type == "interaction_order":
            return self._create_ordered_team(condition, base_roles)
        elif experiment_type == "role_specialization":
            return self._create_specialized_team(condition, base_roles)
        elif experiment_type == "shared_memory":
            return self._create_memory_team(condition, base_roles)
        elif experiment_type == "role_diversity":
            return self._create_diversity_team(condition, base_roles)
        else:
            # Default to standard team
            return self.create_specialized_agents(base_roles)
    
    def _detect_experiment_type(self, condition: Dict[str, Any]) -> str:
        """Detect experiment type from condition configuration."""
        if "removed_roles" in condition or condition.get("id") == "architect_only":
            return "role_ablation"
        elif "speaking_order" in condition:
            return "interaction_order"
        elif "persona_type" in condition:
            return "role_specialization"
        elif "memory_type" in condition:
            return "shared_memory"
        elif "diversity_level" in condition:
            return "role_diversity"
        else:
            return "standard"
    
    def _create_ablation_team(self, condition: Dict[str, Any], base_roles: List[str]) -> List[Agent]:
        """Create team with specific roles removed (Experiment 1)."""
        
        if condition.get("id") == "architect_only":
            # Homogeneous team - all architects
            architect_role = "Software_Architect" if "Software_Architect" in base_roles else "Lead_Software_Architect"
            return [Agent(name=architect_role, persona=PERSONA_BY_ROLE[architect_role]) for _ in range(4)]
        
        # Role ablation - remove specific roles
        roles = condition.get("roles", base_roles)
        removed_roles = condition.get("removed_roles", [])
        
        # Remove specified roles
        active_roles = [role for role in roles if role not in removed_roles]
        
        # Ensure we have at least one agent
        if not active_roles:
            active_roles = [base_roles[0]]  # Fallback to first role
        
        return self.create_specialized_agents(active_roles)
    
    def _create_ordered_team(self, condition: Dict[str, Any], base_roles: List[str]) -> List[Agent]:
        """Create team with specific speaking order (Experiment 2)."""
        
        speaking_order = condition.get("speaking_order", base_roles)
        roles = condition.get("roles", base_roles)
        
        # Create agents in the specified speaking order
        ordered_agents = []
        
        for role_name in speaking_order:
            if role_name in roles:
                agent = Agent(name=role_name, persona=PERSONA_BY_ROLE.get(role_name, ""))
                # Add speaking order metadata
                agent.speaking_order = len(ordered_agents)
                ordered_agents.append(agent)
        
        # Add any remaining roles not in speaking order
        for role_name in roles:
            if role_name not in speaking_order:
                agent = Agent(name=role_name, persona=PERSONA_BY_ROLE.get(role_name, ""))
                agent.speaking_order = len(ordered_agents)
                ordered_agents.append(agent)
        
        return ordered_agents
    
    def _create_specialized_team(self, condition: Dict[str, Any], base_roles: List[str]) -> List[Agent]:
        """Create team with varying specialization levels (Experiment 3)."""
        
        persona_type = condition.get("persona_type", "specialized")
        roles = condition.get("roles", base_roles)
        
        if persona_type == "generic":
            return self.create_generic_agents(len(roles))
        elif persona_type == "specialized":
            return self.create_specialized_agents(roles)
        elif persona_type == "mixed":
            # Mixed team - some specialized, some generic
            agents = []
            for i, role in enumerate(roles):
                if i < len(roles) // 2:  # First half specialized
                    agents.append(Agent(name=role, persona=PERSONA_BY_ROLE.get(role, "")))
                else:  # Second half generic
                    agents.append(Agent(name="Software_Engineer", persona=GENERIC_PERSONA_BY_ROLE["Software_Engineer"]))
            return agents
        else:
            return self.create_specialized_agents(roles)
    
    def _create_memory_team(self, condition: Dict[str, Any], base_roles: List[str]) -> List[Agent]:
        """Create team with shared memory configuration (Experiment 4)."""
        
        memory_type = condition.get("memory_type", "none")
        roles = condition.get("roles", base_roles)
        additional_agents = condition.get("additional_agents", [])
        
        # Create base team
        agents = self.create_specialized_agents(roles)
        
        # Add memory-specific agents if needed
        if memory_type == "glossary" and "Glossary Agent" in additional_agents:
            glossary_agent = Agent(
                name="Glossary_Agent",
                persona=self._get_glossary_agent_persona()
            )
            glossary_agent.memory_type = "glossary"
            agents.append(glossary_agent)
        
        # Configure memory settings for all agents
        for agent in agents:
            agent.memory_type = memory_type
            if memory_type == "persistent":
                agent.memory_capacity = "unlimited"
            elif memory_type == "hierarchical":
                agent.memory_structure = "hierarchical"
        
        return agents
    
    def _create_diversity_team(self, condition: Dict[str, Any], base_roles: List[str]) -> List[Agent]:
        """Create team with specific diversity configuration (Experiment 5)."""
        
        diversity_level = condition.get("diversity_level", "high")
        roles = condition.get("roles", base_roles)
        
        if diversity_level == "none":
            # Homogeneous team - all same role
            primary_role = roles[0] if roles else "Software_Architect"
            return [Agent(name=primary_role, persona=PERSONA_BY_ROLE.get(primary_role, "")) for _ in range(4)]
        
        elif diversity_level == "medium":
            # Reduced diversity - some role duplication
            if len(roles) >= 2:
                # Duplicate first role, keep others unique
                agents = [Agent(name=roles[0], persona=PERSONA_BY_ROLE.get(roles[0], ""))]
                agents.append(Agent(name=roles[0], persona=PERSONA_BY_ROLE.get(roles[0], "")))
                
                for role in roles[1:3]:  # Add 2 more unique roles
                    agents.append(Agent(name=role, persona=PERSONA_BY_ROLE.get(role, "")))
                
                return agents[:4]  # Limit to 4 agents
        
        elif diversity_level == "domain":
            # Domain-focused diversity
            domain_roles = ["Product_Owner", "Business_Analyst", "Domain_Expert", "Product_Manager"]
            available_domain_roles = [role for role in domain_roles if role in PERSONA_BY_ROLE]
            
            if len(available_domain_roles) < 4:
                # Fill with product owner duplicates if not enough domain roles
                while len(available_domain_roles) < 4:
                    available_domain_roles.append("Product_Owner")
            
            return self.create_specialized_agents(available_domain_roles[:4])
        
        else:  # "high" diversity
            return self.create_specialized_agents(roles)
    
    def create_specialized_agents(self, roles: List[str]) -> List[Agent]:
        """Create agents with specialized personas."""
        agents = []
        for role in roles:
            persona = PERSONA_BY_ROLE.get(role, "")
            if not persona:
                print(f"⚠️ No persona found for role: {role}, using generic persona")
                persona = GENERIC_PERSONA_BY_ROLE.get("Software_Engineer", "")
            
            agents.append(Agent(name=role, persona=persona))
        
        return agents
    
    def create_generic_agents(self, count: int) -> List[Agent]:
        """Create generic software engineer agents."""
        generic_persona = GENERIC_PERSONA_BY_ROLE.get("Software_Engineer", "")
        return [Agent(name="Software_Engineer", persona=generic_persona) for _ in range(count)]
    
    def create_agents_with_memory(self, roles: List[str], memory_config: Dict[str, Any]) -> List[Agent]:
        """Create agents with specific memory configuration."""
        agents = self.create_specialized_agents(roles)
        
        for agent in agents:
            agent.memory_config = copy.deepcopy(memory_config)
            agent.memory_type = memory_config.get("type", "none")
        
        return agents
    
    def _get_glossary_agent_persona(self) -> str:
        """Get persona definition for glossary agent."""
        return """You are a specialized Glossary Agent responsible for maintaining naming consistency across the collaborative architecture design process.

Your focus is on:
- **Entity Tracking:** Maintaining a consistent registry of all named entities (systems, containers, components, technologies)
- **Naming Consistency:** Ensuring the same entities use consistent names across different C4 levels
- **Conflict Resolution:** Identifying and resolving naming conflicts or ambiguities
- **Cross-Level Mapping:** Tracking how entities map from Context → Container → Component levels

Your contribution is to **ensure architectural consistency through systematic terminology management.** You intervene when naming inconsistencies arise and provide authoritative entity definitions."""


# Add to prompts.py if not already present
GENERIC_PERSONA_BY_ROLE = {
    "Software_Engineer": """You are a general Software Engineer with broad knowledge across multiple domains.

Your focus is on:
- **General Software Design:** Applying common software engineering principles
- **Best Practices:** Following established patterns and practices
- **Problem Solving:** Using general engineering approaches to address challenges
- **Documentation:** Ensuring clear and maintainable designs

Your contribution is to **provide general software engineering expertise** without specialization in any particular domain or role.""",
    
    "Generic_Architect": """You are a Software Architect with general architectural knowledge.

Your focus is on:
- **System Structure:** Designing overall system organization and components
- **Technology Decisions:** Making general technology stack choices
- **Design Patterns:** Applying common architectural patterns
- **Integration:** Ensuring components work together effectively

Your contribution is to **provide general architectural guidance** across all aspects of system design."""
}