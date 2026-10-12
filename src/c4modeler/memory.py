# src/memory.py
"""
Shared Memory System for Multi-Agent C4 Architecture Design

This module implements shared memory and glossary functionality for collaborative
architecture design, supporting Experiment 4 (Shared Memory/Glossary).
"""

from __future__ import annotations

import copy
import json
from collections import defaultdict
from typing import Dict, List, Optional, Any, Set
from datetime import datetime

import yaml


class SharedMemorySystem:
    """
    Implements shared memory for collaborative agents with different memory types:
    - glossary: Maintains naming consistency and entity definitions
    - persistent: Stores all conversation context and decisions
    - hierarchical: Organizes memory by C4 abstraction levels
    """
    
    def __init__(self, memory_type: str = "none"):
        self.memory_type = memory_type
        self.entities = {}  # Central entity registry
        self.cross_level_mappings = {}  # Context -> Container -> Component mappings
        self.naming_consistency = {}  # Track naming variants
        self.decisions = []  # Design decisions history
        self.conversation_history = []  # Full conversation context
        self.level_specific_memory = {  # Hierarchical organization
            "context": {},
            "containers": {},
            "components": {}
        }
        self.created_at = datetime.now().isoformat()
        
    def add_entity(self, name: str, entity_type: str, description: str, 
                   level: str = "context", metadata: Optional[Dict] = None) -> None:
        """
        Add or update an entity in the shared memory.
        
        Args:
            name: Entity name
            entity_type: Type (system, container, component, person, external_system)
            description: Entity description
            level: C4 level where entity was defined
            metadata: Additional metadata
        """
        entity_id = self._generate_entity_id(name, entity_type)
        
        entity_data = {
            "name": name,
            "type": entity_type,
            "description": description,
            "level": level,
            "metadata": metadata or {},
            "created_at": datetime.now().isoformat(),
            "variants": set([name])  # Track naming variants
        }
        
        # Check for existing similar entities
        existing_id = self._find_similar_entity(name, entity_type)
        if existing_id and existing_id != entity_id:
            # Merge with existing entity
            self._merge_entities(existing_id, entity_data)
        else:
            self.entities[entity_id] = entity_data
            
        # Update level-specific memory if hierarchical
        if self.memory_type == "hierarchical":
            self.level_specific_memory[level][entity_id] = entity_data
    
    def get_entity(self, name: str, entity_type: Optional[str] = None) -> Optional[Dict]:
        """Get entity by name and optionally type."""
        entity_id = self._generate_entity_id(name, entity_type or "")
        
        # Direct lookup
        if entity_id in self.entities:
            return self.entities[entity_id]
        
        # Fuzzy search by name variants
        for eid, entity in self.entities.items():
            if name.lower() in [v.lower() for v in entity["variants"]]:
                return entity
                
        return None
    
    def get_glossary(self) -> Dict[str, Any]:
        """Get current glossary state for agents."""
        if self.memory_type == "none":
            return {}
            
        glossary = {
            "entities": {},
            "naming_guidelines": self._generate_naming_guidelines(),
            "cross_level_mappings": self.cross_level_mappings,
            "last_updated": datetime.now().isoformat()
        }
        
        # Organize entities by type
        for entity_id, entity in self.entities.items():
            entity_type = entity["type"]
            if entity_type not in glossary["entities"]:
                glossary["entities"][entity_type] = []
            
            glossary["entities"][entity_type].append({
                "name": entity["name"],
                "description": entity["description"],
                "level": entity["level"],
                "variants": list(entity["variants"])
            })
        
        return glossary
    
    def update_cross_level_mapping(self, level: str, elements: List[Dict]) -> None:
        """Update cross-level mappings from YAML elements."""
        if level not in self.cross_level_mappings:
            self.cross_level_mappings[level] = {}
            
        for element in elements:
            element_name = element.get("name", "")
            element_type = element.get("type", "")
            
            if element_name and element_type:
                # Add to entity registry
                self.add_entity(
                    name=element_name,
                    entity_type=element_type,
                    description=element.get("description", ""),
                    level=level,
                    metadata=element
                )
                
                # Track cross-level mapping
                self.cross_level_mappings[level][element_name] = {
                    "type": element_type,
                    "description": element.get("description", ""),
                    "technology": element.get("technology", ""),
                    "mapped_to": []  # Will be populated as we traverse levels
                }
    
    def resolve_naming_conflicts(self, elements: List[Dict]) -> List[Dict]:
        """
        Resolve naming conflicts using existing entity registry.
        Returns updated elements with consistent naming.
        """
        if self.memory_type == "none":
            return elements
            
        resolved_elements = []
        
        for element in elements:
            element_name = element.get("name", "")
            element_type = element.get("type", "")
            
            if not element_name:
                resolved_elements.append(element)
                continue
            
            # Check for existing entity
            existing_entity = self.get_entity(element_name, element_type)
            
            if existing_entity:
                # Use canonical name from existing entity
                canonical_name = existing_entity["name"]
                if canonical_name != element_name:
                    # Update element with canonical name
                    updated_element = copy.deepcopy(element)
                    updated_element["name"] = canonical_name
                    
                    # Track the variant
                    existing_entity["variants"].add(element_name)
                    self.entities[self._generate_entity_id(canonical_name, element_type)] = existing_entity
                    
                    resolved_elements.append(updated_element)
                else:
                    resolved_elements.append(element)
            else:
                # New entity - add to registry
                self.add_entity(
                    name=element_name,
                    entity_type=element_type,
                    description=element.get("description", ""),
                    level="unknown"
                )
                resolved_elements.append(element)
        
        return resolved_elements
    
    def add_conversation_turn(self, agent_name: str, message: str, level: str) -> None:
        """Add conversation turn to memory."""
        if self.memory_type in ["persistent", "hierarchical"]:
            turn_data = {
                "agent": agent_name,
                "message": message,
                "level": level,
                "timestamp": datetime.now().isoformat()
            }
            
            self.conversation_history.append(turn_data)
            
            # Extract entities from conversation if possible
            self._extract_entities_from_text(message, level)
    
    def add_design_decision(self, decision: str, rationale: str, level: str, 
                          agents_involved: List[str]) -> None:
        """Record a design decision."""
        decision_data = {
            "decision": decision,
            "rationale": rationale,
            "level": level,
            "agents": agents_involved,
            "timestamp": datetime.now().isoformat()
        }
        
        self.decisions.append(decision_data)
    
    def get_context_for_level(self, level: str) -> Dict[str, Any]:
        """Get relevant memory context for a specific C4 level."""
        if self.memory_type == "none":
            return {}
            
        context = {
            "entities": {},
            "decisions": [],
            "conversation_summary": "",
            "naming_guidelines": self._generate_naming_guidelines()
        }
        
        # Get entities relevant to this level
        if self.memory_type == "hierarchical":
            context["entities"] = self.level_specific_memory.get(level, {})
        else:
            # Get all entities, filter by relevance
            relevant_entities = {}
            for eid, entity in self.entities.items():
                if entity["level"] == level or level == "components":
                    # Components can see all levels
                    relevant_entities[eid] = entity
            context["entities"] = relevant_entities
        
        # Get relevant decisions
        context["decisions"] = [
            decision for decision in self.decisions 
            if decision["level"] == level or decision["level"] == "all"
        ]
        
        # Generate conversation summary if persistent memory
        if self.memory_type == "persistent" and self.conversation_history:
            context["conversation_summary"] = self._summarize_conversation(level)
        
        return context
    
    def _generate_entity_id(self, name: str, entity_type: str) -> str:
        """Generate unique entity ID."""
        return f"{entity_type}_{name}".lower().replace(" ", "_")
    
    def _find_similar_entity(self, name: str, entity_type: str) -> Optional[str]:
        """Find similar entity by name similarity."""
        name_lower = name.lower()
        
        for entity_id, entity in self.entities.items():
            if entity["type"] == entity_type:
                for variant in entity["variants"]:
                    if variant.lower() == name_lower:
                        return entity_id
                    # Simple similarity check
                    if abs(len(variant) - len(name)) <= 2 and variant.lower() in name_lower:
                        return entity_id
        
        return None
    
    def _merge_entities(self, existing_id: str, new_entity: Dict) -> None:
        """Merge new entity data with existing entity."""
        existing = self.entities[existing_id]
        
        # Merge variants
        existing["variants"].add(new_entity["name"])
        
        # Update description if new one is more detailed
        if len(new_entity["description"]) > len(existing["description"]):
            existing["description"] = new_entity["description"]
        
        # Merge metadata
        existing["metadata"].update(new_entity.get("metadata", {}))
        
        # Update level if more specific
        if new_entity["level"] != "unknown":
            existing["level"] = new_entity["level"]
    
    def _generate_naming_guidelines(self) -> List[str]:
        """Generate naming guidelines based on current entities."""
        guidelines = [
            "Use consistent naming across all C4 levels",
            "Prefer descriptive names over abbreviations",
            "Use PascalCase for system and container names",
            "Use camelCase for component names",
            "Avoid special characters in entity names"
        ]
        
        # Add specific guidelines based on existing entities
        if self.entities:
            guidelines.append("Existing entities in this design:")
            for entity_type in ["system", "container", "component"]:
                type_entities = [e["name"] for e in self.entities.values() if e["type"] == entity_type]
                if type_entities:
                    guidelines.append(f"- {entity_type.title()}s: {', '.join(type_entities[:5])}")
        
        return guidelines
    
    def _extract_entities_from_text(self, text: str, level: str) -> None:
        """Extract potential entities from conversation text."""
        # Simple entity extraction - could be enhanced with NLP
        words = text.split()
        
        # Look for patterns that might be entities
        potential_entities = []
        
        for i, word in enumerate(words):
            # Look for capitalized words that might be system names
            if word[0].isupper() and len(word) > 3:
                # Check context for entity type indicators
                context = " ".join(words[max(0, i-3):i+4]).lower()
                
                if any(indicator in context for indicator in ["system", "service", "api", "database"]):
                    potential_entities.append({
                        "name": word,
                        "type": "container",
                        "description": f"Extracted from conversation: {context}",
                        "confidence": 0.5
                    })
        
        # Add high-confidence entities to memory
        for entity in potential_entities:
            if entity["confidence"] > 0.7:
                self.add_entity(
                    name=entity["name"],
                    entity_type=entity["type"],
                    description=entity["description"],
                    level=level,
                    metadata={"extracted": True, "confidence": entity["confidence"]}
                )
    
    def _summarize_conversation(self, level: str) -> str:
        """Generate conversation summary for a specific level."""
        level_conversations = [
            turn for turn in self.conversation_history 
            if turn["level"] == level
        ]
        
        if not level_conversations:
            return ""
        
        # Simple summary - could be enhanced with LLM summarization
        agents_involved = set(turn["agent"] for turn in level_conversations)
        message_count = len(level_conversations)
        
        summary = f"Conversation involved {len(agents_involved)} agents across {message_count} messages. "
        summary += f"Agents: {', '.join(agents_involved)}. "
        
        # Extract key themes
        all_text = " ".join(turn["message"] for turn in level_conversations)
        common_words = self._extract_common_themes(all_text)
        
        if common_words:
            summary += f"Key themes: {', '.join(common_words[:5])}."
        
        return summary
    
    def _extract_common_themes(self, text: str) -> List[str]:
        """Extract common themes from conversation text."""
        from collections import Counter
        
        # Simple word frequency analysis
        words = text.lower().split()
        
        # Filter out common words
        stop_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "will", "would", "should", "could", "can", "may", "might", "must", "this", "that", "these", "those"}
        
        filtered_words = [word for word in words if len(word) > 3 and word not in stop_words]
        
        # Get most common words
        word_counts = Counter(filtered_words)
        return [word for word, count in word_counts.most_common(10) if count > 1]


