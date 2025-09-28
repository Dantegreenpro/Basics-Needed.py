#!/usr/bin/env python3
"""
Python Basics: Functions

This file covers one of the most important concepts in programming:
- Creating and calling functions
- Parameters and arguments
- Return values and scope
- Advanced function features
- Best practices and real-world examples
"""

print("🔧 Welcome to Python Functions! 🔧")
print("=" * 38)

# ============================================================================
# BASIC FUNCTIONS
# ============================================================================

print("\n📝 BASIC FUNCTIONS")
print("-" * 20)

# Simple function without parameters
def greet():
    """A simple greeting function"""
    print("Hello, World!")

print("Calling greet():")
greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

print("\nCalling greet_person():")
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def introduce(name, age, city):
    """Introduce someone with their details"""
    print(f"Hi, I'm {name}, I'm {age} years old, and I live in {city}.")

print("\nCalling introduce():")
introduce("Charlie", 25, "New York")

# ============================================================================
# RETURN VALUES
# ============================================================================

print("\n↩️ RETURN VALUES")
print("-" * 18)

# Function that returns a value
def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# Function with multiple return values
def get_name_parts(full_name):
    """Split a full name into first and last name"""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1]  # Returns a tuple
    else:
        return parts[0], ""

first, last = get_name_parts("Alice Johnson")
print(f"First name: {first}, Last name: {last}")

# Function that returns different types based on condition
def divide_numbers(a, b):
    """Divide two numbers with error handling"""
    if b == 0:
        return None, "Cannot divide by zero"
    else:
        return a / b, "Success"

result, message = divide_numbers(10, 2)
print(f"10 / 2 = {result} ({message})")

result, message = divide_numbers(10, 0)
print(f"10 / 0 = {result} ({message})")

# ============================================================================
# DEFAULT PARAMETERS
# ============================================================================

print("\n🎯 DEFAULT PARAMETERS")
print("-" * 22)

def greet_with_title(name, title="Mr./Ms."):
    """Greet someone with an optional title"""
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))  # Uses default title
print(greet_with_title("Johnson", "Dr."))  # Uses custom title

def calculate_total(price, tax_rate=0.08, discount=0):
    """Calculate total price with optional tax and discount"""
    discounted_price = price * (1 - discount)
    total = discounted_price * (1 + tax_rate)
    return total

print(f"Basic price $100: ${calculate_total(100):.2f}")
print(f"With 10% discount: ${calculate_total(100, discount=0.10):.2f}")
print(f"Custom tax rate 5%: ${calculate_total(100, tax_rate=0.05):.2f}")

# ============================================================================
# KEYWORD ARGUMENTS
# ============================================================================

print("\n🔑 KEYWORD ARGUMENTS")
print("-" * 22)

def create_profile(name, age, city, occupation="Student", hobby="Reading"):
    """Create a user profile"""
    profile = {
        "name": name,
        "age": age,
        "city": city,
        "occupation": occupation,
        "hobby": hobby
    }
    return profile

# Using positional arguments
profile1 = create_profile("Alice", 25, "Boston")
print(f"Profile 1: {profile1}")

# Using keyword arguments (can be in any order)
profile2 = create_profile(
    hobby="Photography",
    name="Bob",
    city="Seattle",
    age=30,
    occupation="Engineer"
)
print(f"Profile 2: {profile2}")

# Mixing positional and keyword arguments
profile3 = create_profile("Charlie", 28, "Portland", hobby="Gaming")
print(f"Profile 3: {profile3}")

# ============================================================================
# VARIABLE ARGUMENTS (*args and **kwargs)
# ============================================================================

print("\n📦 VARIABLE ARGUMENTS")
print("-" * 22)

