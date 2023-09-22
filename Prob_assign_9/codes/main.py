import scipy.stats as stats
import math

# Given probabilities
p = 0.9  # Probability of being right-handed
q = 1 - p  # Probability of being left-handed

# Sample size
n = 10

# Calculate mean and standard deviation
mu = n * p
sigma = math.sqrt(n * p * q)

# Calculate the probability that at most 6 are right-handed using Gaussian approximation
z = (6 - mu) / sigma  # 6 corresponds to at most 6 being right-handed
probability_at_most_6 = 1 - 0.5 * (math.erfc(z / math.sqrt(2)))

print(f"Probability that at most 6 are right-handed : {probability_at_most_6:.5f}")

