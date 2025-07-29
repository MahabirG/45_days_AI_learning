"""
# Day 2: Python Data Structures — Lists, Dicts, Sets, Tuples

## Summary of Key Concepts

### 1. Lists
- Ordered, mutable sequences.
- Support indexing, slicing, append, pop, insert, remove, etc.

### 2. Tuples
- Ordered, immutable sequences (cannot change after creation).
- Useful as keys for dictionaries, for returning multiple values.

### 3. Dictionaries
- Unordered, mutable mapping of key-value pairs (Python 3.7+ keeps insertion order).
- Fast for lookups, supports methods: `.keys()`, `.values()`, `.items()`, etc.

### 4. Sets
- Unordered, mutable collections of unique elements.
- Used for removing duplicates, mathematical set operations (union, intersection, etc.).

### 5. Common Operations
- List comprehensions
- Dictionary comprehensions
- Set operations (`|`, `&`, `-`, `^`)
- Membership tests: `in`, `not in`

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. What is the difference between a list and a tuple?
2. When would you use a set instead of a list?
3. What data types can you use as dictionary keys? Why?
4. How do you remove duplicates from a list?
5. Explain dictionary comprehension with an example.

### Coding Practice

6. Create a list of numbers from 1 to 10. Square each number and store it in a new list using list comprehension.
7. Write a function that swaps the first and last elements of a list.
8. Write a function to invert a dictionary (swap keys and values).
9. Remove all vowels from a given string using a set.
10. Find the intersection and union of two lists as sets.

### Edge Cases

11. What happens if you try to modify a tuple?
12. What is the result of adding duplicate items to a set?
13. What happens if you try to access a non-existent key in a dictionary?
14. What are shallow vs deep copies in context of lists?

### Advanced Thought

15. Explain with an example how to use nested data structures (e.g., a list of dictionaries).
16. When should you use a tuple or set instead of a list in a machine learning pipeline?
17. How can comprehensions enhance performance and readability in data processing?

---

## Formulas, Tips, and Best Practices

- Use list comprehensions for concise transformation/filtering.
- Use sets for fast membership tests and deduplication.
- Use dicts for fast lookup tables, configuration options, frequency counting.
- If a collection shouldn’t change, use a tuple for safety & clarity.

---
"""

# --- CODING EXERCISES & DEMOS ---

# 6. List of squares (1-10): list comprehension
numbers = list(range(1, 11))
squares = [x ** 2 for x in numbers]
print("Squares:", squares)

# 7. Swap first and last element of a list
def swap_first_last(lst):
    """Swaps the first and last elements of a list."""
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

sample_list = [1, 2, 3, 4, 5]
print("Swapped list:", swap_first_last(sample_list.copy()))

# 8. Invert a dictionary (swap keys/values)
def invert_dict(d):
    """Inverts a dict: keys become values and values become keys."""
    return {v: k for k, v in d.items()}

sample_dict = {'a': 1, 'b': 2, 'c': 3}
print("Inverted dict:", invert_dict(sample_dict))

# 9. Remove all vowels from a string using set
def remove_vowels(s):
    vowels = set('aeiouAEIOU')
    return ''.join([ch for ch in s if ch not in vowels])

print("No vowels:", remove_vowels("Better Python Data Structures!"))

# 10. Find intersection and union of two lists using sets
list1 = [1, 2, 3, 4, 5, 2]
list2 = [4, 5, 6, 7, 4]

set1, set2 = set(list1), set(list2)

intersection = set1 & set2
union = set1 | set2

print("Intersection:", intersection)
print("Union:", union)

"""
## Edge Cases - Answers and Demos

11. What happens if you try to modify a tuple?
   - Raises a TypeError: tuples are immutable.
     Example:
     ```
     t = (1, 2, 3)
     t = 9  # TypeError
     ```

12. What is the result of adding duplicate items to a set?
   - Duplicates are ignored, each element appears only once.

13. What happens if you try to access a non-existent key in a dictionary?
   - Raises a KeyError.
     Use .get(key, default) to avoid:
     ```
     d = {'a': 1}
     d['b']      # KeyError
     d.get('b')  # None
     d.get('b', 0)  # 0
     ```

14. What are shallow vs deep copies in lists?
   - Shallow copy: `new = old.copy()` or `list(old)` — copies top-level only. Nested objects are shared.
   - Deep copy: `import copy; new = copy.deepcopy(old)` — copies all levels; fully independent.

## Advanced Thought - Examples

15. Nested data structures:
"""
# Example: list of dicts
students = [
    {'name': 'Alice', 'score': 92},
    {'name': 'Bob', 'score': 85}
]
for student in students:
    print(f"{student['name']} got {student['score']} points")

"""
16. When to use tuple/set vs list in ML pipeline?
   - Tuple: If entries are fixed and you want immutability (e.g. model hyperparameters).
   - Set: For unique labels/classes, duplicate removal, or fast membership tests.

17. How can comprehensions enhance performance/readability?
   - Comprehensions are typically faster than loops and much more concise.
     Example: `[x**2 for x in nums if x%2==0]` vs separate loop & if-statement.
"""

# --- END OF DAY 2 MATERIAL ---