# *args - variable number of positional arguments
def sum_all(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - variable number of keyword arguments
def print_info(**info):
    """Print any number of keyword arguments"""
    print("Information received:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\nCalling print_info():")
print_info(name="Alice", age=25, city="Boston", job="Developer")

# Combining all types of arguments
def flexible_function(required_arg, default_arg="default", *args, **kwargs):
    """Function demonstrating all argument types"""
    print(f"Required: {required_arg}")
    print(f"Default: {default_arg}")
    print(f"Extra positional args: {args}")
    print(f"Keyword args: {kwargs}")

print("\nCalling flexible_function():")
flexible_function("must_have", "custom", 1, 2, 3, extra="value", another="item")

# ============================================================================
# SCOPE AND GLOBAL VARIABLES
# ============================================================================

print("\n🌍 SCOPE AND GLOBAL VARIABLES")
print("-" * 32)

# Global variable
global_counter = 0

def increment_counter():
    """Increment the global counter"""
    global global_counter
    global_counter += 1
    return global_counter

def show_local_scope():
    """Demonstrate local scope"""
    local_variable = "I'm local!"
    print(f"Inside function: {local_variable}")
    return local_variable

print(f"Initial counter: {global_counter}")
print(f"After increment: {increment_counter()}")
print(f"After another increment: {increment_counter()}")

show_local_scope()
# print(local_variable)  # This would cause an error!

# Function with local variable shadowing global
counter = 100

def shadow_example():
    """Example of variable shadowing"""
    counter = 200  # This shadows the global counter
    print(f"Local counter: {counter}")

print(f"Global counter: {counter}")
shadow_example()
print(f"Global counter after function: {counter}")  # Unchanged

# ============================================================================
# LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ============================================================================

print("\n⚡ LAMBDA FUNCTIONS")
print("-" * 20)

# Basic lambda function
square = lambda x: x**2
print(f"square(5) = {square(5)}")

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(f"multiply(3, 4) = {multiply(3, 4)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Using lambda with sorted
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(f"Students sorted by grade: {sorted_by_grade}")

# ============================================================================
# HIGHER-ORDER FUNCTIONS
# ============================================================================

print("\n🔄 HIGHER-ORDER FUNCTIONS")
print("-" * 27)

# Function that takes another function as argument
def apply_operation(numbers, operation):
    """Apply an operation to all numbers in a list"""
    return [operation(num) for num in numbers]

def double(x):
    return x * 2

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
print(f"Doubled: {apply_operation(numbers, double)}")
print(f"Cubed: {apply_operation(numbers, cube)}")

# Function that returns another function
def create_multiplier(factor):
    """Create a function that multiplies by a specific factor"""
    def multiplier(x):
        return x * factor
    return multiplier

times_three = create_multiplier(3)
times_ten = create_multiplier(10)

print(f"times_three(7) = {times_three(7)}")
print(f"times_ten(7) = {times_ten(7)}")

# ============================================================================
# DECORATORS (ADVANCED BUT USEFUL)
# ============================================================================

print("\n🎭 DECORATORS (PREVIEW)")
print("-" * 25)

# Simple decorator
def timer_decorator(func):
    """A decorator that prints when a function starts and ends"""
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}!")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """A function that simulates slow work"""
    import time
    time.sleep(0.1)  # Sleep for 0.1 seconds
    return "Work completed!"

print("Calling decorated function:")
result = slow_function()
print(f"Result: {result}")

# ============================================================================
# REAL-WORLD EXAMPLES
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLES")
print("-" * 25)

# Example 1: Data validation
def validate_email(email):
    """Simple email validation"""
    if "@" not in email:
        return False, "Email must contain @"
    
    parts = email.split("@")
    if len(parts) != 2:
        return False, "Email format invalid"
    
    local, domain = parts
    if not local or not domain:
        return False, "Email parts cannot be empty"
    
    if "." not in domain:
        return False, "Domain must contain a dot"
    
    return True, "Valid email"

test_emails = ["user@example.com", "invalid-email", "user@", "@domain.com"]
for email in test_emails:
    is_valid, message = validate_email(email)
    status = "✅" if is_valid else "❌"
    print(f"{status} {email}: {message}")

# Example 2: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def convert_temperature(value, from_unit, to_unit):
    """Universal temperature converter"""
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        return celsius_to_fahrenheit(value)
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        return fahrenheit_to_celsius(value)
    else:
        return value  # Same unit or unsupported conversion

print(f"\nTemperature conversions:")
print(f"25°C = {convert_temperature(25, 'celsius', 'fahrenheit'):.1f}°F")
print(f"77°F = {convert_temperature(77, 'fahrenheit', 'celsius'):.1f}°C")

# Example 3: Simple calculator
def calculator():
    """Simple calculator with multiple operations"""
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    
    # Simulate some calculations
    calculations = [
        (10, "+", 5),
        (10, "-", 3),
        (6, "*", 7),
        (20, "/", 4),
        (10, "/", 0)
    ]
    
    print("\nCalculator results:")
    for a, op, b in calculations:
        if op in operations:
            result = operations[op](a, b)
            print(f"{a} {op} {b} = {result}")
        else:
            print(f"Unknown operation: {op}")

calculator()

# ============================================================================
# FUNCTION DOCUMENTATION AND BEST PRACTICES
# ============================================================================

print("\n📚 FUNCTION BEST PRACTICES")
print("-" * 30)

def well_documented_function(data, threshold=0.5, reverse=False):
    """
    Filter and sort data based on a threshold.
    
    Args:
        data (list): List of numbers to process
        threshold (float, optional): Minimum value to include. Defaults to 0.5.
        reverse (bool, optional): Sort in descending order. Defaults to False.
    
    Returns:
        list: Filtered and sorted data
    
    Example:
        >>> well_documented_function([0.1, 0.8, 0.3, 0.9])
        [0.8, 0.9]
    """
    # Filter data above threshold
    filtered_data = [x for x in data if x >= threshold]
    
    # Sort the filtered data
    sorted_data = sorted(filtered_data, reverse=reverse)
    
    return sorted_data

# Test the function
test_data = [0.1, 0.8, 0.3, 0.9, 0.2, 0.7]
result = well_documented_function(test_data, threshold=0.4, reverse=True)
print(f"Filtered and sorted data: {result}")

print("\nFunction best practices:")
print("✅ Use descriptive names")
print("✅ Keep functions focused on one task")
print("✅ Use docstrings to document your functions")
print("✅ Handle edge cases and errors")
print("✅ Use type hints for better code clarity")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Create a function that calculates the factorial of a number")
print("2. Write a function that checks if a string is a palindrome")
print("3. Build a function that finds the greatest common divisor (GCD)")
print("4. Create a password generator function")
print("5. Write a function that converts between different units (length, weight, etc.)")

# Example solutions (uncomment to try):

# def factorial(n):
#     """Calculate factorial of n"""
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)

# def is_palindrome(text):
#     """Check if text is a palindrome"""
#     cleaned = text.lower().replace(" ", "")
#     return cleaned == cleaned[::-1]

# def gcd(a, b):
#     """Find greatest common divisor using Euclidean algorithm"""
#     while b:
#         a, b = b, a % b
#     return a

# print(f"factorial(5) = {factorial(5)}")
# print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")
# print(f"gcd(48, 18) = {gcd(48, 18)}")

print("\n🎉 Excellent! You've mastered Python functions!")
print("Next up: File handling and working with external data!")