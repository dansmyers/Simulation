"""
Fritz Stapfer Paz
More Calculations
09/30/2020


Write a Python script to open the file data.txt and read through its values. 
Calculate and print the mean, median, variance, and standard deviation. 
Save (as PDFs) a box plot and a 20-bin histogram calculated from the values.
"""

"""
Importing
"""
from math import sqrt               # Import Square Root for Standard Deviation Calculation
import matplotlib                   # Required setup for matplotlib
matplotlib.use('Agg')               # <-- Required on Mimir
from matplotlib import pyplot as plt


"""
Open the File
"""
f = open('data.txt', 'r')           # Create file from data.txt 
data = f.readlines()                # Read lines of file and put into list


"""
Declare and populate an empty list values
"""
values = []                         # Declaration of list

for line in data:                   # Populate values from data
    line = line.strip()             # Remove Whitespace
    values.append(float(line))      # Cast Line to float and append to values list


"""
Calculation helper functions
"""
def mean(x):                        # Calculate and return the mean of input list x
    return sum(x) / len(x)          # Return Mean (Sum / Length)

def median(x):                      # Calculate and return the median of input list x
    x.sort();                       # Sort x
    if(len(x) % 2 == 0):            # If x has even length, average both middle elements
        e_1 = x[int(len(x) / 2)]    # First Middle Element
        e_2 = x[int(len(x)/2 -1)]   # Second Middle Element
        e_sum = e_1 + e_2           # Add middle two elements
        return (e_sum / 2)          #Return Average of the Middle Elementss
    else:
        e = x[ int(len(x)/2)]       # Middle Element
        return (e)                  # Return Middle Element

def variance(x):                    # Calculate and return the variance of input list x
    m = mean(x)                     # Take the Mean
    sq = [(i-m)**2 for i in x]      # Uses list comprehension to get distance from mean
    
    return(sum(sq) / len(sq))       # Return Variance
    
def standard_deviation(x):          # Calculate and return the standard deviation of input list x
    return (sqrt(variance(x)))      # Return Standard Deviation (Square Root of Variance)


"""
Now you calculate answers using the values list
"""
data_mean = mean(values)
data_median = median(values)
data_variance = variance(values)
data_standard_deviation = standard_deviation(values)


"""
MatPlotLib stuff goes here
"""
plt.boxplot(values)
plt.title("Data.txt Box-Plot")
plt.xlabel("Data")
plt.ylabel("Values")
plt.savefig("more_calculations_boxplot.pdf",bbox_inches="tight")

plt.hist(values,20)
plt.title("Data.txt Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("more_calculations_histogram.pdf",bbox_inches="tight")


