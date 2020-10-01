"""
Open a data text file and read information from it
Calculate and print mean, median, varience, and standard deviation
Save as a box plot and 20 bin histogram

"""
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 

import statistics
import math

def mean(x):
    num = 0
    for line in x:
        num = num + line
    length = len(x)
    return num/length

def varience(list_values, avg):
    numbers = []
    num = 0
    # Calculate value in list - avg
    for line in list_values:
        num = line - avg
        num ** 2
        num = abs(num)
        numbers.append(num)
    
    num2 = mean(numbers)
    return num2

def standard_dev(y):
    dev = math.sqrt(y)
    return dev


# Main


f = open('data.txt', 'r')

values = []

for line in f:
    #Remove white space
    line = line.strip()
    
    # Cast to a float and append to the list
    values.append(float(line))
    
# Calculate answers using values list

sum1 = mean(values)
sum2 = statistics.median(values)
sum3 = varience(values, sum1)
sum4 = standard_dev(sum3)

print("The mean is:", sum1)
print("The median is:", sum2)
print("The varience is:", sum3)
print("The standard deviation is:", sum4)

plt.figure()
plt.hist(values)
plt.xlabel('Num bins')
plt.ylabel('Count per bin')
plt.savefig('values.pdf', bbox_inches='tight')






