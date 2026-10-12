"""
Quick test to verify temperature configuration is working correctly
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from c4modeler.llm import get_llm

def test_temperature_configuration():
    """Test that temperature parameter works correctly"""
    
    print("Testing temperature configuration...\n")
    
    # Test 1: Default temperature (should be 0.5)
    print("Test 1: Default temperature")
    llm_default = get_llm("gemini-2.5-flash-lite")
    print(f"✓ Default LLM instantiated")
    print(f"  Expected temperature: 0.5")
    print(f"  Actual temperature: {llm_default.temperature}")
    assert llm_default.temperature == 0.5, "Default temperature should be 0.5"
    print("  ✓ PASSED\n")
    
    # Test 2: Custom temperature
    print("Test 2: Custom temperature (0.7)")
    llm_custom = get_llm("gemini-2.5-flash-lite", temperature=0.7)
    print(f"  Expected temperature: 0.7")
    print(f"  Actual temperature: {llm_custom.temperature}")
    assert llm_custom.temperature == 0.7, "Custom temperature should be 0.7"
    print("  ✓ PASSED\n")
    
    # Test 3: Deterministic mode
    print("Test 3: Deterministic mode (0.0)")
    llm_deterministic = get_llm("gemini-2.5-flash-lite", temperature=0.0)
    print(f"  Expected temperature: 0.0")
    print(f"  Actual temperature: {llm_deterministic.temperature}")
    assert llm_deterministic.temperature == 0.0, "Deterministic temperature should be 0.0"
    print("  ✓ PASSED\n")
    
    # Test 4: High creativity mode
    print("Test 4: High creativity mode (1.0)")
    llm_creative = get_llm("gemini-2.5-flash-lite", temperature=1.0)
    print(f"  Expected temperature: 1.0")
    print(f"  Actual temperature: {llm_creative.temperature}")
    assert llm_creative.temperature == 1.0, "Creative temperature should be 1.0"
    print("  ✓ PASSED\n")
    
    print("="*60)
    print("✓ All temperature tests passed!")
    print("="*60)
    print("\nTemperature configuration is working correctly.")
    print("You can now run experiments with configurable temperature:")
    print("  python run_parallel_experiments.py --temperature 0.5")

if __name__ == "__main__":
    test_temperature_configuration()
