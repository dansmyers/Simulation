### Implementation of an M/M/1 queue using the discret-event advance strategy
#
# CMS 380

# 

from math import log
from random import random
#--------------------------------------------------------

#-------------------------------------------------------- i made this to try to workaround
import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot as plt

# Priority queue operations
from heapq import heappush, heappop, heapify

percent = 0

def rand_exp(rate):
    
    """ Generate an exponential random variate
    
        input: rate, the parameter of the distribution
        returns: the exponential variate
    """
    
    return -log(random()) / rate

# Dr Myers, 
#   I have had more trouble with this program than anything I've 
#   Ever worked on. I woked on it pretty much all night and ended up
#   sitting in the corner of the study room in the fetal position.
#   I just wanted to pass a value from main to my tag, so I could
#   update the amounts of priority customers and plot as each simulation.
#   With an updated value of priority customers.
def fuck():
    rand = random()
    global percent
    if rand < percent * .01: 
        #print("priority")         
        return "priority"

    elif rand > percent * .01:  
        #print("peasant")        
        return "peasant"

def plot_fig_high_ute(ute_lvl, peasants, priority):
    plt.figure()

    plt.plot(ute_lvl, peasants, label= "Peasant")
    plt.plot(ute_lvl, priority, label = "Priority")

    plt.xlabel('Percent of Priority Customers')
    plt.ylabel('Average Residence Times')
    plt.title('High Utilization')
    plt.savefig("high_plot.pdf", bbox_inches='tight')

def plot_fig_low_ute(ute_lvl, peasants,priority):
    plt.figure()

    plt.plot(ute_lvl, peasants, label= "Peasant")
    plt.plot(ute_lvl, priority, label = "Priority")

    plt.xlabel('Percent of Priority Customers')
    plt.ylabel('Average Residence Times')
    plt.title('Low Utilization')
    plt.savefig("low_plot.pdf", bbox_inches='tight')


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
    num_in_priority = 0
    num_in_peasant = 0
    
    # Simulation data lists
    priority_arrival_times = []
    peasant_arrival_times = []

    enter_service_times = []

    priority_departure_times = []
    peasant_departure_times = []

    # Initialize FEL as an empty list
    future_event_list = []
    
    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival', fuck())
    
    # Insert with a heap operation
    heappush(future_event_list, new_event)
    
    while (len(future_event_list) > 0) and (len(peasant_arrival_times) + len(priority_arrival_times) < max_num_arrivals):

        # Pop the next event with a heap operation
        event = heappop(future_event_list)
        
        # Event attributes
        event_time = event[0]
        event_type = event[1]
        event_tag = event[2]
        
        # Advance simulated time
        time = event_time
        
        # Check event type
        if event_type == 'arrival':

            # Check priority tag
            if event_tag == 'priority':
                num_in_priority += 1
                priority_arrival_times.append(time)
            else:
                num_in_peasant += 1
                peasant_arrival_times.append(time)

            # Generate Next Arrival
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, 'arrival', fuck())

            # Add to heap
            heappush(future_event_list, new_event)

            # Test if there is one person
            if (num_in_peasant + num_in_priority) == 1:
                # Add event time
                enter_service_times.append(time)

                # Test if last man standing is priority
                if num_in_priority == 1:
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    # Create royalty
                    new_event = (time + service_time, 'departure', 'priority')
                    # Add royalty to the riffraf
                    heappush(future_event_list, new_event)
                # Test if the last vagabond standing is a peasant
                elif num_in_peasant == 1:
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    # Create peasant
                    new_event = (time + service_time, 'departure', 'plebian')
                    # Add peasant to the masses
                    heappush(future_event_list, new_event)
     
        # Departure case
        elif event_type == 'departure':
            
            # Departure case for last human standing
                # Is royalty
            if (num_in_priority == 1) & (num_in_peasant == 0):
                 # Log Departure time 
                priority_departure_times.append(time)
                num_in_priority -= 1
                # Is commoner
            elif (num_in_peasant == 1) & (num_in_priority == 0):
                # Log Departure time
                peasant_departure_times.append(time)
                num_in_peasant -= 1
            
                # If there is more than one human left,
                # put the next one into service and generate a departure
                if (num_in_priority & num_in_peasant) > 0:
                
                    # Log enter service time
                    enter_service_times.append(time)
                
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'departure', fuck())
                    heappush(future_event_list, new_event)
            
    
    ### Simulation is over
    #
    # Calculate statistics
    
    # Average residence time
    # Ran into big problem of 0 case assuming my code is acurate, 0 case was added and was getting division by 0
    # error - could not find error in code so I separated the division from the 0 case
    # I tried doing it about six different ways and this was the only one that worked
    peasant_residence_times = [(peasant_departure_times[i] - peasant_arrival_times[i]) for i in range(len(peasant_departure_times))]
    if len(priority_departure_times) > 0:
        priority_residence_times = [(priority_departure_times[x] - priority_arrival_times[x]) for x in range(len(priority_departure_times))]
        average_priority = sum(priority_residence_times) / len(priority_residence_times)
    else:
        average_priority = 0

    if len(peasant_departure_times) > 0:
        average_peasant = sum(peasant_residence_times) / len(peasant_residence_times)
    else:
        average_peasant = 0

    avg_total = average_priority + average_peasant

    avg_res_time = [average_peasant, average_priority, avg_total]

    return avg_res_time

