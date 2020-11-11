"""

Program to model a version of Disney's FastPass+ system using the discret-event simulation strategy.

CMS 380 -- Fall 2020
Maria Morales

"""

from math import log
from random import random

# Set up matplotlib and configure it to be used on Mimir 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot  as plt 

# Priority queue operations
from heapq import heappush, heappop, heapify


def rand_exp(rate):
    
    """ Generate an exponential random variate
    
        input: rate, the parameter of the distribution
        returns: the exponential variate
    """
    
    return -log(random()) / rate
    

def simulate(arrival_rate, fraction_of_HP):

    """ Simulate the M/M/1 queue, discrete-event style
    
        input: arrival_rate and fraction_of_HP, the system's arrival rate and
                the fraction of FastPasses or high priority customers to allocate
        returns: the average simulated residence time for high and low priority customers
    """

    # Stopping condition
    max_num_arrivals = 500000

    # Basic parameters
    service_rate = 1.0
    time = 0.0
    
    # Store the total number of customers in queue
    # Number of customers in queue for low priority
    lp_num_in_queue = 0 
    # Number of customers in queue for high priority
    hp_num_in_queue = 0 
    
    
    # Simulation data lists
    enter_service_times = []
    # Lists to save arrival and departure times 
    # for each type of customer 
    lp_arrival_times = []
    hp_arrival_times = []
    
    lp_departure_times = []
    hp_departure_times = []
    
    # Boolean to check if a low priority customer
    # is currently in service
    isLPCustomerInService = False
    

    # Initialize FEL as an empty list
    future_event_list = []
    
    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival')
    
    # Insert with a heap operation
    heappush(future_event_list, new_event)

    
    
    
    while len(future_event_list) > 0 and len(hp_arrival_times) + len(lp_arrival_times) < max_num_arrivals:
        
        # Pop next event
        event = heappop(future_event_list)

        
        # Event attributes
        event_time = event[0]
        event_type = event[1]
        
        # Advance simulated time
        time = event_time
         
        ### Process events
        
        # Arrivals
        if event_type == 'arrival':
            
            
            # Determine if customer is high or low priority 
            # increment corresponding queue size
            if random() < fraction_of_HP:
                #Arrival is high priority
                hp_num_in_queue += 1
                # Log arrival time
                hp_arrival_times.append(time)
            else:
                # Arrival is low priority 
                lp_num_in_queue += 1
                # Log arrival time
                lp_arrival_times.append(time)
            
            # Generate next arrival
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, 'arrival')
            
            heappush(future_event_list, new_event)
             
               
            # If queue was empty, determine priority, enter service and generate departure event
            if hp_num_in_queue == 1 and lp_num_in_queue == 0:

                    # Log enter service time
                    enter_service_times.append(time)
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'hp_departure')
                     
                    heappush(future_event_list, new_event)
               
            elif hp_num_in_queue == 0 and lp_num_in_queue == 1:
                     # Log enter service time
                    enter_service_times.append(time)
                    # Low-priority  customer in service
                    isLPCustomerInService = True
                    
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'lp_departure')
                    
                     
                    heappush(future_event_list, new_event)

           
        # Departures
        elif event_type == 'hp_departure' or event_type == 'lp_departure':
            
            # Determine if  the ONLY customer in queue is high or low priority
            if hp_num_in_queue == 1 and lp_num_in_queue == 0:
                # Log departure time
                hp_departure_times.append(time)
                hp_num_in_queue -=1 

            elif hp_num_in_queue == 0 and lp_num_in_queue == 1:
                # Log departure time
                isLPCustomerInService = False
                lp_departure_times.append(time)
                lp_num_in_queue -=1
                
            # There is  at least 1 customer in both queues
            # High priority  customers should go first 
            else:
                
                # If there are more high priority customers waiting and there isn't a low-priority customer in service, put the next high-priority customer into service and generate a departure
                if hp_num_in_queue > 0 and isLPCustomerInService == False:

                    
                    hp_departure_times.append(time)
                    hp_num_in_queue -=1 
                    
                    # Log enter service time
                    enter_service_times.append(time)
                        
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'hp_departure')

                    
                    heappush(future_event_list, new_event)
                
                # High priority customers arrived when a low-priority customer is in service, they must wait until the other customer finishes his service
                elif hp_num_in_queue > 0 and isLPCustomerInService == True:
                    
                    isLPCustomerInService = False
                    
                    lp_departure_times.append(time)
                    lp_num_in_queue -= 1
                    
                    # Log enter service time
                    enter_service_times.append(time)
                        
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'hp_departure')
                    
   
                    
                    heappush(future_event_list, new_event)
                    
                # All waiting customers are low priority
                elif hp_num_in_queue == 0 and lp_num_in_queue > 0:
                    

                    lp_departure_times.append(time)
                    lp_num_in_queue -=1
                    
                    
                    # Log enter service time
                    enter_service_times.append(time)
                    isLPCustomerInService = True
                            
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'lp_departure')

                    heappush(future_event_list, new_event)
                            
    
    # Calculate average residence time for each priority
    lp_residence_times = [lp_departure_times[i] - lp_arrival_times[i] for i in range(len(lp_departure_times))]
    lp_average_residence_time = sum(lp_residence_times) / len(lp_residence_times)
    
    
    hp_residence_times = [hp_departure_times[i] - hp_arrival_times[i] for i in range(len(hp_departure_times))]
    hp_average_residence_time = sum(hp_residence_times) / len(hp_residence_times)
    
    

    
    return [hp_average_residence_time, lp_average_residence_time]
    
    
    
    
