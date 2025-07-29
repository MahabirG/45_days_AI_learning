"""
# Day 1: Python Basics — Syntax, Types, Functions

## Summary of Key Concepts

### 1. Python Syntax
- Indentation defines code blocks (no curly braces like C/C++/Java).
- Comments start with #.
- Python is case-sensitive.

### 2. Data Types
- Numbers: int, float, complex
- Text: str
- Booleans: True, False
- Type checking: type()
- Type casting: int("3"), float("3.5"), str(10)

### 3. Variables
- Dynamically typed.
- Naming conventions: lowercase_with_underscores or camelCase.

### 4. Control Structures
- if, elif, else
- for loops, while loops
- break, continue, pass

### 5. Functions
- Defined with def.
- Parameters and return values.
- Default arguments, *args, **kwargs.
- Lambda functions for simple anonymous logic.

### 6. Input/Output
- input(), print()
- String formatting: f-strings (f"Hello, {name}")

### 7. Pythonic Practices
- Follow PEP 8 for code style.
- Use list comprehensions.
- Handle errors with try...except.

---

## Deep Questions (Theory, Coding & Real-world Applications)

### Understanding Concepts
1. What's the difference between `is` and `==` in Python?
2. Why is Python dynamically typed and how does it affect debugging large applications?
3. What are mutable and immutable types? Give examples.
4. How is indentation significant in Python, and what happens with inconsistent whitespace?

### Coding Practice
5. Write a function that returns the factorial of a number using recursion.
6. Implement a function that checks if a string is a palindrome.
7. Accept a line of input and count the number of words.
8. Write a Python program that calculates the sum of elements in a list using both a for-loop and a list comprehension.

### Edge Cases
9. What happens if you access an out-of-range index in a list?
10. How do you handle division by zero in a function?
11. What are the default return values of a function that doesn't use `return`?
12. Can functions be variables in Python? Demonstrate with an example.

### Advanced Thought
13. What are the performance considerations between using loops vs. built-in functions in Python?
14. Explain the scoping rules in Python (LEGB rule).
15. How would you explain lambda functions and where would you use them in machine learning pipelines?

---

## Key Formulas, Tips & Best Practices

- Use f"{value:.2f}" for formatting floating-point numbers (e.g., for accuracy/metrics).
- In a loop: use enumerate(lst) instead of range(len(lst))
- For type-safe code: use type hints:
    def add(x: int, y: int) -> int:
        return x + y
- For better readability and maintenance, always:
    - Import modules at the top.
    - Write clear docstrings.
    - Use meaningful variable names.

---
"""

# --- CODING EXERCISES ---
"""
# Day 1: Answers (Questions 1–15) — Python Basics

## Understanding Concepts

1. **What's the difference between `is` and `==` in Python?**

   - `==` checks whether the values of two operands are equal.
   - `is` checks whether two variables point to the very same object in memory (identity check).

2. **Why is Python dynamically typed and how does it affect debugging large applications?**

   - Python variables do not require explicit type declarations; types are determined at runtime.
   - Pros: Rapid prototyping, flexibility.
   - Cons: Type-related bugs may appear only at runtime (harder to debug in large projects).
   - Mitigations: Use type hints, static analysis tools (like mypy), and thorough testing.

3. **What are mutable and immutable types? Give examples.**

   - Mutable objects can be changed after creation: `list`, `dict`, `set`.
   - Immutable objects cannot be changed: `int`, `str`, `tuple`, `float`.

4. **How is indentation significant in Python, and what happens with inconsistent whitespace?**

   - Indentation defines code blocks (not {}).
   - Mixing tabs and spaces, or inconsistent indentation, causes `IndentationError`.

## Coding Practice Answers

"""

# 5. Factorial with recursion
def factorial(n):
    """Returns factorial of n using recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial (5):", factorial(5))  # Output: 120

# 6. Palindrome checker
def is_palindrome(s):
    """Checks if input string is a palindrome."""
    return s == s[::-1]

print("Is 'racecar' a palindrome?", is_palindrome("racecar"))  # Output: True

# 7. Count number of words in input (example usage)
def count_words(sentence):
    """Returns the number of words in a sentence."""
    return len(sentence.split())

example_sentence = "Hello world, I am learning Python."
print("Word count:", count_words(example_sentence))  # Output: 6

# 8. Sum elements in a list (loop and comprehension)
lst = [1, 2, 3, 4, 5]

# For loop
total = 0
for num in lst:
    total += num
print("Sum with for-loop:", total)

# List comprehension
total_v2 = sum([num for num in lst])
print("Sum with list comprehension:", total_v2)

"""
## Edge Cases

9. **What happens if you access an out-of-range index in a list?**

   - Python raises an `IndexError`.

10. **How do you handle division by zero in a function?**

   - Use a try...except block to catch `ZeroDivisionError`.

11. **What are the default return values of a function that doesn't use `return`?**

   - The function returns `None` by default.

12. **Can functions be variables in Python? Demonstrate with an example.**

   - Yes, functions are first-class citizens in Python. You can assign them to variables and pass as arguments.

## Edge Case Code Answers
"""

# 9. IndexError example
try:
    print(lst[99])
except IndexError as e:
    print("IndexError caught:", e)

# 10. Safe Division
def safe_divide(a, b):
    """Divides a by b, handles division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print("Dividing 10 by 0:", safe_divide(10, 0))  # Output: Cannot divide by zero

# 11. Function with no return
def no_return():
    pass

print("Function with no return gives:", no_return())  # Output: None

# 12. Functions as variables
def greet():
    print("Hello!")

hello = greet
hello()  # Output: Hello!

"""
## Advanced Thought

13. **Performance: loops vs. built-in functions**
   - Built-ins like `sum()`, `map()`, and comprehensions are generally faster than manual loops (internally optimized in C).
   - For data science work, prefer vectorized solutions (NumPy/Pandas) and built-ins over vanilla Python loops.

14. **Explain scoping rules in Python (LEGB rule):**
   - L (Local): inside current function
   - E (Enclosing): in enclosing functions
   - G (Global): at module/script level
   - B (Built-in): Python Keywords/functions

15. **Lambda functions and uses in ML pipelines**
   - Lambda: single-use, anonymous, inline functions.
   - In ML: Useful for quick feature transforms (e.g., DataFrame `.apply()`), data processing pipelines, and simple custom logic without defining a whole function.

## Advanced Code Demos
"""

# 13. Performance demo (timing built-in vs. loop)
import time

lst = list(range(1000000))

start = time.time()
total1 = 0
for n in lst:
    total1 += n
print("For-loop sum:", total1, "Time:", round(time.time() - start, 5), "s")

start = time.time()
total2 = sum(lst)
print("Built-in sum:", total2, "Time:", round(time.time() - start, 5), "s")
# Built-in is much faster.

# 14. LEGB rule - Scoping Demo
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print("LEGB scope example, should print 'local':", x)
    inner()
outer()

# 15. Lambda function use in ML
square = lambda x: x*x
print("3 squared using lambda:", square(3))

# ML pipeline demo
data = [10, 20, 30]
normalized = list(map(lambda x: x/100, data))
print("Normalized values:", normalized)
# In pandas: df['norm'] = df['value'].apply(lambda x: x/100)
