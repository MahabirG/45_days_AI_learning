"""
# Day 6: Data Loading, Cleaning, Handling Missing Data

## Summary of Key Concepts

### 1. Data Loading
- Pandas provides functions: `read_csv()`, `read_excel()`, `read_json()`, `read_sql()`.
- Understand and set parameters such as `delimiter`, `header`, `index_col`, `dtype`.

### 2. Data Cleaning
- Inspect data using `.info()`, `.head()`, `.describe()`.
- Detect and handle outliers, inconsistent data formats, duplicates.
- Rename columns with `.rename()`.
- Change data types with `.astype()`.

### 3. Handling Missing Data
- Missing data represented as `NaN` or None.
- Detect missing: `.isna()`, `.notna()`.
- Remove missing: `.dropna()`.
- Fill missing: `.fillna()` with a value or method (forward fill, backward fill).
- Interpolate missing data.

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. Why is data cleaning crucial before model training?
2. How does Pandas interpret missing values when loading data?
3. Difference between `.dropna()` and `.fillna()`.
4. What are common strategies to handle missing values in datasets?
5. When to use interpolation for missing values?

### Coding Practice

6. Load a CSV file into a DataFrame (simulate with example data).
7. Identify and count missing values per column.
8. Fill missing numeric values with the column mean.
9. Drop rows where critical column values are missing.
10. Rename columns to lowercase and replace spaces with underscores.

### Edge Cases

11. What happens if you call `.dropna()` without parameters?
12. Can filling missing values distort data distribution?
13. How to handle missing data in categorical columns?
14. What is forward fill and backward fill?

### Advanced Thought

15. Explain differences and use-cases for imputation strategies.
16. How does missing data affect statistical summaries?
17. How would you automate data cleaning in a pipeline?

---

## Tips & Best Practices

- Always inspect missing data patterns before filling or dropping.
- Use domain knowledge when deciding how to handle missing data.
- Document all data cleaning steps for reproducibility.
- Leverage pipeline frameworks like scikit-learn’s `Pipeline` for automation.

---

## Answers to Deep Questions

### Understanding Concepts

1. **Why is data cleaning crucial before model training?**  
   Dirty or inconsistent data can lead to incorrect model learning, bias, poor performance, and unreliable predictions. Cleaning ensures data quality, consistency, and accurate representation of real-world phenomena.

2. **How does Pandas interpret missing values when loading data?**  
   Pandas recognizes special markers like empty cells, `NaN`, `null`, or blanks as missing values. It automatically converts these to `NaN` (float type) internally, which it uses for missing data handling.

3. **Difference between `.dropna()` and `.fillna()`.**  
   - `.dropna()` removes rows or columns with missing data, which may reduce dataset size.  
   - `.fillna()` replaces missing values with a specified value/strategy, keeping data size intact but possibly introducing bias.

4. **What are common strategies to handle missing values in datasets?**  
   Common strategies include:  
   - Removing missing data (`dropna`) if sparse.  
   - Filling with statistics (mean/median/mode).  
   - Forward-fill/backward-fill for time series.  
   - Interpolation to estimate missing points.  
   - Model-based imputation or specialized algorithms.

5. **When to use interpolation for missing values?**  
   Use interpolation when data has presumed continuity or temporal structure, e.g., time series or ordered numeric data, to estimate missing values reasonably between known points.

### Edge Cases

11. **What happens if you call `.dropna()` without parameters?**  
    It drops all rows that contain **any** missing value in any column, which can be very aggressive.

12. **Can filling missing values distort data distribution?**  
    Yes, for example replacing with mean reduces variance and can bias the data towards the mean; uncareful imputation can distort underlying patterns.

13. **How to handle missing data in categorical columns?**  
    Commonly fill with mode (most frequent category) or a new category label like `'Unknown'`.

14. **What is forward fill and backward fill?**  
    - Forward fill (`ffill`) fills missing values with the last known valid value going forward.  
    - Backward fill (`bfill`) fills missing values with the next valid value backwards.

### Advanced Thought

15. **Explain differences and use-cases for imputation strategies.**  
    - Simple imputations: mean/median/mode are easy but may bias data.  
    - Forward/backfill are useful for time series.  
    - Model-based imputations (e.g., KNN, MICE) can predict missing values based on other features but are complex.

16. **How does missing data affect statistical summaries?**  
    Missing data can distort means, variances, and correlations if not properly handled, sometimes leading to biased or incorrect conclusions.

17. **How would you automate data cleaning in a pipeline?**  
    Use frameworks like scikit-learn Pipelines or custom preprocessing functions to apply systematic handling of missing data, encoding, scaling, etc., ensuring reproducibility and integration into modeling workflows.

"""
import pandas as pd
import numpy as np

# 6. Simulate loading CSV by creating DataFrame (example data)
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Age': [25, np.nan, 30, 40, 35],
    'City': ['NY', 'LA', 'NY', None, 'Chicago']
}
df = pd.DataFrame(data)
print("Initial DataFrame:\n", df)

# 7. Identify and count missing values per column
missing_counts = df.isna().sum()
print("\nMissing values per column:\n", missing_counts)

# 8. Fill missing numeric values with the column mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 9. Drop rows where 'Name' is missing (critical column)
df_cleaned = df.dropna(subset=['Name'])

# 10. Rename columns to lowercase and replace spaces with underscores
df_cleaned.columns = [col.lower().replace(' ', '_') for col in df_cleaned.columns]

print("\nCleaned DataFrame after filling and dropping missing:")
print(df_cleaned)
