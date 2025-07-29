"""
# Day 4: NumPy — Arrays and Vectorization

## Summary of Key Concepts

### 1. What is NumPy?
- NumPy (Numerical Python) is a powerful library for numerical computing.
- Provides support for large, multi-dimensional arrays and matrices.
- Supports mathematical functions to operate efficiently on arrays.

### 2. NumPy Arrays
- Main object: `ndarray` (n-dimensional array).
- Homogeneous data type.
- More efficient than Python lists (in memory and speed).

### 3. Array Creation
- Create array from list: `np.array([1, 2, 3])`
- Create arrays filled with zeros: `np.zeros(shape)`, ones: `np.ones(shape)`, empty: `np.empty(shape)`
- Use `np.arange(start, stop, step)` for range arrays.
- Use `np.linspace(start, stop, num)` for linearly spaced arrays.

### 4. Array Attributes
- `.shape` gives the dimensions.
- `.dtype` shows data type.
- `.size` gives total number of elements.
- `.ndim` gives number of dimensions.

### 5. Vectorized Operations
- Element-wise operations (add, multiply, subtract, divide) apply to whole arrays without explicit loops.
- Broadcasting allows operations on arrays of different shapes where compatible.
- Avoids Python loops and improves performance drastically.

### 6. Indexing and Slicing
- Similar to Python lists but supports multi-dimensional slicing.
- Boolean indexing and fancy indexing possible.

### 7. Useful Functions
- Aggregations: `np.sum()`, `np.mean()`, `np.min()`, `np.max()`, `np.std()`
- Reshaping: `reshape()`, `flatten()`
- Transpose: `.T`

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. What are the advantages of using NumPy arrays over Python lists?
2. Explain broadcasting in NumPy with an example.
3. How does vectorization improve performance?
4. What is the difference between `np.array()` and `np.asarray()`?
5. What happens if you do arithmetic operations on arrays of different shapes?

### Coding Practice

6. Create a 2D NumPy array of shape (3, 3) filled with values from 1 to 9.
7. Compute the element-wise square of all values in the array.
8. Sum each column and each row of the array.
9. Use boolean indexing to get all elements greater than 5.
10. Reshape the array into shape (1, 9) and then flatten it back to 1D.

### Edge Cases

11. What happens if you try to add a NumPy array to a Python list?
12. How do you handle division by zero in NumPy arrays?
13. Can a NumPy array hold elements of different data types?
14. What is the effect of modifying a view vs a copy of a NumPy array?

### Advanced Thought

15. Why is it preferred to avoid Python loops when working with numerical data in NumPy?
16. Explain how memory layout (C-contiguous, Fortran-contiguous) affects NumPy array operations.
17. How does broadcasting allow for writing flexible machine learning code?

---

## Tips & Best Practices

- Use vectorized operations instead of loops for performance.
- Use built-in NumPy functions for common math operations.
- Always check array shape and use broadcasting deliberately.
- Avoid unnecessary copies; use views and understand when copies are made.
- Document complex array manipulations for readability.

---
"""

# --- CODING EXERCISES & DEMOS ---

import numpy as np

# 6. Create a 2D array (3 x 3) with values 1 to 9
arr = np.arange(1, 10).reshape(3, 3)
print("Original array:\n", arr)

# 7. Element-wise square
squared = arr ** 2
print("Squared array:\n", squared)

# 8. Sum of each column and each row
col_sum = arr.sum(axis=0)
row_sum = arr.sum(axis=1)
print("Sum of columns:", col_sum)
print("Sum of rows:", row_sum)

# 9. Boolean indexing: elements greater than 5
greater_than_5 = arr[arr > 5]
print("Elements greater than 5:", greater_than_5)

# 10. Reshape array to (1, 9)
reshaped = arr.reshape(1, 9)
print("Reshaped (1,9):", reshaped)
# Flatten back to 1D
flattened = reshaped.flatten()
print("Flattened:", flattened)

"""
## Edge Cases - answers / explanations

11. Adding NumPy array to Python list
    - Raises TypeError, or results in unexpected behavior.
    - Convert list to np.array before arithmetic.

12. Division by zero handling
    - NumPy issues RuntimeWarning.
    - Result is `inf` or `nan` for division by zero.
    - Use np.seterr() or np.errstate() to control warnings.

13. Mixed data types in NumPy arrays
    - Arrays are homogeneous.
    - If mixed types given, NumPy upcasts to a common type (usually object).
    - Object arrays lose many NumPy benefits.

14. View vs copy
    - Views share the same data buffer; modifying view modifies original.
    - Copies are independent.
    - Methods like slicing return views; `.copy()` creates a copy.

## Advanced Thought answers

15. Avoiding Python loops leverages lower-level optimized C implementations.
    - Vectorized operations are much faster.

16. Memory layout:
    - C-contiguous arrays are stored row-wise.
    - Fortran-contiguous stored column-wise.
    - Operations may be faster on contiguous arrays.
    - Some libraries require specific layouts for interoperability.

17. Broadcasting:
    - Allows operations on arrays of different shapes by virtually expanding smaller array.
    - Makes code more concise and supports flexible input dimensions in ML.

"""

# --- END OF DAY 4 MATERIAL ---
