from math import log
from random import random

from heapq import heappush, heappop, heapify

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt

# create the arrival time (random variable)
def rand_exp(mu):
	return -log(random()) / mu


# function to determine a fastpass rider or regular rider
def is_fast_pass(fraction_fast_pass):
	number = random()
	
	if number <= fraction_fast_pass:
		return "fast_pass"
	elif number > fraction_fast_pass:
		return "pleb"

# simulate the mm1 queue
def queueing_simulator(arrival_rate, fraction_fast_pass):
	
    """ Simulate the M/M/1 queue, discrete-event style
    
        input: arrival_rate  the system's arrival rate
        returns: the average simulated residence time
    """

    # Stopping condition
    max_num_arrivals = 100000

    # Basic parameters
    service_rate = 1.0
    time = 0.0
    
    num_in_queue = 0
    num_in_fast_pass_queue = 0
    
    # Simulation data lists
    arrival_times = []
    enter_service_times = []
    departure_times = []
    
    fast_pass_arrival_times = []
    fast_pass_departure_times = []
    
    # Initialize FEL as an empty list
    future_event_list = []
    
    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival', is_fast_pass(fraction_fast_pass))
    
    # Insert with a heap operation
    heappush(future_event_list, new_event)
    
    
    while len(future_event_list) > 0 and len(arrival_times) + len(fast_pass_arrival_times) < max_num_arrivals:
        
        # Pop the next event with a heap operation
        event = heappop(future_event_list)
        
        # Event attributes
        event_time = event[0]
        event_type = event[1]
        event_priority = event[2]
        
        #print(event)
        
        # Advance simulated time
        time = event_time
        
        ### Process events
        
        # Arrivals
        
        if event_type == 'arrival':
            
            # Log arrival time
            if event_priority == "fast_pass":
            	fast_pass_arrival_times.append(time)
            	num_in_fast_pass_queue += 1
            else:
            	arrival_times.append(time)
            	num_in_queue += 1
            
            # Generate next arrival
            
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, "arrival", is_fast_pass(fraction_fast_pass))
            
            heappush(future_event_list, new_event)
            
            # If queue was empty, enter service and generate a future departure event
            if num_in_fast_pass_queue == 1 and num_in_queue == 0:
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure', "fast_pass")
                
                heappush(future_event_list, new_event)
                
            elif num_in_queue == 1 and num_in_fast_pass_queue == 0:
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure', "pleb")
                
                heappush(future_event_list, new_event)
              
        # Departure
        elif event_type == 'departure':
            #print(num_in_fast_pass_queue , " ", num_in_queue)
            if num_in_fast_pass_queue > 0:
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                
                new_event = (time + service_time, 'departure', "fast_pass")
                
                heappush(future_event_list, new_event)
                
                # If there are more customers waiting, put the next one into service and generate a departure 
                fast_pass_departure_times.append(time)
                
	            # Decrement queue size
                num_in_fast_pass_queue -= 1
                
            elif num_in_queue > 0:
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                    
                new_event = (time + service_time, 'departure', "pleb")
                    
                heappush(future_event_list, new_event)
                    
                # If there are more customers waiting, put the next one into service and generate a departure 
                departure_times.append(time)
                
	            # Decrement queue size
                num_in_queue -= 1
                
                #print(num_in_queue, " num in the regular queue")
      
    ### Simulation is over
    #
    # Calculate statistics
    
    # Average residence time
    residence_times = [departure_times[i] - arrival_times[i] for i in range(len(departure_times))]
    
    fast_pass_residence_times = [fast_pass_departure_times[i] - fast_pass_arrival_times[i] for i in range(len(fast_pass_departure_times))]
    
    average_residence_time = sum(residence_times) / len(residence_times)
    
    fast_pass_average_residence_time = sum(fast_pass_residence_times) / len(fast_pass_residence_times)
    
    all_residence_times = [average_residence_time, fast_pass_average_residence_time]
    
    return all_residence_times
	
def main():
	
    """ Simulate for different utilization levels """
    
    x_values = []
    
    low_ult_pleb = []
    low_ult_fast = []
        
    high_ult_pleb = []
    high_ult_fast = []
    
    low_ult_pleb_avg = []
    low_ult_fast_avg = []
    
    high_ult_pleb_avg = []
    high_ult_fast_avg = []
    
    for u in range(5, 100, 5):
        
        x_values.append(u)
        
        # Run 20 trials at each utilization level and use the average of the simulated
        # values as the estimate of the residence time
        
        for i in range(20):
            low_residence_times = queueing_simulator(.5, u / 100)
            high_residence_times = queueing_simulator(.95, u / 100)
        
            low_ult_pleb.append(low_residence_times[0])
            low_ult_fast.append(low_residence_times[1])
        
            high_ult_pleb.append(high_residence_times[0])
            high_ult_fast.append(high_residence_times[1])
        
        low_ult_pleb_avg.append(sum(low_ult_pleb) / len(low_ult_pleb))
        low_ult_fast_avg.append(sum(low_ult_fast) / len(low_ult_fast))
        high_ult_pleb_avg.append(sum(high_ult_pleb) / len(high_ult_pleb))
        high_ult_fast_avg.append(sum(high_ult_fast) / len(high_ult_fast))
        
        # iterator = 0
        # print('%d\t%f' % (u, low_ult_pleb_avg[iterator]), " regular pleb low ulitization")
        # print('%d\t%f' % (u, low_ult_fast_avg[iterator]), " fast pass low ulitization ")
        # print('%d\t%f' % (u, high_ult_pleb_avg[iterator]), " pleb high ulitization")
        # print('%d\t%f' % (u, high_ult_fast_avg[iterator]), " fast pass high ulitization")
        # iterator += 1
    
    plt.figure()
    
    plt.title("Low Ulitization Fast-Pass Graph")
    plt.xlabel("Number of Fast Passes Dispersed")
    plt.ylabel("Average Residence Time")
    
    plt.plot(x_values, low_ult_pleb_avg, color="red", label="pleb")
    plt.plot(x_values, low_ult_fast_avg, label="fast_pass")
    
    plt.savefig("low_ulitization_graph.pdf", bbox_inches="tight")
    
    plt.figure()
    
    plt.title("High Ulitization Fast-Pass Graph")
    plt.xlabel("Number of Fast Passes Dispersed")
    plt.ylabel("Average Residence Time")
    
    plt.plot(x_values, high_ult_pleb_avg, color="red", label="pleb")
    plt.plot(x_values, high_ult_fast_avg, label="fast")
    
    plt.savefig("high_ulitization_graph.pdf", bbox_inches="tight")


if __name__ == '__main__':
    main()













































































