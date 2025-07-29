"""
# Day 8: Statistical Foundations — Mean, Variance, Distributions

## Summary of Key Concepts

### 1. Measures of Central Tendency
- **Mean**: average of data points.
- **Median**: middle value.
- **Mode**: most frequent value.

### 2. Dispersion Measures
- **Variance**: average squared deviation from the mean.
- **Standard Deviation**: square root of variance.
- **Range**: difference between max and min values.

### 3. Common Distributions
- Normal (Gaussian), Uniform, Binomial, Poisson.
- Probability Density Function (PDF) and Cumulative Distribution Function (CDF).

### 4. Importance in ML
- Understanding data distribution helps feature engineering and model assumptions.
- Many models assume data is normally distributed.

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. Why is the median sometimes preferred over mean?
2. What does a large variance indicate about a dataset?
3. How do distributions affect model assumptions?
4. What is the difference between PDF and CDF?
5. When would a binomial distribution be an appropriate model?

### Coding Practice

6. Calculate mean, median, mode for a list of numbers.
7. Compute variance and standard deviation.
8. Use scipy to plot a normal distribution PDF.
9. Simulate rolling a die and plot the distribution.
10. Calculate cumulative probability for a normal distribution.

### Edge Cases

11. How does missing data affect mean/variance calculations?
12. What happens when data is skewed in terms of mean and median?
13. Can variance be negative?
14. What is the effect of outliers on variance?

### Advanced Thought

15. How can understanding distributions help in anomaly detection?
16. Explain how variance relates to model overfitting.
17. How to use statistical tests to check distribution fit?

---

## Tips & Best Practices

- Use robust statistics (median, IQR) for skewed data.
- Visualize data distribution with histograms and KDE plots.
- Understand assumptions before applying parametric models.
- Use domain knowledge for selecting distribution models.

---
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 6. Calculate mean, median, mode for a list of numbers
data = [12, 15, 12, 18, 22, 15, 18, 20, 16, 18, 17, 19, 21, 22, 14]
mean_val = np.mean(data)
median_val = np.median(data)
mode_val = stats.mode(data).mode[0]
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")

# 7. Compute variance and standard deviation (sample)
variance = np.var(data, ddof=1)
std_dev = np.std(data, ddof=1)
print(f"Variance (sample): {variance}")
print(f"Standard Deviation (sample): {std_dev}")

# 8. Plot normal distribution PDF using scipy.stats
x = np.linspace(-4, 4, 200)
pdf = stats.norm.pdf(x, loc=0, scale=1)
plt.plot(x, pdf, label='Normal PDF')
plt.title('Standard Normal Distribution PDF')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()

# 9. Simulate rolling a die and plot histogram
rolls = np.random.randint(1, 7, size=1000)
plt.hist(rolls, bins=np.arange(1, 8) - 0.5, edgecolor='black', rwidth=0.8)
plt.xticks(range(1,7))
plt.title('Distribution of Die Rolls (1000 samples)')
plt.xlabel('Die Face')
plt.ylabel('Frequency')
plt.show()

# 10. Calculate cumulative probability for a normal distribution
# Probability that standard normal variable is between -1.96 and 1.96 (approx 95%)
prob = stats.norm.cdf(1.96) - stats.norm.cdf(-1.96)
print(f"Cumulative probability between -1.96 and 1.96: {prob:.4f}")

"""
## Answers to Deep Questions

### Understanding Concepts

1. **Why is the median sometimes preferred over mean?**  
   The median is more robust to outliers and skewed data; it represents the 50th percentile, providing a better measure of central tendency when data is not symmetric.

2. **What does a large variance indicate about a dataset?**  
   It indicates that the data points are spread out widely around the mean, showing high variability.

3. **How do distributions affect model assumptions?**  
   Many models (like linear regression) assume data follows specific distributions (normality, independence). If assumptions don’t hold, model may perform poorly.

4. **What is the difference between PDF and CDF?**  
   PDF shows the likelihood of a variable at each point (density), while CDF gives the cumulative probability up to a point.

5. **When would a binomial distribution be an appropriate model?**  
   For modeling number of successes in a fixed number of independent Bernoulli trials (e.g., coin flips).

### Edge Cases

11. **How does missing data affect mean/variance calculations?**  
    Missing data can bias statistics if not handled properly. By default, numpy ignores NaN in some functions with the `nanmean`, `nanvar` methods.

12. **What happens when data is skewed in terms of mean and median?**  
    The mean is pulled toward the skew tails while the median remains more central.

13. **Can variance be negative?**  
    No, variance is always non-negative as a squared quantity.

14. **What is the effect of outliers on variance?**  
    Outliers increase variance dramatically because variance squares deviations.

### Advanced Thought

15. **How can understanding distributions help in anomaly detection?**  
    By modeling normal data distribution, anomalies can be detected as points with low probability under this distribution.

16. **Explain how variance relates to model overfitting.**  
    High variance in model results indicates overfitting, where the model is too sensitive to training data noise.

17. **How to use statistical tests to check distribution fit?**  
    Tests like the Kolmogorov-Smirnov test, Shapiro-Wilk test, or Anderson-Darling test evaluate if data follows a specified distribution.

"""

# --- End of Day 8 material ---
