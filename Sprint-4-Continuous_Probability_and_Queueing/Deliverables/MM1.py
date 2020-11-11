#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
from math import log 
from random import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    #
    # Look at the inverse CDF examples
    x = -log(random())/mu 
    return x

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
    for i in range (0, n):
        interarrival_times[i] = rand_exp(arrival_rate)
    #print(interarrival_times)
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    service_times = [0] * n
    i = 0
    for i in range (0, n):
        service_times[i] = rand_exp(1/avg_service_time)
 
    #print(service_times)
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    arrival_times = [0] * n
    for i in range (0, n):
        if i < 1:
            arrival_times[i]= 0
        else:
            arrival_times[i] = interarrival_times[i] + arrival_times[i-1]
    #print(arrival_times)
    
    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    residence_times = [0] * n
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
        residence_times[i] = departure_times[i] - arrival_times[i]
    # TODO: return average residence time
    avg_residence_time = sum(residence_times)/n
    return avg_residence_time
    
def main():
    
    avg_service_time = 1.0
    n = 5000
    arrival_rate = [0.05, .10, .15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
    result = [] 
    utilization = [0] * (len(arrival_rate))
    
    for i in range(0, len(arrival_rate)):
        result.append(simulate(arrival_rate[i], avg_service_time, n))
        utilization[i] = arrival_rate[i] * avg_service_time
        
    #print(result)
    #Create a new figure, always do this before calling a plotting function
    plt.figure()
    
    plt.plot(utilization, result)
    #Set title ad axis label
    plt.title("M/M/1 Simulation")
    plt.xlabel("utilization")
    plt.ylabel("avg. residence time")
    
    #Save figure on file
    plt.savefig("MM1.pdf", bbox_inches="tight")
  
main()      
    
    
    
    