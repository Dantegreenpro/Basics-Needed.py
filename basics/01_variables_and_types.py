#!/usr/bin/env python3
"""
Python Basics: Variables and Data Types

This file covers the fundamental building blocks of Python programming:
- Variables and how to create them
- Different data types in Python
- Basic operations with each type
"""

print("🐍 Welcome to Python Variables and Data Types! 🐍")
print("=" * 50)

# ============================================================================
# VARIABLES IN PYTHON
# ============================================================================

print("\n📦 VARIABLES")
print("-" * 20)

# Variables are like containers that store data
# In Python, you don't need to declare the type - it's inferred automatically!

name = "Alice"              # String (text)
age = 25                    # Integer (whole number)
height = 5.6                # Float (decimal number)
is_student = True           # Boolean (True/False)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is student: {is_student}")

# Variables can be reassigned to different values
age = 26  # Alice had a birthday!
print(f"Updated age: {age}")

# ============================================================================
# DATA TYPES IN PYTHON
# ============================================================================

print("\n🔤 DATA TYPES")
print("-" * 20)

# 1. STRINGS (str) - Text data
greeting = "Hello, World!"
quote = 'Python is awesome!'  # Single or double quotes work
multiline = """This is a
multiline string that
spans multiple lines."""

print(f"Greeting: {greeting}")
print(f"Quote: {quote}")
print(f"Multiline:\n{multiline}")

# String methods (functions that work on strings)
print(f"Uppercase: {greeting.upper()}")
print(f"Lowercase: {greeting.lower()}")
print(f"Length: {len(greeting)} characters")

# 2. INTEGERS (int) - Whole numbers
small_number = 42
big_number = 1000000
negative_number = -15

print(f"\nSmall number: {small_number}")
print(f"Big number: {big_number}")
print(f"Negative number: {negative_number}")

# Integer operations
print(f"Addition: {small_number} + {negative_number} = {small_number + negative_number}")
print(f"Multiplication: {small_number} * 2 = {small_number * 2}")
print(f"Division: {small_number} / 2 = {small_number / 2}")
print(f"Integer division: {small_number} // 2 = {small_number // 2}")
print(f"Remainder: {small_number} % 5 = {small_number % 5}")

# 3. FLOATS (float) - Decimal numbers
price = 19.99
temperature = -2.5
pi = 3.14159

print(f"\nPrice: ${price}")
print(f"Temperature: {temperature}°C")
print(f"Pi: {pi}")

# Float operations work the same as integers
print(f"Price with tax (10%): ${price * 1.10:.2f}")  # :.2f rounds to 2 decimal places

# 4. BOOLEANS (bool) - True or False
is_sunny = True
is_raining = False
is_weekend = True

print(f"\nIs sunny: {is_sunny}")
print(f"Is raining: {is_raining}")
print(f"Is weekend: {is_weekend}")

# Boolean operations
print(f"Sunny AND not raining: {is_sunny and not is_raining}")
print(f"Weekend OR sunny: {is_weekend or is_sunny}")

# ============================================================================
# TYPE CHECKING AND CONVERSION
# ============================================================================

print("\n🔍 TYPE CHECKING")
print("-" * 20)

# Check the type of a variable
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")

# Type conversion (casting)
number_as_string = "123"
string_as_number = int(number_as_string)

print(f"\nOriginal: '{number_as_string}' (type: {type(number_as_string)})")
print(f"Converted: {string_as_number} (type: {type(string_as_number)})")

# More conversions
float_number = float("45.67")
string_from_number = str(123)
boolean_from_number = bool(1)  # Any non-zero number is True

print(f"String to float: {float_number}")
print(f"Number to string: '{string_from_number}'")
print(f"Number to boolean: {boolean_from_number}")

# ============================================================================
# USER INPUT
# ============================================================================

print("\n💬 USER INPUT")
print("-" * 20)

# Note: input() always returns a string, even if the user types numbers!
print("Let's get some information about you:")

# Uncomment these lines to try interactive input:
# user_name = input("What's your name? ")
# user_age = input("What's your age? ")  # This will be a string!
# user_age_number = int(user_age)  # Convert to integer

# For demo purposes, we'll use preset values:
user_name = "Demo User"
user_age_number = 30

print(f"Hello, {user_name}! You are {user_age_number} years old.")
print(f"In 10 years, you'll be {user_age_number + 10} years old.")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises on your own:")
print("1. Create variables for your favorite color, lucky number, and whether you like pizza")
print("2. Calculate the area of a rectangle (length × width)")
print("3. Convert your height from feet to meters (1 foot = 0.3048 meters)")
print("4. Create a greeting message using f-strings or .format()")

# Example solutions (uncomment to see):
# favorite_color = "blue"
# lucky_number = 7
# likes_pizza = True

# length = 10
# width = 5
# area = length * width
# print(f"Rectangle area: {area}")

print("\n🎉 Great job! You've learned about Python variables and data types!")
print("Next up: Working with strings in more detail!")