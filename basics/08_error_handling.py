#!/usr/bin/env python3
"""
Python Basics: Error Handling and Debugging

This file covers how to handle errors gracefully in Python:
- Understanding different types of errors
- Try-except-finally blocks
- Custom exceptions
- Debugging techniques
- Best practices for error handling
"""

print("🚨 Welcome to Python Error Handling! 🚨")
print("=" * 44)

# ============================================================================
# COMMON TYPES OF ERRORS
# ============================================================================

print("\n📋 COMMON TYPES OF ERRORS")
print("-" * 26)

print("Python has many built-in exception types:")
print("• SyntaxError: Invalid Python syntax")
print("• NameError: Variable not defined")
print("• TypeError: Wrong data type")
print("• ValueError: Right type, wrong value")
print("• IndexError: Index out of range")
print("• KeyError: Key not found in dictionary")
print("• FileNotFoundError: File doesn't exist")
print("• ZeroDivisionError: Division by zero")

# Examples of different errors (commented to prevent crashes)
# print(hello)  # NameError: name 'hello' is not defined
# len(42)       # TypeError: object of type 'int' has no len()
# int("hello")  # ValueError: invalid literal for int()
# [1, 2, 3][5]  # IndexError: list index out of range
# {"a": 1}["b"] # KeyError: 'b'

# ============================================================================
# BASIC TRY-EXCEPT BLOCKS
# ============================================================================

print("\n🛡️ BASIC TRY-EXCEPT BLOCKS")
print("-" * 28)

# Simple try-except
print("Example 1: Basic exception handling")
try:
    number = int("abc")  # This will cause a ValueError
    print(f"Number: {number}")
except ValueError:
    print("Error: Could not convert string to integer")
    print("The program continues running!")

# Catching multiple exception types
print("\nExample 2: Multiple exception types")
def safe_divide(a, b):
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both arguments must be numbers"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))

# Catching any exception
print("\nExample 3: Catching any exception")
def safe_operation(operation):
    try:
        result = operation()
        return f"Success: {result}"
    except Exception as e:
        return f"Error occurred: {e}"

# Test with different operations
print(safe_operation(lambda: 10 / 2))
print(safe_operation(lambda: 10 / 0))
print(safe_operation(lambda: int("hello")))

# ============================================================================
# TRY-EXCEPT-ELSE-FINALLY
# ============================================================================

print("\n🔄 TRY-EXCEPT-ELSE-FINALLY")
print("-" * 30)

def demonstrate_try_blocks(filename):
    """Demonstrate all parts of try-except-else-finally"""
    file_handle = None
    try:
        print(f"  Trying to open {filename}")
        file_handle = open(filename, "r")
        content = file_handle.read()
        print(f"  File opened successfully")
        return content
    except FileNotFoundError:
        print(f"  Error: File {filename} not found")
        return None
    except PermissionError:
        print(f"  Error: Permission denied for {filename}")
        return None
    else:
        print(f"  No exceptions occurred!")
    finally:
        print(f"  Cleanup: Closing file handle if open")
        if file_handle:
            file_handle.close()

# Create a test file first
test_file = "/tmp/test.txt"
with open(test_file, "w") as f:
    f.write("Hello, World!")

print("Test 1: File exists")
content = demonstrate_try_blocks(test_file)

print("\nTest 2: File doesn't exist")
content = demonstrate_try_blocks("/tmp/nonexistent.txt")

# ============================================================================
# RAISING EXCEPTIONS
# ============================================================================

print("\n🚀 RAISING EXCEPTIONS")
print("-" * 22)

