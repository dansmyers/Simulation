# M/M/1 Simulation problem
# CMS 380
# Matthew Trautmann Fall 2020

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# Math imports
from math import log
from random import random

#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    #
    # Look at the inverse CDF examples
    return -log(random()) / mu
    
    
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
    for i in range(1, n):
        interarrival_times[i] = rand_exp(arrival_rate)
        
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    service_times = [0] * n
    for i in range(0, n):
        service_times[i] = rand_exp(1 / avg_service_time)
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    arrival_times = [0] * n
    arrival_times[0] = 1
    for i in range(1, n):
        time = arrival_times[i - 1] + interarrival_times[i]
        arrival_times[i] = time

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
    for i in range(0, n):
        residence_times[i] = departure_times[i] - arrival_times[i]
    # TODO: return average residence time
    average_residence_time = sum(residence_times) / len(residence_times)
    return average_residence_time

def main():

    n = 5000
    arrival_rate = .05
    avg_service_time = 1
    
    avg_residence_times = []
    utilization_list = []
    
    while arrival_rate < 1:
        utilization = arrival_rate * avg_service_time
        utilization_list.append(utilization)
        residence_time = simulate(arrival_rate, avg_service_time, n)
        avg_residence_times.append(residence_time)
        arrival_rate = arrival_rate + .05
        
     # Create a new figure
    plt.figure()

    # Create line plots for simulated data
    plt.plot(utilization_list, avg_residence_times)
    
    
    # Title and axis labels
    plt.title('Single Queue Simulation')
    plt.xlabel('Utilization Rate')
    plt.ylabel('Simulated Average residence times')

    # Save the figure to a file
    plt.savefig('mm1.pdf', bbox_inches='tight')
    

    
    
# Call main() when this program runs
if __name__ == '__main__':
    main()
