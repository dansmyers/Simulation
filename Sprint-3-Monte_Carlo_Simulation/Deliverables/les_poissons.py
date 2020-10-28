# import the random library to use in the simulate method
import random

#import the matplotlib library
import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt

# import a counter to count the number of occurences in a list 
from collections import Counter

# import the math library
import math

def simulate():
	"""
		Function to simulate 1000 biased coin flips with heads comming up with a probability of .025
	"""
	
	# random number telling the probability of the coin landing on a heads 
	number = 0
	
	# number of seccesses in 1000 flips
	successes = 0 
	
	# variable of probability
	PROBABILITY = .025
	
	for i in range(1000):
		number = random.random()
		
		if number <= PROBABILITY:
			successes = successes + 1 
		
	return successes



def main():
	"""
		This function will run the simulate method 100 times and will find the fraction
		of successes. It returns a fraction of successes for each simulation
	"""
	num_interations = 1000 # number of simulated trials
	
	# fraction of successes for each simulation run 
	# example 10/1000 if 10 out of all the coin flips were heads (in decimal form)
	fraction_successes = [] 
	
	# Variable to keep track of the number of successes of each fraction 
	# This variable will be reset every time a different fraction is found 
	num_successes = 1
	
	# run the simulation 1000 times and find the fraction number of successes
	# Add each fraction from each simulation into a list 
	for i in range(1000):
		fraction_successes.append(simulate() / 1000)
		
	# Sort the list of fractions so we can find the number of the same fractions 
	fraction_successes.sort()
	
	# Dictionary mapping the success fraction to the number of times it has appeared 
	# example 10/1000 happend 4 times the dictionary maps 10/1000 -> 4
	# This number will be used in the graph to show the distribution
	
	# go through the list and find the number of similar elements
	# store those elements into a dictionary with the key as the fraction
	# and the value as the number of occurences of that fraction
	
	# Counter from the collections library has a method to do this logic 
	successes_count = Counter(fraction_successes)
	
	# # put those values into sorted tuples and plot the tuples as x and y values 
	# values = sorted(successes_count.items())
	
	# # unpack the tuples and store the lists into the x and y variables 
	# x, y = zip(*values)
	
	# # plot the values in a line chart using the x and y coordinates
	# plt.plot(x, y)
	
	# plt.savefig("line_chart.pdf", bbox_inches = "tight")
	
	return successes_count
	
def poisson_pmf_25(k):
	"""
		This method will calcualte the pmf of a poisson distribution with a given k
	"""
	return (math.exp(-25) * 25 ** k) / math.factorial(k)
	
def plotFigs():
	"""
		This method will get all of the data calculated in the above functions and plot it into a line plot
	"""
	successes_count = main()
	
	print(successes_count)
	
	x = list(successes_count.keys())
	y = list(successes_count.values())
	print("y-axis ",y)
	
	# list holding the poisson_values
	poisson_values = []
	
	# find the poisson pmf for all of the keys in the successes_count
	for i in x:
		poisson_values.append(poisson_pmf_25(i * 1000))

	poisson_values.sort()
	print("x-axis ",poisson_values)
	
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	
	plt.plot(x, y, label = "Simulated Values")
	plt.plot(poisson_values, y, label = "Poisson Values")
	
	plt.legend()
	
	plt.savefig("line_chart.pdf", bbox_inches = "tight")
	
	
plotFigs()