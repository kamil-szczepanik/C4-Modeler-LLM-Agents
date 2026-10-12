"""
Quick test to verify token optimization changes work correctly.
This test will run a simple collaborative workflow to ensure no regressions.
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from c4modeler.graph import create_c4_modeler_graph
from c4modeler.types import State
from collections import deque

def test_basic_workflow():
    """Test that the optimized workflow still works correctly."""
    print("=" * 60)
    print("Testing Token-Optimized Workflow")
    print("=" * 60)
    
    # Simple test brief
    test_brief = """
name: Simple Test System
description: A minimal system for testing token optimization
type: web_application
users:
  - name: Test User
    description: A user who tests the system
features:
  - name: Basic Feature
    description: A simple feature to test workflow
"""
    
    # Create graph with optimized settings
    graph = create_c4_modeler_graph(
        model_name="gemini-2.5-flash",
        analysis_method="collaborative",
        collab_rounds=1  # Just 1 round for quick test
    )
    
    initial_state = State(
        system_brief=test_brief,
        c4_model={},
        component_queue=None
    )
    
    try:
        print("\n🧪 Running optimized workflow...")
        result = graph.invoke(initial_state)
        
        # Verify we got the expected outputs
        assert "c4_model" in result, "Missing c4_model in result"
        assert "context" in result["c4_model"], "Missing context level"
        assert "analysis" in result["c4_model"]["context"], "Missing context analysis"
        
        print("\n✅ SUCCESS: Workflow completed successfully!")
        print(f"\n📊 Results:")
        print(f"  - Context analysis length: {len(result['c4_model']['context']['analysis'])} chars")
        
        # Check containers
        if "containers" in result["c4_model"]:
            print(f"  - Container analysis length: {len(result['c4_model']['containers'].get('analysis', ''))} chars")
            container_yaml = result['c4_model']['containers'].get('yaml_definition', '')
            if container_yaml:
                print(f"  - Container YAML length: {len(container_yaml)} chars")
                # Try to parse and count containers
                try:
                    import yaml
                    parsed = yaml.safe_load(container_yaml)
                    containers = [e for e in parsed.get('elements', []) if e.get('type') == 'container']
                    print(f"  - Containers defined: {len(containers)}")
                    if len(containers) > 0:
                        print(f"    ✅ Container names: {[c['name'] for c in containers]}")
                    else:
                        print(f"    ⚠️  WARNING: No containers found in YAML!")
                except Exception as e:
                    print(f"    ⚠️  Could not parse container YAML: {e}")
        
        # Check component queue
        if result.get("component_queue") is not None:
            print(f"  - Component queue: {list(result['component_queue'])}")
        
        # Check if analysis is reasonably sized (should be much shorter with optimization)
        if len(result['c4_model']['context']['analysis']) < 5000:
            print("\n✅ Analysis is concise (< 5000 chars) - optimization working!")
        else:
            print("\n⚠️  Analysis is still quite long - may need further optimization")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_basic_workflow()
    sys.exit(0 if success else 1)
