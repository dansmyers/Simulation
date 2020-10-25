"""

	This program simulates the ticket problem and finds the probability that passenger 100 gets to sit in their assigned seat.

"""

import math
import random



def simulate(available_seats):
	
	"""
	Simulate choosing a seat for each passenger. Takes an input of available seats and output the chosen seat of the passenger
	
	"""
	
	# Get the length of the values list to get total number of seats available
	# n is the number of seats available
	n = len(available_seats)
	
		
	
	# probability p is the probability of picking a randoms seat out of n seats
	
	# p = 1/n 

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
		
	
		
		
	
	#print(unavailable_seats)
	if(unavailable_seats[99] == 99):
		return 1;
	else: 
		return 0;


def main():
	
	# set up our list of all available seats
	#available_seats = list(range(0, 100))
	
	# start running trials
	
	
	# save outcomes of trials
	
	successes = 0
	
	for trial in range(1000):
		available_seats = list(range(0, 100))
		successes += simulate(available_seats)
	
	print(successes/(1000))
		
		

		
		
		
		
		


if __name__ == '__main__':
	main()