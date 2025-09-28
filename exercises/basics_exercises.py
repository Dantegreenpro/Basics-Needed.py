#!/usr/bin/env python3
"""
Python Basics Exercises

Practice problems covering fundamental Python concepts:
- Variables and data types
- Control flow
- Functions
- Basic data structures

Each exercise includes the problem, solution, and explanation.
"""

print("💪 Python Basics Exercises 💪")
print("=" * 32)

# ============================================================================
# EXERCISE 1: TEMPERATURE CONVERTER (🟢 Easy)
# ============================================================================

print("\n🌡️ Exercise 1: Temperature Converter")
print("-" * 38)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# Test the functions
test_temps = [0, 25, 100, -10, 37]
print("Temperature conversions:")
for temp in test_temps:
    f_temp = celsius_to_fahrenheit(temp)
    c_temp = fahrenheit_to_celsius(f_temp)
    print(f"{temp}°C = {f_temp:.1f}°F = {c_temp:.1f}°C")

# ============================================================================
# EXERCISE 2: GRADE CALCULATOR (🟢 Easy)
# ============================================================================

print("\n📊 Exercise 2: Grade Calculator")
print("-" * 34)

def calculate_grade(scores):
    """Calculate letter grade from list of scores"""
    if not scores:
        return "No scores provided"
    
    average = sum(scores) / len(scores)
    
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

# Test cases
student_scores = [
    [95, 87, 92, 89],
    [78, 82, 75, 88],
    [65, 70, 68, 72],
    [45, 52, 48, 55]
]

for i, scores in enumerate(student_scores, 1):
    grade = calculate_grade(scores)
    print(f"Student {i}: {scores} -> {grade}")

# ============================================================================
# EXERCISE 3: WORD FREQUENCY COUNTER (🟡 Medium)
# ============================================================================

print("\n📝 Exercise 3: Word Frequency Counter")
print("-" * 40)

def count_words(text):
    """Count frequency of each word in text"""
    # Convert to lowercase and split into words
    words = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

def print_word_frequency(word_count, top_n=5):
    """Print top N most frequent words"""
    # Sort by frequency (descending)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    print(f"Top {top_n} most frequent words:")
    for word, count in sorted_words[:top_n]:
        print(f"  '{word}': {count} times")

# Test with sample text
sample_text = """
Python is a powerful programming language. Python is easy to learn and Python is fun to use.
Many developers love Python because Python is versatile and Python has great libraries.
"""

word_freq = count_words(sample_text)
print_word_frequency(word_freq, 5)

# ============================================================================
# EXERCISE 4: NUMBER GUESSING GAME (🟡 Medium)
# ============================================================================

print("\n🎲 Exercise 4: Number Guessing Game")
print("-" * 37)

import random

def number_guessing_game(min_num=1, max_num=100, max_attempts=7):
    """Simple number guessing game"""
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"Guess the number between {min_num} and {max_num}!")
    print(f"You have {max_attempts} attempts.")
    
    # Simulate some guesses for demonstration
    demo_guesses = [50, 75, 88, 82, 85, 87, 86]  # Simulate strategic guessing
    
    for guess in demo_guesses:
        if attempts >= max_attempts:
            break
            
        attempts += 1
        print(f"Attempt {attempts}: Guessed {guess}")
        
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            return True
        elif guess < secret_number:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")
    
    print(f"😔 Game over! The number was {secret_number}")
    return False

# Play the game
number_guessing_game()

# ============================================================================
# EXERCISE 5: PALINDROME CHECKER (🟢 Easy)
# ============================================================================

print("\n🔄 Exercise 5: Palindrome Checker")
print("-" * 36)

def is_palindrome(text):
    """Check if text is a palindrome (reads same forwards and backwards)"""
    # Remove spaces and convert to lowercase
    cleaned = ''.join(text.lower().split())
    
    # Remove punctuation
    cleaned = ''.join(char for char in cleaned if char.isalnum())
    
    # Check if it reads the same forwards and backwards
    return cleaned == cleaned[::-1]

