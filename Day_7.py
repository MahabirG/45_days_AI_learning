"""
# Day 7: Exploratory Data Analysis — Matplotlib, Seaborn

## Summary of Key Concepts

### 1. Exploratory Data Analysis (EDA)
- Understand data distributions, relationships, and anomalies.
- Visual summaries aid intuition and feature selection.

### 2. Matplotlib Basics
- Core plotting library.
- Functions: `plot()`, `scatter()`, `hist()`, `bar()`.
- Figure and axes objects.

### 3. Seaborn Basics
- Built on Matplotlib, easier statistical visualizations.
- Functions: `sns.histplot()`, `sns.boxplot()`, `sns.heatmap()`, `sns.pairplot()`.

### 4. Plot Customization
- Titles, labels, legends, colors, styles.
- Subplots for multiple plots.

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. How does visualization help in feature engineering?
2. What is a histogram and what insights does it give?
3. How do boxplots detect outliers?
4. When to use scatterplot vs line plot?
5. What is a heatmap and how is it useful in ML?

### Coding Practice

6. Plot a histogram of ages from a sample DataFrame.
7. Create a scatter plot showing Age vs another numeric feature.
8. Use Seaborn to create a boxplot of Age grouped by City.
9. Generate a correlation heatmap for numeric columns.
10. Plot pairplots for exploratory relationships.

### Edge Cases

11. What happens if you try to plot empty data?
12. How to change the size of the plot?
13. How to save plots to a file?
14. How does seaborn differ from matplotlib in usage?

### Advanced Thought

15. How can you use plots to detect data imbalance?
16. Explain how EDA may influence model selection.
17. How do you build interactive dashboards from these plots?

---

## Tips & Best Practices

- Always label your axes and add titles.
- Check data scales before choosing plot types.
- Use color palette to improve readability.
- Use jitter in scatterplots to avoid overplotting.
- Explore summary statistics before plotting.

---
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame for plotting
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 22, 27, 33, 38],
    'Salary': [50000, 60000, 65000, 70000, 48000, 52000, 58000, 69000],
    'City': ['NY', 'NY', 'LA', 'LA', 'NY', 'SF', 'SF', 'LA']
})

# 6. Histogram of ages
plt.figure(figsize=(6,4))
plt.hist(df['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 7. Scatter plot Age vs Salary
plt.figure(figsize=(6,4))
plt.scatter(df['Age'], df['Salary'], color='green', edgecolor='black')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# 8. Boxplot Age by City using Seaborn
plt.figure(figsize=(6,4))
sns.boxplot(x='City', y='Age', data=df)
plt.title('Age distribution by City')
plt.show()

# 9. Correlation heatmap for numeric columns
corr = df[['Age', 'Salary']].corr()
plt.figure(figsize=(4,3))
sns.heatmap(corr, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation matrix')
plt.show()

# 10. Pairplot for numeric columns
sns.pairplot(df[['Age', 'Salary']])
plt.show()

"""
## Answers to Deep Questions

### Understanding Concepts

1. Visualization helps feature engineering by revealing distributions, trends, anomalies, and relationships which might inform feature selection or transformation.

2. A histogram displays the distribution of a numeric variable, showing frequency of values in bins.

3. Boxplots detect outliers as points beyond the whiskers (1.5*IQR from quartiles).

4. Scatterplots show relationships/dependencies between two numeric variables; line plots are for ordered data trends.

5. Heatmaps display matrix-like data, often correlations, helping identify strong feature relations.

### Edge Cases

11. Plotting empty data results in an empty plot or errors; always check data before plotting.

12. Size is changed using `plt.figure(figsize=(width, height))`.

13. Save plot via `plt.savefig('filename.png')`.

14. Seaborn provides higher-level APIs with statistical features over Matplotlib’s low-level plotting features.

### Advanced Thought

15. Plots can highlight class imbalance via bar plots or frequency distributions.

16. EDA insights influence choice of model type (e.g., linear vs tree-based), feature transformations, and hyperparameters.

17. Interactive dashboards built with libraries like Plotly Dash, Streamlit, or Bokeh use these plot types for rich UI.

"""

# --- End of Day 7 material ---