def main():
    
    """ Simulate the queue under a low-load and high-load period.
        Simulation is repeated for different fractions of FastPass
        customers from .05 to .95.
        The results for each load period wich different fractions are 
        plotted into graphs that show residence times for each type of customer.
        """
    # Utilization
    high_utilization = .95
    low_utilization = .50
    
    # Store results from high and low utilization 
    sim_residence_times_high_u = []
    sim_residence_times_low_u = []
    
    
    # Store results for each type of customer under each load period
    sim_lp_residence_times_low_u = []
    sim_lp_residence_times_high_u = []
    
    sim_hp_residence_times_low_u = []
    sim_hp_residence_times_high_u = []
    
    # Fraction values for plots
    f_values = []
    
    
    for f in range(5, 95, 5):
        
        f_values.append(f/100.0)
        
        sim_residence_times_high_u = (simulate(high_utilization, f/100.0))
        sim_residence_times_low_u = (simulate(low_utilization, f/100.00))
        
        sim_hp_residence_times_low_u.append(sim_residence_times_low_u[0])
        sim_lp_residence_times_low_u.append(sim_residence_times_low_u[1])
        
        
        sim_hp_residence_times_high_u.append(sim_residence_times_high_u[0])
        sim_lp_residence_times_high_u.append(sim_residence_times_high_u[1])
        

    
    # Create new figure 
    plt.figure()
    # Set values to be plotted
    plt.plot(f_values, sim_lp_residence_times_high_u, label="Low priority")
    plt.plot(f_values, sim_hp_residence_times_high_u, label="High priority")
    # Set title and axis labels
    plt.title("Residence times  during high-load periods")
    plt.ylabel("Residence time")
    plt.xlabel("Fraction of customers with FastPass")
    plt.legend()
    # Save as a PDF 
    plt.savefig("High_Utilization_plots.pdf", bbox_inches='tight')
    
    # Create new  figure
    plt.figure()
    # Set values to be plotted 
    plt.plot(f_values, sim_lp_residence_times_low_u, label="Low priority")
    plt.plot(f_values, sim_hp_residence_times_low_u, label="High priority")
    # Set title and axis labels 
    plt.title("Residence times during low-load periods")
    plt.ylabel("Residence time")
    plt.xlabel("Fraction of customers with FastPass")
    plt.legend()
    # Save as a PDF
    plt.savefig("Low_Utilization_plots.pdf", bbox_inches='tight')
    
    


if __name__ == '__main__':
    main()


