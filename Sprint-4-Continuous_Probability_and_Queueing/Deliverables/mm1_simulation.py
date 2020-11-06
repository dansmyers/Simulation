from math import log
from random import random


import matplotlib
matplotlib.use("AGG")
from matplotlib import pyplot as plt
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
    print(total)
    
    return total
    

def main():
	
	iterator = .05
	residence_times = []
	ulitization = []
	i = 0
	
	while iterator < .95:
		
		residence_times.append(simulate(iterator, 1.0, 5000))
		
		ulitization.append(iterator)
		
		iterator += .05
		i += 1
	
	plt.figure()
	plt.plot(ulitization, residence_times)
	plt.savefig("ulitization.pdf", bbox_inches = "tight")
	
main()






    