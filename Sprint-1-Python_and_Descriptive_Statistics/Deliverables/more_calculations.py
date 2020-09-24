"""
For this Python script I worked with Jacob and Griffin.

<<<<<<< HEAD
This script calculates and prints the mean, meadian, variance, and standard deviation of the data set defined in the data.txt file. It also saves, as PDFs, a box plot and a 20-bin histogram calculated from the values.

CMS380, Fall 2020 
Maria Morales
"""

import math
# Import and setup of matplotlib for Mimir IDE
import matplotlib
# Required when running on a remote environment
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# Open file for reading
file = open ("data.txt", "r")


data_values = []

for value in file:
    value = value.strip() # Remove whitespace from the lines
=======
This script calculates and prints the mean, meadian, variance, and standard deviation of a dataset defined in the data.txt file. It also saves, as PDFs  a box plot and a 20-bin histogram calculated from the  values.
"""
import statistics
import math
import matplotlib

matplotlib.use('Agg')
from matplotlib import pyplot as plt 
# Open file for reading
file = open ("data.txt", "r")

# Empty list
data_values = []

#print (file.read())

for value in file:
    value = value.strip() # Remove whitespace
>>>>>>> cc added
    # Cast to a float and then append to the list
    data_values.append(float(value))


"""
<<<<<<< HEAD
Function to calculate and return the mean of an input list
=======
Calculate and return the mean of input list x
>>>>>>> cc added
"""
def calc_mean(x):
    number_of_values = len(x)
    values_sum = 0
    
    for num in x:
        values_sum += num
    
    mean = values_sum / number_of_values
    
    return  mean
"""
<<<<<<< HEAD
Function to calculate and return the median of an input list
=======
Calculate and return the median of input list x 
>>>>>>> cc added
"""    
def calc_median(x):
    number_of_values = len(x)
    sorted_list = sorted(x)
    middle = (number_of_values - 1) // 2
    
    if number_of_values % 2 == 1:
        return sorted_list[middle]
    else:
        return (sorted_list[middle] + sorted_list[middle + 1]) / 2

"""
<<<<<<< HEAD
Function to calculate and return the variance of an input list
=======
Calculate and return the variance of input list x 
>>>>>>> cc added
"""        
def calc_variance(x):
    number_of_values  = len(x)
    mean = calc_mean(x)
    value_sum = 0
    
    for num in x:
        value_sum += pow((num - mean), 2)
        
    return value_sum/number_of_values
    
"""
<<<<<<< HEAD
Function to calculate and return the standard deviation of an input list
=======
Calculate and return the standard deviation of input list x 
>>>>>>> cc added
"""
def calc_standard_deviation(x):
    variance = calc_variance(x)
    
    return math.sqrt(variance)
    
<<<<<<< HEAD

# Save (as PDFs) a box plot and a 20-bin histogram calculated from the values.

=======
"""
Save (as PDFs) a box plot and a 20-bin histogram calculated from the values.
"""
>>>>>>> cc added

# Create a new  figure
plt.figure()

# Plot a histogram of the data from data.txt file with 20 bins
plt.hist(data_values, 20)

# Title and axis labels 
plt.title('data.txt histogram')
plt.xlabel('Data value')
plt.ylabel('Count')

# Save the histogram to a file
plt.savefig('more_calculations_histogram.pdf', bbox_inches='tight')
        
# Create new figure and axis for boxplot
fig, ax  =  plt.subplots()

# Set title 
ax.set_title('data.txt boxplot')

ax.boxplot(data_values, vert=False)

# Save the boxplot to a file 
plt.savefig('more_calculations_boxplot.pdf', bbox_inches='tight')


<<<<<<< HEAD

=======
    
    
    
test = [4, 5, 8, 9, 10]
>>>>>>> cc added

print('The mean of the data set:', calc_mean(data_values))
print('The median of the data set: ', calc_median(data_values))
print ('The variance of the data set: ', calc_variance(data_values))
print('The standard deviation of the data set: ', calc_standard_deviation(data_values))
