import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters
n = 10  # Number of trials (sample size)
p = 0.9  # Probability of success (right-handed)
k_values = np.arange(7)  # At most 6 people

# Calculate binomial PMF
binomial_pmf = binom.pmf(k_values, n, p)

# Calculate Gaussian PDF (approximation)
mean = n * p
variance = n * p * (1 - p)
std_dev = np.sqrt(variance)
x = np.linspace(0, n, 1000)
gaussian_pdf = norm.pdf(x, mean, std_dev)

# Plot PMF and PDF
plt.figure(figsize=(10, 5))

# Plot binomial PMF
plt.subplot(1, 2, 1)
plt.bar(k_values, binomial_pmf, width=0.6, label='Binomial PMF', alpha=0.7)
plt.xlabel('Number of Right-Handed People')
plt.ylabel('Probability')
plt.title('Binomial PMF (n=10, p=0.9)')
plt.legend()

# Plot Gaussian PDF
plt.subplot(1, 2, 2)
plt.plot(x, gaussian_pdf, label='Gaussian PDF', linewidth=2)
plt.xlabel('Number of Right-Handed People')
plt.ylabel('Probability Density')
plt.title('Gaussian PDF (Approximation)')
plt.legend()

plt.tight_layout()
plt.show()

# Calculate and compare values
binomial_prob_at_most_6 = binom.cdf(6, n, p)
gaussian_prob_at_most_6 = norm.cdf(6, mean, std_dev)

print(f"Probability of at most 6 right-handed people (Binomial): {binomial_prob_at_most_6:.6f}")
print(f"Probability of at most 6 right-handed people (Gaussian): {gaussian_prob_at_most_6:.6f}")

