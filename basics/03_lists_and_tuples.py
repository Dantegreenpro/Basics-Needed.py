#!/usr/bin/env python3
"""
Python Basics: Lists and Tuples

This file covers Python's most important data structures:
- Lists: mutable sequences for storing multiple items
- Tuples: immutable sequences for storing related data
- Common operations and methods for both
"""

print("📋 Welcome to Python Lists and Tuples! 📋")
print("=" * 45)

# ============================================================================
# LISTS - MUTABLE SEQUENCES
# ============================================================================

print("\n📝 LISTS")
print("-" * 15)

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["Alice", 25, True, 3.14]  # Lists can contain different types
empty_list = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")
print(f"Empty list: {empty_list}")

# Accessing elements (indexing)
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")  # Negative indexing
print(f"Second number: {numbers[1]}")

# Slicing (getting sublists)
print(f"First two fruits: {fruits[0:2]}")
print(f"Last two fruits: {fruits[-2:]}")
print(f"Every other number: {numbers[::2]}")

# ============================================================================
# LIST METHODS AND OPERATIONS
# ============================================================================

print("\n🔧 LIST OPERATIONS")
print("-" * 20)

# Adding elements
shopping_list = ["milk", "bread"]
print(f"Original shopping list: {shopping_list}")

shopping_list.append("eggs")  # Add one item to the end
print(f"After append: {shopping_list}")

shopping_list.extend(["butter", "cheese"])  # Add multiple items
print(f"After extend: {shopping_list}")

shopping_list.insert(1, "yogurt")  # Insert at specific position
print(f"After insert: {shopping_list}")

# Removing elements
shopping_list.remove("bread")  # Remove by value
print(f"After remove: {shopping_list}")

removed_item = shopping_list.pop()  # Remove and return last item
print(f"Removed item: {removed_item}")
print(f"After pop: {shopping_list}")

removed_item = shopping_list.pop(0)  # Remove and return item at index 0
print(f"Removed item: {removed_item}")
print(f"After pop(0): {shopping_list}")

# List information
print(f"Length of list: {len(shopping_list)}")
print(f"Count of 'eggs': {shopping_list.count('eggs')}")

if "butter" in shopping_list:
    print("Found butter in the list!")

# ============================================================================
# LIST METHODS
# ============================================================================

print("\n🛠️ MORE LIST METHODS")
print("-" * 20)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original numbers: {numbers}")

# Sorting
sorted_numbers = sorted(numbers)  # Returns new sorted list
print(f"Sorted (new list): {sorted_numbers}")
print(f"Original unchanged: {numbers}")

numbers.sort()  # Sorts the list in place
print(f"After sort(): {numbers}")

numbers.reverse()  # Reverses the list in place
print(f"After reverse(): {numbers}")

# Finding elements
print(f"Index of 5: {numbers.index(5)}")
print(f"Min value: {min(numbers)}")
print(f"Max value: {max(numbers)}")
print(f"Sum of all: {sum(numbers)}")

# ============================================================================
# LIST COMPREHENSIONS (ADVANCED BUT USEFUL)
# ============================================================================

print("\n✨ LIST COMPREHENSIONS")
print("-" * 25)

# Traditional way to create a list of squares
squares_traditional = []
for i in range(1, 6):
    squares_traditional.append(i ** 2)
print(f"Squares (traditional): {squares_traditional}")

# List comprehension way (more Pythonic)
squares_comprehension = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares_comprehension}")

# List comprehension with condition
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Working with strings
words = ["python", "java", "javascript", "go", "rust"]
long_words = [word.upper() for word in words if len(word) > 4]
print(f"Long words (uppercase): {long_words}")

# ============================================================================
# TUPLES - IMMUTABLE SEQUENCES
# ============================================================================

print("\n📌 TUPLES")
print("-" * 15)

# Creating tuples
point = (3, 4)  # Coordinates
rgb_color = (255, 128, 0)  # RGB values
person = ("Alice", 30, "Engineer")  # Name, age, job
single_item = ("hello",)  # Single item tuple (note the comma!)
empty_tuple = ()

print(f"Point: {point}")
print(f"RGB color: {rgb_color}")
print(f"Person: {person}")
print(f"Single item: {single_item}")
print(f"Empty tuple: {empty_tuple}")

# Accessing tuple elements (same as lists)
print(f"X coordinate: {point[0]}")
print(f"Y coordinate: {point[1]}")
print(f"Person's name: {person[0]}")

# Tuple unpacking (very useful!)
x, y = point
name, age, job = person
print(f"Unpacked point: x={x}, y={y}")
print(f"Unpacked person: {name} is {age} years old and works as a {job}")

