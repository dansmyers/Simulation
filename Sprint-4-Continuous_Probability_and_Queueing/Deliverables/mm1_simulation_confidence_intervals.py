from math import log
from math import sqrt
from random import random


import matplotlib
matplotlib.use("AGG")
from matplotlib import pyplot as plt

def calculate_mean(values):
	num_values = len(values)
	value_sum = 0
	
	for number in values:
		value_sum += number
	
	mean = value_sum / num_values
	
	return mean

def calculate_variance(values):
	median = calculate_mean(values)
	element_sum = 0
	
	for elements in values:
		element_sum += pow(elements - median, 2)
		
	variance = element_sum / len(values)
		
	return variance 

def calculate_standard_deviation(values):
	deviation = sqrt(calculate_variance(values))
	
	return deviation 

#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    #
    # Look at the inverse CDF examples
    
    return -log(random())/mu

#--- Simulate the M/M/1 queue
#
# Inputs:
#    arrival_rate
#    avg_service_time
#    n: number of simulated customers
#
# Output: the average residence time of customer in the queue

def simulate(arrival_rate, avg_service_time, n):

    # Generate interarrival times
    # TODO: use rand_exp to generate n interarrival times with parameter arrival_rate
    
    interarrival_times = []
    for i in range(n):
    	interarrival_times.append(rand_exp(arrival_rate))
    	
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    
    service_times = []
    for i in range(n):
    	service_times.append(rand_exp((1 / avg_service_time)))
    
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    arrival_times = []
    for i in range(len(interarrival_times)):
    	if i == 0:
    		arrival_times.append(interarrival_times[i])
    	else:
    		arrival_times.append(arrival_times[i - 1] + interarrival_times[i])
    
    arrival_times.sort()
    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    residence_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[0]
    residence_times[0] = service_times[0] - arrival_times[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i-1])
        
        # TODO: calculate departure_times[i]
        departure_times[i] = enter_service_times[i] + service_times[i]
        
    # Calculate residence times
    # TODO: calculate list of residence times
    for i in range(n):
    	residence_times[i] = departure_times[i] - arrival_times[i]
    
    # TODO: return average residence time
    total = 0
    for i in residence_times:
    	total += i
    
    total = total / n
    
    return total
    

def get_residence_times():
	
	iterator = .05
	residence_times = []
	ulitization = []
	i = 0
	
	while i <= 18:
		#print("iterator is: ", iterator)
		residence_times.append(simulate(iterator, 1.0, 5000))
		ulitization.append(iterator)
		
		iterator += .05
		i += 1
	
	return residence_times

def main():
	
	residence_times_trail_1 = get_residence_times()
	residence_times_trail_2 = get_residence_times()
	residence_times_trail_3 = get_residence_times()
	residence_times_trail_4 = get_residence_times()
	residence_times_trail_5 = get_residence_times()
	
	y_bar_list = []
	s = []
	
	for i in range(len(residence_times_trail_1)):
		y_bar_list.append( (residence_times_trail_1[i] + residence_times_trail_2[i] + residence_times_trail_3[i] + residence_times_trail_4[i] + residence_times_trail_5[i]) / 5)
		
	for i in range(len(residence_times_trail_1)):
		current_times = []
		current_times.append(residence_times_trail_1[i])
		current_times.append(residence_times_trail_2[i])
		current_times.append(residence_times_trail_3[i])
		current_times.append(residence_times_trail_4[i])
		current_times.append(residence_times_trail_5[i])
		
		s.append(calculate_standard_deviation(current_times))
		
		current_times.clear()
		
	
	UCL = []
	LCL = []
	
	for i in range(len(s)):
		UCL.append(y_bar_list[i] + 2.776 * s[i] / sqrt(5))
		LCL.append(y_bar_list[i] - 2.776 * s[i] / sqrt(5))
	
	ulitization = []
	number = 0;
	for i in range(19):
		number += .05
		ulitization.append(number)
	
	plt.figure()
	plt.errorbar(ulitization, y_bar_list, UCL)
	plt.savefig("ulitization_confidence_intervals.pdf", bbox_inches = "tight")
	
main()



    