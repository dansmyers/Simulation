"""
	I worked on this problem with Jacob and Maria.
	
	This script calculates and prints the mean, median, variance, and standard deviation of a dataset
	defined in a data.txt file
"""

# import the square root function from the math library
from math import sqrt

# import matplotlib to create the box plot and histogram
import matplotlib

# tell matplotlib we are using a virtual environment for our code
matplotlib.use("Agg")

# import pyplot as plt to use later in the histogram and box plot functions
from matplotlib import pyplot as plt

# open the data.txt file 
file = open("data.txt", "r")

data_values = []

data = [1,2]

for value in file:
	value = value.strip()
	
	data_values.append(float(value))

	

"""
	Function that calculates the mean of the data values in the data.txt file
"""
def calculate_mean(values):
	num_values = len(values)
	value_sum = 0
	
	for number in values:
		value_sum += number
	
	mean = value_sum / num_values
	
	return mean


"""
	Function that caluclates the median of the data values in the data.txt file
"""
def calculate_median(values):
	values = sorted(values)
	list_length = len(values)
	
	if len(values) % 2 == 0:
		
		middleElem1 = values[int(list_length / 2) - 1]
		middleElem2 = values[int(list_length / 2)]
		
		average = (middleElem1 + middleElem2) / 2 
		
		return average
		
	else:
		median = values[int(list_length / 2)]
		
		return median 

"""
	Function that calculates the variance of the data values in the data.txt file
"""

def calculate_variance(values):
	median = calculate_median(values)
	element_sum = 0
	
	for elements in values:
		element_sum += pow(elements - median, 2)
		
	variance = element_sum / len(values)
		
	return variance 


"""
	Function to calculate the standard deviation of the values in the data.txt file
"""
def calculate_standard_deviation(values):
	deviation = sqrt(calculate_variance(values))
	
	return deviation 
	
	
"""
	Function to create a 20 bin histogram of the values in the data.txt file
	
	Function will save the created histogram as a pdf 
"""

def histogram_of_data(values):
	plt.figure()
	
	plt.hist(values, 20)
	
	plt.title("Data.txt Values")
	plt.xlabel("Data value")
	plt.ylabel("count")
	
	plt.savefig("data.txt_histogram.pdf", bbox_inches = "tight")
	
"""
	Function to create a box plot of the values in the data.txt file 
	
	Function will save the created box plot as a pdf
"""

def box_plot_of_data(values):
	plt.figure()
	
	plt.boxplot(values)
	
	plt.title("Data.txt Box Plot")
	
	plt.savefig("data.txt_box_plot.pdf", bbox_inches = "tight")

print("The mean of the data set is :", calculate_mean(data_values))
print("The median of the data set is :",calculate_median(data_values))
print("The variance of the data set is :",calculate_variance(data_values))
print("The standard deviation of the data set is :",calculate_standard_deviation(data_values))








































