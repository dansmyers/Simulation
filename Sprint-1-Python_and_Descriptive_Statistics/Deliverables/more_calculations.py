"""

	I worked on this problem with Griffin and Maria
	
	This program reads the file "data.txt" and calculates the mean, median, variance, and standard deviation. Also, this program creates a box plot and histogram to graphically model the data. 
	
<<<<<<< upstream/master
	CMS380, Fall 2020

=======
>>>>>>> HEAD~5
"""
import math
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


"""
	Function that calculates the average(mean) of a list of data values.

"""

def mean(values):
	
	# Find size of the data set
	count = len(values)
	total = 0
	
	# Sum the values in the data set together
	for i in values:
		total += i
	
	return total/count
	
"""
	Function that calculates the median of a list of data values. The function first sorts the list and then deals with two possible cases in which the length of the data is either even or odd.

"""


def median(values):
	
	# Find Size of data set
	
	count = len(values)
	
	# Sort the data set in order to find the median
	values = sorted(values)
	
	# Check if size of data set is divisible by 2(even size). If so, then the list indexes from 0 to n, where n is an odd number. If not, then the data set must be of an odd size and will index from 0 to n where n is an even number.
	
	if count % 2 == 0:
		# Subtract .5 and add .5 to the nth index(count - 1)/2 in order to find the two numbers that are needed for finding the median.
		
		number_1 = values[int(((count - 1) / 2) - (.5))]
		number_2 = values[int(((count - 1) / 2) + (.5))]
		return (number_1 + number_2)/ 2
	else:
		# The median can be found by just doing nth index/2 and finding the value at that index in the list.
		
		return (values[int((count - 1) / 2)])
		

"""
	Function that calculates the variance of a list of data values. 
	
"""

def variance(values):
	
	# Setup a variable for summation
	count = 0
	
	# Find size of data set
	
	length = len(values)
	
	# Find mean of the data set 
	
	average = mean(values)
	
	# iterate through the list and sum together (values[0] - mean)^2 ... (values[n] - mean)^2 where n is the last index in the list.
	
	for i in values:
		count += (i - average) ** 2
	
	return count/length

"""
	Function that calculates the standard devation of a list of data values. This function calls the function variance() in order to calculate the variance of a list and then use the square root operation on that value.  

"""

def std_dev(values):
	# Take the square root of variance to find the standard deviation
	
	return math.sqrt(variance(values))
	

"""
	build_histogram() uses the pyplot from matplotlib in order to create a histogram for a list of data values. 

"""


def build_histogram(values):
	
	plt.figure()
	plt.hist(values, 20)

	plt.title('Data Histogram')
	plt.xlabel('Data value')
	plt.ylabel('Count')

	plt.savefig("Data_Histogram.pdf", bbox_inches= "tight")
	

"""
	build_boxplot() uses the pyplot from matplotlib in order to create a boxplot for a list of data values.

"""
	
def build_boxplot(values):

	plt.figure()
	plt.boxplot(values)
<<<<<<< upstream/master
<<<<<<< upstream/master
	plt.title('Data Boxplot')
=======
>>>>>>> HEAD~5
=======
	plt.title('Data Boxplot')
>>>>>>> HEAD~4
	plt.savefig("Data_Boxplot.pdf", bbox_inches= "tight")


# MAIN

# open data.txt file
file = open("data.txt", "r")

values = []

# save data in a list
for i in file:
	i = i.strip() # remove whitespace
	values.append(float(i))

build_histogram(values)
build_boxplot(values)

	
print("The mean of the data set is: ", mean(values))
print("The median of the data set is: ", median(values))
print("The variance of the data set is: ", variance(values))
print("The standard deviation of the data set is: ", std_dev(values))

	


