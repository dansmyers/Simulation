"""

	This program will simulate the relationship between the binomial distribution and the poisson distribution. The result will show that the poisson distribution is a good approximation for the binomial distribution.

	Jacob Buckelew
	CMS380 Fall 2020

"""

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 
import random
import math
import numpy as np

def simulate():
	"""
	
	Simulate a coin flip with flipping a heads having probability .025
	
	Return 1 if a heads comes up and return 0 if a tail comes up
	
	"""
	
	p = .025
	
	coin_flip = random.random()
	
	if(coin_flip <= p):
		return 1 
	
	if(coin_flip > p):
		return 0
	

def calculate_frequencies(values):
	
	"""
	
	Calculate the frequencies at which the fractional values occur. This will help us to figure out our overall distribution and returns a dictionary that maps the fractions to frequencies. Takes an array as input.
	
	
	"""
	
	
	frequencies = {}
	

	for value in values:
		if value not in frequencies:
			frequencies[value] = values.count(value)
			
	return frequencies

def calculate_poisson(values):
	
	
	"""
	
	Calculate the poisson pmf given an array of values. Each value will be plugged into the poisson pmf and these values will be saved in a dictionary where we keep up with the fractional values and their pmf values.
	
	
	"""
	
	frequencies = {}
	
	for i in values:
		i = i * 1000
		value = (math.exp(-25)) * (25 ** i)/(math.factorial(i))
		if i/1000 not in frequencies:
			frequencies[i/1000] = value
	
	return frequencies

def main():
	
	"""
	
	Call simulate 1000 times and record the fraction of heads that occur. Then, record the number of successes from that simulation. Repeat this process 1000 times to get 1000 simulations each having 1000 trials. Each simulation will then have a fraction of successes associated with it. 
	Also, plot a poisson distribution given that lambda is 25.
	
	"""
	
	max_trials = 1000
	
	# list holds the total num of successes from each simulation aka trial
	
	total_successes = []
	
	for simulation in range(1000):
		num_successes_value = 0
		
		for trial in range(max_trials):
			
			num_successes_value += simulate()
		
		total_successes.append(num_successes_value/ max_trials)
	
	total_successes.sort()

	
	fraction_success_frequencies = calculate_frequencies(total_successes)
	
	

	poisson_frequencies = calculate_poisson(total_successes)
	
	# Save the poisson values from the dictionary we got from calculate_poisson and sort
	poisson_values = list(poisson_frequencies.values())
	poisson_values.sort()
	
	plt.figure()
	plt.xlabel('values')
	plt.ylabel('frequency')
	plt.title('Les Poissons Line Plot')
	plt.plot(list(fraction_success_frequencies.keys()), list(fraction_success_frequencies.values()), color='red', label="binomial distribution")
	plt.plot(poisson_values, list(fraction_success_frequencies.values()), label="poisson distribution")
	plt.legend()
	
	
	
	plt.savefig("Les_Poissons_Plot.pdf", bbox_inches = "tight")

"""

We will run 1000 simulations of this 1000 trial experiment to see the binomial distribution of the fraction of trials that returned "x" number of successes, which we expect to have an average of around 25 successes per trial. 

"""

if __name__ == '__main__':
		main()

