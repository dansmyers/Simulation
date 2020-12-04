# Fast Pass Simulation, Sprint 5
# CMS 380
# Matthew Trautmann Fall 2020

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# Math imports
from math import log
from random import random

# Heap imports for event list
from heapq import heappush, heappop, heapify


def rand_exp(mu):
	""" Generate an exponential random variate
    
        input: rate, the parameter of the distribution
        returns: the exponential variate
    """
	return -log(random()) / mu



#--- Is Fast Pass
#
# Inputs:
#    fast pass rate =  f
#
# Output: whether or not event is fast pass
def is_fast_pass(f):
    
	# Determine if high priority
    if random() < f:
        return 'fp'
        
    else:
        return 'r'



#--- Simulate the priority queue
#
# Inputs:
#    arrival_rate
#    % of high priority customers
#
# Output: the average residence time of customer in the system
def simulate(arrival_rate, f):

    # Stopping condition
    max_num_arrivals = 10000

    # Basic parameters
    service_rate = 1.0
    time = 0.0
    num_in_queue_high = 0
    num_in_queue_low = 0
    
    
    # Simulation data lists
    enter_service_times = []
    
    
    # Simulation data lists for fast pass averages
    fp_arrival_times = []
    fp_departure_times = []
    
    # Simulation data lists for regular customer averages
    r_arrival_times = []
    r_departure_times = []
    
    # Initialize FEL as an empty list
    future_event_list = []
    
    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival', is_fast_pass(f))
    
    # Push initial event onto heap
    heappush(future_event_list, new_event)
    
    
    while len(future_event_list) > 0 and len(fp_arrival_times) + len(r_arrival_times) < max_num_arrivals:
        
        # Pop the next event with a heap operation
        event = heappop(future_event_list)
        
        # Event attributes
        event_time = event[0]
        event_type = event[1]
        event_priority = event[2]
        
        
        # Advance simulated time
        time = event_time
        
        # Process events
        
        # Arrivals
        if event_type == 'arrival':
            
            # Check for fast pass, log arrival time
            if event_priority == "fp":
            	# Increment fast pass queue
                num_in_queue_high += 1
                
                # log time for fast pass arrival
                fp_arrival_times.append(time)
            
            # Arrival is regular 
            else:
            	# Increment regular queue
                num_in_queue_low += 1
                
                # log time for regular arrival
                r_arrival_times.append(time)
            
            
            # Generate next arrival
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, "arrival", is_fast_pass(f))
            heappush(future_event_list, new_event)
            
            
            # If event was high priortity
            if num_in_queue_high == 1 and num_in_queue_low == 0:
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure', "fp")
                heappush(future_event_list, new_event)
            
                
            # If high priortity queue was empty, enter service and generate a future departure event    
            elif num_in_queue_low == 1 and num_in_queue_high == 0:
                
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure', "r")
                heappush(future_event_list, new_event)
                
              
        # Departure
        elif event_type == 'departure':
            
            if event_priority == "fp":
                # Log departure
                fp_departure_times.append(time)
                
                # Decrement fast pass queue
                num_in_queue_high -= 1
                
            elif event_priority == "r":
                # log departure
                r_departure_times.append(time)
                
                # Decrement regular queue
                num_in_queue_low -= 1
            
            # Check if there are fast past departures first
            if num_in_queue_high > 0:
                
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure', "fp")
                heappush(future_event_list, new_event)
                
                
                
            
            # If priortity queue is empty and low priortity queue has
            elif num_in_queue_low > 0 and num_in_queue_high == 0:
                
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure', "r")
                heappush(future_event_list, new_event)
                    
                
      
    ### Simulation is over
    #
    # Calculate statistics
    
    # Regular Average residence time
    r_residence_times = [r_departure_times[i] - r_arrival_times[i] for i in range(len(r_departure_times))]
    
    r_average_residence_time = sum(r_residence_times) / len(r_residence_times)
    
    # Fast pass average residence time
    fp_residence_times = [fp_departure_times[i] - fp_arrival_times[i] for i in range(len(fp_departure_times))]
    
    fp_average_residence_time = sum(fp_residence_times) / len(fp_residence_times)
    
    
    return r_average_residence_time, fp_average_residence_time
    

#--- PLot function
#
# Inputs:
#    Utilization rate
#    name of plot
#
# Output: none, creates plot
def plot(u, name):
    
    fast_passes = []
    
    fp_sim_residence_avg = []
    r_sim_residence_avg = []
    
    for f in range(5, 95, 5):
        
        fast_passes.append(f)
        fp_sim_residence_times = []
        r_sim_residence_times = []
        
        # At each fraction of fast passes run 20 simulations and record the average
        
        for i in range(20):
            temp = simulate(u, f / 100)
        
            fp_sim_residence_times.append(temp[1])
            r_sim_residence_times.append(temp[0])
        
        
        fp_sim_residence_avg.append(sum(fp_sim_residence_times) / len(fp_sim_residence_times))
        r_sim_residence_avg.append(sum(r_sim_residence_times) / len(r_sim_residence_times))
        
        
    plt.figure()
    plt.title("Simulated Fast Pass")
    plt.xlabel("Percentage of Fast Passes")
    plt.ylabel("Average Residence Time")
    plt.plot(fast_passes, fp_sim_residence_avg, label="Fast Pass")
    plt.plot(fast_passes, r_sim_residence_avg, label="Regular")
    plt.legend()
    
    plt.savefig(name, bbox_inches="tight")
    
def main():
	plot(.5, "50.pdf")
	plot(.95, "95.pdf")
	

if __name__ == '__main__':
    main()
