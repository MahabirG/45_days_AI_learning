"""
# Day 5: Pandas — DataFrames, Series, Essential Methods

## Summary of Key Concepts

### 1. What is Pandas?
- Pandas is a powerful Python library for data manipulation and analysis.
- Provides two main data structures: 
  - **Series:** One-dimensional labeled array (like a column).
  - **DataFrame:** Two-dimensional labeled data structure (like a table/spreadsheet).

### 2. Series
- Created from lists, arrays, or dicts.
- Supports indexing and slicing.
- Can have custom index labels (default is integer index).

### 3. DataFrame
- Collection of Series sharing the same index.
- Columns can have different data types.
- Supports filtering, grouping, merging, sorting, and aggregation.

### 4. Reading/Writing Data
- Import from CSV, Excel, JSON, SQL, etc.
- Export to various file formats.

### 5. Essential Operations
- Selecting columns: `df['col']` or `df.col`
- Filtering: boolean masks
- Adding/removing columns
- GroupBy operations for aggregation/summarization
- Handling missing data: `isna()`, `fillna()`, `dropna()`

### 6. Important Methods
- `head()`, `tail()`, `info()`, `describe()`
- `value_counts()`, `unique()`, `sort_values()`
- `apply()` and `map()` for transformations

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. What is the difference between a Series and a DataFrame?
2. How does Pandas handle indexing and labels?
3. What are some advantages of DataFrames over traditional Python lists/dicts?
4. How do you handle missing data in Pandas?
5. Describe how groupby works and give an example use case.

### Coding Practice

6. Create a Series from a list with custom index labels.
7. Create a DataFrame from a dictionary of lists.
8. Select rows from a DataFrame where a column value exceeds a threshold.
9. Add a new column to a DataFrame based on another column’s values.
10. Calculate the mean of a numeric column grouped by a categorical column.

### Edge Cases

11. What happens if you access a DataFrame column that does not exist?
12. How does Pandas treat NaN values when performing calculations?
13. What happens if columns have duplicate names?
14. How to reset the index of a DataFrame after filtering?

### Advanced Thought

15. Explain the difference between `apply()`, `map()`, and `applymap()` in Pandas.
16. How does Pandas optimize performance when dealing with large datasets?
17. How would you chain multiple operations in Pandas efficiently and readably?

---

## Tips & Best Practices

- Use vectorized operations instead of applying row-wise whenever possible.
- Use `.loc[]` and `.iloc[]` properly for label vs integer based indexing.
- Always inspect data with `.info()` and `.describe()` before analysis.
- When chaining multiple operations, consider using method chaining with parenthesis.
- Use categorical data types for memory optimization.

---
"""

# --- CODING EXERCISES & DEMOS ---

import pandas as pd
import numpy as np

# 6. Create a Series from a list with custom index
data = [10, 20, 30, 40]
custom_index = ['a', 'b', 'c', 'd']
series = pd.Series(data, index=custom_index)
print("Series with custom index:")
print(series)

# 7. Create a DataFrame from dictionary of lists
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'SF', 'Chicago']
}
df = pd.DataFrame(data_dict)
print("\nDataFrame from dictionary:")
print(df)

# 8. Select rows where Age > 30
filtered_df = df[df['Age'] > 30]
print("\nRows where Age > 30:")
print(filtered_df)

# 9. Add a new column 'Senior' (True if Age >= 35 else False)
df['Senior'] = df['Age'].apply(lambda age: age >= 35)
print("\nDataFrame with new column 'Senior':")
print(df)

# 10. Calculate mean Age grouped by City category 
# (example with grouping by City to get mean Age)
mean_age_by_city = df.groupby('City')['Age'].mean()
print("\nMean Age by City:")
print(mean_age_by_city)

"""
## Edge Cases - Answers/Explanations

11. Accessing a non-existent column:
    - Raises a KeyError when accessing via df['NonExisting'].
    - Using df.get('NonExisting') returns None or default if provided.

12. NaN treatment in calculations:
    - Pandas generally ignores NaN in aggregation functions like mean(), sum().
    - NaN propagates in operations unless explicitly handled.

13. Duplicate column names:
    - Allowed but can cause ambiguous behavior in selection.
    - Can be avoided using unique column names or hierarchical columns (MultiIndex).

14. Resetting index after filtering:
    - Use df.reset_index(drop=True) to reset the index for continuous numbering.

## Advanced Thought - Answers

15. Differences between apply(), map(), applymap()
    - `apply()`: applies a function along an axis (rows or columns) in DataFrame or on a Series.
    - `map()`: used with Series; maps values according to input correspondence (e.g., dict or function).
    - `applymap()`: element-wise function application on entire DataFrame.

16. Pandas performance optimization:
    - Vectorized operations instead of loops.
    - Using categorical data types.
    - Avoiding copies when possible.
    - Leveraging NumPy under the hood.

17. Efficient chaining example:
    ```
    df_filtered = (df[df['Age'] > 30]
                   .assign(Senior=lambda x: x['Age'] >= 35)
                   .sort_values('Age')
                   .reset_index(drop=True))
    ```

"""

# --- END OF DAY 5 MATERIAL ---
