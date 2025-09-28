#!/usr/bin/env python3
"""
Python Basics: Control Flow

This file covers how to control the flow of your program:
- Conditional statements (if, elif, else)
- Loops (for, while)
- Loop control (break, continue, else)
- Practical examples and patterns
"""

print("🔄 Welcome to Python Control Flow! 🔄")
print("=" * 42)

# ============================================================================
# CONDITIONAL STATEMENTS - IF, ELIF, ELSE
# ============================================================================

print("\n🤔 CONDITIONAL STATEMENTS")
print("-" * 25)

# Basic if statement
age = 18
if age >= 18:
    print(f"You are {age} years old and can vote!")

# If-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot outside.")

# If-elif-else chain
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")

# ============================================================================
# COMPARISON OPERATORS
# ============================================================================

print("\n⚖️ COMPARISON OPERATORS")
print("-" * 25)

a, b = 10, 20

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # Equal
print(f"a != b: {a != b}")  # Not equal
print(f"a < b: {a < b}")    # Less than
print(f"a <= b: {a <= b}")  # Less than or equal
print(f"a > b: {a > b}")    # Greater than
print(f"a >= b: {a >= b}")  # Greater than or equal

# Chained comparisons
x = 15
print(f"\n10 < {x} < 20: {10 < x < 20}")  # Very Pythonic!

# ============================================================================
# LOGICAL OPERATORS
# ============================================================================

print("\n🔗 LOGICAL OPERATORS")
print("-" * 20)

sunny = True
warm = True
windy = False

print(f"Sunny: {sunny}, Warm: {warm}, Windy: {windy}")
print(f"Sunny AND warm: {sunny and warm}")
print(f"Sunny OR windy: {sunny or windy}")
print(f"NOT windy: {not windy}")

# Perfect beach day?
perfect_beach_day = sunny and warm and not windy
print(f"Perfect beach day: {perfect_beach_day}")

# ============================================================================
# MEMBERSHIP AND IDENTITY OPERATORS
# ============================================================================

print("\n🎯 MEMBERSHIP & IDENTITY")
print("-" * 25)

# Membership operators (in, not in)
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# Identity operators (is, is not)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"\na = {a}")
print(f"b = {b}")
print(f"c = a")
print(f"a == b: {a == b}")  # Same content
print(f"a is b: {a is b}")  # Same object? No
print(f"a is c: {a is c}")  # Same object? Yes

# Special case with None
value = None
print(f"value is None: {value is None}")  # Preferred way
print(f"value == None: {value == None}")  # Works but not preferred

# ============================================================================
# FOR LOOPS
# ============================================================================

print("\n🔁 FOR LOOPS")
print("-" * 15)

# Basic for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# For loop with list
colors = ["red", "green", "blue"]
print("\nColors:")
for color in colors:
    print(f"  I like {color}")

