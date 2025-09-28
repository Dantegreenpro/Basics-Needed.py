#!/usr/bin/env python3
"""
Python Basics: Dictionaries and Sets

This file covers Python's key-value data structures:
- Dictionaries: key-value pairs for mapping relationships
- Sets: unique collections for mathematical operations
- Common operations and real-world applications
"""

print("🗂️ Welcome to Python Dictionaries and Sets! 🗂️")
print("=" * 50)

# ============================================================================
# DICTIONARIES - KEY-VALUE PAIRS
# ============================================================================

print("\n📖 DICTIONARIES")
print("-" * 20)

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com"
}

# Different ways to create dictionaries
empty_dict = {}  # Empty dictionary
dict_from_tuples = dict([("name", "Bob"), ("age", 25)])
dict_comprehension = {i: i**2 for i in range(1, 6)}

print(f"Person: {person}")
print(f"Empty dict: {empty_dict}")
print(f"From tuples: {dict_from_tuples}")
print(f"Comprehension: {dict_comprehension}")

# Accessing values
print(f"\nName: {person['name']}")
print(f"Age: {person['age']}")

# Safe access with get() method
print(f"Phone: {person.get('phone', 'Not provided')}")  # Default value
print(f"Email: {person.get('email')}")

# ============================================================================
# DICTIONARY OPERATIONS
# ============================================================================

print("\n🔧 DICTIONARY OPERATIONS")
print("-" * 25)

# Adding and updating values
person["phone"] = "555-1234"  # Add new key-value pair
person["age"] = 31  # Update existing value

print(f"After updates: {person}")

# Removing values
del person["phone"]  # Remove key-value pair
removed_value = person.pop("email", "Not found")  # Remove and return value

print(f"Removed email: {removed_value}")
print(f"After removals: {person}")

