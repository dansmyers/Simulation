"""
Alejandra De Osma 
CMS_380 Sprint 4 

M/M/1 PROGRAM:
This program will simulate a M/M/1 queue. 

"""

#   IMPORTS

import matplotlib 
matplotlib.use('Agg')
from matplotlib import pyplot as plt 

from random import random
import math 
from math import log 

#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    # Get random value from PRNG
    # Use formula = (-ln(random))/mu 
    return -log(random())/mu


#--- Simulate the M/M/1 queue
#
# Inputs:
#    arrival_rate
#    avg_service_time
#    n: number of simulated customers
#
# Output: the average residence time of customer in the queue
"""
Simulation:

"""
def simulate(arrival_rate, avg_service_time, n):

    # Generate interarrival times
    # TODO: use rand_exp to generate n interarrival times with parameter arrival_rate
    # Initializing interarrival_times: 

    
    interarrival_times = [0] * n
    
    # Looping through range n
    # Calling thw rand_exp using the arrival rate 
    # storing the values in the interarrival_times list
    
    for i in range(n):
        interarrival_times[i]= rand_exp(arrival_rate)
        
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    # Initializing service times 
    
    service_times = [0] * n
    
    # using the same proccess to store values in service_times list 
    
    for i in range(n):
        service_times[i]= rand_exp((1 / avg_service_time))
        
        
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times   
    # Initializing arrival_times list 
    
    arrival_times = [0] * n 
    
    # Using loop to store values in arraival times list
    for i in range(n):
        
        # conditional tests to see if i is equal to 0 
        if(i == 0 ):
            
            #if so, set the first index to interarrival_times also at 0 
             arrival_times[0] = 0 + interarrival_times[i]
             
        else:
            # Else locte the previous value 
            # And added to the interarrival_times at the current index 
      
            arrival_times[i] = arrival_times[i - 1] + interarrival_times[i]
        
    
    # Sorting the arrrival times list
    arrival_times.sort()
    
    # Initialize other lists: 
    departure_times = [0] * n
    enter_service_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    
    # set departures times at index 0 equal to the fist enter service time + service_times
    departure_times[0] = enter_service_times[0] + service_times[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i],departure_times[i - 1])
        
        # TODO: calculate departure_times[i]
        departure_times[i] = enter_service_times[i] + service_times[i]
        
    # Calculate residence times
    # TODO: calculate list of residence times
    residence_times = [0] * n 
    
    for i in range(n):
        residence_times[i] = departure_times[i] - arrival_times[i]
    
    # TODO: return average residence time
    
    return (sum(residence_times)/ n)

"""
Standard Deviation:

"""
    
def standard_d (data):
    
    count = 0 
    # Find lenght of the list 
    # set temporary value equal to the size of the list 
    length = len(data)
    
    # finding mean of the list:
    
    mean = (sum(data)/length)
    
    # calculating the variance 
   
    # using a loop to calculate the sumation before deviding it by n 
    for i in data:
        count+= (i - mean) ** 2
    
    # returning the sum of (x - mean)^2 / n 
    return math.sqrt(count/length)
    
"""
MAIN : 
    
"""

def main():
    # initializing values : 
    
    SIMULATIONS = 19
    arrival_rate = .05
    avg_service_time = 1.0
    n = 1000
    
    # rep is the number of replications:
    REP = 5 
    
    # initializing lists : 
    
    utilizations = [0] * SIMULATIONS
    Y_BAR = [0] * SIMULATIONS
        
        
    UCL = [0] * SIMULATIONS
    LCL = [0] * SIMULATIONS
    
    # Loop compleating all the needed simulations     
    for trial in range(SIMULATIONS):
        residence_times = [0] * REP
         
        # Loop compleating all the needed REPLICATION: 
        for replication in range(REP):
            
            #sore the residence time at each replication
            residence_times[replication] = simulate(arrival_rate, avg_service_time, n)
               
        Y_BAR[trial] = (sum(residence_times)/REP)
            
              # Modify and update values of previously initialized values
            
        utilizations[trial] = arrival_rate * avg_service_time
            
        s = standard_d(residence_times)
          
        UCL[trial] = Y_BAR[trial] + ((2.776 * s) / math.sqrt(5))
        LCL[trial] = Y_BAR[trial] - ((2.776 * s) / math.sqrt(5))
            
        arrival_rate = arrival_rate + .05
        
    # Ploting figure 
    # Using a errorbar plot 
     
    plt.figure()
    plt.subplots()
    plt.errorbar(utilizations, Y_BAR, yerr= UCL)
    plt.title("Utilization vs Residence Times M/M/1 Queue")
    plt.xlabel("Utilization")
    plt.ylabel(" Average Residence Time")
    plt.savefig("MM1_Queue.pdf",bbox_inches = 'tight')
        
# Calling main to execute: 

if __name__ == '__main__':
    main()
            
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    