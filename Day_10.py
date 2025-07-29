"""
# Day 10: Probability and Statistics Concepts

## Summary of Key Concepts

### 1. Probability Basics
- Events, outcomes, sample space.
- Probability axioms (0 ≤ P ≤ 1).
- Conditional probability, independence.

### 2. Random Variables
- Discrete vs continuous.
- PMF (probability mass function) and PDF (probability density function).

### 3. Expectation and Variance
- Expected value (mean) of random variable.
- Variance as measure of spread.

### 4. Bayes’ theorem and its importance.

### 5. Common Distributions in ML & Stats
- Bernoulli, Binomial, Gaussian, Exponential.

---

## Deep Questions (Theory, Coding & Applications)

### Understanding Concepts

1. What is the difference between independent and mutually exclusive events?
2. How is conditional probability calculated?
3. What is the law of total probability?
4. Why is variance important in probability?
5. How is Bayes’ theorem applied in ML?

### Coding Practice

6. Calculate the probability of getting heads in two coin tosses.
7. Simulate rolling two dice 1000 times and plot sum distribution.
8. Calculate expected value of a discrete random variable.
9. Compute conditional probability from a dataset.
10. Use Bayes’ theorem to update probability given new evidence.

### Edge Cases

11. What happens if probabilities sum to more than 1?
12. Can conditional probability be zero?
13. What’s the difference between PDF and PMF?
14. How are continuous random variables handled differently from discrete?

### Advanced Thought

15. Explain Monte Carlo simulation in ML.
16. How does the law of large numbers relate to model training?
17. How can understanding probability prevent overfitting?

---

## Tips & Best Practices

- Always validate probabilities sum to 1 in distributions.
- Use simulations to understand complex probability scenarios.
- Understand assumptions behind probability models.
- Incorporate prior knowledge with Bayesian approaches.

---
"""

import numpy as np
import matplotlib.pyplot as plt

# 6. Calculate the probability of getting heads in two coin tosses.
# Each toss is independent, probability(Heads) = 0.5
# Probability of two heads = 0.5 * 0.5
p_two_heads = 0.5 * 0.5
print("Probability of two heads in two tosses:", p_two_heads)

# 7. Simulate rolling two dice 1000 times and plot sum distribution.
rolls_1 = np.random.randint(1, 7, size=1000)
rolls_2 = np.random.randint(1, 7, size=1000)
sum_rolls = rolls_1 + rolls_2

plt.hist(sum_rolls, bins=np.arange(2, 14) - 0.5, edgecolor='black', rwidth=0.8)
plt.title('Sum of Two Dice Rolls (1000 trials)')
plt.xlabel('Sum')
plt.ylabel('Frequency')
plt.xticks(range(2, 13))
plt.show()

# 8. Calculate expected value of a discrete random variable.
values = np.array([1, 2, 3, 4])
probabilities = np.array([0.1, 0.2, 0.3, 0.4])  # must sum to 1
expected_value = np.sum(values * probabilities)
print("Expected value of the discrete random variable:", expected_value)

# 9. Compute conditional probability P(A|B)
# Example scenario: P(sum=7 | one die showed 3)
#
# Total pairs when one die is 3:
# - (3,1), (3,2), (3,3), (3,4), (3,5), (3,6)
# - (1,3), (2,3), (4,3), (5,3), (6,3)
# Total 11 favorable pairs
#
# Among those, pairs where sum=7:
# - (3,4), (4,3)
# So number of favorable pairs = 2
#
# P(A and B) = 2/36
# P(B) = 11/36
p_sum7_and_die3 = 2 / 36
p_die3 = 11 / 36
p_sum7_given_die3 = p_sum7_and_die3 / p_die3
print("Conditional probability P(sum=7 | one die=3):", p_sum7_given_die3)

# 10. Use Bayes’ theorem to update probability given new evidence.
# Example:
# P(A) = 0.01 (probability of having a disease)
# P(B|A) = 0.8 (probability of positive test given disease)
# P(B|~A) = 0.1 (probability of positive test without disease)
#
# Compute P(A|B), probability of disease given positive test.

P_A = 0.01
P_B_given_A = 0.8
P_B_given_notA = 0.1
P_notA = 1 - P_A

# Total probability of positive test
P_B = P_B_given_A * P_A + P_B_given_notA * P_notA

# Bayes formula
P_A_given_B = (P_B_given_A * P_A) / P_B
print("Posterior probability P(A|B) given test positive:", P_A_given_B)


"""
## Answers to Deep Questions

### Understanding Concepts

1. **Difference between independent and mutually exclusive events:**  
   - Independent events: occurrence of one does not affect probability of the other.  
   - Mutually exclusive: both cannot happen simultaneously.

2. **Conditional probability calculation:**  
   \( P(A|B) = \frac{P(A \cap B)}{P(B)} \)

3. **Law of total probability:**  
   For partitioned events \(B_i\), \( P(A) = \sum_i P(A|B_i)P(B_i) \)

4. **Importance of variance:**  
   Variance measures the spread of random variable values; important to quantify uncertainty.

5. **Bayes’ theorem in ML:**  
   Used to update model beliefs/posteriors as new data arrives; foundational in Bayesian inference.

### Edge Cases

11. **If probabilities sum to more than 1:**  
    Invalid probability distribution; total probabilities must equal 1.

12. **Conditional probability can be zero:**  
    Yes, if event A never occurs given B.

13. **Difference between PDF and PMF:**  
    PMF applies to discrete variables (probability of exact values), PDF applies to continuous variables (density).

14. **Handling continuous vs discrete variables:**  
    Continuous variables use PDFs and integrals; discrete use PMFs and summations.

### Advanced Thought

15. **Monte Carlo simulation:**  
    Use random sampling to approximate complex probability distributions or integrals.

16. **Law of large numbers and model training:**  
    As data size increases, sample averages converge to expected values, improving model reliability.

17. **Preventing overfitting via probability understanding:**  
    Modeling uncertainty and noise properly prevents fitting to random fluctuations.

"""

# --- End of Day 10 material ---
