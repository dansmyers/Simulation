"""
Christian Huber
CMS 380, Fall 2020 / Sprint 4 / The M/M/1 Queue
This script simulates a system with a single server
queue and calculates the confidence intervals for the
average residence time estimate
"""

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

from random import random

from math import log
from math import sqrt



#### FUNCTIONS ####


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
    
    # Generate interarrival times
    interarrival_times = [rand_exp(arrival_rate) for i in range(n)]

    # Generate service times using the inverse of interarrival times
    service_times = [rand_exp(1/avg_service_time) for i in range(n)]

    # Calculate arrival times (uses interarrival times to calculate
    # a list of arrival times)
    arrival_times = [sum(interarrival_times[:(i+1)]) for i in range(n)]

    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n

    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = (enter_service_times[0] + service_times[0])

    # Loop over all other arrivals
    for i in range(1, n):
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        departure_times[i] = (enter_service_times[i] + service_times[i])

    # Calculate residence times
    residence_times = [(departure_times[i]-arrival_times[i]) for i in range(n)]

    # Return average residence time
    return sum(residence_times) / n



#### MAIN ####

#---- Main method that calls 'simulate' for increasing values of arrival_rate
#     and calculates confidence intervals for avg. residence time estimate
#     (Part One and Two in one main method)
def main():

 ## Simulation of increasing values of arrival_rate
    
    # Generate list of arrival rates with values .05, .10, .15, ..., .95
    arrival_rates = [(i / 20) for i in range(1, 20)]

    # Call 'simulate' and store avg. residence times
    average_residence_times = [simulate(i, 1.0, 5000) for i in arrival_rates]

    # Calculate utilization
    utilization = [average_residence_times[i] * arrival_rates[i] for i in range(19)]

    # Plot the data
    plt.figure()
    plt.title("M/M/1 Queue Utilization and Avg. Residence Times")
    plt.xlabel("Server Utilization")
    plt.ylabel("Average Residence Time")
    plt.plot(arrival_rates, utilization)
    plt.savefig("MM1_Util_and_Avg_Res_Times.pdf", bbox_inches="tight")


 ## Calculation of Confidence Intervals
    
    # Generate five samples of each arrival rate
    multi_repl = [[simulate(rate, 1.0, 1000) for i in range(5)] for rate in arrival_rates]

    # Calculate the average for each group of samples
    Y_bar = [(sum(x) / 5) for x in multi_repl]

    # Calculate the Standard Deviation of the samples
    s = [sqrt((sum([((x[ii] - Y_bar[i]) ** 2) for ii in range(5)]))/4) for i,x in enumerate(multi_repl)]

    # Calculate upper confidence limit
    ucl = [(Y_bar[i] + 2.776 * s[i] / sqrt(5)) for i in range(19)]

    # Calculate lower confidence limit
    lcl = [(Y_bar[i] - 2.776 * s[i] / sqrt(5)) for i in range(19)]

    # Calculate the utilization of 
    Y_bar_util = [Y_bar[i] * arrival_rates[i] for i in range(19)]  #  utilization of sample averages
    ucl_util = [ucl[i] * arrival_rates[i] for i in range(19)]#  utilization of upper 95% confidence limit
    lcl_util = [lcl[i] * arrival_rates[i] for i in range(19)]#  utilization of lower 95% confidence limit

    plt.figure()
    plt.title("M/M/1 Queue Confidence Intervals of Avg. Residence Time Estimate")
    plt.xlabel("Utilization")
    plt.ylabel("Average Residence Times")
    plt.plot(arrival_rates, ucl_util, color = "orange", label = "UCL")
    plt.plot(arrival_rates, lcl_util, color = "purple", label = "LCL")
    plt.plot(arrival_rates, Y_bar_util, color = "black", label = "AVG")
    plt.legend()
    plt.savefig("MM1_CI.pdf", bbox_inches = "tight")



#### MAIN CALL ####

if(__name__=="__main__"): main()
