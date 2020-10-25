"""

This is a program that simulate roulette games using the Martingale strategy.

"""

import random
import math
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def simulate():
	
	"""
	
	Simulate rounds of roulette either up to 100 spins or until the player goes into bankruptcy. Take the final outcome of money that the player ended with and return it to main.
	
	"""
	
	money_value = 255
	spin = 0
	bet = 0
	

	
	while((spin != 100) and ((2 ** bet ) < money_value)):
		
		# simulate a spin
		
		value = random.random() 
		
		if value <= (18/38):
			money_value += (2 ** bet)
			bet = 0
		else:
			
			money_value = money_value - (2 ** bet)
			
			bet = bet + 1
		
		spin = spin + 1
	
	return money_value
	

def main():
	
	outcomes = []
	
	
	for trials in range(1000):
		outcome = 0
		outcome += simulate()
		outcomes.append(outcome)
	
	
	plt.figure()
	plt.hist(outcomes, 30)
	plt.savefig("Martingale.pdf", bbox_inches = 'tight')
	
	

if __name__ == '__main__':
	main()