# For loop with enumerate (getting index and value)
print("\nColors with index:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# For loop with enumerate starting from 1
print("\nColors numbered from 1:")
for number, color in enumerate(colors, 1):
    print(f"  {number}. {color}")

# For loop with dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print("\nPerson details:")
for key, value in person.items():
    print(f"  {key}: {value}")

# For loop with string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(f"  {letter}")

# ============================================================================
# RANGE FUNCTION
# ============================================================================

print("\n📏 RANGE FUNCTION")
print("-" * 20)

# Different ways to use range
print("range(5):", list(range(5)))           # 0 to 4
print("range(2, 8):", list(range(2, 8)))     # 2 to 7
print("range(0, 10, 2):", list(range(0, 10, 2)))  # 0, 2, 4, 6, 8
print("range(10, 0, -1):", list(range(10, 0, -1)))  # 10, 9, 8, ..., 1

# Using range in for loops
print("\nEven numbers from 0 to 10:")
for num in range(0, 11, 2):
    print(f"  {num}")

print("\nCountdown from 5:")
for num in range(5, 0, -1):
    print(f"  {num}")
print("  Blast off! 🚀")

# ============================================================================
# WHILE LOOPS
# ============================================================================

print("\n🔄 WHILE LOOPS")
print("-" * 15)

# Basic while loop
print("Counting up:")
counter = 1
while counter <= 3:
    print(f"  Count: {counter}")
    counter += 1

# While loop with user input simulation
print("\nGuessing game simulation:")
secret_number = 7
guess = 5  # Simulated guesses
attempts = 0

while guess != secret_number and attempts < 3:
    attempts += 1
    print(f"  Attempt {attempts}: Guessed {guess}")
    
    if guess < secret_number:
        print("    Too low!")
        guess += 1  # Simulate next guess
    elif guess > secret_number:
        print("    Too high!")
        guess -= 1  # Simulate next guess

if guess == secret_number:
    print(f"  Correct! The number was {secret_number}")
else:
    print(f"  Game over! The number was {secret_number}")

# ============================================================================
# LOOP CONTROL: BREAK AND CONTINUE
# ============================================================================

print("\n🛑 LOOP CONTROL")
print("-" * 18)

# Break statement - exits the loop
print("Finding first even number:")
numbers = [1, 3, 5, 8, 9, 10, 12]
for num in numbers:
    print(f"  Checking {num}")
    if num % 2 == 0:
        print(f"  Found first even number: {num}")
        break
else:
    print("  No even numbers found")  # This runs if loop completes without break

# Continue statement - skips to next iteration
print("\nPrinting only odd numbers:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"  {num}")

# ============================================================================
# NESTED LOOPS
# ============================================================================

print("\n🎭 NESTED LOOPS")
print("-" * 18)

# Multiplication table
print("3x3 Multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"{product:2}", end=" ")
    print()  # New line after each row

# Pattern printing
print("\nStar pattern:")
for row in range(1, 5):
    for star in range(row):
        print("*", end="")
    print()

# Working with 2D data
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatrix:")
for row in matrix:
    for element in row:
        print(f"{element:2}", end=" ")
    print()

# ============================================================================
# REAL-WORLD EXAMPLES
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLES")
print("-" * 25)

# Example 1: Grade calculator
def calculate_final_grade(grades):
    """Calculate final grade from a list of grades"""
    if not grades:
        return "No grades available"
    
    total = sum(grades)
    average = total / len(grades)
    
    if average >= 90:
        return f"A ({average:.1f}%)"
    elif average >= 80:
        return f"B ({average:.1f}%)"
    elif average >= 70:
        return f"C ({average:.1f}%)"
    elif average >= 60:
        return f"D ({average:.1f}%)"
    else:
        return f"F ({average:.1f}%)"

student_grades = [85, 92, 78, 96, 88]
final_grade = calculate_final_grade(student_grades)
print(f"Student grades: {student_grades}")
print(f"Final grade: {final_grade}")

# Example 2: Password validator
def validate_password(password):
    """Validate password strength"""
    issues = []
    
    if len(password) < 8:
        issues.append("At least 8 characters")
    
    if not any(c.isupper() for c in password):
        issues.append("At least one uppercase letter")
    
    if not any(c.islower() for c in password):
        issues.append("At least one lowercase letter")
    
    if not any(c.isdigit() for c in password):
        issues.append("At least one number")
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        issues.append("At least one special character")
    
    return issues

test_passwords = ["weak", "Better123", "VeryStrong123!", "perfect_Pass123!"]

for pwd in test_passwords:
    problems = validate_password(pwd)
    if problems:
        print(f"'{pwd}': Issues - {', '.join(problems)}")
    else:
        print(f"'{pwd}': Strong password! ✅")

# Example 3: Simple menu system
def show_menu():
    """Display menu options"""
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def calculator():
    """Simple calculator with menu"""
    while True:
        show_menu()
        
        # Simulate user choice (in real program, use input())
        choice = "5"  # Simulate exit choice for demo
        
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in ["1", "2", "3", "4"]:
            print(f"You selected option {choice}")
            # In real program, you'd do the calculation here
            break  # Exit for demo
        else:
            print("Invalid choice. Please try again.")

print("\nCalculator demo:")
calculator()

# ============================================================================
# LIST COMPREHENSIONS WITH CONDITIONS
# ============================================================================

print("\n✨ LIST COMPREHENSIONS WITH CONDITIONS")
print("-" * 40)

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Square positive numbers only
mixed_numbers = [-3, -1, 0, 2, 4, -2, 5]
positive_squares = [n**2 for n in mixed_numbers if n > 0]
print(f"Positive squares: {positive_squares}")

# Filter and transform strings
words = ["python", "java", "javascript", "go", "rust", "c++"]
long_uppercase = [word.upper() for word in words if len(word) > 4]
print(f"Long words (uppercase): {long_uppercase}")

# Conditional expression in comprehension
ages = [15, 22, 17, 35, 12, 28]
age_categories = ["adult" if age >= 18 else "minor" for age in ages]
print(f"Age categories: {age_categories}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Write a program that finds all prime numbers up to 50")
print("2. Create a number guessing game")
print("3. Build a simple ATM system with menu options")
print("4. Write a function that finds the largest number in a list without using max()")
print("5. Create a program that prints the Fibonacci sequence")

# Example solutions (uncomment to try):

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def find_primes(limit):
#     return [n for n in range(2, limit + 1) if is_prime(n)]

# def fibonacci(n):
#     sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence

# print(f"Primes up to 20: {find_primes(20)}")
# print(f"First 10 Fibonacci numbers: {fibonacci(10)}")

print("\n🎉 Fantastic! You've mastered control flow!")
print("Next up: Functions and how to organize your code!")