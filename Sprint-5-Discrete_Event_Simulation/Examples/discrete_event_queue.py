### Implementation of an M/M/2 queue using the discret-event advance strategy
#
# CMS 380

from math import log
from random import random

# Priority queue operations
from heapq import heappush, heappop, heapify


def rand_exp(rate):
    
    """ Generate an exponential random variate
    
        input: rate, the parameter of the distribution
        returns: the exponential variate
    """
    
    return -log(random()) / rate
    

def simulate(arrival_rate):

    """ Simulate the M/M/1 queue, discrete-event style
    
        input: arrival_rate  the system's arrival rate
        returns: the average simulated residence time
    """

    # Stopping condition
    max_num_arrivals = 50000

    # Basic parameters
    service_rate = 1.0
    time = 0.0
    num_in_queue = 0
    num_in_priority = 0
    
    # Simulation data lists
    arrival_times = []
    enter_service_times = []
    departure_times = []

    # Initialize FEL as an empty list
    future_event_list = []
    
    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival')
    
    # Insert with a heap operation
    heappush(future_event_list, new_event)
    
    while len(future_event_list) > 0 and len(arrival_times) < max_num_arrivals:
        
        # Pop the next event with a heap operation
        event = heappop(future_event_list)
        
        # Event attributes
        event_time = event[0]
        event_type = event[1]
        
        # Advance simulated time
        time = event_time
        
        ### Process events
        
        # Arrivals
        if event_type == 'arrival':
            
            # Log arrival time
            arrival_times.append(time)
            
            # Increment queue size
            num_in_queue += 1
            
            # Generate next arrival
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, 'arrival')
            heappush(future_event_list, new_event)
            
            # If queue was empty, enter service and generate a future departure event
            if num_in_queue == 1:
                
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure')
                heappush(future_event_list, new_event)
              
              
        # Departure
        elif event_type == 'departure':
            
            # Log departure time
            departure_times.append(time)
            
            # Decrement queue size
            num_in_queue -= 1
            
            # If there are more customers waiting, put the next one into service and generate a departure
            if num_in_queue > 0:
                
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure')
                heappush(future_event_list, new_event)
                
    
    ### Simulation is over
    #
    # Calculate statistics
    
    # Average residence time
    residence_times = [departure_times[i] - arrival_times[i] for i in range(len(departure_times))]
    average_residence_time = sum(residence_times) / len(residence_times)
    
    return average_residence_time
    


def main():
    
    """ Simulate for different utilization levels """
    
    for u in range(50, 100, 5):
        
        # Run 20 trials at each utilization level and use the average of the simulated
        # values as the estimate of the residence time
        
        sim_residence_times = []
        
        for trial in range(20):
            sim_residence_times.append(simulate(u / 100.0))
        
        sim_r_avg = sum(sim_residence_times) / len(sim_residence_times)
        
        print('%d\t%f' % (u, sim_r_avg))
        


if __name__ == '__main__':
    main()
