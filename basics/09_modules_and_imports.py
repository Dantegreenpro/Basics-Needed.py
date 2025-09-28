#!/usr/bin/env python3
"""
Python Basics: Modules and Imports

This file covers how to organize and reuse code in Python:
- What are modules and packages
- Different ways to import modules
- Creating your own modules
- Understanding Python's module system
- Best practices for organizing code
"""

print("📦 Welcome to Python Modules and Imports! 📦")
print("=" * 48)

# ============================================================================
# WHAT ARE MODULES?
# ============================================================================

print("\n📚 WHAT ARE MODULES?")
print("-" * 21)

print("A module is a file containing Python code.")
print("Modules can contain:")
print("• Functions")
print("• Classes")  
print("• Variables")
print("• Executable statements")
print("\nModules help you:")
print("• Organize code into logical units")
print("• Reuse code across different programs")
print("• Avoid naming conflicts")
print("• Keep your main program clean and focused")

# ============================================================================
# IMPORTING BUILT-IN MODULES
# ============================================================================

print("\n🔧 IMPORTING BUILT-IN MODULES")
print("-" * 30)

# Method 1: Import entire module
import math
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi:.4f}")

# Method 2: Import specific functions
from datetime import datetime, timedelta
current_time = datetime.now()
print(f"Current time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

tomorrow = current_time + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

# Method 3: Import with alias
import random as rnd
print(f"Random number: {rnd.randint(1, 100)}")

# Method 4: Import all (generally not recommended)
# from math import *  # Imports everything from math module

# ============================================================================
# EXPLORING MODULE CONTENTS
# ============================================================================

print("\n🔍 EXPLORING MODULE CONTENTS")
print("-" * 30)

# Using dir() to see what's available in a module
print("Functions available in math module (first 10):")
math_functions = [func for func in dir(math) if not func.startswith('_')]
for func in math_functions[:10]:
    print(f"  {func}")

# Using help() to get documentation
print(f"\nHelp for math.sqrt:")
print("  math.sqrt(x) - Return the square root of x")

# Check module file location
print(f"Math module location: {math.__file__ if hasattr(math, '__file__') else 'Built-in'}")

# ============================================================================
# COMMON BUILT-IN MODULES
# ============================================================================

print("\n📋 COMMON BUILT-IN MODULES")
print("-" * 28)

# os module - Operating system interface
import os
print(f"Current working directory: {os.getcwd()}")
print(f"Environment PATH exists: {'PATH' in os.environ}")

# sys module - System-specific parameters
import sys
print(f"Python version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")

# json module - JSON encoder and decoder
import json
data = {"name": "Alice", "age": 30, "city": "Boston"}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

parsed_data = json.loads(json_string)
print(f"Parsed back: {parsed_data}")

# collections module - Specialized container datatypes
from collections import Counter, defaultdict
text = "hello world hello python"
word_count = Counter(text.split())
print(f"Word frequency: {word_count}")

# defaultdict example
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(f"Default dict: {dict(dd)}")

# ============================================================================
# CREATING YOUR OWN MODULES
# ============================================================================

print("\n🛠️ CREATING YOUR OWN MODULES")
print("-" * 31)

# Let's create a simple utility module
utility_module_content = '''"""
Utility functions for common tasks
"""

def greet(name, title=""):
    """Greet a person with optional title"""
    if title:
        return f"Hello, {title} {name}!"
    return f"Hello, {name}!"

def calculate_tax(amount, rate=0.08):
    """Calculate tax on an amount"""
    return amount * rate

def format_currency(amount):
    """Format amount as currency"""
    return f"${amount:.2f}"

# Module-level variable
VERSION = "1.0.0"

# Code that runs when module is imported
print(f"Utility module loaded (version {VERSION})")

# Code that runs only when module is run directly
if __name__ == "__main__":
    print("Running utility module directly")
    print(greet("World"))
    print(f"Tax on $100: {format_currency(calculate_tax(100))}")
'''

# Create the module file
with open("/tmp/utilities.py", "w") as f:
    f.write(utility_module_content)

# Add /tmp to Python path so we can import our module
sys.path.append("/tmp")

# Import our custom module
import utilities

# Use functions from our module
print(f"Greeting: {utilities.greet('Alice', 'Ms.')}")
print(f"Tax calculation: {utilities.format_currency(utilities.calculate_tax(150, 0.10))}")
print(f"Module version: {utilities.VERSION}")

# ============================================================================
# DIFFERENT IMPORT STYLES
# ============================================================================

print("\n🎭 DIFFERENT IMPORT STYLES")
print("-" * 28)

# Style 1: Import module
import utilities as util
print(f"Using alias: {util.greet('Bob')}")

# Style 2: Import specific functions
from utilities import greet, calculate_tax
print(f"Direct function call: {greet('Charlie')}")

# Style 3: Import with different name
from utilities import format_currency as fmt_curr
print(f"Renamed function: {fmt_curr(25.99)}")

# ============================================================================
# MODULE SEARCH PATH
# ============================================================================

print("\n🗺️ MODULE SEARCH PATH")
print("-" * 21)

print("Python searches for modules in this order:")
print("1. Current directory")
print("2. PYTHONPATH environment variable directories")
print("3. Standard library directories")
print("4. Site-packages directory")

print(f"\nCurrent module search paths (first 5):")
for i, path in enumerate(sys.path[:5]):
    print(f"  {i+1}. {path}")

# ============================================================================
# PACKAGES - ORGANIZING MODULES
# ============================================================================

print("\n📁 PACKAGES - ORGANIZING MODULES")
print("-" * 34)

print("A package is a directory containing modules.")
print("Packages help organize related modules together.")

# Create a sample package structure
package_dir = "/tmp/mypackage"
os.makedirs(package_dir, exist_ok=True)

# Create __init__.py (makes it a package)
init_content = '''"""
My Package - A sample Python package
"""

# Package initialization code
print("MyPackage initialized")

# Make some functions available at package level
from .math_utils import add, multiply
from .string_utils import capitalize_words

__version__ = "1.0.0"
__all__ = ["add", "multiply", "capitalize_words"]
'''

with open(f"{package_dir}/__init__.py", "w") as f:
    f.write(init_content)

# Create math_utils module
math_utils_content = '''"""
Mathematical utility functions
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
'''

with open(f"{package_dir}/math_utils.py", "w") as f:
    f.write(math_utils_content)

# Create string_utils module
string_utils_content = '''"""
String utility functions
"""

def capitalize_words(text):
    """Capitalize each word in text"""
    return " ".join(word.capitalize() for word in text.split())

def reverse_words(text):
    """Reverse the order of words"""
    return " ".join(reversed(text.split()))

def count_vowels(text):
    """Count vowels in text"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
'''

with open(f"{package_dir}/string_utils.py", "w") as f:
    f.write(string_utils_content)

print("Created sample package structure:")
print("mypackage/")
print("├── __init__.py")
print("├── math_utils.py")
print("└── string_utils.py")

# Import and use our package
import mypackage

# Use functions made available at package level
print(f"Package add function: {mypackage.add(5, 3)}")
print(f"Package capitalize: {mypackage.capitalize_words('hello world')}")

# Import specific module from package
from mypackage import string_utils
print(f"Count vowels: {string_utils.count_vowels('Hello Python')}")

# ============================================================================
# RELATIVE IMPORTS (IN PACKAGES)
# ============================================================================

print("\n🔗 RELATIVE IMPORTS")
print("-" * 20)

print("Within packages, you can use relative imports:")
print("• from . import module_name (same directory)")
print("• from .. import module_name (parent directory)")
print("• from .subpackage import module (subdirectory)")

print("\nRelative imports only work within packages!")
print("They help avoid conflicts with similarly named modules.")

# ============================================================================
# THE __name__ VARIABLE
# ============================================================================

print("\n🏷️ THE __name__ VARIABLE")
print("-" * 23)

print(f"Current module's __name__: {__name__}")

print("\nThe __name__ variable:")
print("• Equals '__main__' when script is run directly")
print("• Equals the module name when imported")
print("• Used to create executable modules that can also be imported")

# Demonstrate with our utilities module
exec_code = '''
# This is what we put in utilities.py:
if __name__ == "__main__":
    print("Running as main script")
    # Code here only runs when script is executed directly
else:
    print("Imported as module")
'''

print(f"\nExample pattern:")
print(exec_code)

# ============================================================================
# THIRD-PARTY PACKAGES (pip)
# ============================================================================

print("\n🌐 THIRD-PARTY PACKAGES")
print("-" * 26)

print("Python has a huge ecosystem of third-party packages:")
print("• requests - HTTP library")
print("• numpy - Numerical computing")
print("• pandas - Data analysis")
print("• matplotlib - Plotting")
print("• flask/django - Web frameworks")

print("\nInstall packages with pip:")
print("  pip install package_name")
print("  pip install requests numpy pandas")
print("  pip list  # Show installed packages")
print("  pip show package_name  # Show package info")

# ============================================================================
# VIRTUAL ENVIRONMENTS
# ============================================================================

print("\n🏠 VIRTUAL ENVIRONMENTS")
print("-" * 25)

print("Virtual environments isolate project dependencies:")
print("• Create: python -m venv myenv")
print("• Activate: source myenv/bin/activate (Linux/Mac)")
print("•          myenv\\Scripts\\activate (Windows)")
print("• Deactivate: deactivate")
print("• Requirements file: pip freeze > requirements.txt")
print("• Install from requirements: pip install -r requirements.txt")

# ============================================================================
# MODULE BEST PRACTICES
# ============================================================================

print("\n✅ MODULE BEST PRACTICES")
print("-" * 26)

print("1. Use descriptive module names (lowercase with underscores)")
print("2. Include docstrings at the top of modules")
print("3. Import standard library modules first, then third-party, then local")
print("4. Use absolute imports when possible")
print("5. Avoid 'from module import *' in production code")
print("6. Use __all__ to control what gets exported")
print("7. Handle ImportError exceptions for optional dependencies")

# Example of import organization
import_example = '''
# Standard library imports
import os
import sys
import json

# Third-party imports
import requests
import numpy as np

# Local application imports
from mypackage import utilities
from . import config
'''

print(f"\nImport organization example:")
print(import_example)

# ============================================================================
# HANDLING IMPORT ERRORS
# ============================================================================

print("\n🚨 HANDLING IMPORT ERRORS")
print("-" * 27)

def safe_import_demo():
    """Demonstrate safe importing with error handling"""
    
    # Try to import optional dependency
    try:
        import sqlite3
        print("✅ sqlite3 is available")
        return True
    except ImportError:
        print("❌ sqlite3 is not available")
        return False
    
    # Alternative approach for optional features
    try:
        import matplotlib.pyplot as plt
        HAS_MATPLOTLIB = True
        print("✅ matplotlib is available")
    except ImportError:
        HAS_MATPLOTLIB = False
        print("❌ matplotlib not available - plotting disabled")
    
    return HAS_MATPLOTLIB

has_optional = safe_import_demo()

# ============================================================================
# REAL-WORLD EXAMPLES
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLES")
print("-" * 25)

# Example 1: Configuration module
config_content = '''"""
Application configuration settings
"""

# Database settings
DATABASE = {
    "host": "localhost",
    "port": 5432,
    "name": "myapp",
    "user": "admin"
}

# API settings
API_SETTINGS = {
    "base_url": "https://api.example.com",
    "timeout": 30,
    "retry_attempts": 3
}

# Feature flags
FEATURES = {
    "debug_mode": True,
    "email_notifications": True,
    "advanced_analytics": False
}

def get_database_url():
    """Build database URL from settings"""
    return f"postgresql://{DATABASE['user']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['name']}"
'''

with open("/tmp/config.py", "w") as f:
    f.write(config_content)

# Import and use configuration
import config
print(f"Database URL: {config.get_database_url()}")
print(f"Debug mode: {config.FEATURES['debug_mode']}")

# Example 2: Logger utility module
logger_content = '''"""
Logging utilities for the application
"""

import logging
import sys
from datetime import datetime

def setup_logger(name, level=logging.INFO):
    """Set up a logger with standard configuration"""
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

# Module-level logger
logger = setup_logger(__name__)

def log_function_call(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} failed: {e}")
            raise
    return wrapper
'''

with open("/tmp/logger_utils.py", "w") as f:
    f.write(logger_content)

# Import and use logger utility
import logger_utils

# Create application logger
app_logger = logger_utils.setup_logger("MyApp")
app_logger.info("Application started")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Create a math utilities module with various calculation functions")
print("2. Build a package for file operations (read, write, backup, etc.)")
print("3. Create a configuration system using modules")
print("4. Build a simple plugin system using dynamic imports")
print("5. Create a module that works both as script and import")

# Example: Simple calculator module
calculator_content = '''"""
Simple calculator module

Can be used as:
1. Import: from calculator import add, subtract
2. Script: python calculator.py
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# This runs only when script is executed directly
if __name__ == "__main__":
    print("Calculator Module")
    print("=================")
    
    # Simple calculator interface
    while True:
        try:
            expr = input("Enter calculation (or 'quit'): ")
            if expr.lower() == 'quit':
                break
            
            result = eval(expr)  # Note: eval is dangerous in real apps
            print(f"Result: {result}")
            
        except Exception as e:
            print(f"Error: {e}")
    
    print("Calculator closed!")
'''

with open("/tmp/calculator.py", "w") as f:
    f.write(calculator_content)

# Import and test the calculator
import calculator
print(f"\nTesting calculator module:")
print(f"5 + 3 = {calculator.add(5, 3)}")
print(f"10 - 4 = {calculator.subtract(10, 4)}")
print(f"6 * 7 = {calculator.multiply(6, 7)}")
print(f"15 / 3 = {calculator.divide(15, 3)}")

print("\n🎉 Fantastic! You've mastered Python modules and imports!")
print("You now have all the basic Python skills needed!")
print("Ready to move on to intermediate topics! 🚀")