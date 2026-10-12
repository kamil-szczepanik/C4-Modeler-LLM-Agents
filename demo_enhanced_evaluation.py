#!/usr/bin/env python3
"""
Enhanced Evaluation Demo Script

Demonstrates the new ISO/IEC 25010, ATAM, and Architectural Soundness evaluation layers
for the C4-Modeler-LLM-Agents journal extension.

Usage:
    python demo_enhanced_evaluation.py
"""

import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from c4modeler.evaluation import (
    run_full_evaluation,
    run_enhanced_evaluation_only,
    evaluate_iso_25010_attributes,
    evaluate_atam_scenarios,
    evaluate_architectural_soundness
)
from c4modeler.experiments import EnhancedExperimentRunner


def load_sample_c4_model():
    """Load a sample C4 model from the existing results."""
    
    # Try to load an existing result
    results_dir = Path("notebooks/data/results")
    
    # Look for existing results
    for result_dir in results_dir.glob("*"):
        if result_dir.is_dir():
            context_yaml = result_dir / "1_context_definition.yaml"
            context_puml = result_dir / "1_context_diagram.puml"
            container_yaml = result_dir / "2_container_definition.yaml"
            container_puml = result_dir / "2_container_diagram.puml"
            
            if all(f.exists() for f in [context_yaml, context_puml, container_yaml, container_puml]):
                print(f"📁 Loading sample C4 model from: {result_dir}")
                
                c4_model = {
                    "context": {
                        "yaml_definition": context_yaml.read_text(encoding='utf-8'),
                        "diagram": context_puml.read_text(encoding='utf-8')
                    },
                    "containers": {
                        "yaml_definition": container_yaml.read_text(encoding='utf-8'), 
                        "diagram": container_puml.read_text(encoding='utf-8')
                    },
                    "components": {}
                }
                
                # Load component files if they exist
                components_dir = result_dir / "3_components"
                if components_dir.exists():
                    for yaml_file in components_dir.glob("*_definition.yaml"):
                        comp_name = yaml_file.stem.replace("_definition", "")
                        puml_file = components_dir / f"{comp_name}_diagram.puml"
                        
                        if puml_file.exists():
                            c4_model["components"][comp_name] = {
                                "yaml_definition": yaml_file.read_text(encoding='utf-8'),
                                "diagram": puml_file.read_text(encoding='utf-8')
                            }
                
                return c4_model
    
    # Fallback to mock model if no existing results
    print("⚠️ No existing results found, using mock model")
    return create_mock_c4_model()