# Test cases
test_strings = [
    "racecar",
    "A man a plan a canal Panama",
    "race a car",
    "hello",
    "Madam",
    "Was it a rat I saw?"
]

print("Palindrome tests:")
for text in test_strings:
    result = is_palindrome(text)
    status = "✅" if result else "❌"
    print(f"{status} '{text}': {result}")

# ============================================================================
# EXERCISE 6: FIBONACCI SEQUENCE (🟡 Medium)
# ============================================================================

print("\n🔢 Exercise 6: Fibonacci Sequence")
print("-" * 35)

def fibonacci_iterative(n):
    """Generate first n Fibonacci numbers iteratively"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

def fibonacci_recursive(n):
    """Calculate nth Fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test both approaches
print("First 10 Fibonacci numbers (iterative):")
fib_sequence = fibonacci_iterative(10)
print(fib_sequence)

print("\nFibonacci numbers using recursion:")
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

# ============================================================================
# EXERCISE 7: PRIME NUMBER CHECKER (🟡 Medium)
# ============================================================================

print("\n🔍 Exercise 7: Prime Number Checker")
print("-" * 36)

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def find_primes(limit):
    """Find all prime numbers up to limit"""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Test prime checking
test_numbers = [2, 3, 4, 5, 17, 25, 29, 100, 101]
print("Prime number tests:")
for num in test_numbers:
    result = is_prime(num)
    status = "✅" if result else "❌"
    print(f"{status} {num}: {'Prime' if result else 'Not prime'}")

print(f"\nPrimes up to 30: {find_primes(30)}")

# ============================================================================
# EXERCISE 8: SHOPPING CART (🟡 Medium)
# ============================================================================

print("\n🛒 Exercise 8: Shopping Cart")
print("-" * 29)

class ShoppingCart:
    """Simple shopping cart implementation"""
    
    def __init__(self):
        self.items = {}  # {item_name: (price, quantity)}
        
    def add_item(self, name, price, quantity=1):
        """Add item to cart"""
        if name in self.items:
            # Update quantity if item exists
            current_price, current_qty = self.items[name]
            self.items[name] = (price, current_qty + quantity)
        else:
            self.items[name] = (price, quantity)
        
        return f"Added {quantity} x {name} at ${price:.2f} each"
    
    def remove_item(self, name, quantity=None):
        """Remove item from cart"""
        if name not in self.items:
            return f"{name} not in cart"
        
        price, current_qty = self.items[name]
        
        if quantity is None or quantity >= current_qty:
            # Remove all of this item
            del self.items[name]
            return f"Removed all {name} from cart"
        else:
            # Remove partial quantity
            self.items[name] = (price, current_qty - quantity)
            return f"Removed {quantity} x {name} from cart"
    
    def get_total(self):
        """Calculate total cart value"""
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total
    
    def display_cart(self):
        """Display cart contents"""
        if not self.items:
            return "Cart is empty"
        
        print("Shopping Cart:")
        print("-" * 40)
        for name, (price, quantity) in self.items.items():
            subtotal = price * quantity
            print(f"{name}: {quantity} x ${price:.2f} = ${subtotal:.2f}")
        print("-" * 40)
        print(f"Total: ${self.get_total():.2f}")

# Test shopping cart
cart = ShoppingCart()

print(cart.add_item("Apple", 0.50, 6))
print(cart.add_item("Bread", 2.99, 1))
print(cart.add_item("Milk", 3.49, 2))
print(cart.add_item("Apple", 0.50, 2))  # Add more apples

print("\nCurrent cart:")
cart.display_cart()

print(f"\n{cart.remove_item('Apple', 3)}")
print("\nUpdated cart:")
cart.display_cart()

# ============================================================================
# EXERCISE 9: TEXT ANALYZER (🔴 Hard)
# ============================================================================

print("\n📊 Exercise 9: Text Analyzer")
print("-" * 30)

