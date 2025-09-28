#!/usr/bin/env python3
"""
Python Intermediate: Object-Oriented Programming (OOP)

This file covers the fundamental concepts of OOP in Python:
- Classes and objects
- Instance and class attributes
- Methods and properties
- Inheritance and polymorphism
- Encapsulation and abstraction
- Magic methods and operator overloading
"""

print("🏗️ Welcome to Object-Oriented Programming! 🏗️")
print("=" * 50)

# ============================================================================
# CLASSES AND OBJECTS
# ============================================================================

print("\n🎯 CLASSES AND OBJECTS")
print("-" * 23)

class Dog:
    """A simple Dog class to demonstrate basic OOP concepts"""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age, breed):
        """Initialize a new Dog instance"""
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def celebrate_birthday(self):
        """Increase the dog's age by 1"""
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age} years old."
    
    def __str__(self):
        """String representation of the dog"""
        return f"{self.name} is a {self.age}-year-old {self.breed}"

# Creating objects (instances of the class)
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

print(f"Dog 1: {dog1}")
print(f"Dog 2: {dog2}")
print(f"Dog 1 barks: {dog1.bark()}")
print(f"Dog 2 birthday: {dog2.celebrate_birthday()}")

# Accessing class attributes
print(f"Both dogs are: {Dog.species}")
print(f"Via instance: {dog1.species}")

# ============================================================================
# PROPERTIES AND ENCAPSULATION
# ============================================================================

print("\n🔒 PROPERTIES AND ENCAPSULATION")
print("-" * 35)

class BankAccount:
    """Bank account class demonstrating encapsulation"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance  # Protected attribute (convention)
        self.__account_number = f"ACC{id(self) % 100000:05d}"  # Private attribute
    
    @property
    def balance(self):
        """Get the current balance"""
        return self._balance
    
    @property
    def account_number(self):
        """Get the account number (read-only)"""
        return self.__account_number
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            raise ValueError("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                return f"Withdrew ${amount}. New balance: ${self._balance}"
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")
    
    def __str__(self):
        return f"Account({self.account_holder}): ${self._balance}"

# Demonstrate encapsulation
account = BankAccount("Alice", 1000)
print(f"Account: {account}")
print(f"Account number: {account.account_number}")
print(f"Balance: ${account.balance}")

print(account.deposit(500))
print(account.withdraw(200))

# Try to access private attribute (won't work as expected)
print(f"Private attribute access: {account._BankAccount__account_number}")

# ============================================================================
# INHERITANCE
# ============================================================================

print("\n👥 INHERITANCE")
print("-" * 15)

class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        """Base method to be overridden by subclasses"""
        return "Some generic animal sound"
    
    def info(self):
        """Get basic information about the animal"""
        return f"{self.name} is {self.age} years old"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)  # Call parent constructor
        self.indoor = indoor
    
    def make_sound(self):
        """Override the make_sound method"""
        return f"{self.name} says Meow!"
    
    def purr(self):
        """Cat-specific method"""
        return f"{self.name} is purring contentedly"

class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self):
        """Override the make_sound method"""
        return f"{self.name} says Woof!"
    
    def fetch(self):
        """Dog-specific method"""
        return f"{self.name} fetches the ball!"

# Demonstrate inheritance
cat = Cat("Whiskers", 2)
dog = Dog("Rex", 4, "Labrador")

print(f"Cat: {cat}")
print(f"Dog: {dog}")
print(f"Cat sound: {cat.make_sound()}")
print(f"Dog sound: {dog.make_sound()}")
print(f"Cat purr: {cat.purr()}")
print(f"Dog fetch: {dog.fetch()}")

# Polymorphism - same method, different behavior
animals = [cat, dog]
print("\nPolymorphism demonstration:")
for animal in animals:
    print(f"{animal.info()} - {animal.make_sound()}")

# ============================================================================
# MULTIPLE INHERITANCE
# ============================================================================

print("\n🔗 MULTIPLE INHERITANCE")
print("-" * 25)

class Flyable:
    """Mixin class for flying behavior"""
    
    def fly(self):
        return f"{self.name} is flying high!"

class Swimmable:
    """Mixin class for swimming behavior"""
    
    def swim(self):
        return f"{self.name} is swimming gracefully!"

class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance"""
    
    def make_sound(self):
        return f"{self.name} says Quack!"

# Duck inherits from Animal, Flyable, and Swimmable
duck = Duck("Donald", 3)
print(f"Duck: {duck}")
print(f"Duck sound: {duck.make_sound()}")
print(f"Duck flying: {duck.fly()}")
print(f"Duck swimming: {duck.swim()}")

# Check Method Resolution Order (MRO)
print(f"Duck MRO: {Duck.__mro__}")

# ============================================================================
# ABSTRACT CLASSES
# ============================================================================

print("\n🎭 ABSTRACT CLASSES")
print("-" * 20)

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass
    
    def describe(self):
        """Common method for all shapes"""
        return f"This is a {self.name} with area {self.area():.2f}"