def create_mock_c4_model():
    """Create a mock C4 model for demonstration."""
    
    return {
        "context": {
            "yaml_definition": """
level: context
scope: "System Context diagram for Healthcare Management System"
system:
  name: "Healthcare Management System"
  description: "Manages patient records, appointments, and billing for healthcare providers"
elements:
  - type: "person"
    name: "Healthcare Provider"
    description: "Medical professionals who need access to patient information"
  - type: "person" 
    name: "Patient"
    description: "Individuals seeking healthcare services"
  - type: "person"
    name: "Administrator"
    description: "Staff managing clinic operations and billing"
  - type: "externalSystem"
    name: "Insurance API"
    description: "External system for insurance claim processing"
  - type: "externalSystem"
    name: "Lab System"
    description: "Laboratory information management system"
relationships:
  - source: "Healthcare Provider"
    destination: "Healthcare Management System"
    description: "Access patient records and schedule appointments"
    technology: "HTTPS/Web Browser"
  - source: "Patient"
    destination: "Healthcare Management System"
    description: "Book appointments and view medical records"
    technology: "Mobile App/Web"
  - source: "Healthcare Management System"
    destination: "Insurance API"
    description: "Submit insurance claims and verify coverage"
    technology: "REST API"
""",
            "diagram": """
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

title System Context - Healthcare Management System

Person(provider, "Healthcare Provider", "Medical professionals")
Person(patient, "Patient", "Individuals seeking healthcare")
Person(admin, "Administrator", "Clinic operations staff")

System(hms, "Healthcare Management System", "Manages patient records, appointments, and billing")

System_Ext(insurance, "Insurance API", "External insurance system")
System_Ext(lab, "Lab System", "Laboratory information system")

Rel(provider, hms, "Access patient records", "HTTPS")
Rel(patient, hms, "Book appointments", "Mobile/Web")
Rel(admin, hms, "Manage operations", "Web")
Rel(hms, insurance, "Submit claims", "REST API")
Rel(hms, lab, "Request lab results", "HL7 FHIR")

@enduml
"""
        },
        "containers": {
            "yaml_definition": """
level: containers
scope: "Container diagram for Healthcare Management System"
system:
  name: "Healthcare Management System"
  description: "Manages patient records, appointments, and billing"
elements:
  - type: "container"
    name: "Web Application"
    description: "Provides web-based interface for healthcare providers and administrators"
    technology: "React, TypeScript"
  - type: "container"
    name: "Mobile Application"
    description: "Mobile app for patients to manage appointments and access records"
    technology: "React Native"
  - type: "container"
    name: "API Gateway"
    description: "Routes requests and handles authentication"
    technology: "Kong, JWT"
  - type: "container"
    name: "Patient Service"
    description: "Manages patient demographics and medical records"
    technology: "Node.js, Express"
  - type: "container"
    name: "Appointment Service"
    description: "Handles appointment scheduling and calendar management"
    technology: "Python, FastAPI"
  - type: "container"
    name: "Billing Service"
    description: "Processes billing and insurance claims"
    technology: "Java, Spring Boot"
  - type: "container"
    name: "Database"
    description: "Stores all system data with encryption at rest"
    technology: "PostgreSQL, AES-256"
relationships:
  - source: "Web Application"
    destination: "API Gateway"
    description: "Makes API requests"
    technology: "HTTPS, REST"
  - source: "API Gateway"
    destination: "Patient Service"
    description: "Routes patient requests"
    technology: "HTTP, JSON"
""",
            "diagram": """
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Container_Boundary(hms, "Healthcare Management System") {
    Container(web, "Web Application", "React, TypeScript", "Web interface for providers")
    Container(mobile, "Mobile Application", "React Native", "Patient mobile app")
    Container(gateway, "API Gateway", "Kong, JWT", "Authentication and routing")
    Container(patient_svc, "Patient Service", "Node.js", "Patient data management")
    Container(appt_svc, "Appointment Service", "Python, FastAPI", "Scheduling")
    Container(billing_svc, "Billing Service", "Java, Spring", "Billing and claims")
    ContainerDb(db, "Database", "PostgreSQL", "System data store")
}

Rel(web, gateway, "API requests", "HTTPS")
Rel(mobile, gateway, "API requests", "HTTPS")
Rel(gateway, patient_svc, "Patient requests", "HTTP")
Rel(gateway, appt_svc, "Appointment requests", "HTTP")
Rel(gateway, billing_svc, "Billing requests", "HTTP")
Rel(patient_svc, db, "Read/Write", "SQL")
Rel(appt_svc, db, "Read/Write", "SQL")
Rel(billing_svc, db, "Read/Write", "SQL")

@enduml
"""
        },
        "components": {
            "patient_service": {
                "yaml_definition": """
level: components
scope: "Component diagram for Patient Service"
container:
  name: "Patient Service"
  description: "Manages patient demographics and medical records"
elements:
  - type: "component"
    name: "Patient Controller"
    description: "REST API endpoints for patient operations"
    technology: "Express Router"
  - type: "component" 
    name: "Patient Repository"
    description: "Data access layer for patient information"
    technology: "Sequelize ORM"
  - type: "component"
    name: "EMR Manager"
    description: "Electronic medical records business logic"
    technology: "Node.js Service"
  - type: "component"
    name: "Audit Logger"
    description: "HIPAA-compliant audit trail for patient access"
    technology: "Winston Logger"
relationships:
  - source: "Patient Controller"
    destination: "EMR Manager"
    description: "Delegates business logic"
    technology: "Function calls"
  - source: "EMR Manager"
    destination: "Patient Repository"
    description: "Data persistence operations"
    technology: "ORM calls"
""",
                "diagram": """
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

Container_Boundary(patient_svc, "Patient Service") {
    Component(controller, "Patient Controller", "Express Router", "REST endpoints")
    Component(emr_mgr, "EMR Manager", "Node.js Service", "Business logic")
    Component(repo, "Patient Repository", "Sequelize ORM", "Data access")
    Component(audit, "Audit Logger", "Winston", "HIPAA audit trail")
}

Rel(controller, emr_mgr, "Delegates to", "Function calls")
Rel(emr_mgr, repo, "Persists data", "ORM")
Rel(emr_mgr, audit, "Log access", "Events")

@enduml
"""
            }
        }
    }