# ============================================================================
# TUPLE METHODS AND OPERATIONS
# ============================================================================

print("\n🔍 TUPLE OPERATIONS")
print("-" * 20)

numbers_tuple = (1, 2, 3, 2, 4, 2, 5)
print(f"Numbers tuple: {numbers_tuple}")

print(f"Length: {len(numbers_tuple)}")
print(f"Count of 2: {numbers_tuple.count(2)}")
print(f"Index of first 4: {numbers_tuple.index(4)}")
print(f"Min value: {min(numbers_tuple)}")
print(f"Max value: {max(numbers_tuple)}")

# Tuples are immutable - you can't change them!
# numbers_tuple[0] = 10  # This would cause an error!

# But you can create new tuples
new_tuple = numbers_tuple + (6, 7, 8)
print(f"Combined tuple: {new_tuple}")

# ============================================================================
# WHEN TO USE LISTS VS TUPLES
# ============================================================================

print("\n🤔 LISTS VS TUPLES")
print("-" * 20)

print("Use LISTS when:")
print("  - You need to modify the data (add, remove, change items)")
print("  - The data represents a collection of similar items")
print("  - The size might change during program execution")
print("  Examples: shopping list, user scores, file names")

print("\nUse TUPLES when:")
print("  - The data shouldn't change (coordinates, RGB values)")
print("  - You're returning multiple values from a function")
print("  - The data represents a record with different types")
print("  Examples: (x, y) coordinates, (name, age, email)")

# ============================================================================
# REAL-WORLD EXAMPLES
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLES")
print("-" * 25)

# Example 1: Managing a playlist
playlist = ["Song A", "Song B", "Song C"]

def add_song(playlist, song):
    if song not in playlist:
        playlist.append(song)
        print(f"Added '{song}' to playlist")
    else:
        print(f"'{song}' is already in playlist")

def remove_song(playlist, song):
    if song in playlist:
        playlist.remove(song)
        print(f"Removed '{song}' from playlist")
    else:
        print(f"'{song}' not found in playlist")

print(f"Current playlist: {playlist}")
add_song(playlist, "Song D")
add_song(playlist, "Song A")  # Already exists
remove_song(playlist, "Song B")
print(f"Final playlist: {playlist}")

# Example 2: Student grades
students_grades = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 96)
]

print(f"\nStudent grades: {students_grades}")

# Calculate average grade
total_grade = sum(grade for name, grade in students_grades)
average = total_grade / len(students_grades)
print(f"Average grade: {average:.1f}")

# Find top student
top_student = max(students_grades, key=lambda student: student[1])
print(f"Top student: {top_student[0]} with {top_student[1]} points")

# Example 3: Working with coordinates
def distance_between_points(point1, point2):
    """Calculate distance between two points"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

point_a = (0, 0)
point_b = (3, 4)
dist = distance_between_points(point_a, point_b)
print(f"\nDistance between {point_a} and {point_b}: {dist}")

# ============================================================================
# NESTED LISTS AND TUPLES
# ============================================================================

print("\n🎭 NESTED STRUCTURES")
print("-" * 25)

# Matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print(f"Element at row 1, column 2: {matrix[1][2]}")

# List of tuples (database-like structure)
employees = [
    ("John", "Developer", 75000),
    ("Jane", "Designer", 65000),
    ("Bob", "Manager", 85000)
]

print(f"\nEmployees: {employees}")

# Find employees with salary > 70000
high_earners = [emp for emp in employees if emp[2] > 70000]
print(f"High earners: {high_earners}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Create a function that finds the second largest number in a list")
print("2. Write a function that removes duplicates from a list while preserving order")
print("3. Create a function that rotates a list by n positions")
print("4. Build a simple grade book using lists and tuples")
print("5. Write a function that finds common elements between two lists")

# Example solutions (uncomment to try):

# def second_largest(numbers):
#     unique_numbers = list(set(numbers))
#     unique_numbers.sort()
#     return unique_numbers[-2] if len(unique_numbers) >= 2 else None

# def remove_duplicates(items):
#     seen = []
#     for item in items:
#         if item not in seen:
#             seen.append(item)
#     return seen

# test_list = [1, 3, 2, 3, 4, 2, 5]
# print(f"Second largest in {test_list}: {second_largest(test_list)}")
# print(f"Remove duplicates: {remove_duplicates(test_list)}")

print("\n🎉 Fantastic! You've mastered lists and tuples!")
print("Next up: Working with dictionaries!")