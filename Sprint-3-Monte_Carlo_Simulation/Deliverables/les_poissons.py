"""

This program will simulate the relationship between the binomial distribution and the poisson distribution. The result will show that the poisson distribution is a good approximation for the binomial distribution.

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
	
	
	frequencies = {}
	

	for value in values:
		if value not in frequencies:
			frequencies[value] = values.count(value)
			
	return frequencies

def calculate_poisson(values):
	
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
	
	
	# successes_output = list(dict.fromkeys(total_successes))
	
	
	#print(poisson_output)
	#poisson_output.sort()
	#print(total_successes)
	poisson_frequencies = calculate_poisson(total_successes)
	#print(poisson_frequencies.keys())
	#print(fraction_success_frequencies.keys())
	#print(poisson_frequencies)
	
	poisson_values = list(poisson_frequencies.values())
	poisson_values.sort()
	
	plt.figure()
	plt.plot(list(fraction_success_frequencies.keys()), list(fraction_success_frequencies.values()), color='red')
	plt.plot(poisson_values, list(fraction_success_frequencies.values()))
	
	
	
	plt.savefig("Les_Poissons_Plot.pdf", bbox_inches = "tight")

"""

We will run 1000 simulations of this 1000 trial experiment to see the binomial distribution of the fraction of trials that returned "x" number of successes, which we expect to have an average of around 25 successes per trial. 

"""

if __name__ == '__main__':
		main()

