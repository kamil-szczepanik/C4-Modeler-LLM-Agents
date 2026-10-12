"""
Test script to verify markdown code fence stripping for Gemini output.

Issue: Gemini models often wrap YAML and PlantUML output in markdown code fences:
    ```yaml
    level: container
    ...
    ```

This causes YAML parser to fail with: "found character '`' that cannot start any token"

Solution: Strip markdown code fences before parsing YAML or saving diagram code.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from c4modeler.agents import strip_markdown_code_fences

def test_yaml_with_fences():
    """Test stripping YAML code fences."""
    
    gemini_output = """```yaml
level: container
scope: "Container diagram for Clinic Management System"
system:
  name: "Clinic Management System"
elements:
  - type: "container"
    name: "Web Application"
    technology: "React"
```"""
    
    cleaned = strip_markdown_code_fences(gemini_output)
    
    print("📝 Testing YAML fence stripping:")
    print("-" * 60)
    print("Original output (with fences):")
    print(gemini_output[:100] + "...")
    print("\nCleaned output:")
    print(cleaned[:100] + "...")
    
    # Verify it can be parsed as YAML
    import yaml
    try:
        data = yaml.safe_load(cleaned)
        print(f"\n✅ SUCCESS: YAML parsed correctly")
        print(f"   Level: {data.get('level')}")
        print(f"   System: {data.get('system', {}).get('name')}")
        return True
    except yaml.YAMLError as e:
        print(f"\n❌ FAILED: YAML parsing error: {e}")
        return False

def test_plantuml_with_fences():
    """Test stripping PlantUML code fences."""
    
    gemini_output = """```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(user, "User", "System user")
System(system, "My System", "Does something")

Rel(user, system, "Uses")
@enduml
```"""
    
    cleaned = strip_markdown_code_fences(gemini_output)
    
    print("\n🎨 Testing PlantUML fence stripping:")
    print("-" * 60)
    print("Original output (with fences):")
    print(gemini_output[:80] + "...")
    print("\nCleaned output:")
    print(cleaned[:80] + "...")
    
    # Verify it starts with @startuml
    if cleaned.strip().startswith("@startuml"):
        print("\n✅ SUCCESS: PlantUML code cleaned correctly")
        return True
    else:
        print(f"\n❌ FAILED: PlantUML code doesn't start with @startuml")
        print(f"   Actual start: {cleaned[:20]}")
        return False

def test_no_fences():
    """Test that content without fences is unchanged."""
    
    plain_yaml = """level: container
scope: "Test"
system:
  name: "Test System"
"""
    
    cleaned = strip_markdown_code_fences(plain_yaml)
    
    print("\n📄 Testing plain content (no fences):")
    print("-" * 60)
    
    if cleaned.strip() == plain_yaml.strip():
        print("✅ SUCCESS: Plain content unchanged")
        return True
    else:
        print("❌ FAILED: Plain content was modified")
        return False

def test_language_variants():
    """Test different language specifiers in code fences."""
    
    test_cases = [
        ("```yaml\ncontent\n```", "yaml"),
        ("```plantuml\ncontent\n```", "plantuml"),
        ("```\ncontent\n```", "no language"),
        ("``` yaml\ncontent\n```", "yaml with space"),
    ]
    
    print("\n🔤 Testing different fence variants:")
    print("-" * 60)
    
    all_passed = True
    for fence_input, description in test_cases:
        cleaned = strip_markdown_code_fences(fence_input)
        if cleaned.strip() == "content":
            print(f"✅ {description}: cleaned correctly")
        else:
            print(f"❌ {description}: failed (got '{cleaned}')")
            all_passed = False
    
    return all_passed

if __name__ == "__main__":
    print("=" * 70)
    print("Testing Markdown Code Fence Stripping")
    print("=" * 70)
    
    results = []
    
    results.append(("YAML stripping", test_yaml_with_fences()))
    results.append(("PlantUML stripping", test_plantuml_with_fences()))
    results.append(("Plain content", test_no_fences()))
    results.append(("Fence variants", test_language_variants()))
    
    print("\n" + "=" * 70)
    print("Test Results:")
    print("=" * 70)
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {test_name}")
    
    all_passed = all(passed for _, passed in results)
    
    print("=" * 70)
    if all_passed:
        print("✅ ALL TESTS PASSED: Code fence stripping works correctly")
        print("   Gemini models should now generate valid YAML and PlantUML")
    else:
        print("❌ SOME TESTS FAILED: Further investigation needed")
    print("=" * 70)