def main():
    
    # Record priority customer amounts used
    percent_priority_customers = []
    # Low utilization values
    graph_low_util_peasant = []
    graph_low_util_priority = []
    # High utilization values
    graph_high_util_peasant =[]
    graph_high_util_priority = []

    for p in range(0, 50, 1):
        global percent
        percent = p
        print(percent)
        # Record percentage of priority customers
        percent_priority_customers.append(p)
        # Utilization levels
        low_utilization = .50
        high_utilization = .95
        # Lists to hold simulated results with low utilization
        low_utilization_priority = []
        low_utilization_peasant = []
        # Lists to hold simulated results with high utilization
        high_utilization_priority = []
        high_utilization_peasant = []

        trials = 0
        while trials < 20:
            # Advance loop condition
            trials = trials + 1
            # Get averages from simulate run at low utilization
            sim_avg_peasant_low = simulate( low_utilization )[0]
            sim_avg_priority_low = simulate( low_utilization  )[1]
            # Add to lists
            low_utilization_peasant.append(sim_avg_peasant_low)
            low_utilization_priority.append(sim_avg_priority_low)

            # Get averages from simulate run at high utilization
            sim_avg_peasant_high = simulate( high_utilization )[0]
            sim_avg_priority_high = simulate( high_utilization  )[1]
            # Add to lists
            high_utilization_peasant.append(sim_avg_peasant_high)
            high_utilization_priority.append(sim_avg_priority_high)


        # Get low utilization averages for the trials 
        total_average_low_peasant = (sum(low_utilization_peasant)/ len(low_utilization_peasant))
        total_average_low_priority = (sum(low_utilization_priority)/ len(low_utilization_priority))
        # Set graph lists
        graph_low_util_peasant.append(total_average_low_peasant)
        graph_low_util_priority.append(total_average_low_priority)
        # Get high utilization averages for the trials
        total_average_high_peasant = (sum(high_utilization_peasant)/ len(high_utilization_peasant))
        total_average_high_priority = (sum(high_utilization_priority)/ len(high_utilization_priority))
        # Set graph lists
        graph_high_util_peasant.append(total_average_high_peasant)
        graph_high_util_priority.append(total_average_high_priority)

    # Share data with low utilization def for graphing
    plot_fig_low_ute(percent_priority_customers, graph_low_util_peasant, graph_low_util_priority)
    # Share data with high utilization def fo graphing
    plot_fig_high_ute(percent_priority_customers, graph_high_util_peasant, graph_high_util_priority)


if __name__ == '__main__':
    main()

""" WRITE UP:

    Strategy. I created a relatively simple m-m-1 queue, then I implemented a tagging system where customers would
    have their priority level set as 'priority' and 'peasant'. 
    The priority customers would be served before the peasants. Then I got the residence times of all the peasants
    and all the priority customers. 

    In the main def, I ran the simulation at utilizations .50 customers per minite and .95 customers per minute, 
    low and high respectively. I also ran it 30 times at each fast pass percentage level, 
    stepping in intervas of 2 percent from 0 - 100 percent. 

    The method I used for applying the percentage of priority customers seemed good to me in practice, however I
    wasted about 15 - 20 hours working on this one specific part of the program. Initially, I tried to pass the 
    different percentages of fast passes through to " def tag(percent): " and then call that in the main simulation.
    That did not work at all. Many hours, mental breakdowns, and trips to stack overflow later, I finally managed
    to make the code run and it seems to accept the percentages and run with them properly. I was initially trying
    to use a " def tag() " and pass a value from main to tag, refrencing tag with the passed in value from main.
    values. I saw many sources online saying that using a global was bad so I didnt do that until the very end and
    tried everything I could to avoid using the global. I eventually caved as you can see.

    QUESTIONS:

    When I say "best case" I am refering to maximum efficiency of the queue system. Meaning the lowest overall
    wait times, not the best case for the low priority exclusively, or the high priority exclusively.

    The best case percentages of priority customers changes for low utilization and high utilization. During 
    periods of low utilization, the best case percentage of priority customers out of the total arrivals occurs
    when approximately 28% of the riders are priority customers. This changes for periods of high utilization
    where the best case performance occurs with approximately 5% of all customers holding high priority status.
    
    NOTE:
    I sincerelly apologize for submitting this assignment so late. I could not find anyone to help me with the
    problems I was running into. I am still bad at coding in python and do not know my way around troubleshooting
    issues for more complicated programs. 
    
"""   
        

    
