"""
Calculator functions for displaying data to matplotlib
Calculating the mean, median, variance, and std deviation
Of a given data text tile
CMS380 Fall 2020
"""
# Import math and matplotlib libraries
import math
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


# Open the file
f = open('data.txt', 'r')

# Declare an empty list
values = []

for line in f:
    line = line.strip()  # Remove whitespace
    
    # Cast to a float and then append to the list
    values.append(float(line))
    


#Calculates the mean or average
def mean(x):
    """
    Calculate and return the mean of input list x
    """
    
    return sum(x) / len(x)
    

# Calculates the median of a given list  
def median(x):
    """
    Calculate and return the median of input list x
    """
    # Sort the list
    sorted(x)
    
    # Get the length
    n = len(x)
    
    # if even the median is in the middle
    if n % 2 != 0: 
        return float(x[n / 2]) 
    
    # If its odd average two numbers in the middle    
    return float((x[int((n-1)/ 2 )] + x[int(n / 2)]) / 2)
 

#Calculates the variance of a list
def variance(x):
    """
    Calculate and return the variance of input list x
    """
    #Get the length
    n = len(x)
    
    #get the average
    mean = sum(x) / len(x)
    
    #Make a deviations list to store deviations
    deviations = []
    
    #Go thorugh list calculate deviations
    for i in x:
        deviation = (i - mean) ** 2
        deviations.append(deviation)
    
    #find variance
    variance = sum(deviations) / n
    
    return variance

# Calculate the standard_deviation using the variance   
def standard_deviation(x):
    """
    Calculate and return the standard deviation of input list x
    """
    standard_deviation = math.sqrt(variance(x))
    
    return standard_deviation

#Print the values found
print('The mean is ', mean(values))
print('The median is ', median(values))
print('The variance is ', variance(values))
print('The standard deviation is ', standard_deviation(values))

# Create a new figure
plt.figure()

# Create a histogram with 15 bins
plt.hist(values, 20)

# Title and axis labels
plt.title('Values Histogram')
plt.ylabel('Data Value')

# Save the figure to a file
plt.savefig('values_histogram.pdf', bbox_inches='tight')

#Make a new figure
plt.figure() 

# Creating plot 
plt.boxplot(values)

# Title and axis labels
plt.title('Values Box Plot')
plt.xlabel('Data value')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('values_boxplot.pdf', bbox_inches='tight')