def load_sample_brief():
    """Load a sample system brief."""
    
    brief_path = Path("data/briefs/clinic-management-system.yaml")
    if brief_path.exists():
        return brief_path.read_text(encoding='utf-8')
    
    # Fallback mock brief
    return """
title: Healthcare Management System
description: >
  Comprehensive healthcare management platform for medical practices,
  handling patient records, appointment scheduling, and billing operations.
domain: Healthcare IT
constraints:
  - "HIPAA compliance required"
  - "High availability 99.9%"
  - "Data encryption at rest and in transit"
functional_requirements:
  - id: R-01
    desc: "Patient registration and demographic management"
  - id: R-02
    desc: "Electronic medical records with audit trail"
  - id: R-03
    desc: "Appointment scheduling with conflict detection"
  - id: R-04
    desc: "Billing and insurance claim processing"
nonfunctional_requirements:
  - id: R-05
    quality: Security
    desc: "Multi-factor authentication and role-based access"
  - id: R-06
    quality: Performance
    desc: "Response times under 2 seconds for 95% of requests"
  - id: R-07
    quality: Availability
    desc: "System uptime of 99.9% with disaster recovery"
target_cloud:
  provider: AWS
  regions:
    - us-east-1
    - us-west-2
"""


def demo_individual_layers():
    """Demonstrate each evaluation layer individually."""
    
    print("\n" + "="*60)
    print("🧪 DEMO: Individual Evaluation Layers")
    print("="*60)
    
    system_brief = load_sample_brief()
    c4_model = load_sample_c4_model()
    
    # Demo Layer A: ISO/IEC 25010
    print("\n📊 Layer A: ISO/IEC 25010 Quality Attributes")
    print("-" * 50)
    
    # Create minimal legacy results for mapping
    mock_legacy = {
        "missingInformation": {"score": 95},
        "compilationSuccess": {"score": 100},
        "abstractionAdherence": {"score": 85},
        "emergentNamingConsistency": {"score": 78},
        "securityAssessment": {"riskCount": 3},
        "contextEvaluation": {"semanticConsistency": {"score": 88}, "qualitativeRubric": {"clarity": 8}},
        "containerEvaluation": {"definitionalConsistency": {"score": 92}, "qualitativeRubric": {"clarity": 7}},
        "componentEvaluations": {}
    }
    
    iso_results = evaluate_iso_25010_attributes(system_brief, c4_model, mock_legacy)
    print("ISO/IEC 25010 Scores:")
    for attr, score in iso_results["scores"].items():
        print(f"  {attr}: {score}/5")
    print(f"Overall Score: {iso_results['overall_score']}/5")
    
    # Demo Layer B: ATAM Scenarios
    print("\n🎯 Layer B: ATAM Scenario Responsiveness")
    print("-" * 50)
    
    atam_results = evaluate_atam_scenarios(system_brief, c4_model)
    print("Scenario Responsiveness:")
    for scenario in atam_results["scenarios"]:
        print(f"  {scenario['scenario_id']} ({scenario['quality_attribute']}): RI = {scenario['responsiveness_index']}")
    print(f"Overall Responsiveness: {atam_results['overall_responsiveness']}")
    
    # Demo Layer C: Architectural Soundness
    print("\n🏗️ Layer C: Architectural Soundness Metrics")
    print("-" * 50)
    
    soundness_results = evaluate_architectural_soundness(c4_model, system_brief)
    print("Soundness Metrics:")
    print(f"  Coupling Density: {soundness_results['coupling_density']}")
    print(f"  Abstraction Coherence: {soundness_results['abstraction_coherence']}")
    print(f"  Layering Violations: {soundness_results['layering_violations']}")
    print(f"  Semantic Completeness: {soundness_results['semantic_completeness']}")


