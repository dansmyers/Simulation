# Confidence.py is a modified version of mm1 solution
# Intent is to solve the confidence intervals problem in sprint 4
# CMS 380
# Matthew Trautmann Fall 2020

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# Math imports
import math
from math import log
from random import random


#Calculates the variance of a list
def variance(x):
    """
    Calculate and return the variance of input list x
    """
    #Get the length
    n = len(x)
    
    #get the average
    mean = sum(x) / len(x)
    
    #Make a deviations list to store deviations
    deviations = []
    
    #Go thorugh list calculate deviations
    for i in x:
        deviation = (i - mean) ** 2
        deviations.append(deviation)
    
    #find variance
    variance = sum(deviations) / n
    
    return variance

# Calculate the standard_deviation using the variance   
def standard_deviation(x):
    """
    Calculate and return the standard deviation of input list x
    """
    standard_deviation = math.sqrt(variance(x))
    
    return standard_deviation
    

#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):

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
    # use rand_exp to generate n interarrival times with parameter arrival_rate
    interarrival_times = [0] * n
    for i in range(1, n):
        interarrival_times[i] = rand_exp(arrival_rate)
        
    
    # Generate service times
    # use rand_exp to generate n service times with parameter 1 / avg_service_time
    service_times = [0] * n
    for i in range(0, n):
        service_times[i] = rand_exp(1 / avg_service_time)
        
    # Calculate arrival times
    # use interarrival times to calculate a list of arrival times
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
        
        # calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        # calculate departure_times[i]
        departure_times[i] = enter_service_times[i] + service_times[i]
        
    # Calculate residence times
    # calculate list of residence times
    residence_times = [0] * n
    for i in range(0, n):
        residence_times[i] = departure_times[i] - arrival_times[i]
        
    # return average residence time
    average_residence_time = sum(residence_times) / len(residence_times)
    return average_residence_time

def main():

    n = 1000
    arrival_rate = .05
    avg_service_time = 1
    
    
    # Create a list to track utilization rates
    utilization_list = []
    # Create a list to track average residence times
    y_bar_list = []
    # Create a list to track the Upper Confidence interval
    ucl_list = []
    # Create a list to track the lower confidence interrval
    lcl_list = []
    
    # Iterate for each arrival rate
    while arrival_rate < 1:
        # Make a list for the 5 simulates
        replications = [0] * 5
        for i in range(0, 4):
            replications[i] = simulate(arrival_rate, avg_service_time, n)
        
        # Find the average of the simulations    
        y_bar = sum(replications) / len(replications)
        
        # Add average to list of averages
        y_bar_list.append(y_bar)
        
        # Calculate the standard deviation of the list
        s = standard_deviation(replications)
        
        # Calculate the upper confidence interval and add to list
        UCL = y_bar + ((2.776 * s) / math.sqrt(5))
        ucl_list.append(UCL)
        
        # Calculate lower confidence interval and add to list
        LCL = y_bar - ((2.776 * s) / math.sqrt(5))
        lcl_list.append(LCL)
        
        # Calculate utilization rate and store it
        utilization = arrival_rate * avg_service_time
        utilization_list.append(utilization)
        
        #Increase the arrival rate
        arrival_rate = arrival_rate + .05
        
     # Create a new figure
    plt.figure()

    # Create line plots for simulated data
    plt.plot(utilization_list, y_bar_list, label = "Average Residence Time")
    plt.plot(utilization_list, ucl_list, label = "Upper Confidence Interval")
    plt.plot(utilization_list, lcl_list, label = "Lower Confidence Interval")
    
    # Make a legend
    plt.legend()
    
    # Title and axis labels
    plt.title('Single Queue Simulation')
    plt.xlabel('Utilization Rate')
    plt.ylabel('Simulated Average residence times')

    # Save the figure to a file
    plt.savefig('confidence_interval.pdf', bbox_inches='tight')
    

    
    
# Call main() when this program runs
if __name__ == '__main__':
    main()
