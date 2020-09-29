"""
Fritz Stapfer Paz
More Calculations
09/30/2020


Write a Python script to open the file data.txt and read through its values. 
Calculate and print the mean, median, variance, and standard deviation. 
Save (as PDFs) a box plot and a 20-bin histogram calculated from the values.
"""

from math import sqrt               # Import Square Root for Standard Deviation Calculation
# Required setup for matplotlib
import matplotlib
matplotlib.use('Agg')               # <-- Required on Mimir
from matplotlib import pyplot as plt


# Add code here to open the file
f = open('data.txt', 'r')           # Create file from data.txt 
data = f.readlines()                # Read lines of file and put into array


# Declare an empty list
values = []


# Populate values from data
for line in data:
    line = line.strip()             # Remove Whitespace
    values.append(float(line))      # Cast Line to float and append to values array


# Calculation Helper Functions

"""
Calculate and return the mean of input list x
"""
def mean(x):
    
    return sum(x) / len(x)          # Return Mean (Sum / Length)

"""
Calculate and return the median of input list x
"""
def median(x):
    x.sort();                       # Sort x
    
    # If x has even length, average both middle elements
    if(len(x) % 2 == 0): 
        e_1 = x[int(len(x) / 2)]    # First Middle Element
        e_2 = x[int(len(x)/2 -1)]   # Second Middle Element
        e_sum = e_1 + e_2           # Add middle two elements

        return (e_sum / 2)          #Return Average of the Middle Elementss
    else:
        e = x[ int(len(x)/2)]       # Middle Element
        return (e)                  # Return Middle Element

"""
Calculate and return the variance of input list x
""" 
def variance(x):
    m = mean(x)                     # Take the Mean
    sq = [(i-m)**2 for i in x]      # Uses list comprehension to get distance from mean
    
    return(sum(sq) / len(sq))       # Return Variance
    
"""
Calculate and return the standard deviation of input list x
""" 
def standard_deviation(x):
    return (sqrt(variance(x)))      # Return Standard Deviation (Square Root of Variance)


# Now you calculate answers using the values list
data_mean = mean(values)
data_median = median(values)
data_variance = variance(values)
data_standard_deviation = standard_deviation(values)


# NatPlotLib stuff goes here

plt.figure()
plt.boxplot(values)
plt.title("Data.txt Box-Plot")
plt.xlabel("Data")
plt.ylabel("Values")
plt.savefig("more_calculations.pdf",bbox_inches="tight")