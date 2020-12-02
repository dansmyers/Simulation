from math import log
from random import random

from heapq import heappush, heappop, heapify


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
    max_num_arrivals = 10

    # Basic parameters
    service_rate = 1.0
    time = 0.0
    
    num_in_queue = 0
    num_in_fast_pass_queue = 0
    
    # Simulation data lists
    arrival_times = []
    enter_service_times = []
    departure_times = []

    # Initialize FEL as an empty list
    future_event_list = []
    future_fastpass_event_list = []
    
    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival', is_fast_pass(fraction_fast_pass))
    
    # Insert with a heap operation
    if new_event[2] == "fast_pass":
    	heappush(future_fastpass_event_list, new_event)
    else:
    	heappush(future_event_list, new_event)
    
    while (len(future_event_list) > 0 or len(future_fastpass_event_list) > 0) and len(arrival_times) < max_num_arrivals:
        
        # Pop the next event with a heap operation
        if(len(future_fastpass_event_list) >= 1):
        	event = heappop(future_fastpass_event_list)
        else:
        	event = heappop(future_event_list)
        	
        #print(event)
        
        # Event attributes
        event_time = event[0]
        event_type = event[1]
        event_priority = event[2]
        
        # Advance simulated time
        time = event_time
        
        ### Process events
        
        # Arrivals
        if event_type == 'arrival':
            # Log arrival time
            arrival_times.append(time)
            
            # Increment queue size
            if event_priority == "fast_pass":
            	num_in_fast_pass_queue += 1
            else:
            	num_in_queue += 1
            
            # Generate next arrival
            
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, 'arrival', is_fast_pass(fraction_fast_pass))
            
            if new_event[2] == "fast_pass":
            	heappush(future_fastpass_event_list, new_event)
            	#print("push high priority arrival")
            else:
            	heappush(future_event_list, new_event)
            	#print("push low priority arrival")
            
            # If queue was empty, enter service and generate a future departure event
            if num_in_queue == 1 and num_in_fast_pass_queue == 0:
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure', "pleb")
                
                heappush(future_event_list, new_event)
                
            elif num_in_fast_pass_queue == 1:
            	# Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                new_event = (time + service_time, 'departure', "fast_pass")
                
                heappush(future_fastpass_event_list, new_event)
              
              
        # Departure
        elif event_type == 'departure':
                
            if num_in_queue > 0 and num_in_fast_pass_queue == 0:
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
                
            elif num_in_fast_pass_queue > 0:
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                
                new_event = (time + service_time, 'departure', "fast_pass")
                
                heappush(future_fastpass_event_list, new_event)
                
                # If there are more customers waiting, put the next one into service and generate a departure 
                departure_times.append(time)
	            # Decrement queue size
                num_in_fast_pass_queue -= 1
                
            elif num_in_fast_pass_queue > 1 and num_in_queue == 0:
            	
                # Log enter service time
                enter_service_times.append(time)
                
                # Generate new departure event
                service_time = rand_exp(service_rate)
                
                new_event = (time + service_time, 'departure', "fast_pass")
                
                heappush(future_fastpass_event_list, new_event)
                
                # If there are more customers waiting, put the next one into service and generate a departure 
                departure_times.append(time)
                
	            # Decrement queue size
                num_in_fast_pass_queue -= 1
            #else:
            	#print ("another edge case")
                
        #print(num_in_fast_pass_queue, "fast_pass queue")
        #print(num_in_queue, "pleb queue")
    
    ### Simulation is over
    #
    # Calculate statistics
    
    # Average residence time
    
    #print(len(departure_times), "departure_times")
    #print(len(arrival_times), "arrival_times")
    residence_times = [departure_times[i] - arrival_times[i] for i in range(len(departure_times))]
    average_residence_time = sum(residence_times) / len(residence_times)
    
    return average_residence_time
	
def main():
	
    """ Simulate for different utilization levels """
    
    for u in range(5, 95, 5):
        
        # Run 20 trials at each utilization level and use the average of the simulated
        # values as the estimate of the residence time
        
        sim_residence_times = []
        
        for trial in range(20):
            sim_residence_times.append(queueing_simulator(.5, .5))
        
        sim_r_avg = sum(sim_residence_times) / len(sim_residence_times)
        
        print('%d\t%f' % (u, sim_r_avg))
        


if __name__ == '__main__':
    main()













































