class Rectangle(Shape):
    """Rectangle implementation of Shape"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle implementation of Shape"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Demonstrate abstract classes
rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle: {rectangle.describe()}")
print(f"Circle: {circle.describe()}")

# Can't instantiate abstract class
# shape = Shape("Generic")  # This would raise TypeError

# ============================================================================
# MAGIC METHODS (DUNDER METHODS)
# ============================================================================

print("\n✨ MAGIC METHODS")
print("-" * 18)

class Vector:
    """2D Vector class demonstrating magic methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for users"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Addition operator overloading"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraction operator overloading"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Multiplication with scalar"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        """Length of vector (magnitude) - returns integer for len() compatibility"""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))
    
    def magnitude(self):
        """Get the actual magnitude of the vector as a float"""
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    def __getitem__(self, index):
        """Index access"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __bool__(self):
        """Boolean conversion"""
        return self.x != 0 or self.y != 0

# Demonstrate magic methods
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Addition: {v1 + v2}")
print(f"Subtraction: {v1 - v2}")
print(f"Multiplication: {v1 * 2}")
print(f"Equality: {v1 == v2}")
print(f"Length of v1 (integer): {len(v1)}")
print(f"Magnitude of v1: {v1.magnitude():.2f}")
print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")
print(f"Boolean v1: {bool(v1)}")
print(f"Boolean Vector(0,0): {bool(Vector(0, 0))}")

# ============================================================================
# CLASS DECORATORS AND METHODS
# ============================================================================

print("\n🎨 CLASS DECORATORS AND METHODS")
print("-" * 33)

class MathUtils:
    """Utility class demonstrating different types of methods"""
    
    pi = 3.14159  # Class attribute
    
    def __init__(self, precision=2):
        self.precision = precision
    
    def round_number(self, number):
        """Instance method"""
        return round(number, self.precision)
    
    @classmethod
    def create_high_precision(cls):
        """Class method - alternative constructor"""
        return cls(precision=5)
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't need instance or class"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Another static method"""
        return a * b
    
    @property
    def pi_rounded(self):
        """Property that uses instance precision"""
        return round(self.pi, self.precision)

# Demonstrate different method types
math_util = MathUtils()
print(f"Instance method: {math_util.round_number(3.14159)}")
print(f"Static method: {MathUtils.add(5, 3)}")
print(f"Property: {math_util.pi_rounded}")

# Using class method
high_precision = MathUtils.create_high_precision()
print(f"High precision pi: {high_precision.pi_rounded}")

# ============================================================================
# REAL-WORLD EXAMPLE: LIBRARY SYSTEM
# ============================================================================

print("\n🌍 REAL-WORLD EXAMPLE: LIBRARY SYSTEM")
print("-" * 40)

from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """Abstract base class for library items"""
    
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.is_borrowed = False
        self.borrowed_date = None
        self.due_date = None
    
    @abstractmethod
    def get_loan_period(self):
        """Get the loan period for this item type"""
        pass
    
    def borrow(self):
        """Borrow the item"""
        if self.is_borrowed:
            raise ValueError(f"{self.title} is already borrowed")
        
        self.is_borrowed = True
        self.borrowed_date = datetime.now()
        self.due_date = self.borrowed_date + timedelta(days=self.get_loan_period())
        return f"Borrowed '{self.title}' - Due: {self.due_date.strftime('%Y-%m-%d')}"
    
    def return_item(self):
        """Return the item"""
        if not self.is_borrowed:
            raise ValueError(f"{self.title} is not currently borrowed")
        
        self.is_borrowed = False
        was_overdue = datetime.now() > self.due_date
        self.borrowed_date = None
        self.due_date = None
        
        status = "on time" if not was_overdue else "OVERDUE"
        return f"Returned '{self.title}' ({status})"
    
    def __str__(self):
        status = "Available" if not self.is_borrowed else f"Borrowed (due: {self.due_date.strftime('%Y-%m-%d')})"
        return f"{self.__class__.__name__}: '{self.title}' by {self.author} - {status}"

class Book(LibraryItem):
    """Book class"""
    
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.pages = pages
    
    def get_loan_period(self):
        return 14  # 2 weeks for books

class DVD(LibraryItem):
    """DVD class"""
    
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.duration = duration
    
    def get_loan_period(self):
        return 7  # 1 week for DVDs

class Library:
    """Library management system"""
    
    def __init__(self, name):
        self.name = name
        self.items = {}
    
    def add_item(self, item):
        """Add an item to the library"""
        self.items[item.item_id] = item
        return f"Added '{item.title}' to {self.name}"
    
    def find_item(self, item_id):
        """Find an item by ID"""
        return self.items.get(item_id)
    
    def borrow_item(self, item_id):
        """Borrow an item"""
        item = self.find_item(item_id)
        if not item:
            return f"Item {item_id} not found"
        
        try:
            return item.borrow()
        except ValueError as e:
            return str(e)
    
    def return_item(self, item_id):
        """Return an item"""
        item = self.find_item(item_id)
        if not item:
            return f"Item {item_id} not found"
        
        try:
            return item.return_item()
        except ValueError as e:
            return str(e)
    
    def list_available_items(self):
        """List all available items"""
        available = [item for item in self.items.values() if not item.is_borrowed]
        return available

# Demonstrate the library system
library = Library("City Library")

# Add items
book1 = Book("Python Programming", "John Smith", "B001", 350)
book2 = Book("Data Science", "Jane Doe", "B002", 420)
dvd1 = DVD("The Matrix", "Wachowski Sisters", "D001", 136)

print(library.add_item(book1))
print(library.add_item(book2))
print(library.add_item(dvd1))

# Borrow and return items
print(f"\n{library.borrow_item('B001')}")
print(f"{library.borrow_item('D001')}")
print(f"{library.return_item('B001')}")

# List available items
print(f"\nAvailable items in {library.name}:")
for item in library.list_available_items():
    print(f"  {item}")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n🏋️ PRACTICE TIME!")
print("-" * 20)

print("Try these exercises:")
print("1. Create a Vehicle hierarchy (Car, Motorcycle, Truck) with inheritance")
print("2. Build a Employee management system with different employee types")
print("3. Design a Shape calculator with abstract classes")
print("4. Create a Bank system with different account types")
print("5. Build a Game character system with different classes and abilities")

print("\n🎉 Excellent! You've mastered Object-Oriented Programming!")
print("Next up: Advanced data structures and collections!")