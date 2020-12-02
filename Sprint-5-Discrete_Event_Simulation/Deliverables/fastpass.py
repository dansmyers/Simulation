"""

CMS 380

My favorite themed project ever. Thank you Dr. Myers.

 

A simulation of the Disney FastPass+ System.

"""

from math import log
from random import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
 

# Priority queue operations
from heapq import heappush, heappop, heapify

 

# Function to determine if person has fastpass
def is_fastpass(fraction_of_fastpass):
    num = random()

    if num <= fraction_of_fastpass:
        return 'fastpass'

    elif num > fraction_of_fastpass:
        return 'plebian'

   

def rand_exp(rate):
    """ Generate an exponential random variate

   

        input: rate, the parameter of the distribution

        returns: the exponential variate

    """
    return -log(random()) / rate

   


def plot2(xs, vals1,vals2):
    plt.figure()
  
    plt.plot(xs, vals1, label= "plebian")
    plt.plot(xs, vals2, label = "fastpass")
    plt.xlabel('%fastpass')
    plt.ylabel('Average residence time')

    plt.title('High utilization plot')
    plt.savefig("plot_high_u.pdf", bbox_inches='tight')

def plot1(xs, vals1,vals2):
    plt.figure()
  
    plt.plot(xs, vals1, label= "plebian")
    plt.plot(xs, vals2, label = "fastpass")
    plt.xlabel('%fastpass')
    plt.ylabel('Average residence time')
    plt.title('Low utilization plot')
    plt.savefig("plot_low_u.pdf", bbox_inches='tight')

def simulate(arrival_rate, fraction_of_fastpass):

    """ Simulate the M/M/1 queue, discrete-event style

        input: arrival_rate  the system's arrival rate

        returns: the average simulated residence time

    """

    # Stopping condition
    max_num_arrivals = 500000

 

    # Basic parameters
    service_rate = 1.0
    time = 0.0
    num_in_queue_pleb = 0
    num_in_queue_fp = 0

    isPlebInService = False

   

    # Simulation data lists
    arrival_times = []

   

    p_arrivals = []
    fp_arrivals = []

    p_departures = []
    fp_departures = []

   

    

    enter_service_times = []
    departure_times = []

 

    # Initialize FEL as an empty list
    future_event_list = []

   

    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival', is_fastpass(fraction_of_fastpass))

   

    #print(new_event)
    # Insert with a heap operation
    heappush(future_event_list, new_event)

   

    while (len(future_event_list) > 0 or len(future_fastpass_event_list)) and (len(p_arrivals) + len(fp_arrivals)) < max_num_arrivals:
        # Pop the next event with a heap operation
     
        event = heappop(future_event_list)

           

        

        # Event attributes
        event_time = event[0]
        event_type = event[1]
        event_priority = event[2]

       

        

        # Advance simulated time
        time = event_time


        ### Process events

       

        # Arrivals
        if event_type == 'arrival':

            if event_priority == 'fastpass':
                num_in_queue_fp += 1
                fp_arrivals.append(time)

               

           

            else:

                num_in_queue_pleb += 1
                p_arrivals.append(time)
                #isPlebInService = True

               

            # Next arrival event
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time, 'arrival', is_fastpass(fraction_of_fastpass))

   

            # Insert with a heap operation
            heappush(future_event_list, new_event)

             

            

            # If queue was empty, enter service and generate a future departure event

            if num_in_queue_pleb + num_in_queue_fp == 1:

               

                # Log enter service time
                enter_service_times.append(time)
                if num_in_queue_fp == 1:
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    isPlebInService = False

                    new_event = (time + service_time, 'departure', 'fastpass')

                    heappush(future_event_list, new_event)

                   

                else:
                    isPlebInService = True
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'departure', 'plebian')
                    heappush(future_event_list, new_event)

              

                """if new_event[2] == 'fastpass':

                    heappush(future_fastpass_event_list, new_event)

                else:

                    heappush(future_event_list, new_event)"""

             

              

        # Departure

        elif event_type == 'departure':

           

            """ if event_priority == 'fastpass':

                fp_departures.append(time)

            else:

                p_departures.append(time)"""


            if num_in_queue_fp == 1 and num_in_queue_pleb == 0:
                fp_departures.append(time)
                num_in_queue_fp -= 1

               

            elif num_in_queue_pleb == 1 and num_in_queue_fp == 0:
                isPlebInService = True
                p_departures.append(time)
                num_in_queue_pleb -= 1

          

                

            else:
                if num_in_queue_pleb > 0 and num_in_queue_fp == 0:
                    p_departures.append(time)

                    # Log enter service time
                    enter_service_times.append(time)
                    num_in_queue_pleb -= 1
                    isPlebInService = True

                   

                    # Generate new departure event
                  
                   
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'departure', 'plebian')
                    heappush(future_event_list, new_event)
                elif num_in_queue_fp > 0 and isPlebInService == False:
                     # Log enter service time
                    enter_service_times.append(time)
                    num_in_queue_fp -= 1
                    fp_departures.append(time)

                   

                    # Generate new departure event
                    service_time = rand_exp(service_rate)

                    

                    new_event = (time + service_time, 'departure', 'fastpass')
                    heappush(future_event_list, new_event)

                   

                elif num_in_queue_fp > 0 and isPlebInService == True:
                    isPlebInService = False
                    # Log enter service time
                    enter_service_times.append(time)
                    num_in_queue_pleb -= 1
                    p_departures.append(time)
                    # Generate new departure event
                    service_time = rand_exp(service_rate)
                    new_event = (time + service_time, 'departure', 'fastpass')
                    heappush(future_event_list, new_event)

 

               

                    """

                    if len(future_fastpass_event_list) >= 1:

                        new_event = (time + service_time, 'departure', 'fastpass')

                    else:"""


   
    ### Simulation is over

    #

    # Calculate statistics

   

    # Average residence time

    low_residence_times = [(p_departures[i] - p_arrivals[i]) for i in range(len(p_departures))]
    
    if len(fp_departures) > 0:
        fp_residence_times = [(fp_departures[i] - fp_arrivals[i]) for i in range(len(fp_departures))]

        average_residence_time_fp = sum(fp_residence_times) / len(fp_residence_times)
    else:
        average_residence_time_fp = 0

    
    if len(p_departures) > 0:
        average_residence_time_low = sum(low_residence_times) / len(low_residence_times)
    else:
        average_residence_time_low = 0


   

    
    avg_res_time = [average_residence_time_low, average_residence_time_fp]

    return avg_res_time

   

 

 

def main():

   

    

    """ Simulate for different utilization levels """

    low_u_fastpass = []
    low_u_plebian = []

   

    high_u_fastpass = []
    high_u_plebian = []

   

    x_values = []
    

   

    for f in range(5, 95, 5):

       #Save values from simulate into a results list

       high_u_results = simulate(.95, f/100.0)
       low_u_results = simulate(.5, f/100.0)

      

       # Creates X axis
       x_values.append(f)
       high_u_plebian.append(high_u_results[0])
       high_u_fastpass.append(high_u_results[1])
       low_u_plebian.append(low_u_results[0])
       low_u_fastpass.append(low_u_results[1])

    plot2(x_values,high_u_plebian, high_u_fastpass)
    plot1(x_values,low_u_plebian, low_u_fastpass)

 

if __name__ == '__main__':

    main()