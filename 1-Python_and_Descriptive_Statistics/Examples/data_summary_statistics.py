"""
Example descriptive statistics and plotting using Python libraries

Hat-tip to Claude
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

filename = 'data.txt'

# Read the data
with open(filename, 'r') as file:
    data = [float(line.strip()) for line in file]

# Convert to pandas Series for easier analysis
series = pd.Series(data)

# Basic statistics
print("\nBasic Statistics:")
print(f"Mean: {series.mean():.2f}")
print(f"Median: {series.median():.2f}")

# Five-number summary
q1 = series.quantile(0.25)
q3 = series.quantile(0.75)
iqr = q3 - q1

print("\nFive-Number Summary:")
print(f"Minimum: {series.min():.2f}")
print(f"Q1: {q1:.2f}")
print(f"Median: {series.median():.2f}")
print(f"Q3: {q3:.2f}")
print(f"Maximum: {series.max():.2f}")

# Identify outliers using the 1.5 * IQR rule
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# This statement selects all entries that are less than lower_bound or
# greater than upper_bound
outliers = series[(series < lower_bound) | (series > upper_bound)]

if len(outliers) > 0:
    print("\nOutliers detected:")
    for idx, value in outliers.items():
        print(f"Index {idx}: {value:.2f}")
else:
    print("\nNo outliers detected")

# Create a new figure
plt.figure()

# Histogram
plt.hist(data, bins='auto', edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Save to a PNG image to view
plt.tight_layout()
plt.savefig('data_hist.png')

# Repeat to produce a box plot
plt.figure()
plt.boxplot(data)
plt.title('Box Plot of Data')
plt.ylabel('Value')
plt.tight_layout()
plt.savefig('data_box.png')
