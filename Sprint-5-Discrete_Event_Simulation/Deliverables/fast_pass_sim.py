### Simulator for a two-class priority queueing system
### to model a fast past system
### Randall Lee Springer
### CMS 380
### Sprint 5

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
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
    
def graph(u, name):
    
    """ Generate the graph
    
        input: utilization, name of graph
        returns: None
    """
    
    # List to hold avgerage residence times
    sim_r_avg = []
    
    # for loop to run thru the different % of fast passes
    for f in range(0, 96, 1):
        
        # List to hold simulated residence times
        sim_residence_times = []
        
        # Run 20 trials at each f
        for trial in range(20):
            sim_residence_times.append(simulate(u, (f / 100)))
        
        # Append average residence time
        sim_r_avg.append(sum(sim_residence_times) / len(sim_residence_times))
        
        # Display residence times per f
        print('%d\t%f' % (f, (sum(sim_residence_times) / len(sim_residence_times))))
        
    # Create list to hold fast pass %
    fast_pass = [(i / 100) for i in range(0, 96, 1)]
    
    # Plot Graph
    plt.figure()
    plt.title("Fast Pass + Simulation")
    plt.xlabel("% Of Fast Passes Given Out")
    plt.ylabel("Average Residence Time")
    plt.plot(fast_pass, sim_r_avg)
    plt.savefig(name, bbox_inches="tight")   
    
    
def simulate(arrival_rate, f):
    
    """ Simulate the high priority / low priority system
    
        input: arrival_rate, and % of high priority
        returns: the average simulated residence time
    """
    
    # Stopping condition
    max_num_arrivals = 50000
    
    # Basic parameters
    service_rate = 1.0
    time = 0.0
    num_in_queue_low = 0.0
    num_in_queue_high = 0.0
    
    # Simulation data lists
    arrival_times = []
    enter_service_times = []
    departure_times = []
    
    # Initialize FEL as en empty list
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
            
            # Check to see if arrival is high or low queue
            # and increment the correct queue
            if random() < f:
                num_in_queue_high += 1
            else:
                num_in_queue_low += 1
            
            # Generate next arrival
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, 'arrival')
            heappush(future_event_list, new_event)
            
            # If queue was empty, enter service and generate a future departure event
            if num_in_queue_high == 1:
                
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure')
                heappush(future_event_list, new_event)
                
            elif num_in_queue_low == 1:
                
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure')
                heappush(future_event_list, new_event)
                
                
        # Departure
        elif event_type == 'departure':
            
            # If there are customers in high queue
            if num_in_queue_high > 0:
                
                # Log departure time
                departure_times.append(time)
                
                # Decrement queue size
                num_in_queue_high -= 1
                
                # If there are more customers waiting, put the next one into
                # service and generate a departure
                if num_in_queue_high > 0:
                    
                    # Log enter service time
                    enter_service_times.append(time)
                    
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'departure')
                    heappush(future_event_list, new_event)
                    
            # If there are customers in low queue
            elif num_in_queue_low > 0:
                
                # Log departure time
                departure_times.append(time)
                
                # Decrement queue size
                num_in_queue_low -= 1
                
                # If there are more customers waiting, put the next one into
                # service and generate a departure
                if num_in_queue_low > 0:
                    
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
    
    # Create 2 different graphs using different utilization
    graph(.5, "Fast_Pass_50.pdf")
    graph(.95, "Fast_Pass_95.pdf")


if __name__ == '__main__':
    main()