class GlossaryAgent:
    """
    Specialized agent for maintaining glossary and naming consistency.
    Works in conjunction with SharedMemorySystem.
    """
    
    def __init__(self, memory_system: SharedMemorySystem):
        self.memory_system = memory_system
        self.name = "Glossary_Agent"
        self.active_conflicts = []
        
    def maintain_consistency(self, new_elements: List[Dict]) -> Dict[str, str]:
        """
        Check new elements for naming consistency and provide recommendations.
        
        Returns:
            Dictionary mapping original names to recommended names
        """
        recommendations = {}
        
        for element in new_elements:
            element_name = element.get("name", "")
            element_type = element.get("type", "")
            
            if not element_name:
                continue
            
            # Check against existing entities
            existing_entity = self.memory_system.get_entity(element_name, element_type)
            
            if existing_entity:
                canonical_name = existing_entity["name"]
                if canonical_name != element_name:
                    recommendations[element_name] = canonical_name
            else:
                # Check for similar names that might be variants
                similar = self._find_naming_variants(element_name, element_type)
                if similar:
                    recommendations[element_name] = similar["name"]
        
        return recommendations
    
    def resolve_naming_conflicts(self, elements: List[Dict]) -> List[Dict]:
        """Resolve naming conflicts and return updated elements."""
        return self.memory_system.resolve_naming_conflicts(elements)
    
    def generate_naming_report(self) -> Dict[str, Any]:
        """Generate a report on naming consistency across the design."""
        report = {
            "total_entities": len(self.memory_system.entities),
            "entity_types": {},
            "naming_conflicts": [],
            "recommendations": [],
            "consistency_score": 0.0
        }
        
        # Count entities by type
        for entity in self.memory_system.entities.values():
            entity_type = entity["type"]
            if entity_type not in report["entity_types"]:
                report["entity_types"][entity_type] = 0
            report["entity_types"][entity_type] += 1
        
        # Identify potential conflicts
        conflicts = self._identify_conflicts()
        report["naming_conflicts"] = conflicts
        
        # Calculate consistency score
        total_entities = len(self.memory_system.entities)
        conflict_count = len(conflicts)
        
        if total_entities > 0:
            report["consistency_score"] = max(0.0, 1.0 - (conflict_count / total_entities))
        
        # Generate recommendations
        report["recommendations"] = self._generate_recommendations()
        
        return report
    
    def _find_naming_variants(self, name: str, entity_type: str) -> Optional[Dict]:
        """Find potential naming variants of an entity."""
        name_lower = name.lower()
        
        for entity in self.memory_system.entities.values():
            if entity["type"] == entity_type:
                entity_name_lower = entity["name"].lower()
                
                # Check for exact match in variants
                if name_lower in [v.lower() for v in entity["variants"]]:
                    return entity
                
                # Check for partial matches
                if (name_lower in entity_name_lower or 
                    entity_name_lower in name_lower) and abs(len(name) - len(entity["name"])) <= 3:
                    return entity
        
        return None
    
    def _identify_conflicts(self) -> List[Dict]:
        """Identify potential naming conflicts."""
        conflicts = []
        
        # Group entities by type
        entities_by_type = defaultdict(list)
        for entity in self.memory_system.entities.values():
            entities_by_type[entity["type"]].append(entity)
        
        # Check for conflicts within each type
        for entity_type, entities in entities_by_type.items():
            for i, entity1 in enumerate(entities):
                for entity2 in entities[i+1:]:
                    similarity = self._calculate_name_similarity(entity1["name"], entity2["name"])
                    if similarity > 0.7:  # High similarity threshold
                        conflicts.append({
                            "entity1": entity1["name"],
                            "entity2": entity2["name"],
                            "type": entity_type,
                            "similarity": similarity,
                            "issue": "Similar names may cause confusion"
                        })
        
        return conflicts
    
    def _calculate_name_similarity(self, name1: str, name2: str) -> float:
        """Calculate similarity between two names (simple implementation)."""
        name1_lower = name1.lower()
        name2_lower = name2.lower()
        
        if name1_lower == name2_lower:
            return 1.0
        
        # Simple character-based similarity
        shorter = min(len(name1_lower), len(name2_lower))
        longer = max(len(name1_lower), len(name2_lower))
        
        if shorter == 0:
            return 0.0
        
        # Count common characters
        common_chars = sum(1 for c1, c2 in zip(name1_lower, name2_lower) if c1 == c2)
        
        return common_chars / longer
    
    def _generate_recommendations(self) -> List[str]:
        """Generate naming recommendations based on current state."""
        recommendations = []
        
        # Basic recommendations
        if len(self.memory_system.entities) > 0:
            recommendations.append("Maintain consistent naming conventions across all C4 levels")
            recommendations.append("Use descriptive names that clearly indicate purpose")
        
        # Specific recommendations based on entities
        entity_types = set(entity["type"] for entity in self.memory_system.entities.values())
        
        if "container" in entity_types:
            recommendations.append("Use Service/API/App suffixes for containers to indicate their nature")
        
        if "component" in entity_types:
            recommendations.append("Use Controller/Manager/Repository patterns for component naming")
        
        return recommendations