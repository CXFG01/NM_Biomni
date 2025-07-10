#!/usr/bin/env python3
"""
Basic functionality test for Biomni repository.
Tests core components without requiring full environment setup.
"""

import sys
import os
from pathlib import Path

# Add the current directory to the path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that core modules can be imported."""
    print("Testing imports...")
    
    try:
        from biomni.version import __version__
        print(f"✓ Biomni version: {__version__}")
    except ImportError as e:
        print(f"✗ Failed to import version: {e}")
        return False
    
    try:
        from biomni.tool.support_tools import run_python_repl
        print("✓ Support tools imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import support tools: {e}")
        return False
    
    try:
        from biomni.utils import pretty_print
        print("✓ Utils imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import utils: {e}")
        return False
    
    return True

def test_python_repl():
    """Test the Python REPL functionality."""
    print("\nTesting Python REPL...")
    
    try:
        from biomni.tool.support_tools import run_python_repl
        
        # Test basic Python execution
        result = run_python_repl('print("Hello from Biomni!")')
        if "Hello from Biomni!" in result:
            print("✓ Basic Python REPL works")
        else:
            print(f"✗ Unexpected REPL output: {result}")
            return False
            
        # Test mathematical operations
        result = run_python_repl('x = 5 + 3\nprint(f"Result: {x}")')
        if "Result: 8" in result:
            print("✓ Mathematical operations work")
        else:
            print(f"✗ Mathematical operations failed: {result}")
            return False
            
        # Test persistent namespace
        result = run_python_repl('print(f"Previous x value: {x}")')
        if "Previous x value: 8" in result:
            print("✓ Persistent namespace works")
        else:
            print(f"✗ Persistent namespace failed: {result}")
            return False
            
    except Exception as e:
        print(f"✗ Python REPL test failed: {e}")
        return False
    
    return True

def test_tool_registry():
    """Test the tool registry system."""
    print("\nTesting tool registry...")
    
    try:
        from biomni.tool.tool_registry import ToolRegistry
        
        # Create a test tool
        test_tools = {
            "test_module": [
                {
                    "name": "test_function",
                    "description": "A test function",
                    "required_parameters": ["param1"],
                    "optional_parameters": ["param2"]
                }
            ]
        }
        
        # Initialize registry
        registry = ToolRegistry(test_tools)
        
        # Test basic operations
        tool = registry.get_tool_by_name("test_function")
        if tool and tool["name"] == "test_function":
            print("✓ Tool registry creation and retrieval works")
        else:
            print("✗ Tool registry failed")
            return False
            
        # Test tool listing
        tools = registry.list_tools()
        if len(tools) == 1 and tools[0]["name"] == "test_function":
            print("✓ Tool listing works")
        else:
            print("✗ Tool listing failed")
            return False
            
    except Exception as e:
        print(f"✗ Tool registry test failed: {e}")
        return False
    
    return True

def test_environment_description():
    """Test the environment description system."""
    print("\nTesting environment description...")
    
    try:
        from biomni.env_desc import data_lake_dict, library_content_dict
        
        # Check data lake dictionary
        if len(data_lake_dict) > 0:
            print(f"✓ Data lake contains {len(data_lake_dict)} datasets")
            # Print first few entries
            for i, (key, value) in enumerate(data_lake_dict.items()):
                if i < 3:
                    print(f"  - {key}: {value[:50]}...")
        else:
            print("✗ Data lake dictionary is empty")
            return False
            
        # Check library content dictionary
        if len(library_content_dict) > 0:
            print(f"✓ Library content contains {len(library_content_dict)} entries")
        else:
            print("✗ Library content dictionary is empty")
            return False
            
    except Exception as e:
        print(f"✗ Environment description test failed: {e}")
        return False
    
    return True

def test_tool_modules():
    """Test that tool modules can be imported."""
    print("\nTesting tool modules...")
    
    tool_modules = [
        "biochemistry",
        "genomics", 
        "pharmacology",
        "cell_biology",
        "molecular_biology"
    ]
    
    imported_count = 0
    for module_name in tool_modules:
        try:
            module = __import__(f"biomni.tool.{module_name}", fromlist=[module_name])
            print(f"✓ {module_name} module imported successfully")
            imported_count += 1
        except ImportError as e:
            print(f"✗ Failed to import {module_name}: {e}")
        except Exception as e:
            print(f"✗ Error importing {module_name}: {e}")
    
    if imported_count >= len(tool_modules) // 2:
        print(f"✓ Successfully imported {imported_count}/{len(tool_modules)} tool modules")
        return True
    else:
        print(f"✗ Only imported {imported_count}/{len(tool_modules)} tool modules")
        return False

def main():
    """Run all tests."""
    print("=== Biomni Basic Functionality Test ===")
    print()
    
    tests = [
        test_imports,
        test_python_repl,
        test_tool_registry,
        test_environment_description,
        test_tool_modules
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"✗ Test {test.__name__} crashed: {e}")
            print()
    
    print("=== Test Summary ===")
    print(f"Passed: {passed}/{total} tests")
    
    if passed == total:
        print("🎉 All tests passed! Biomni core functionality is working.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())