# Dictionary information
print(f"Number of keys: {len(person)}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Checking for keys
if "name" in person:
    print("Name is in the dictionary")

if "email" not in person:
    print("Email is not in the dictionary")

# ============================================================================
# DICTIONARY METHODS
# ============================================================================

print("\n🛠️ DICTIONARY METHODS")
print("-" * 25)

# Sample data
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(f"Original scores: {scores}")

# Update with another dictionary
new_scores = {"Diana": 96, "Alice": 88}  # Alice's score will be updated
scores.update(new_scores)
print(f"After update: {scores}")

# Get all keys, values, items
print(f"Students: {list(scores.keys())}")
print(f"Scores: {list(scores.values())}")
print(f"Student-Score pairs: {list(scores.items())}")

# Clear dictionary
backup_scores = scores.copy()  # Make a copy first
scores.clear()
print(f"After clear: {scores}")
print(f"Backup: {backup_scores}")

scores = backup_scores  # Restore for further examples

# ============================================================================
# NESTED DICTIONARIES
# ============================================================================

print("\n🎭 NESTED DICTIONARIES")
print("-" * 25)

# Complex nested structure
company = {
    "name": "Tech Corp",
    "employees": {
        "engineering": [
            {"name": "Alice", "role": "Senior Developer", "salary": 90000},
            {"name": "Bob", "role": "Junior Developer", "salary": 60000}
        ],
        "marketing": [
            {"name": "Charlie", "role": "Marketing Manager", "salary": 70000}
        ]
    },
    "founded": 2010
}

print(f"Company: {company['name']}")
print(f"Founded: {company['founded']}")

# Accessing nested data
engineering_team = company["employees"]["engineering"]
print(f"Engineering team size: {len(engineering_team)}")

for employee in engineering_team:
    print(f"  {employee['name']}: {employee['role']} (${employee['salary']:,})")

# ============================================================================
# SETS - UNIQUE COLLECTIONS
# ============================================================================

print("\n🎯 SETS")
print("-" * 10)

# Creating sets
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicates are removed
numbers = set([1, 2, 3, 2, 4, 3, 5])  # Convert list to set
empty_set = set()  # Note: {} creates an empty dict, not set!

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Empty set: {empty_set}")

# Adding to sets
fruits.add("date")
fruits.update(["elderberry", "fig"])  # Add multiple items

print(f"After additions: {fruits}")

# Removing from sets
fruits.remove("banana")  # Raises error if not found
fruits.discard("grape")  # No error if not found

print(f"After removals: {fruits}")

# ============================================================================
# SET OPERATIONS
# ============================================================================

print("\n🧮 SET OPERATIONS")
print("-" * 20)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union (all elements in either set)
union = set_a | set_b  # or set_a.union(set_b)
print(f"Union (A | B): {union}")

# Intersection (elements in both sets)
intersection = set_a & set_b  # or set_a.intersection(set_b)
print(f"Intersection (A & B): {intersection}")

# Difference (elements in A but not in B)
difference = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference (A - B): {difference}")

# Symmetric difference (elements in either set, but not both)
symmetric_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric difference (A ^ B): {symmetric_diff}")

# Subset and superset checks
small_set = {2, 3}
print(f"Is {small_set} subset of A? {small_set.issubset(set_a)}")
print(f"Is A superset of {small_set}? {set_a.issuperset(small_set)}")

# ============================================================================
# REAL-WORLD EXAMPLES
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLES")
print("-" * 25)

# Example 1: User preferences and settings
user_profile = {
    "username": "alice_123",
    "preferences": {
        "theme": "dark",
        "notifications": True,
        "language": "en"
    },
    "recent_activity": ["login", "view_profile", "update_settings"],
    "badges": {"early_adopter", "contributor", "helper"}
}

print(f"User: {user_profile['username']}")
print(f"Theme: {user_profile['preferences']['theme']}")
print(f"Badges: {user_profile['badges']}")

# Example 2: Inventory management
inventory = {
    "electronics": {
        "laptop": {"price": 999, "stock": 15},
        "phone": {"price": 599, "stock": 25},
        "tablet": {"price": 399, "stock": 8}
    },
    "books": {
        "python_guide": {"price": 29, "stock": 50},
        "web_development": {"price": 39, "stock": 30}
    }
}

def check_stock(inventory, category, item):
    """Check if item is in stock"""
    if category in inventory and item in inventory[category]:
        stock = inventory[category][item]["stock"]
        if stock > 0:
            return f"{item}: {stock} in stock"
        else:
            return f"{item}: Out of stock"
    return f"{item}: Not found"

print(f"\nInventory check:")
print(check_stock(inventory, "electronics", "laptop"))
print(check_stock(inventory, "books", "python_guide"))
print(check_stock(inventory, "electronics", "smartwatch"))

# Example 3: Finding common interests
alice_interests = {"python", "machine_learning", "photography", "travel"}
bob_interests = {"javascript", "photography", "travel", "cooking"}
charlie_interests = {"python", "data_science", "travel", "music"}

all_people = {"Alice": alice_interests, "Bob": bob_interests, "Charlie": charlie_interests}

# Find common interests between all people
common_to_all = alice_interests & bob_interests & charlie_interests
print(f"\nCommon interests to all: {common_to_all}")

# Find who shares interests with Alice
for name, interests in all_people.items():
    if name != "Alice":
        shared = alice_interests & interests
        print(f"Alice and {name} share: {shared}")

# ============================================================================
# DICTIONARY AND SET COMPREHENSIONS
# ============================================================================

print("\n✨ COMPREHENSIONS")
print("-" * 20)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# Conditional dictionary comprehension
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Set comprehension
vowels_in_words = {char.lower() for word in ["Hello", "World", "Python"] 
                   for char in word if char.lower() in "aeiou"}
print(f"Vowels found: {vowels_in_words}")

# Transform existing dictionary
names_lengths = {"Alice": 5, "Bob": 3, "Charlotte": 9}
length_categories = {name: "long" if length > 5 else "short" 
                    for name, length in names_lengths.items()}
print(f"Name length categories: {length_categories}")

# ============================================================================
# PERFORMANCE CONSIDERATIONS
# ============================================================================

print("\n⚡ PERFORMANCE TIPS")
print("-" * 20)

print("Dictionary lookups are O(1) - very fast!")
print("Lists searches are O(n) - slower for large datasets")

# Example: Fast membership testing
large_list = list(range(10000))
large_set = set(large_list)

# This would be slow: 9999 in large_list
# This is fast: 9999 in large_set

print("Use dictionaries for:")
print("  - Key-value mappings")
print("  - Fast lookups by key")
print("  - Counting occurrences")

print("Use sets for:")
print("  - Unique collections")
print("  - Fast membership testing")
print("  - Mathematical set operations")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Create a word frequency counter using a dictionary")
print("2. Build a simple phone book with add/remove/search functions")
print("3. Find duplicate elements in a list using sets")
print("4. Create a function that merges two dictionaries")
print("5. Build a simple voting system that counts votes")

# Example solutions (uncomment to try):

# def word_frequency(text):
#     words = text.lower().split()
#     freq = {}
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
#     return freq

# def find_duplicates(items):
#     seen = set()
#     duplicates = set()
#     for item in items:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#     return duplicates

# # Test examples
# text = "the quick brown fox jumps over the lazy dog the fox"
# print(f"Word frequencies: {word_frequency(text)}")

# numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]
# print(f"Duplicates in {numbers}: {find_duplicates(numbers)}")

print("\n🎉 Excellent! You've mastered dictionaries and sets!")
print("Next up: Control flow with if statements and loops!")