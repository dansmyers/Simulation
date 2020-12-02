"""
Hiroki Sato 
11/10/20

Deliverable problems: Simulating M/M/1 & Confidence Intervals

Simulation of a Single Server Queue depending on the rate of arrival rate. 


"""


# Importing necessary library
from math import log
from math import sqrt
from random import random
import matplotlib 
matplotlib.use('Agg')
from matplotlib import pyplot as plt


# Helper functions
def sample_std(l, mean):
    values = list()
    for x in l:
        value = (x - mean)**2
        values.append(value)
    
    s = sqrt(sum(values) / (len(l) - 1))
    return s


# we want to plot the residence time
# with utilization on x axis and simulated average residence time on y axis
# Input: the simulated average residence times, 
def plot_main(utilization,residence_times):
    
    plt.figure()
    plt.title('Simulation of M/M/1')
    plt.xlabel("Utilization")
    plt.ylabel("Average residence time")
    plt.xlim(0,1)
    plt.plot(utilization, residence_times)
    plt.savefig('Exponential_Queuing.pdf', bbox_inches='tight')


# plot three different lines average residence time, upper confidence interval, lower confidence interval

def plot_confidence_intervals(utilization, residence_times, UCI, LCI):
    
    plt.figure()
    plt.title('Confidence Interval of M/M/1')
    plt.xlabel("Utilization")
    plt.ylabel("Average residence time")
    plt.xlim(0,1)
    plt.plot(utilization, residence_times,color='green')
    plt.plot(utilization, UCI,color='red')
    plt.plot(utilization,LCI, color='blue')
    plt.savefig('Confidence_intervals.pdf', bbox_inches='tight')



#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu

def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    #
    # Look at the inverse CDF examples ln(x)/ lambda
    numerator = -log(random())
    return numerator/mu

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
    interarrivals = list()
    for i in range(0,n):
        interarrivals.append(rand_exp(arrival_rate))
    # print("the interarrivals")
    # print(interarrivals[0:5])

    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    service_times = list()
    for i in range(0,n):
        service_times.append(rand_exp(1 / avg_service_time))
    # print("service_times")
    # print(service_times[0:5])

    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    arrival_times = list()
    for x in range(0, n):
        if x == 0:
            arrival_times.append(interarrivals[x])
        else:
            arr_time = arrival_times[x - 1] + interarrivals[x]
            arrival_times.append(arr_time)
    # print("arrival_times")        # debugging 
    # print(arrival_times[0:5])     # debugging

    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    residence_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[i]
    residence_times[0] = departure_times[0] - arrival_times[0]              # to avoid confusion, I am calculating the residence times for each customer as we 
                                                                            # iterate through instead of calculating enter_service_times and departure_times in first loop and doing additional loop
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        # TODO: calculate departure_times[i]
        departure_times[i] = enter_service_times[i] + service_times[i]
        residence_times[i] = departure_times[i] - arrival_times[i]
    
    # Calculate residence times
    # TODO: calculate list of residence times
    # TODO: return average residence time
    
    return sum(residence_times)/len(residence_times)
    


def main():
    
    avg_service_time = 1.0
    arrival_rates = list()
    arrival_rate = 0.05
    avg_residence_times = list()
    n = 5000
    for x in range(0,19):
        arrival_rates.append(arrival_rate)
        arrival_rate = arrival_rate + 0.05
    
    
    for i in arrival_rates:
        residence_time = simulate(i,avg_service_time,n)
        avg_residence_times.append(residence_time)
        
    avg_residence_times.sort()
    plot_main(arrival_rates, avg_residence_times)


# the function for the last question
# replicate the 1000-trial simulation 5 times to get the average of average,
# and plot the upper confidence interval and lower confidence interval
def replication():
    # we run 5 replication of the simulation with n = 1000
    avg_service_time = 1.0
    arrival_rates = list()
    arrival_rate = 0.05
    n = 1000
    
    # we need three list for true mean, upper confidence interval and lower confidence interval
    true_means = list()
    UCI = list()
    LCI = list()
    
    # creating a list of arrival_rate 
    for x in range(0,19):
        arrival_rates.append(arrival_rate)
        arrival_rate = arrival_rate + 0.05
    
    # for each utilization, we do 5 replication
    for a in arrival_rates:
        avg_residence_times = list()
        for rep in range(0, 5):
            residence_time = simulate(a,avg_service_time,n)
            avg_residence_times.append(residence_time)
        
        # print(avg_residence_times)    debugging
        # get the average of the 5 residence estimates
        Y_bar = sum(avg_residence_times) / 5
        
        # print(Y_bar)  debugging
        true_means.append(Y_bar)
        
        # get the standard deviation of 5 residence estimates
        s = sample_std(avg_residence_times, Y_bar)
        # print(s)      debugging 
        
        # calculate the upper confidence interval and lower confidence interval
        upper_confidence = Y_bar + 2.776 * s / sqrt(5)
        lower_confidence = Y_bar - 2.776 * s / sqrt(5)
        UCI.append(upper_confidence)
        LCI.append(lower_confidence)
    
    # because average service time is fixed at 1.0 by the utilization law, utilization is the arrival rates sort
    plot_confidence_intervals(arrival_rates, true_means, UCI, LCI)

        
        
        
if __name__ == '__main__':
     main()
     replication()
     