class TextAnalyzer:
    """Comprehensive text analysis tool"""
    
    def __init__(self, text):
        self.text = text
        self.words = self._extract_words()
    
    def _extract_words(self):
        """Extract words from text, removing punctuation"""
        import string
        # Remove punctuation and convert to lowercase
        translator = str.maketrans('', '', string.punctuation)
        clean_text = self.text.translate(translator).lower()
        return clean_text.split()
    
    def word_count(self):
        """Count total words"""
        return len(self.words)
    
    def character_count(self, include_spaces=True):
        """Count characters"""
        if include_spaces:
            return len(self.text)
        else:
            return len(self.text.replace(' ', ''))
    
    def sentence_count(self):
        """Count sentences"""
        sentence_endings = '.!?'
        count = 0
        for char in self.text:
            if char in sentence_endings:
                count += 1
        return count
    
    def average_word_length(self):
        """Calculate average word length"""
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return total_length / len(self.words)
    
    def most_common_words(self, n=5):
        """Find most common words"""
        word_freq = {}
        for word in self.words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Sort by frequency
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]
    
    def reading_time(self, wpm=200):
        """Estimate reading time in minutes"""
        return self.word_count() / wpm
    
    def generate_report(self):
        """Generate comprehensive text analysis report"""
        print("Text Analysis Report")
        print("=" * 50)
        print(f"Total characters: {self.character_count()}")
        print(f"Characters (no spaces): {self.character_count(False)}")
        print(f"Total words: {self.word_count()}")
        print(f"Total sentences: {self.sentence_count()}")
        print(f"Average word length: {self.average_word_length():.2f}")
        print(f"Estimated reading time: {self.reading_time():.1f} minutes")
        
        print(f"\nMost common words:")
        for word, count in self.most_common_words():
            print(f"  '{word}': {count} times")

# Test text analyzer
sample_text = """
Python is a high-level, interpreted programming language with dynamic semantics.
Its high-level built-in data structures, combined with dynamic typing and dynamic binding,
make it very attractive for Rapid Application Development, as well as for use as a
scripting or glue language to connect existing components together.
Python's simple, easy to learn syntax emphasizes readability and therefore reduces
the cost of program maintenance. Python supports modules and packages, which encourages
program modularity and code reuse.
"""

analyzer = TextAnalyzer(sample_text)
analyzer.generate_report()

# ============================================================================
# EXERCISE 10: PASSWORD GENERATOR (🟡 Medium)
# ============================================================================

print("\n🔐 Exercise 10: Password Generator")
print("-" * 36)

import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, 
                     include_numbers=True, include_symbols=True):
    """Generate a random password with specified criteria"""
    
    if length < 4:
        raise ValueError("Password length must be at least 4")
    
    # Build character pool
    char_pool = ""
    required_chars = []
    
    if include_lowercase:
        char_pool += string.ascii_lowercase
        required_chars.append(random.choice(string.ascii_lowercase))
    
    if include_uppercase:
        char_pool += string.ascii_uppercase
        required_chars.append(random.choice(string.ascii_uppercase))
    
    if include_numbers:
        char_pool += string.digits
        required_chars.append(random.choice(string.digits))
    
    if include_symbols:
        symbols = "!@#$%^&*"
        char_pool += symbols
        required_chars.append(random.choice(symbols))
    
    if not char_pool:
        raise ValueError("At least one character type must be included")
    
    # Generate remaining characters
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [random.choice(char_pool) for _ in range(remaining_length)]
    
    # Shuffle to randomize positions
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def check_password_strength(password):
    """Check password strength"""
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include uppercase letters")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Include lowercase letters")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include numbers")
    
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        feedback.append("Include special characters")
    
    strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
    strength = strength_levels[min(score, 4)]
    
    return strength, score, feedback

# Test password generator
print("Generated passwords:")
for i in range(3):
    password = generate_password(12)
    strength, score, feedback = check_password_strength(password)
    print(f"Password {i+1}: {password}")
    print(f"  Strength: {strength} ({score}/5)")
    if feedback:
        print(f"  Suggestions: {', '.join(feedback)}")
    print()

print("\n🎉 Great job completing the basic exercises!")
print("These problems cover essential Python concepts and problem-solving skills.")
print("Keep practicing to build your programming confidence! 💪")