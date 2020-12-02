"""

This program simulates Disney's Fastpass+ system in the form of an M/M/1 style queue. 
Reflection of results is included in fastpass_reflection.txt
Jacob Buckelew
CMS380, Fall 2020

"""

from math import log
from random import random
from heapq import heappush, heappop, heapify
import matplotlib 
matplotlib.use('Agg')
from matplotlib import pyplot as plt


def rand_exp(rate):
    
    """ rand_exp(rate) generates an exponential random variate
    
        input a rate
        return an exponential variable
    """
    
    return -log(random()) / rate


def simulate(arrival_rate, fraction_fastpasses):
	
	"""
	Simulate the M/M/1 Queue, discrete-event style
	input: arrival_rate the system's arrival rate
	returns: the average simulated residence time
	
	"""
	
	max_arrivals = 1000000
	
	# parameters
	service_rate = 1.0 
	time = 0.0 
	
	# Need two variables to store the total number of customers
	# One will store the number of low priority customers
	# The other will store the number of high priority customers
	num_in_queue_low = 0
	num_in_queue_high = 0
	
	# lists to save times
	arrival_times_low = []
	enter_service_times = []
	departure_times_low = []
	
	arrival_times_high = []
	departure_times_high = []
	
	
	# Ensure 
	isOccupiedByLow = False
	
	
	
	# Initialize FEL
	future_event_list = []
	

	#First arrival 
	
	interarrival_time = rand_exp(arrival_rate)
	new_event = (time + interarrival_time, 'arrival')
	
	# Insert using heappush
	
	heappush(future_event_list, new_event)
	
	while len(future_event_list) > 0 and (len(arrival_times_low) + len(arrival_times_high)) < max_arrivals:
		
		# Pop next new_event
		event = heappop(future_event_list)
		
		event_time = event[0]
		event_type = event[1]
		
		time = event_time
		if event_type == 'arrival':
			# log arrival time
			
			# Figure out, based on value of fraction_fastpasses, whether this is the arrival of high priority or low priority customer
			if(random() < fraction_fastpasses):
				num_in_queue_high += 1
				arrival_times_high.append(time)
			else:
				num_in_queue_low += 1 
				arrival_times_low.append(time)
			
			
			# generate the next arrival 
			
			interarrival_time = rand_exp(arrival_rate)
			new_event = (time + interarrival_time, 'arrival')
			heappush(future_event_list, new_event)
			
			# If queue empty, enter service and generate the departure for this arrival
			
			if (num_in_queue_high + num_in_queue_low) == 1: 
				# enter a service time
				enter_service_times.append(time)
				
				# generate new departure
				if (num_in_queue_low) == 1:
					isOccupiedByLow = True
				service_time = rand_exp(service_rate)
				new_event = (time + service_time, 'departure')
				heappush(future_event_list, new_event)
				
				
		elif event_type == 'departure':
				
			# When generating next customer's service time, we need to check if anyone is in the high priority queue so that they may enter before low priority customers
			
			# Two cases when there is only 1 customer waiting to get on the ride. We won't need to generate a new service time for these cases
			if num_in_queue_high == 1 and num_in_queue_low == 0:
				num_in_queue_high -= 1
				departure_times_high.append(time)
			elif num_in_queue_low == 1 and num_in_queue_high == 0:
				num_in_queue_low -= 1
				isOccupiedByLow = False
				departure_times_low.append(time)
		
			
			# There's at least 1 person in both lines so we must decide which customer goes into service next
			else:
				
				# Scenario: we have customers in the high priority line that will go into service before other low priority customers
				if num_in_queue_high > 0 and (isOccupiedByLow == False):
				
					# log enter service time 
					departure_times_high.append(time)
					enter_service_times.append(time)
					num_in_queue_high -= 1 
					# generate new departure event 
					service_time = rand_exp(service_rate)
					new_event = (time + service_time, 'departure')
					heappush(future_event_list, new_event)
				# Special case is when the high priority customers that arrive during a low priority customer's service time must wait 
				elif num_in_queue_high > 0 and (isOccupiedByLow == True):
					isOccupiedByLow = False
					num_in_queue_low -= 1
					departure_times_low.append(time)
					enter_service_times.append(time)
					# generate new departure event 
					service_time = rand_exp(service_rate)
					new_event = (time + service_time, 'departure')
					heappush(future_event_list, new_event)
				
				# All customers are in the low priority line so this will be FCFS
				elif num_in_queue_high == 0 and num_in_queue_low > 0:
					# log enter service time 
					departure_times_low.append(time)
					enter_service_times.append(time)
					num_in_queue_low -= 1
					isOccupiedByLow = True
					# generate new departure event 
				
					service_time = rand_exp(service_rate)
					new_event = (time + service_time, 'departure')
					heappush(future_event_list, new_event)
					
	# Calculate average residence time
	residence_times_high = [departure_times_high[i] - arrival_times_high[i] for i in range(len(departure_times_high))]
	average_residence_time_high = sum(residence_times_high) / len(residence_times_high)
	
	residence_times_low = [departure_times_low[i] - arrival_times_low[i] for i in range(len(departure_times_low))]
	average_residence_time_low = sum(residence_times_low) / len(residence_times_low)
	
	
	return [average_residence_time_high, average_residence_time_low]
	
def main():
	
	"""
	Simulate the queue in two scenarios: one when there is a high u and one when there is a low u. In each scenario, the main() will keep track of the average residence times of the high priority customers and low priority customers given to it from the simulate() function. Then the data will be plotted in two separate graphs, each one having two lines representing priority and regular customers.
	
	"""
	# utilization parameter
	low_u = .50
	high_u = .95
	
	# Run two simulations, one for high-load(u = .95) and one for low-load(u = .50)
	# in which 20 trials will be performed for each value of u
	sim_residence_times_low_lp = []
	sim_residence_times_low_hp = []
	sim_residence_times_high_lp = []
	sim_residence_times_high_hp = []
	
	results_low_u = []
	results_high_u = []
	
	x_values = []
	
	# Run 20 trials at each utilization level and use the average of the simulated
    # values as the estimate of the residence time
	for f in range(5, 95, 5):
		results_low_u = simulate(low_u, f/100.0)
		results_high_u = simulate(high_u, f/100.0)
		
		sim_residence_times_low_hp.append(results_low_u[0])
		sim_residence_times_low_lp.append(results_low_u[1])
		
		sim_residence_times_high_hp.append(results_high_u[0])
		sim_residence_times_high_lp.append(results_high_u[1])
		x_values.append(f/100.0)


	
	plt.figure()
	plt.plot(x_values, sim_residence_times_low_hp, color ='red', label='high priority')
	plt.plot(x_values, sim_residence_times_low_lp, label='low priority')
	plt.legend()
	plt.title('FastPass+ MM1 Queue Under a Low Load')
	plt.xlabel("Fraction of Fastpasses")
	plt.ylabel("Residence Times")
	plt.savefig("FastPass_Queue_Low_Load.pdf", bbox_inches = "tight")
	
	plt.figure()
	plt.plot(x_values, sim_residence_times_high_hp, color ='red', label='high priority')
	plt.plot(x_values, sim_residence_times_high_lp, label='low priority')
	plt.title('FastPass+ MM1 Queue Under a High Load')
	plt.xlabel("Fraction of Fastpasses")
	plt.ylabel("Residence Times")
	plt.legend()
	plt.savefig("FastPass_Queue_High_Load.pdf", bbox_inches = "tight")



if __name__ == '__main__':
    main()
	
		
		