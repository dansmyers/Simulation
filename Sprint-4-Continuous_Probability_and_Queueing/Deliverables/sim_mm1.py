#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu

from statistics import stdev
from math import log
from math import sqrt
from random import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    #
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
    
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    
    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        
        # TODO: calculate departure_times[i]
        
    # Calculate residence times
    # TODO: calculate list of residence times
    
    # TODO: return average residence time