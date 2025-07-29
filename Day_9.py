"""
# Day 9: Linear Algebra for ML — Matrices, Vectors, Dot Products

## Summary of Key Concepts

### 1. Vectors and Matrices
- Vectors: 1D arrays with magnitude and direction.
- Matrices: 2D arrays representing linear transformations or datasets.

### 2. Operations
- Dot product: sum of element-wise products.
- Matrix multiplication.
- Transpose, inverse, determinant.
- Identity matrix.

### 3. Importance for ML
- Data represented as matrices.
- Linear transformations fundamental to models like linear regression and neural networks.

### 4. Vector spaces, basis, and linear independence (intro).
- Vectors span a space.
- Linear independence is critical for model robustness.

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. What is the geometric meaning of a dot product?
2. How does matrix multiplication differ from element-wise multiplication?
3. What is a transpose of a matrix used for?
4. When is a matrix invertible and why does it matter?
5. Explain identity matrix and its significance.

### Coding Practice

6. Create two numpy vectors and compute their dot product.
7. Perform matrix multiplication of two compatible matrices.
8. Find transpose of a matrix.
9. Calculate the determinant and inverse (for square matrix).
10. Multiply a matrix by an identity matrix and check result.

### Edge Cases

11. What happens if dimensions do not align for multiplication?
12. What if you try to invert a singular matrix?
13. How does NumPy handle shape broadcasting with matrix ops?
14. Can the dot product result be a matrix or scalar?

### Advanced Thought

15. How are vector norms used in ML algorithms?
16. Explain eigenvectors and eigenvalues in context of data.
17. How does matrix factorization benefit recommender systems and ML?

---

## Tips & Best Practices

- Always check shapes before performing operations.
- Use NumPy’s `@` operator or `np.dot()` for dot/matmul.
- Avoid manual loops for efficiency.
- Use try-except when computing inverse to catch errors.

---
"""

import numpy as np

# 6. Create two numpy vectors and compute their dot product.
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
dot_product = np.dot(v1, v2)
print("Dot product of v1 and v2:", dot_product)
# Expected output: 1*4 + 2*5 + 3*6 = 32

# 7. Perform matrix multiplication of two compatible matrices.
m1 = np.array([[1, 2],
               [3, 4]])
m2 = np.array([[5, 6],
               [7, 8]])
matmul_result = m1 @ m2  # or np.dot(m1, m2)
print("Matrix multiplication result:\n", matmul_result)
# Expected output:
# [[19 22]
#  [43 50]]

# 8. Find transpose of a matrix.
print("Transpose of m1:\n", m1.T)

# 9. Calculate the determinant and inverse (for square matrix).
det_m1 = np.linalg.det(m1)
print(f"Determinant of m1: {det_m1}")

try:
    inv_m1 = np.linalg.inv(m1)
    print("Inverse of m1:\n", inv_m1)
except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be inverted.")

# 10. Multiply a matrix by an identity matrix and check result.
identity_matrix = np.eye(2)
product_with_identity = m1 @ identity_matrix
print("m1 multiplied by identity matrix:\n", product_with_identity)

"""
## Answers to Deep Questions

### Understanding Concepts

1. The geometric meaning of a dot product of two vectors is a measure of how much one vector goes in the direction of another. It equals the product of their magnitudes and the cosine of the angle between them.

2. Matrix multiplication is a linear algebra operation involving rows and columns producing a matrix; element-wise multiplication multiplies corresponding elements only.

3. Transpose of a matrix flips rows and columns. It's used in linear algebra to interchange the orientation of matrices and is important for operations like dot product, symmetric matrices, and more.

4. A matrix is invertible if its determinant is non-zero. Matrix inverse 'undoes' the linear transformation, essential for solving linear systems—e.g., in linear regression normal equation.

5. Identity matrix is a square matrix with ones on the diagonal and zeros elsewhere. It serves as the multiplicative identity in matrix multiplication (anything times identity matrix is itself).

### Edge Cases

11. If dimensions don't align for multiplication (e.g., incompatible inner dimensions), NumPy raises a ValueError.

12. Attempting to invert a singular matrix (determinant zero) raises a LinAlgError; inversion is undefined.

13. NumPy does not broadcast shapes for matrix multiplication (the dimensions must align exactly); broadcasting applies to element-wise ops.

14. Dot product between two vectors returns a scalar; if inputs are matrices, the result can be a matrix.

### Advanced Thought

15. Vector norms measure vector length and are used for normalization and measuring distances in ML algorithms.

16. Eigenvectors and eigenvalues describe directions along which transformations scale a vector. They reveal important properties for dimensionality reduction and understanding data structure.

17. Matrix factorization decomposes data matrices (e.g., user-item matrices) to discover latent factors in recommender systems and reduce dimensions in ML.

"""

# --- End of Day 9 material ---
