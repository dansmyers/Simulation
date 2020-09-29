"""
Christian Huber
CMS 380, Fall 2020 / Sprint 1 / MoreCalculations
This script reads a text file's values and calculates and prints
the mean, median, variance, and standard deviation.
"""

from math import sqrt
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt


def mean(x):
    """
    Calculate and return the mean of input list x
    """

    return sum(x) / len(x)


def median(x):
    """
    Calculate and return the median of input list x
    """
    values.sort()
    
    # Calculate mean for middle indexes for even set
    # Averaging middle two indexes
    if(len(x)%2==0):
        return ((x[int(len(x)/2)]+x[int(len(x)/2)-1])/2)
    
    # Referencing the middle index of uneven set
    else:
        return(x[(int(len(x)/2))])
    


def variance(x):
    """
    Calculate and return the variance of input list x
    """
    m = mean(x)

    # Create an array with the value of each (element - mean)^2
    v = [((i-m)**2) for i in x]
    return mean(v)



def sDeviation(x):
    """
    Calculate and return the standard Deviation of
    input list x
    """

    return sqrt(variance(x))


values = []

# Read all data from the file into value list
with open("data.txt") as f:
    data = f.readlines()
    for line in data:

        # Remove trailing whitespace
        line = line.strip()
        
        values.append(float(line))


dataMean = mean(values)
dataMedian = median(values)
dataVariance = variance(values)
dataSDeviation = sDeviation(values)


# Use matlibplot to output boxplot and histogram to pdf
plt.figure()
plt.boxplot(values)
plt.title("Data.txt Values visualization in Boxplot")
plt.xlabel("Data")
plt.ylabel("Values")
plt.savefig("MoreCalculationsBoxplot.pdf", bbox_inches = "tight")

plt.figure()
plt.hist(values,20)
plt.title("Data.txt Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("moreCalculationsHistogram.pdf", bbox_inches = "tight")