def demo_full_evaluation():
    """Demonstrate the full evaluation with both legacy and enhanced layers."""
    
    print("\n" + "="*60)
    print("🔬 DEMO: Full Enhanced Evaluation")
    print("="*60)
    
    system_brief = load_sample_brief()
    c4_model = load_sample_c4_model()
    
    # Run full evaluation with enhanced metrics
    print("\n⚡ Running full evaluation (this may take a moment with LLM calls)...")
    
    # Note: This would make actual LLM calls for the judge evaluations
    # For demo purposes, we'll use the enhanced-only version
    results = run_enhanced_evaluation_only(system_brief, c4_model)
    
    print("\n📋 Enhanced Evaluation Results Summary:")
    print("-" * 40)
    
    # ISO Results
    iso_data = results.get("iso25010Attributes", {})
    print(f"\n🌟 ISO/IEC 25010 Overall Score: {iso_data.get('overall_score', 'N/A')}/5")
    
    # ATAM Results  
    atam_data = results.get("atamScenarios", {})
    print(f"🎯 ATAM Overall Responsiveness: {atam_data.get('overall_responsiveness', 'N/A')}")
    
    # Soundness Results
    soundness_data = results.get("architecturalSoundness", {})
    print(f"🏗️ Coupling Density: {soundness_data.get('coupling_density', 'N/A')}")
    print(f"🏗️ Abstraction Coherence: {soundness_data.get('abstraction_coherence', 'N/A')}")
    
    # Save results
    output_file = "demo_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Full results saved to: {output_file}")


def demo_experiment_runner():
    """Demonstrate the enhanced experiment runner."""
    
    print("\n" + "="*60)
    print("🧬 DEMO: Enhanced Experiment Runner")
    print("="*60)
    
    # Initialize experiment runner
    runner = EnhancedExperimentRunner()
    
    # Check if config exists
    if not runner.config:
        print("⚠️ No experiment config found. Please ensure experiment_configs.yaml exists.")
        return
    
    print(f"📚 Loaded {len(runner.config.get('experiments', {}))} experiment configurations:")
    for exp_name, exp_config in runner.config.get("experiments", {}).items():
        print(f"  - {exp_name}: {exp_config['name']}")
    
    print("\n🔧 Experiment runner initialized successfully!")
    print("📝 Note: To run actual experiments, use runner.run_experiment(experiment_name)")
    print("🚀 Example: runner.run_experiment('role_ablation')")


def main():
    """Main demonstration function."""
    
    print("🌟 Enhanced C4 Evaluation System Demo")
    print("=" * 60)
    print("This demo showcases the new evaluation layers for the journal extension:")
    print("  • Layer A: ISO/IEC 25010 Quality Attribute Mapping")
    print("  • Layer B: ATAM-Inspired Scenario Evaluation") 
    print("  • Layer C: Quantitative Architectural Soundness Metrics")
    print("=" * 60)
    
    try:
        # Demo individual layers
        demo_individual_layers()
        
        # Demo full evaluation
        demo_full_evaluation()
        
        # Demo experiment runner
        demo_experiment_runner()
        
        print("\n🎉 Demo completed successfully!")
        print("\nNext steps:")
        print("  1. Integrate the enhanced evaluation with your C4 generation system")
        print("  2. Run the enhanced experiments using EnhancedExperimentRunner")
        print("  3. Analyze results for your journal paper")
        
    except Exception as e:
        print(f"\n❌ Demo failed with error: {str(e)}")
        print("Please check that all dependencies are installed and files exist.")


if __name__ == "__main__":
    main()