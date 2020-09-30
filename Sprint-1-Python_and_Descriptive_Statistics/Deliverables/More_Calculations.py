"""
Randy Springer
CMS 380 Sprint 1
Open a data file and read its contents into a list
Calculate and print the mean, median, variance, and standard
  deviation
Plot a histogram of the data
"""

import math

# Required set for matplotlib
import matplotlib
matplotlib.use('Agg')   # required on mimir
from matplotlib import pyplot as plt


# Calculate the mean of the list x
def mean(x):
  return sum(x) / len(x)

  
# Calculate the median of the list x
# Sort the list first then check if there are 
#  an even number or odd number of values
# If even need to find the middle plus the 
#  next number, add them together, and divide by 2
# If odd we are finding the floor cause python3 is evil,
#  so we need to add 1 to get the correct middle
def median(x):
  y = sorted(x)
  if len(y) % 2 == 0:
    return ((y[len(y)//2] + y[len(y)//2 + 1]) / 2)
  else:
    return (y[(len(y)//2) + 1])

    
# Calculate the variance of the list x
def variance(x):
  variance = 0
  for i in x:
    variance += (i ** 2)
  return variance/len(x)


# Calculate the standard deviation of the list x
def standard_deviation(x):
  return (math.sqrt(variance(x)))
  

# Open the data file
f = open('data.txt', 'r')


# create an empty list
values = []


# Use the for loop to iterate through the file's lines
for line in f:
  
  # strip method removes white space
  line = line.strip()
  
  # Append to the data list
  values.append(float(line))

print("The mean is", mean(values))
print("The median is", median(values))
print("The variance is", variance(values))
print("The standard deviation is", standard_deviation(values))


  
# Plot the histogram
plt.figure()
plt.hist(values, 20)
plt.xlabel('Data Value')
plt.ylabel('Count')

plt.savefig('More_Calculations.pdf', bbox_inches='tight')

