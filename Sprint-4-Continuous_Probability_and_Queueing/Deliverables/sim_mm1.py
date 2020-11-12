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
    interarrival_times = []
    for i in range(n):
        interarrival_times.append(rand_exp(arrival_rate))
    
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    service_time = []
    for j in range(n):
        service_time.append(rand_exp(1/avg_service_time))
    
    
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    
    arrival_times = []
    arrival_times.append(interarrival_times[0])
    for k in range(1, n):
        arrival_times.append(interarrival_times[k] + arrival_times[k-1])
    
    
    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_time[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i-1])
        
        
        # TODO: calculate departure_times[i]
        departure_times[i] = enter_service_times[i] + service_time[i]
    residence_times = [0] * n
        
    # Calculate residence times
    # TODO: calculate list of residence times
    for i in range(n):
        residence_times[i] = departure_times[i] - arrival_times[i]
    
    
    # TODO: return average residence time
    return sum(residence_times)/len(residence_times)

def plotpts(vals1, vals2):
    plt.figure()
    plt.plot(vals1,vals2)
    plt.savefig("util_demo.pdf", bbox_inches='tight')

def plotpts2(vals1, vals2, vals3):
    plt.figure()
    x = []
    start = .05
    for i in range(0,19):
        x.append(start)
        start += .05
    plt.plot(x, vals1, label= "UCL")
    plt.plot(x, vals2, label = "LCL")
    plt.plot(x, vals3, label = "Average Residence Time")
    plt.savefig("Average_res_times.pdf", bbox_inches='tight')
def main():
    arrival_rate = .05
    util = []
    sim_resident_times = []
    
    while arrival_rate <= .90:
        sim_resident_times.append(simulate(arrival_rate , 1, 5000))
        util.append(arrival_rate)
        arrival_rate += .05
   
    plotpts(util, sim_resident_times)
    
    arrival_rate = .05
    value = 0 
    
    total_res = 0 
    nums = [0] * 5
    ucl_vals = [0] * 19
    lcl_vals = [0] * 19
    art_vals = [0] * 19
    level = 0
    
    while arrival_rate <= 1.0:
        res= simulate(arrival_rate,1,1000)
        if value % 5 == 0 and value != 0:
            nums[value % 5] = res
            y_bar = total_res / 5
            art_vals[level] = y_bar
            UCL = y_bar +2.776 * stdev(nums, y_bar)/sqrt(5)
            ucl_vals[level] = UCL 
            LCL = y_bar - 2.776 * stdev(nums, y_bar)/sqrt(5)
            lcl_vals[level] = LCL
            
        
            print(round(arrival_rate, 3), " UCL is", round(UCL, 3), "LCL is", round(LCL,3))
            arrival_rate +=.05
            total_res = 0
            level +=1
            
        else:
            nums[value % 5] = res
            total_res += res 
        value += 1 
        
    plotpts2(ucl_vals,lcl_vals, art_vals)   


   
if __name__ == '__main__':
    main()











