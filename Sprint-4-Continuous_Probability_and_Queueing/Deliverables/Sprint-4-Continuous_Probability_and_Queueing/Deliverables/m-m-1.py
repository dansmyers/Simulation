# Write a Python program that implements the single-server queue simulation
#   algorithm. Use the pseudocode below as a starting point for your program. 
#   I've given you some `TODO` notes where you need to fill in code.

#IMPORTS 
from math import log
from math import sqrt
from random import random

import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("Agg")

#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):
     return(-log(random())/mu)

#--- Simulate the M/M/1 queue
#
# Inputs:
#    arrival_rate
#    avg_service_time
#    n: number of simulated customers
#
# Output: the average residence time of customer in the queue

def simulate(arrival_rate, avg_service_time, n):

    #INTERARIVAL TIMES
    interarrival_times = [rand_exp(arrival_rate) for i in range(n)]

    #SERVICE TIMES
    service_times = [rand_exp(1/avg_service_time) for i in range(n)]

    #ARRIVAL TIMES
    arrival_times = [sum(interarrival_times[:(i+1)]) for i in range(n)]

    #Initialize other lists 
    enter_service_times = [0] * n
    departure_times = [0] * n

    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = (enter_service_times[0] + service_times[0])

    # Loop over all other arrivals
    for i in range(1, n):
        # TODO: calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        # TODO: calculate departure_times[i]
        departure_times[i] = (enter_service_times[i] + service_times[i])

    # TODO: calculate list of residence times
    residence_times = [(departure_times[i]-arrival_times[i]) for i in range(n)]

    # TODO: return average residence time
    return sum(residence_times) / n

#1. Run five replications for each utilization value. 
#   Let `n = 1000` for all trials.

#2. Calculate the average of the five replications as your best estimate of the 
#   true mean residence time for that utilization level. 
#   Call this number `Y_bar`

#3. Calculate the standard deviation of the five residence time estimates. 
#   Call this value `s`.

#4. Calculate the upper and lower 95% confidence limits for your simulated estimates. 
#   For a t-distribution with four degrees of freedom, 
#   the critical value is 2.776 and the relevant formulas are:

#   UCL = Y_bar + 2.776 * s / sqrt(5)

#   LCL = Y_bar - 2.776 * s / sqrt(5)

def main():

 ## Simulation of increasing values of arrival_rate

    # Generate list of arrival rates with values .05, .10, .15, ..., .95
    arrival_rates = [(i / 20) for i in range(1, 20)]

    # Call 'simulate' and store avg. residence times
    average_residence_times = [simulate(i, 1.0, 5000) for i in arrival_rates]

    # Utilization
    utilization = [average_residence_times[i] * arrival_rates[i] for i in range(19)]

    plt.figure()
    plt.xlabel("Utilization")
    plt.ylabel("Avg. Residence Time")
    plt.plot(arrival_rates, utilization)
    plt.savefig("IncreasingValues.pdf", bbox_inches="tight")


 ## Calculation of Confidence Intervals

    # Five arrival rate samples
    samples = [[simulate(rate, 1.0, 1000) for i in range(5)] for rate in arrival_rates]

    # Sample Average
    Y_bar = [(sum(x) / 5) for x in samples]

    # Standard Deviation
    s = [sqrt((sum([((x[ii] - Y_bar[i]) ** 2) for ii in range(5)]))/4) for i,x in enumerate(samples)]

    # Upper confidence limit
    ucl = [(Y_bar[i] + 2.776 * s[i] / sqrt(5)) for i in range(19)]

    # Lower confidence limit
    lcl = [(Y_bar[i] - 2.776 * s[i] / sqrt(5)) for i in range(19)]
    
    # Utilization of averages
    Y_bar_util = [Y_bar[i] * arrival_rates[i] for i in range(19)]  
    
    # Utilization of upper confidence
    ucl_util = [ucl[i] * arrival_rates[i] for i in range(19)]
    
    # Utilization of lower confidence
    lcl_util = [lcl[i] * arrival_rates[i] for i in range(19)]

    plt.figure()
    plt.xlabel("Utilization")
    plt.ylabel("Avg. Residence Times")
    plt.plot(arrival_rates, ucl_util, color = "royalblue", label = "UCL")
    plt.plot(arrival_rates, lcl_util, color = "blue", label = "LCL")
    plt.plot(arrival_rates, Y_bar_util, color = "cornflowerblue", label = "AVG")
    plt.legend()
    plt.savefig("ConfidenceIntervals.pdf", bbox_inches = "tight")


# CALL MAIN
if(__name__=="__main__"): main()

