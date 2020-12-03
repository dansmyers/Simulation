### Implementation of an M/M/1 queue using the discret-event advance strategy
#
# CMS 380

from math import log
from random import random
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# Priority queue operations
from heapq import heappush, heappop


def rand_exp(rate):
    
    """ Generate an exponential random variate
    
        input: rate, the parameter of the distribution
        returns: the exponential variate
    """
    
    return -log(random()) / rate
    

def simulate(arrival_rate, fastpass_rate):

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
    
    # Simulation data lists
    arrival_times_fastpass = []
    arrival_times_plebs = []
    enter_service_times_fastpass = []
    enter_service_times_plebs = []
    departure_times_fastpass = []
    departure_times_plebs = []

    # Initialize FEL as an empty list
    future_event_list = []
    
    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival')
    
    # Insert with a heap operation
    heappush(future_event_list, new_event)
    
    while len(future_event_list) > 0 and len(arrival_times_fastpass) + len(arrival_times_plebs) < max_num_arrivals:
        
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
            #check for fastpass and log in appropriate arrival list
            if random() < fastpass_rate:
                arrival_times_fastpass.append(time)
            else:
                arrival_times_plebs.append(time)
            
            # Increment queue size
            num_in_queue += 1
            
            # Generate next arrival
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, 'arrival')
            heappush(future_event_list, new_event)
            
            # If queue was empty, enter service and generate a future departure event
            if num_in_queue == 1:       
            # Log service time in appropriate service time list
                if len(arrival_times_fastpass) > len(enter_service_times_fastpass):
                    enter_service_times_fastpass.append(time)
                else:
                    enter_service_times_plebs.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure')
                heappush(future_event_list, new_event)
              
              
        # Departure
        elif event_type == 'departure':
            
            # Log departure time in appropriate departure list
            if len(enter_service_times_fastpass) > len(departure_times_fastpass):
                departure_times_fastpass.append(time)
            else:
                departure_times_plebs.append(time)
            
            # Decrement queue size
            num_in_queue -= 1
            
            # If there are more customers waiting, put the next one into service and generate a departure
            if num_in_queue > 0:
                
                # Log enter service time in appropriate service list
                if len(arrival_times_fastpass) > len(enter_service_times_fastpass):    
                    enter_service_times_fastpass.append(time)
                else:
                    enter_service_times_plebs.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure')
                heappush(future_event_list, new_event)
                
    
    ### Simulation is over
    #
    # Calculate statistics
    
    # Average residence time calculated for fastpass and non-fastpass holders
    residence_times_fastpass = [departure_times_fastpass[i] - arrival_times_fastpass[i] for i in range(len(departure_times_fastpass))]
    residence_times_plebs = [departure_times_plebs[i] - arrival_times_plebs[i] for i in range(len(departure_times_plebs))]
    average_residence_time_fastpass = sum(residence_times_fastpass) / len(residence_times_fastpass)
    average_residence_time_plebs = sum(residence_times_plebs) / len(residence_times_plebs)
    
    return [average_residence_time_fastpass, average_residence_time_plebs]
  
    


def main():
    
    # Sets up the graph and legend
    plt.figure()
    plt.xlabel('Percentage of Fastpasses')
    plt.ylabel('Average Residence Time')
    green_patches = mpatches.Patch(color = 'green', label = 'Fastpass Holders')
    red_patches = mpatches.Patch(color = 'red', label = 'Non-Fastpass Holders')
    
    # Initialized data lists
    xvalues = []
    fastpass_avg_residence = []
    plebs_avg_residence = []
    
    # Simulates queue at different fastpass rates
    for x in range (5,100,5):
        xvalues.append(x)
        simulation = simulate(0.95, x / 100.0)
        print(simulation)
        fastpass_avg_residence.append(simulation[0])
        plebs_avg_residence.append(simulation[1])
    
    # Plots the data
    plt.legend(handles = [green_patches, red_patches])
    plt.plot(xvalues, fastpass_avg_residence, color = 'green')
    plt.plot(xvalues, plebs_avg_residence, color = 'red')
    
    


if __name__ == '__main__':
    main()