def validate_age(age):
    """Validate age and raise appropriate exceptions"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age > 150:
        raise ValueError("Age cannot be greater than 150")
    
    return f"Valid age: {age}"

# Test the validation function
test_ages = [25, -5, 200, "thirty", 0, 100]

for age in test_ages:
    try:
        result = validate_age(age)
        print(f"✅ {result}")
    except (TypeError, ValueError) as e:
        print(f"❌ Invalid age {age}: {e}")

# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

print("\n🎭 CUSTOM EXCEPTIONS")
print("-" * 22)

# Define custom exception classes
class BankingError(Exception):
    """Base class for banking-related errors"""
    pass

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance ${balance}, attempted ${amount}")

class InvalidAccountError(BankingError):
    """Raised when account number is invalid"""
    pass

# Simple banking class using custom exceptions
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        if not account_number or len(str(account_number)) < 4:
            raise InvalidAccountError("Account number must be at least 4 digits")
        
        self.account_number = account_number
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

# Test the banking system
print("Banking system demo:")

try:
    # Create account
    account = BankAccount("12345", 100)
    print(f"Account created with balance: ${account.balance}")
    
    # Successful deposit
    print(account.deposit(50))
    
    # Successful withdrawal
    print(account.withdraw(30))
    
    # This will raise InsufficientFundsError
    print(account.withdraw(200))
    
except InvalidAccountError as e:
    print(f"Account Error: {e}")
except InsufficientFundsError as e:
    print(f"Insufficient Funds: {e}")
    print(f"Available balance: ${e.balance}")
except ValueError as e:
    print(f"Value Error: {e}")

# ============================================================================
# DEBUGGING TECHNIQUES
# ============================================================================

print("\n🔍 DEBUGGING TECHNIQUES")
print("-" * 25)

# Technique 1: Print debugging
def debug_function(numbers):
    """Function with debug prints"""
    print(f"DEBUG: Input numbers: {numbers}")
    
    total = 0
    for i, num in enumerate(numbers):
        print(f"DEBUG: Processing item {i}: {num}")
        total += num
        print(f"DEBUG: Running total: {total}")
    
    print(f"DEBUG: Final total: {total}")
    return total

result = debug_function([1, 2, 3, 4, 5])
print(f"Result: {result}")

# Technique 2: Using assert statements
def calculate_percentage(part, whole):
    """Calculate percentage with assertions"""
    assert isinstance(part, (int, float)), "Part must be a number"
    assert isinstance(whole, (int, float)), "Whole must be a number"
    assert whole != 0, "Whole cannot be zero"
    assert part >= 0, "Part cannot be negative"
    assert whole > 0, "Whole must be positive"
    
    percentage = (part / whole) * 100
    return percentage

# Test assertions
try:
    print(f"50% of 100 = {calculate_percentage(50, 100)}")
    print(f"25% of 80 = {calculate_percentage(25, 80)}")
    # This will raise AssertionError
    print(f"Invalid: {calculate_percentage(-10, 100)}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Technique 3: Using logging (more professional than print)
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def professional_debug_function(data):
    """Function using proper logging"""
    logging.info(f"Starting function with data: {data}")
    
    try:
        processed_data = [x * 2 for x in data]
        logging.debug(f"Processed data: {processed_data}")
        
        result = sum(processed_data)
        logging.info(f"Function completed successfully. Result: {result}")
        return result
        
    except Exception as e:
        logging.error(f"Error in function: {e}")
        raise

# Test with logging
try:
    result = professional_debug_function([1, 2, 3])
    print(f"Final result: {result}")
except Exception as e:
    print(f"Function failed: {e}")

# ============================================================================
# ERROR HANDLING PATTERNS
# ============================================================================

print("\n🎯 ERROR HANDLING PATTERNS")
print("-" * 28)

# Pattern 1: EAFP (Easier to Ask for Forgiveness than Permission)
def eafp_example(dictionary, key):
    """EAFP: Try the operation and handle the exception"""
    try:
        return dictionary[key]
    except KeyError:
        return f"Key '{key}' not found"

# Pattern 2: LBYL (Look Before You Leap)
def lbyl_example(dictionary, key):
    """LBYL: Check conditions before performing the operation"""
    if key in dictionary:
        return dictionary[key]
    else:
        return f"Key '{key}' not found"

# Test both patterns
test_dict = {"name": "Alice", "age": 30}

print("EAFP vs LBYL comparison:")
print(f"EAFP result: {eafp_example(test_dict, 'name')}")
print(f"LBYL result: {lbyl_example(test_dict, 'name')}")
print(f"EAFP result: {eafp_example(test_dict, 'email')}")
print(f"LBYL result: {lbyl_example(test_dict, 'email')}")

# ============================================================================
# CONTEXT MANAGERS AND WITH STATEMENTS
# ============================================================================

print("\n🔄 CONTEXT MANAGERS")
print("-" * 20)

# Context managers ensure proper cleanup
class TimedOperation:
    """Custom context manager for timing operations"""
    
    def __init__(self, operation_name):
        self.operation_name = operation_name
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        print(f"Starting {self.operation_name}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        end_time = time.time()
        duration = end_time - self.start_time
        
        if exc_type is not None:
            print(f"{self.operation_name} failed after {duration:.2f} seconds")
            print(f"Error: {exc_val}")
        else:
            print(f"{self.operation_name} completed in {duration:.2f} seconds")
        
        # Return False to propagate exceptions
        return False

# Using the custom context manager
with TimedOperation("File processing"):
    # Simulate some work
    import time
    time.sleep(0.1)
    data = [i**2 for i in range(1000)]
    print(f"Processed {len(data)} items")

# ============================================================================
# REAL-WORLD ERROR HANDLING EXAMPLES
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLES")
print("-" * 25)

# Example 1: Robust file processing
def process_data_file(filename):
    """Process a data file with comprehensive error handling"""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        numbers = []
        errors = []
        
        for line_num, line in enumerate(lines, 1):
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                errors.append(f"Line {line_num}: '{line.strip()}' is not a valid number")
        
        if errors:
            print("Warnings during processing:")
            for error in errors[:3]:  # Show first 3 errors
                print(f"  {error}")
            if len(errors) > 3:
                print(f"  ... and {len(errors) - 3} more errors")
        
        if numbers:
            return {
                "total_lines": len(lines),
                "valid_numbers": len(numbers),
                "errors": len(errors),
                "sum": sum(numbers),
                "average": sum(numbers) / len(numbers)
            }
        else:
            return {"error": "No valid numbers found"}
            
    except FileNotFoundError:
        return {"error": f"File '{filename}' not found"}
    except PermissionError:
        return {"error": f"Permission denied to read '{filename}'"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}

# Create test data file
test_data_file = "/tmp/data.txt"
with open(test_data_file, 'w') as f:
    f.write("10.5\n")
    f.write("20.3\n")
    f.write("invalid\n")
    f.write("30.7\n")
    f.write("not_a_number\n")
    f.write("40.2\n")

result = process_data_file(test_data_file)
print("File processing result:")
for key, value in result.items():
    print(f"  {key}: {value}")

# Example 2: Web-like request handler with retries
import time
import random

def unreliable_api_call():
    """Simulate an unreliable API that sometimes fails"""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network timeout")
    return {"status": "success", "data": "Important data"}

def call_api_with_retry(max_retries=3, delay=1):
    """Call API with retry logic"""
    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt + 1} of {max_retries}")
            result = unreliable_api_call()
            print(f"  Success on attempt {attempt + 1}")
            return result
        
        except ConnectionError as e:
            print(f"  Attempt {attempt + 1} failed: {e}")
            
            if attempt < max_retries - 1:  # Don't sleep on last attempt
                print(f"  Waiting {delay} seconds before retry...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                print(f"  All {max_retries} attempts failed")
                raise
    
    return None

# Test the retry mechanism
print("API call with retry demo:")
try:
    response = call_api_with_retry(max_retries=3)
    print(f"Final result: {response}")
except ConnectionError:
    print("API call failed after all retries")

# ============================================================================
# BEST PRACTICES
# ============================================================================

print("\n✅ ERROR HANDLING BEST PRACTICES")
print("-" * 36)

print("1. Be specific with exception types - catch only what you can handle")
print("2. Use try-except-else-finally appropriately")
print("3. Don't ignore exceptions silently")
print("4. Log errors for debugging")
print("5. Fail fast - validate inputs early")
print("6. Use custom exceptions for domain-specific errors")
print("7. Clean up resources in finally blocks or use context managers")
print("8. Provide meaningful error messages")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Create a calculator that handles all possible errors gracefully")
print("2. Build a file backup system with comprehensive error handling")
print("3. Write a user input validator with custom exceptions")
print("4. Create a retry decorator for functions that might fail")
print("5. Build a configuration file parser with detailed error reporting")

# Example solutions (uncomment to try):

# def safe_calculator():
#     """Calculator with comprehensive error handling"""
#     while True:
#         try:
#             expression = input("Enter calculation (or 'quit'): ")
#             if expression.lower() == 'quit':
#                 break
#             
#             result = eval(expression)  # Note: eval is dangerous in real apps!
#             print(f"Result: {result}")
#             
#         except ZeroDivisionError:
#             print("Error: Division by zero")
#         except SyntaxError:
#             print("Error: Invalid expression")
#         except Exception as e:
#             print(f"Error: {e}")

# def retry_decorator(max_retries=3, delay=1):
#     """Decorator to retry a function on failure"""
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for attempt in range(max_retries):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     if attempt == max_retries - 1:
#                         raise
#                     print(f"Attempt {attempt + 1} failed: {e}")
#                     time.sleep(delay)
#         return wrapper
#     return decorator

print("\n🎉 Excellent! You've mastered error handling in Python!")
print("Next up: Modules and organizing your code!")