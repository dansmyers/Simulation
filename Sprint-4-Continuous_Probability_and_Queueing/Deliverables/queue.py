""" 
Program that implements the single-server  queue simulation algorithm.

CMS 380 -- Fall 2020
Maria Morales
"""
from math import log 
from math import sqrt
from random import random
import numpy

# Set up matplotlib and configure it to be used on Mimir 
import matplotlib
matplotlib.use('Agg') # Required because we are using a remote environment
from matplotlib import pyplot  as plt 


def rand_exp(mu):
    """
    Function to generate an exponential random variate
    input: mu, the parameter of the exponential distribution
    output: a value x drawn from the exponential distribution with rate mu
    """
    #Generate and return an exponential RV
    return -log(random()) / mu
    
def simulate(arrival_rate, avg_service_time, n):
    """
    Function to simulate the M/M/1 queue
    inputs:
        arrival_rate
        avg_service_time
        n: number of simulated customers
    output: the average residence time of customer in the queue
    """
    # Generate interarrival times, the average time between 2 arrivals
    interarrival_times = []
    
    # Use rand_exp to generate n interarrival times with parameter arrival_rate
    for i in range(n):
        interarrival_times.append(rand_exp(arrival_rate))
    
    # Generate service times
    service_times = []
    # Use rand_exp to generate n service times with parameter 1 / avg_service_time
    for i in  range(n):
        service_times.append(rand_exp(1/avg_service_time))
    
    # Calculate arrival times
    arrival_times = [0] * n
    # Use interarrival times to calculate a list of arrival times
    arrival_times[0] = interarrival_times[0]
 
    for i in range(1, n):
        arrival_times[i] = arrival_times[i - 1] + interarrival_times[i]
    
    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    residence_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # Calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        # Calculate departure_times[i]
        departure_times[i] = enter_service_times[i] + service_times[i]
    
    # Calculate residence times
    for i in range(n):
        residence_times[i] = departure_times[i] - arrival_times[i]
    
    # Return average residence time
    r_sum = 0
    for i in range(0, len(residence_times)):
        r_sum += residence_times[i]
    
    return r_sum/n
    
def replicate_5_times(arrival_rate, avg_service_time, n):
    """
    Function to simulate running M/M/1 queue 5 times
    inputs:
        arrival_rate
        avg_service_time
        n: number of simulated customers
    output: a list of the average residence time of customer in the queue for each replication
    """
    rep_num =  5
    r_times =  []
    
    for i in range(rep_num):
        r_times.append(simulate(arrival_rate, avg_service_time, n))
    
    return r_times
    
    
def calculate_Y_bar(residence_times_list):
    """
    Function to calculate the average of a list of average residence times.
    inputs: a list of residence times
    output: mean of the list
    """
    total_sum = 0 
    for i in range(0, len(residence_times_list)):
        total_sum += residence_times_list[i]
    
    return total_sum / len(residence_times_list)
    
    
def main():

    avg_service_time = 1.0 
    n = 1000
    arrival_rate = .05
    
    mean_residence_times = []
    
    utilization = []
    Y_bar =  0
    s = 0
    replications = []
    
    # Upper confidence limits
    UCL = []
    # Lower confidence limits
    LCL = []
    
    
    while arrival_rate <= .95:
        
        # Run five replications for each utilization value
        replications = replicate_5_times(arrival_rate, avg_service_time, n)
        
        # Calculate the average of the five replications as your best estimate of the true mean residence time for that utilization level
        Y_bar = calculate_Y_bar(replications)
        mean_residence_times.append(Y_bar)
        
        #Calculate the standard deviation of the five residence time estimates
        s = numpy.std(replications)
        
        # Calculate the upper and lower 95% confidence limits for your simulated estimates.
        UCL.append((Y_bar + 2.776 * s / sqrt(5)))
        LCL.append((Y_bar - 2.776 * s / sqrt(5)))
        
        utilization.append(arrival_rate * avg_service_time)
        
        arrival_rate += 0.05
    

    utilization.sort()
    
    # Create a new figure
    plt.figure()
    # Use the upper confidence limits for the errorbar parameter
    yerr = UCL
    
    # Plot the averagee residence  time  estimates  and the upper and  lower confidence levels
    plt.errorbar(utilization, mean_residence_times, yerr=yerr)
    

    plt.title('Utilization and mean residence times for MM1 queue')
    plt.xlabel('Utilization')
    plt.ylabel('Average residence time')
    
    plt.savefig('Utilization_times.pdf', bbox_inches = 'tight')

if __name__ == '__main__':
    main()
        
    