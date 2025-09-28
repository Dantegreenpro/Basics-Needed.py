#!/usr/bin/env python3
"""
Python Basics: Working with Strings

This file covers everything you need to know about strings in Python:
- String creation and manipulation
- String methods and operations
- Formatting and interpolation
- Common string tasks
"""

print("📝 Welcome to Python Strings! 📝")
print("=" * 40)

# ============================================================================
# STRING BASICS
# ============================================================================

print("\n🔤 STRING CREATION")
print("-" * 20)

# Different ways to create strings
single_quotes = 'Hello, World!'
double_quotes = "Python is amazing!"
triple_quotes = """This is a multiline string.
It can span multiple lines
and preserve formatting."""

# Escape characters
escaped_string = "She said, \"Python is fun!\""
newline_string = "Line 1\nLine 2\nLine 3"
tab_string = "Name\tAge\tCity"

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Triple quotes:\n{triple_quotes}")
print(f"Escaped quotes: {escaped_string}")
print(f"With newlines:\n{newline_string}")
print(f"With tabs:\n{tab_string}")

# ============================================================================
# STRING OPERATIONS
# ============================================================================

print("\n🔧 STRING OPERATIONS")
print("-" * 20)

first_name = "Alice"
last_name = "Johnson"

# Concatenation (joining strings)
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Repetition
separator = "-" * 20
print(f"Separator: {separator}")

# Length
print(f"Length of full name: {len(full_name)} characters")

# Accessing individual characters (indexing)
print(f"First character: {full_name[0]}")
print(f"Last character: {full_name[-1]}")  # Negative indexing starts from the end

# Slicing (getting parts of a string)
print(f"First name from full name: {full_name[0:5]}")  # Characters 0 to 4
print(f"Last name from full name: {full_name[6:]}")    # From character 6 to end
print(f"Every other character: {full_name[::2]}")      # Every 2nd character

# ============================================================================
# STRING METHODS
# ============================================================================

print("\n🛠️ STRING METHODS")
print("-" * 20)

sample_text = "  Python Programming is FUN!  "
print(f"Original: '{sample_text}'")

# Case methods
print(f"Upper case: {sample_text.upper()}")
print(f"Lower case: {sample_text.lower()}")
print(f"Title case: {sample_text.title()}")
print(f"Capitalize: {sample_text.capitalize()}")
print(f"Swap case: {sample_text.swapcase()}")

# Whitespace methods
print(f"Strip whitespace: '{sample_text.strip()}'")
print(f"Left strip: '{sample_text.lstrip()}'")
print(f"Right strip: '{sample_text.rstrip()}'")

# Search and replace
email = "user@example.com"
print(f"Original email: {email}")
print(f"Replace domain: {email.replace('example.com', 'python.org')}")

# Check methods (return True/False)
print(f"Starts with 'Python': {sample_text.strip().startswith('Python')}")
print(f"Ends with '!': {sample_text.strip().endswith('!')}")
print(f"Contains 'Program': {'Program' in sample_text}")
print(f"Is all uppercase: {sample_text.isupper()}")
print(f"Is all lowercase: {sample_text.islower()}")

# ============================================================================
# STRING FORMATTING
# ============================================================================

print("\n📐 STRING FORMATTING")
print("-" * 20)

name = "Bob"
age = 30
salary = 50000.50

# Method 1: f-strings (recommended for Python 3.6+)
message1 = f"Hi, I'm {name}, I'm {age} years old, and I earn ${salary:,.2f}"
print(f"f-string: {message1}")

# Method 2: .format() method
message2 = "Hi, I'm {}, I'm {} years old, and I earn ${:,.2f}".format(name, age, salary)
print(f"format(): {message2}")

# Method 3: Named placeholders with .format()
message3 = "Hi, I'm {name}, I'm {age} years old, and I earn ${salary:,.2f}".format(
    name=name, age=age, salary=salary
)
print(f"Named format: {message3}")

# Method 4: % formatting (older style)
message4 = "Hi, I'm %s, I'm %d years old, and I earn $%.2f" % (name, age, salary)
print(f"% formatting: {message4}")

# ============================================================================
# USEFUL STRING OPERATIONS
# ============================================================================

print("\n💡 USEFUL STRING OPERATIONS")
print("-" * 20)

# Splitting and joining
sentence = "Python is a powerful programming language"
words = sentence.split()  # Split by whitespace
print(f"Words: {words}")

# Join words back together
rejoined = " ".join(words)
print(f"Rejoined: {rejoined}")

# Split by specific character
csv_data = "apple,banana,cherry,date"
fruits = csv_data.split(",")
print(f"Fruits: {fruits}")

# Finding substrings
text = "The quick brown fox jumps over the lazy dog"
print(f"Position of 'fox': {text.find('fox')}")
print(f"Position of 'cat': {text.find('cat')}")  # Returns -1 if not found
print(f"Count of 'the': {text.lower().count('the')}")

# ============================================================================
# STRING VALIDATION
# ============================================================================

print("\n✅ STRING VALIDATION")
print("-" * 20)

# Check if string contains only certain types of characters
test_strings = ["123", "abc", "123abc", "Hello World", ""]

for test in test_strings:
    print(f"'{test}':")
    print(f"  Is digit: {test.isdigit()}")
    print(f"  Is alpha: {test.isalpha()}")
    print(f"  Is alphanumeric: {test.isalnum()}")
    print(f"  Is space: {test.isspace()}")
    print(f"  Is empty: {len(test) == 0}")
    print()

# ============================================================================
# REAL-WORLD EXAMPLES
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLES")
print("-" * 20)

# Example 1: Processing user input
def clean_user_input(user_input):
    """Clean and validate user input"""
    return user_input.strip().title()

raw_input = "  alice johnson  "
clean_input = clean_user_input(raw_input)
print(f"Raw input: '{raw_input}' -> Clean: '{clean_input}'")

# Example 2: Creating a username from email
def username_from_email(email):
    """Extract username from email address"""
    return email.split("@")[0]

email_address = "alice.johnson@company.com"
username = username_from_email(email_address)
print(f"Email: {email_address} -> Username: {username}")

# Example 3: Password strength checker
def check_password_strength(password):
    """Basic password strength checker"""
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("At least 8 characters")
    
    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("At least one uppercase letter")
    
    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("At least one lowercase letter")
    
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("At least one number")
    
    return strength, feedback

# Test passwords
test_passwords = ["weak", "Better123", "VeryStrong123!"]

for pwd in test_passwords:
    score, suggestions = check_password_strength(pwd)
    print(f"Password '{pwd}': Score {score}/4")
    if suggestions:
        print(f"  Suggestions: {', '.join(suggestions)}")
    print()

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Create a function that counts vowels in a string")
print("2. Write a function that reverses a string")
print("3. Create a function that checks if a string is a palindrome")
print("4. Build a simple word counter that counts words in a sentence")
print("5. Create a function that formats a phone number (e.g., '1234567890' -> '(123) 456-7890')")

# Example solutions (uncomment to see):

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in text if char in vowels)

# def reverse_string(text):
#     return text[::-1]

# def is_palindrome(text):
#     cleaned = text.lower().replace(" ", "")
#     return cleaned == cleaned[::-1]

# print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")
# print(f"Reverse 'Python': {reverse_string('Python')}")
# print(f"Is 'racecar' a palindrome: {is_palindrome('racecar')}")

print("\n🎉 Excellent! You've mastered Python strings!")
print("Next up: Working with lists and tuples!")