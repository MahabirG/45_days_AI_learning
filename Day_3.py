"""
# Day 3: Python OOP and Modules

## Summary of Key Concepts

### 1. Object-Oriented Programming (OOP) Basics
- OOP organizes code using **classes** and **objects** (instances of classes).
- **Class:** Blueprint for objects.
- **Object/Instance:** Specific realization of a class.
- Key concepts:  
  - **Encapsulation:** Bundling data (attributes) and behaviors (methods).
  - **Inheritance:** Deriving new classes from existing ones to reuse code.
  - **Polymorphism:** Ability to use a unified interface for different data types/methods.
  - **Abstraction:** Hiding internal details, exposing only necessary parts.

### 2. Defining Classes and Objects
- Use `class` keyword.
- `__init__` method is the constructor that initializes objects.
- Instance variables defined via `self`.
- Methods take `self` as the first parameter.

### 3. Inheritance and Method Overriding
- Subclass inherits parent’s attributes and methods.
- Override methods by redefining in subclass.
- Use `super()` to call parent class methods.

### 4. Modules and Packages
- **Module:** A `.py` file containing functions, classes, variables.
- **Importing modules:** `import module`, `from module import func`
- **Packages:** Directories containing `__init__.py`, bundling multiple modules.
- Use built-in `sys` and `os` modules for system operations.

### 5. Encapsulation & Access Modifiers (Python style)
- Prefix attribute/methods with a single `_` to indicate “protected” (by convention).
- Prefix with double `__` to trigger name mangling (pseudo-private).

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. What is the difference between a class and an object?
2. Explain the purpose of `self` in class methods.
3. What is inheritance and why is it useful?
4. How does method overriding work? How do you call the parent class method?
5. What is the difference between importing a module with `import` vs `from ... import`?

### Coding Practice

6. Define a simple `Car` class with attributes: `make`, `model`, and a method `display_info()`.
7. Create a subclass `ElectricCar` that inherits from `Car` and adds a new attribute `battery_size`.
8. Override the `display_info()` method in `ElectricCar` to include battery information.
9. Write a function that imports `math` module and calculates the square root of a number.
10. Demonstrate the use of `dir()` and `help()` on a custom class.

### Edge Cases

11. Can we create an object without defining `__init__`? What happens?
12. What happens if you try to access a “private” attribute (with `__`) directly?
13. What if two modules have functions with the same name—how to handle it?
14. Can you import a module inside a function? What is the use-case?

### Advanced Thought

15. Explain how Python implements polymorphism with method overriding.
16. How do modules help in large AI projects?
17. What are best practices for structuring Python packages?

---

## Tips & Best Practices

- Keep classes small, focused on a single responsibility.
- Use meaningful attribute and method names.
- Use docstrings for classes and methods.
- Always import modules at the top unless conditional import is required.
- Organize related classes in packages for better maintainability.

---
"""

# --- CODING EXERCISES ---

# 6. Define Car class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}")

car1 = Car("Toyota", "Camry")
car1.display_info()

# 7. Subclass ElectricCar inheriting Car
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

# 8. Override display_info in ElectricCar
    def display_info(self):
        super().display_info()
        print(f"Battery Size: {self.battery_size} kWh")

elec_car = ElectricCar("Tesla", "Model S", 100)
elec_car.display_info()

# 9. Function to import math and calculate square root
def calculate_sqrt(x):
    import math
    return math.sqrt(x)

print("Square root of 16:", calculate_sqrt(16))

# 10. Using dir() and help() on custom class
print("Attributes and methods of ElectricCar:", dir(ElectricCar))
# Uncomment below to see detailed help info (this will print a lot)
# help(ElectricCar)

"""
## Edge Cases - Answers & Demo

11. Can we create an object without __init__ method?
    - Yes, Python provides a default __init__ if none is defined.

12. Accessing “private” attribute with __ prefix
    - Direct access raises AttributeError due to name mangling.
    - It can be accessed via _ClassName__attr syntax but discouraged.

13. Handling functions with same name from different modules
    - Use aliases: `import module as mod`
    - Use explicit module prefix: `module.func()`
    - Use selective import with different names: `from module import func as func1`

14. Importing module inside function
    - Allowed, useful for reducing startup time or conditional imports.

## Advanced Thought

15. Polymorphism via method overriding:
    - Subclasses provide their own method implementations.
    - Code using base class references behaves differently based on object type.

16. Modules in large AI projects:
    - Facilitate reuse, modularity, isolation of components.
    - Help organize code logically: data processing, models, utils, etc.

17. Package structuring best practices:
    - Group related modules.
    - Use __init__.py to expose clean API.
    - Follow naming conventions and avoid circular imports.
"""

# Edge Case Demos

# 11. Creating object without __init__
class Empty:
    pass

obj = Empty()
print("Created object without __init__:", obj)

# 12. "Private" attribute access demo
class PrivateDemo:
    def __init__(self):
        self.__secret = "hidden"

    def reveal(self):
        print("Secret:", self.__secret)

pd = PrivateDemo()
pd.reveal()

try:
    print(pd.__secret)
except AttributeError as e:
    print("AttributeError:", e)

# Accessing with name mangling (not recommended)
print("Accessing mangled attribute:", pd._PrivateDemo__secret)

# 13. Handling functions with same name in different modules
import math
import cmath

print("Square root (math):", math.sqrt(16))
print("Square root (cmath):", cmath.sqrt(16))

from math import sqrt as math_sqrt
from cmath import sqrt as cmath_sqrt

print("math_sqrt(9):", math_sqrt(9))
print("cmath_sqrt(9):", cmath_sqrt(9))

# 14. Importing inside a function (conditional import example)
def get_random_int():
    import random
    return random.randint(1, 10)

print("Random int:", get_random_int())
