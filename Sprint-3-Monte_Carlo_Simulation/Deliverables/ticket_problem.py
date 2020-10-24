"""
	Program to calculate the probability of the 
	ticket problem
"""

import random

def random_open_seat(availiable_seats):
	open_seats = []
	
	for i in range(100):
		if availiable_seats[i] == 1:
			open_seats.append(i)
		#print(availiable_seats[i], " is availiable seat ", i)
	
	random_seat = int(random.random() * (len(open_seats)))
	
	# print(open_seats, " number of open seats")
	# print(random_seat, " is the index of the random seat")
	# print(len(open_seats), " is the number of open seats")
	# print("the passenger sat randomly in ", open_seats[random_seat])

	return open_seats[random_seat]

def simulate():
	"""
		run one simulation of the train ticket problem
	"""
	# the seat the first passenger will sit in 
	first_passenger_seat = int(random.random() * 100 - 1)
	
	#print("the first passenger sat in ", first_passenger_seat)
	
	# list holding a value for availiable seats 
	# 1 if seat is availiable 
	# 0 if seat is not availiable 
	availiable_seats = []
	
	# all seats are initially availiable 
	for i in range(100):
		availiable_seats.append(1)
		
	# remove the seat the first passenger has sat in
	availiable_seats[first_passenger_seat] = 0
	
	# for every subsequent passenger check to see if their seat is
	# open if so take the seat Otherwise find a new random open seat
	# start the loop at 1 as the frist passenger has already sat
	# down
	for i in range(1, len(availiable_seats) - 1):
		# check to see if the seat is open 
		if availiable_seats[i] == 1:
			availiable_seats[i] = 0 
		else:
			# the passengers seat has been taken find a random open
			# seat 
			availiable_seats[random_open_seat(availiable_seats)] = 0
	return availiable_seats[99] == 1

def main():
	
	num_trials = 10000
	num_true = 0 
	
	for i in range(num_trials):
		if simulate() == True:
			num_true += 1
			
	fraction_successes = float(num_true / num_trials)
	
	return fraction_successes
	
print(main())















































