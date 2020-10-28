"""

	This program simulates the ticket problem and finds the probability that passenger 100 gets to sit in their assigned seat.
	Jacob Buckelew
	CMS380 Fall 2020

"""

import math
import random



def simulate(available_seats):
	
	"""
	Simulate choosing a seat for each passenger. Takes an input of available seats and output 1 if a success occurs, which is when the last passenger gets their assigned seat(100th passenger gets seat 100). Return 0 if it fails.
	
	"""

	seat = 0
	
	# List of unavailable seats 
	
	unavailable_seats = []
	
	# for each i, we simulate the choosing of a seat in the list of available seats
	for i in range(0, 100):
		
		# case where there are 100 seats available(1st passenger boards)
		if (i == 0):
			seat = random.choice(available_seats)
		# case after the first passenger boards
		else:
			
			if i not in available_seats:
				altered_seats = list(available_seats)
				# remove 0s
				while(-1 in altered_seats):
					altered_seats.remove(-1)
					if len(altered_seats) == 1:
						break;
				seat = random.choice(altered_seats)
			else:
				seat = available_seats[i]
		unavailable_seats.append(seat)
		available_seats[seat] = -1
		
	if(unavailable_seats[99] == 99):
		return 1;
	else: 
		return 0;


def main():
	"""
	Going to run 1000 simulations of the ticket problem and find a good approximation by averaging the total number of successes that occur over the total number of simulations.
	
	"""
	
	# start running trials
	# save outcomes of trials
	
	successes = 0
	
	for trial in range(1000):
		available_seats = list(range(0, 100))
		successes += simulate(available_seats)
	
	print(successes/(1000))
		


if __name__ == '__main__':
	main()