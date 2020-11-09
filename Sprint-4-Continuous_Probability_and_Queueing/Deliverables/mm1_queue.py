"""

Jacob Buckelew
CMS380, Fall 2020

This program simulates an mm1 queue. In the main() function, the mm1 queue is simulated multiple times for each value of utilization from 0.05, 0.10, 0.15, ..., 0.95.
For each simulation, there are 5 trials where the total average residence time will be found using the average residence time from each trial. At the end, all of the these average residence times(19 total) are plotted along with each corresponding utilization value. 


"""

from random import random
import math
from math import log
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    
    # We can use the formula x = -(ln(randomvalue))/mu where randomvalue is some randomly chosen uniform random value from the PRNG
    return -log(random())/mu
    # Look at the inverse CDF examples

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
    
    interarrival_times = [0] * n
    
    for i in range(n):
    	interarrival_times[i] = rand_exp(arrival_rate)
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    
    service_times = [0] * n
    
    for i in range(n):
    	service_times[i] = rand_exp((1 / avg_service_time))

    
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    
    arrival_times = [0] * n
    
    for i in range(n):
    	if(i == 0):
    		arrival_times[0] = 0 + interarrival_times[i]
    	else:
    		arrival_times[i] = arrival_times[i - 1] + interarrival_times[i]
    
    arrival_times.sort()
    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        
        # TODO: calculate departure_times[i]
        
        departure_times[i] = enter_service_times[i] + service_times[i]
        
    # Calculate residence times
    # TODO: calculate list of residence times
    
    residence_times = [0] * n 
    
    for i in range(n):
    	residence_times[i] = departure_times[i] - arrival_times[i]
    
    
    # TODO: return average residence time
    
    return (sum(residence_times)/ n )
    
   
# standard_deviation(values) takes a list as a parameter and returns the standard deviation of the list of values.

def standard_deviation(values):
	
	# Setup a variable for summation
	count = 0
	
	# Find size of data set
	
	length = len(values)
	
	# Find mean of the data set 
	
	average = (sum(values)/length)
	
	# iterate through the list and sum together (values[0] - mean)^2 ... (values[n] - mean)^2 where n is the last index in the list.
	
	for i in values:
		count += (i - average) ** 2
	
	return math.sqrt(count/length)

# Main() holds the main loop that will run all of the replications for each simulation where each simulation is running with a different utilization value. 
# The average residence times are calculated for all 19 utilization values and then these values along with the utilizations are plotted on a line plot with confidence intervals present.
    
def main():
	
	NUM_OF_TRIALS = 19
	arrival_rate = .05
	avg_service_time = 1.0
	n = 1000
	REPLICATIONS = 5
	
	Y_bar = [0] * NUM_OF_TRIALS
	utilizations = [0] * NUM_OF_TRIALS
	
	LCL = [0] * NUM_OF_TRIALS
	UCL = [0] * NUM_OF_TRIALS
	
	# run simulations to fill the avg_residence_times list
	

	for trial in range(NUM_OF_TRIALS):
		residence_times = [0] * REPLICATIONS
		for replication in range(REPLICATIONS):
			residence_times[replication] = simulate(arrival_rate, avg_service_time, n)
	
		Y_bar[trial] = (sum(residence_times)/ REPLICATIONS)
		
		# update the utilization values list
		utilizations[trial] = arrival_rate * avg_service_time
		s = standard_deviation(residence_times)
		UCL[trial] = Y_bar[trial] + ((2.776 * s) / math.sqrt(5))
		LCL[trial] = Y_bar[trial] - ((2.776 * s) / math.sqrt(5))
		arrival_rate = arrival_rate + .05
	
	
	plt.figure()
	
	plt.subplots()
	plt.errorbar(utilizations, Y_bar, yerr= UCL)
	plt.title("Utilization and Residence Times for the MM1 Queue")
	plt.xlabel("Utilization")
	plt.ylabel("Average Residence Time")
	plt.savefig("MM1_Queue.pdf", bbox_inches = 'tight')
	



if __name__ == '__main__':
	main()