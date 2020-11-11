# Importing necessary library
from math import log
from math import sqrt
import matplotlib                   # Required setup for matplotlib
from random import random
import matplotlib 
matplotlib.use('Agg')
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
    for i in range(0,n):
        interarrival_times.append(rand_exp(arrival_rate))
    #print(interarrival_times)
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    service_times = []
    for i in range(0,n):
        service_times.append(rand_exp(1 / avg_service_time))
    #print(service_times)
    
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    arrival_times = [];
    for i in range(0,n):
        if i != 0:
            arrival_times.append(arrival_times[i - 1] + interarrival_times[i])
        else:
            arrival_times.append(interarrival_times[i])
    #print(arrival_times)
    
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
    
    # Loop over residence times
    for i in range(1, n):
        residence_times[i] = departure_times[i] - arrival_times[i]
    
    # TODO: return average residence time
    return sum(residence_times)/len(residence_times)

# Graph the MM1 Queue Average Residence Time to Utilization
def graph_MM1(utilization, avg_residence_times):
    plt.figure()
    plt.xlabel("Utilization")
    plt.ylabel("Average residence time")
    plt.plot(utilization, avg_residence_times)
    plt.savefig('Simulating MM1.pdf', bbox_inches='tight')

# Graph the Confidence Intervals Graph
def graph_CI(UCL, LCL, utilization, avg_residence_times):
    plt.figure()
    plt.xlabel("Utilization")
    plt.ylabel("Average residence time")
    plt.plot(utilization, avg_residence_times)
    plt.plot(utilization, UCL)
    plt.plot(utilization, LCL)
    plt.savefig('Confidence Intervals.pdf', bbox_inches='tight')
    
    

# 1st Part of the Problem
# Simulating M/M/1
def part_1():
    arrival_rate = [0] * 19                 # arrival rate has 19 numbers (0.05 to 0.95)
    for i in range(0,19):                   # loop through arrival rate
        arrival_rate[i] = (i + 1) * 0.05    # initialize arrival rate
    avg_service_time = 1.0                  # given avg_service_time
    n = 5000                                # given n
    
    avg_residence_times = []                # average residence times
    
    for i in range(0, len(arrival_rate)):   # loop through arrival 
                                            # residence time 'rt' is equal to simulation
                                            # then append to avg_residence_times
        rt = simulate(arrival_rate[i], avg_service_time, n)
        avg_residence_times.append(rt)
    
                                            # given definition of utilization
    utilization = arrival_rate
    
                                            # helper function to graph results
    graph_MM1(utilization, avg_residence_times)

# 2nd Part of the Problem
# Confidence Intervals
def part_2():
    arrival_rate = [0] * 19                 # arrival rate has 19 numbers (0.05 to 0.95)
    for i in range(0,19):                   # loop through arrival rate
        arrival_rate[i] = (i + 1) * 0.05    # initialize arrival rate
    avg_service_time = 1.0                  # given avg_service_time
    n = 1000                                # given n
    
    avg_residence_times = []                # average residence times
    
    UCL = []                                # list to store upper confidence limits
    LCL = []                                # list to store lower confidence limits
    
    for i in range(0, len(arrival_rate)):   # loop through arrival
                                            # residence time 'rt' is equal to simulation
                                            # then append to avg_residence_times
        results = []                        # results will store all results per arrival_rate
        for j in range (0, 5):
            rt = simulate(arrival_rate[i], avg_service_time, n)
            results.append(rt)
        
        Y_bar = sum(results)/len(results)   # Take the y_bar
        avg_residence_times.append(Y_bar)   # Append Y_bar into avg_residence_times
       
        m = sum(results) / len(results)     # Take the Mean
        sq = [(i-m)**2 for i in results]    # Uses list comprehension to get distance from mean
        v = sum(sq) / len(sq)               # Find the Variance
        s = sqrt(v)                         # Find the Standatd Deviation
        
        UCL.append(Y_bar + 2.776 * s / sqrt(5))     # Calculate and append UCL
        LCL.append(Y_bar - 2.776 * s / sqrt(5))     # Calculate and append LCL
        
                                            # given definition of utilization
    utilization = arrival_rate
    
    graph_CI(UCL, LCL, utilization, avg_residence_times)

def main():
    part_1()
    part_2()

if __name__ == '__main__':
    main()