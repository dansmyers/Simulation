"""

Objective: to simulate the Fast Pass system using discrete event simulation

"""
###############  Necessary libraries #############################################################################################################
##################################################################################################################################################

from math import log
from random import random
from heapq import heappush, heappop, heapify
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


##################################################################################################################################################
###############  exponential random value function  ##############################################################################################

def expo_rand(rate):
    
    return -log(random())/ rate
    

##################################################################################################################################################
###############  Plot function  ##################################################################################################################

def plot(FastPass_frac, avg_res_times_high, avg_res_times_low):
   
    fig, axis = plt.subplots()
    axis.plot(FastPass_frac, avg_res_times_high,color='red',label='FastPass')
    axis.plot(FastPass_frac, avg_res_times_low,color='blue',label='Non-FastPass')
    axis.set_xlabel('FastPass Fraction')
    axis.set_ylabel('Average Residence Time')
    axis.set_title('Average Residence time for give fraction of Fast Passes\n.50 utilization rate')
    axis.legend()
    fig.savefig('FastPass_Resident_Time_.50.pdf', bbox_inches='tight')
    
    





##################################################################################################################################################
############### Simulate function ################################################################################################################
"""
    Simulate the priority queue
        1. Started with just the single no-priority queue and its average_residence_time was about 2 which is very close to the example. 
        2. Moving on to the priority queue implementation
            a. things to be careful, we want to know the average residence time of both high priority customer and low priority customer
               so we need few more things such as num_in_queue_low and num_in_queue_high to distinguish the number of customers in the system by the priority
            b. we also need to differentiate the type of arrivals and departures. 
    
    input: the arrival_rate and f 
    output: Averate residence time 
    
    
    *** Importatnt insight
        the service time is fixed and known as 1.00 which means we have a deterministic service time so 
        the residual service time is .5
    
"""

def simulate(arrival_rate, f):
    
    # stopping condition
    max_time = 100000
    
    # Basic parameters
    time = 0.0
    average_service_time = 1.0
    
    num_in_queue_low = 0
    num_in_queue_high = 0       # because this is a priority queue, we have two num_in_queue variables to keep track of number of customers


    # lists to keep track of simulation data
    arrival_times_low = list()
    arrival_times_high = list()
    enter_service_times = list()
    departure_times_low = list()
    departure_times_high = list()
    
    # initializing the FEL
    future_event_list = list()
    
    # make the first arrival event 
    # BECASUSE this is a priority queue we would create condition to 
    # have two cases one for high priority arrival and the otehr for the low priority arrival
    
    
    if random() < f:

        intervarrival_time = expo_rand(arrival_rate)
        new_event = (time + intervarrival_time,'arrival','high')

    else: 

        intervarrival_time = expo_rand(arrival_rate)
        new_event = (time + intervarrival_time, 'arrival', 'low')


    # Insert the first arrival to the future_event_list
    heappush(future_event_list,new_event)
    
    # while len(future_event_list) > 0 and time < max_time:
    while len(future_event_list) > 0 and time < max_time:
        
        # pop the event in the future_event_list to carry out the event
        event = heappop(future_event_list)
        
        # this would return a python tuple so 
        event_time = event[0]
        event_type = event[1]
        event_priority = event[2]
        
        # advance the time
        time = event_time


        # we are going to process the events 
        
        # in the situation of arrival
        if event_type == 'arrival':
            
            # update the arrival_times
            # we want to know if that is a higher priority customer's arrival or not 
            # and we will determine that using a random and threshold f
            
            if event_priority == 'high':

                num_in_queue_high += 1
                arrival_times_high.append(time)
                
            if event_priority == 'low':
                
                num_in_queue_low += 1
                arrival_times_low.append(time)


            # generate another arrival, push it to the future_event_list
            intervarrival_time = expo_rand(arrival_rate)
            
            if random() < f:

                new_event = (time + intervarrival_time,'arrival','high')
                heappush(future_event_list,new_event)

            else:

                new_event = (time + intervarrival_time,'arrival','low')
                heappush(future_event_list,new_event)

            # when the number of customer in queue became just 1, depending on the condition 
            # we will create the departure event of corresponding priority

            """ Condition 1: the number of queue in the high priority just became 1. """
            if num_in_queue_high == 1 and num_in_queue_low == 0:
                
                # high priority customer can immediately enter service only when we do not have any customer currently in service
                # so if we did have a customer in service

                enter_service_times.append(time)
                service_time = expo_rand(average_service_time)
                new_event = (time + service_time, 'departure','high')
                heappush(future_event_list,new_event)


            """ Condition 2: the low priority customer can go into service without waiting only when there are no waiting high priority customer in line """ 
            
            if num_in_queue_low == 1 and num_in_queue_high == 0:


                enter_service_times.append(time)
                service_time = expo_rand(average_service_time)
                new_event = (time + service_time, 'departure','low')
                heappush(future_event_list,new_event)

                
        # Departure
        elif event_type == 'departure':


            # Demonstrating the customer leaving the system.
            if event_priority == 'high':

                departure_times_high.append(time)
                num_in_queue_high -= 1

            elif event_priority == 'low':

                departure_times_low.append(time)
                num_in_queue_low -= 1

            
            # if there are more high priority customers waiting, put them in the service
            if num_in_queue_high > 0:


                enter_service_times.append(time)
                service_time = expo_rand(average_service_time)
                new_event = (time + service_time, 'departure', 'high')
                heappush(future_event_list,new_event)


            # low priority customer can only go into the service when there are no high priority customers
            elif num_in_queue_low > 0 and num_in_queue_high == 0:

                # print('creating a low priority customer departure')
                enter_service_times.append(time)
                service_time = expo_rand(average_service_time)
                new_event = (time + service_time, 'departure','low')
                heappush(future_event_list,new_event)
            
    
    
    
    
    residence_times_high = [departure_times_high[i] - arrival_times_high[i] for i in range(len(departure_times_high))]
    
    residence_times_low = [departure_times_low[i] - arrival_times_low[i] for i in range(len(departure_times_low))]
   
    avg_res_high_priority = sum(residence_times_high) / len(residence_times_high)
    avg_res_time_low = sum(residence_times_low) / len(residence_times_low)


    return ( avg_res_high_priority, avg_res_time_low )

#######################################################################################################################################################
###############  Replicate function  ##################################################################################################################
# Input: the level of utilization
# Objective: to run 20 replication of simulation, and get the average of the average residence time for both FastPass and Non-FastPass customers.
#            and plot the data. 


def replicate(utilization):
    
    """ Simulate for different fraction of FastPasses """
    
    sim_r_avg_high = []
    sim_r_avg_low = []
    FastPass_frac = [x / 100.00 for x in range (10,100,10)]


    for f in FastPass_frac:
        
        sim_residence_time_high = []
        sim_residence_time_low = []
        
        for trial in range(20):
            
            residence_times = simulate( utilization , f)
            sim_residence_time_high.append(residence_times[0])
            sim_residence_time_low.append(residence_times[1])
            
        sim_rt_avg_high = sum(sim_residence_time_high) / len(sim_residence_time_high)
        sim_rt_avg_low = sum(sim_residence_time_low) / len(sim_residence_time_low)
        
        sim_r_avg_high.append(sim_rt_avg_high)
        sim_r_avg_low.append(sim_rt_avg_low)
        
    # printing out each average residence times for debugging purpose
    print(sim_r_avg_high)        
    print(sim_r_avg_low)

    # plot the data we've collected
    plot(FastPass_frac, sim_r_avg_high, sim_r_avg_low)
    



if __name__ == '__main__':
    replicate(.50)


