#!/usr/bin/env python3
"""
Python Basics: File Handling

This file covers how to work with files in Python:
- Reading from files
- Writing to files
- File operations and best practices
- Working with different file formats
- Error handling with files
"""

import os
import json
import csv
from pathlib import Path

print("📁 Welcome to Python File Handling! 📁")
print("=" * 42)

# ============================================================================
# BASIC FILE OPERATIONS
# ============================================================================

print("\n📝 BASIC FILE OPERATIONS")
print("-" * 25)

# Create a sample text file
sample_content = """Welcome to Python File Handling!

This is a sample text file that demonstrates:
- Reading from files
- Writing to files
- File operations

Python makes file handling easy and intuitive.
"""

# Writing to a file
filename = "/tmp/sample.txt"
with open(filename, "w") as file:
    file.write(sample_content)

print(f"Created file: {filename}")

# Reading from a file
print("\nReading the entire file:")
with open(filename, "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("Reading line by line:")
with open(filename, "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# ============================================================================
# FILE MODES
# ============================================================================

print("\n🔧 FILE MODES")
print("-" * 15)

print("Common file modes:")
print("'r'  - Read only (default)")
print("'w'  - Write only (overwrites existing content)")
print("'a'  - Append only (adds to end of file)")
print("'r+' - Read and write")
print("'x'  - Create new file (fails if exists)")

# Demonstrating append mode
append_filename = "/tmp/append_demo.txt"

# Write initial content
with open(append_filename, "w") as file:
    file.write("Initial content\n")

# Append more content
with open(append_filename, "a") as file:
    file.write("Appended line 1\n")
    file.write("Appended line 2\n")

# Read the result
print(f"\nContent of {append_filename}:")
with open(append_filename, "r") as file:
    print(file.read())

# ============================================================================
# READING FILES IN DIFFERENT WAYS
# ============================================================================

print("\n📖 DIFFERENT WAYS TO READ FILES")
print("-" * 32)

# Create a sample file with multiple lines
multi_line_content = """Line 1: Python is awesome
Line 2: File handling is important
Line 3: Always use 'with' statements
Line 4: This prevents resource leaks
Line 5: Happy coding!"""

multi_line_file = "/tmp/multiline.txt"
with open(multi_line_file, "w") as file:
    file.write(multi_line_content)

# Method 1: read() - entire file as string
print("Method 1: read() entire file")
with open(multi_line_file, "r") as file:
    content = file.read()
    print(f"Type: {type(content)}")
    print(f"Length: {len(content)} characters")

# Method 2: readline() - one line at a time
print("\nMethod 2: readline() one line at a time")
with open(multi_line_file, "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"First line: {line1.strip()}")
    print(f"Second line: {line2.strip()}")

# Method 3: readlines() - all lines as list
print("\nMethod 3: readlines() all lines as list")
with open(multi_line_file, "r") as file:
    lines = file.readlines()
    print(f"Type: {type(lines)}")
    print(f"Number of lines: {len(lines)}")
    for i, line in enumerate(lines[:2]):  # Show first 2 lines
        print(f"Line {i+1}: {line.strip()}")

# Method 4: Iterating over file object (most Pythonic)
print("\nMethod 4: Iterating over file object")
with open(multi_line_file, "r") as file:
    for line_num, line in enumerate(file, 1):
        if line_num <= 2:  # Show first 2 lines
            print(f"Line {line_num}: {line.strip()}")

# ============================================================================
# WORKING WITH PATHS
# ============================================================================

print("\n🛤️ WORKING WITH PATHS")
print("-" * 22)

# Using pathlib (modern approach)
from pathlib import Path

# Current directory
current_dir = Path.cwd()
print(f"Current directory: {current_dir}")

# Create path objects
file_path = Path("/tmp/example.txt")
print(f"File path: {file_path}")
print(f"Parent directory: {file_path.parent}")
print(f"File name: {file_path.name}")
print(f"File stem: {file_path.stem}")
print(f"File suffix: {file_path.suffix}")

# Check if path exists
print(f"File exists: {file_path.exists()}")

# Create directories
new_dir = Path("/tmp/python_demo")
new_dir.mkdir(exist_ok=True)  # exist_ok=True prevents error if already exists
print(f"Created directory: {new_dir}")

# Using os.path (traditional approach)
import os

print(f"\nUsing os.path:")
example_path = "/tmp/python_demo/test.txt"
print(f"Directory: {os.path.dirname(example_path)}")
print(f"Filename: {os.path.basename(example_path)}")
print(f"Exists: {os.path.exists(example_path)}")
print(f"Is file: {os.path.isfile(example_path)}")
print(f"Is directory: {os.path.isdir('/tmp/python_demo')}")

# ============================================================================
# ERROR HANDLING WITH FILES
# ============================================================================

print("\n🚨 ERROR HANDLING WITH FILES")
print("-" * 30)

def safe_read_file(filename):
    """Safely read a file with error handling"""
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content, None
    except FileNotFoundError:
        return None, f"File '{filename}' not found"
    except PermissionError:
        return None, f"Permission denied to read '{filename}'"
    except Exception as e:
        return None, f"Error reading file: {e}"

# Test with existing file
content, error = safe_read_file("/tmp/sample.txt")
if error:
    print(f"Error: {error}")
else:
    print(f"Successfully read file ({len(content)} characters)")

# Test with non-existent file
content, error = safe_read_file("/tmp/nonexistent.txt")
if error:
    print(f"Error: {error}")
else:
    print("File read successfully")

# ============================================================================
# WORKING WITH CSV FILES
# ============================================================================

print("\n📊 WORKING WITH CSV FILES")
print("-" * 25)

# Create sample CSV data
csv_filename = "/tmp/students.csv"
students_data = [
    ["Name", "Age", "Grade", "Subject"],
    ["Alice", "20", "A", "Math"],
    ["Bob", "19", "B", "Science"],
    ["Charlie", "21", "A", "History"],
    ["Diana", "20", "B+", "Math"]
]

# Writing CSV file
with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print(f"Created CSV file: {csv_filename}")

# Reading CSV file
print("\nReading CSV file:")
with open(csv_filename, "r") as file:
    reader = csv.reader(file)
    for row_num, row in enumerate(reader):
        if row_num == 0:
            print(f"Headers: {row}")
        else:
            print(f"Student {row_num}: {row}")

# Using DictReader for more convenient access
print("\nUsing DictReader:")
with open(csv_filename, "r") as file:
    reader = csv.DictReader(file)
    for student in reader:
        print(f"{student['Name']} ({student['Age']}) - Grade: {student['Grade']} in {student['Subject']}")

# ============================================================================
# WORKING WITH JSON FILES
# ============================================================================

print("\n🔄 WORKING WITH JSON FILES")
print("-" * 25)

# Sample data
student_records = {
    "students": [
        {
            "id": 1,
            "name": "Alice Johnson",
            "age": 20,
            "courses": ["Math", "Physics", "Chemistry"],
            "gpa": 3.8
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "age": 19,
            "courses": ["History", "English", "Art"],
            "gpa": 3.6
        }
    ],
    "semester": "Fall 2024",
    "school": "Python University"
}

# Writing JSON file
json_filename = "/tmp/students.json"
with open(json_filename, "w") as file:
    json.dump(student_records, file, indent=2)

print(f"Created JSON file: {json_filename}")

# Reading JSON file
print("\nReading JSON file:")
with open(json_filename, "r") as file:
    data = json.load(file)
    
    print(f"School: {data['school']}")
    print(f"Semester: {data['semester']}")
    print(f"Number of students: {len(data['students'])}")
    
    for student in data['students']:
        print(f"  {student['name']} (ID: {student['id']}) - GPA: {student['gpa']}")
        print(f"    Courses: {', '.join(student['courses'])}")

# ============================================================================
# FILE OPERATIONS AND UTILITIES
# ============================================================================

print("\n🛠️ FILE OPERATIONS AND UTILITIES")
print("-" * 35)

def get_file_info(filename):
    """Get detailed information about a file"""
    try:
        path = Path(filename)
        if not path.exists():
            return f"File '{filename}' does not exist"
        
        stat = path.stat()
        info = {
            "name": path.name,
            "size": stat.st_size,
            "created": stat.st_ctime,
            "modified": stat.st_mtime,
            "is_file": path.is_file(),
            "is_directory": path.is_dir()
        }
        return info
    except Exception as e:
        return f"Error getting file info: {e}"

# Test file info
info = get_file_info("/tmp/sample.txt")
if isinstance(info, dict):
    print("File information:")
    print(f"  Name: {info['name']}")
    print(f"  Size: {info['size']} bytes")
    print(f"  Is file: {info['is_file']}")
else:
    print(info)

# Copy file content
def copy_file(source, destination):
    """Copy content from source file to destination"""
    try:
        with open(source, "r") as src_file:
            content = src_file.read()
        
        with open(destination, "w") as dest_file:
            dest_file.write(content)
        
        return f"Successfully copied '{source}' to '{destination}'"
    except Exception as e:
        return f"Error copying file: {e}"

# Test file copying
result = copy_file("/tmp/sample.txt", "/tmp/sample_copy.txt")
print(f"\n{result}")

# ============================================================================
# REAL-WORLD EXAMPLES
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLES")
print("-" * 25)

# Example 1: Log file analyzer
def analyze_log_file(filename):
    """Analyze a log file and count error occurrences"""
    # Create a sample log file
    log_content = """2024-01-01 10:00:00 INFO: Server started
2024-01-01 10:05:00 ERROR: Database connection failed
2024-01-01 10:06:00 INFO: Retrying database connection
2024-01-01 10:06:30 INFO: Database connected successfully
2024-01-01 10:15:00 WARNING: High memory usage detected
2024-01-01 10:20:00 ERROR: User authentication failed
2024-01-01 10:25:00 INFO: User logged in successfully
2024-01-01 10:30:00 ERROR: File not found
"""
    
    with open(filename, "w") as file:
        file.write(log_content)
    
    # Analyze the log file
    log_stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    with open(filename, "r") as file:
        for line in file:
            for level in log_stats.keys():
                if level in line:
                    log_stats[level] += 1
                    break
    
    return log_stats

log_file = "/tmp/application.log"
stats = analyze_log_file(log_file)
print("Log analysis:")
for level, count in stats.items():
    print(f"  {level}: {count} occurrences")

# Example 2: Configuration file manager
def create_config_file(filename, config_dict):
    """Create a simple configuration file"""
    with open(filename, "w") as file:
        file.write("# Configuration File\n")
        file.write("# Generated by Python\n\n")
        for key, value in config_dict.items():
            file.write(f"{key}={value}\n")

def read_config_file(filename):
    """Read configuration from file"""
    config = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "=" in line:
                        key, value = line.split("=", 1)
                        config[key] = value
        return config
    except Exception as e:
        return f"Error reading config: {e}"

# Test configuration management
config_data = {
    "database_host": "localhost",
    "database_port": "5432",
    "debug_mode": "True",
    "max_connections": "100"
}

config_file = "/tmp/app_config.txt"
create_config_file(config_file, config_data)
loaded_config = read_config_file(config_file)

print(f"\nConfiguration loaded:")
for key, value in loaded_config.items():
    print(f"  {key}: {value}")

# ============================================================================
# BEST PRACTICES
# ============================================================================

print("\n✅ FILE HANDLING BEST PRACTICES")
print("-" * 35)

print("1. Always use 'with' statements for file operations")
print("2. Handle exceptions appropriately")
print("3. Use pathlib for path operations (Python 3.4+)")
print("4. Specify encoding when dealing with text files")
print("5. Close files properly (automatic with 'with' statement)")
print("6. Use appropriate file modes")
print("7. Consider file size and memory usage for large files")

# Example of specifying encoding
def read_with_encoding(filename, encoding="utf-8"):
    """Read file with specific encoding"""
    try:
        with open(filename, "r", encoding=encoding) as file:
            return file.read()
    except UnicodeDecodeError:
        return f"Error: Could not decode file with {encoding} encoding"

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Create a function that counts words in a text file")
print("2. Build a simple contact manager using CSV files")
print("3. Write a log file parser that extracts specific information")
print("4. Create a backup utility that copies files to a backup directory")
print("5. Build a simple inventory system using JSON files")

# Example solutions (uncomment to try):

# def count_words_in_file(filename):
#     """Count words in a text file"""
#     try:
#         with open(filename, "r") as file:
#             content = file.read().lower()
#             words = content.split()
#             return len(words)
#     except Exception as e:
#         return f"Error: {e}"

# def backup_file(source, backup_dir):
#     """Backup a file to a specified directory"""
#     from shutil import copy2
#     try:
#         backup_dir = Path(backup_dir)
#         backup_dir.mkdir(exist_ok=True)
#         source_path = Path(source)
#         destination = backup_dir / source_path.name
#         copy2(source, destination)
#         return f"Backed up {source} to {destination}"
#     except Exception as e:
#         return f"Backup failed: {e}"

print("\n🎉 Fantastic! You've mastered file handling in Python!")
print("Next up: Error handling and debugging techniques!")