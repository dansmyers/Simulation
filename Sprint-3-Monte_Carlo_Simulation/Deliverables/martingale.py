# import the random library to get random numbers
import random

#import the matplotlib library
import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt

def spin_wheel():
	wheel_spin = int(random.random() * 38)
	if wheel_spin < 19:
		roulette_color = "red"
	elif 19 <= wheel_spin <= 36:
		roulette_color = "black"
	else:
		roulette_color = "green"
		
	return roulette_color

def simulate():
	bankroll = 255
	num_spins = 0
	max_bet = 1
	
	while True:
		if num_spins == 100:
			break
		
		if max_bet > bankroll:
			break
		
		bankroll -= max_bet
		
		color = spin_wheel()
		
		if color == "black":
			bankroll += max_bet * 2 
			max_bet = 1 
			num_spins += 1 
			
		else:
			num_spins += 1
			max_bet *= 2
	
	return bankroll

def main():
	
	results = []
	for i in range(1000):
		results.append(simulate())
	
	plt.figure()
	
	plt.xlabel("Value")
	plt.ylabel("Count")
	
	plt.hist(results, 30)
	
	plt.savefig("martingale_strategy_results.pdf", bbox_inches = "tight")

main()
	
	
	
	
	
	
	
	
	
	


















