"""
Alejandra De Osma 
CMS_380
Sprint 4 Fast_Pass

This program will simulate a fast pass system for disney as a M/M/1 queue 

"""
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from random import random
import math
from math import log 
from math import sqrt

from heap import Heap 



def rand_e(r):                                              # Generating random exponential
    return -log(random())/r
    
def simulation(lam, f = 0.0, s = 1.0, m_time = 9999.9):
    
    t = 0.0                                                 # Variable t, keeps track of time   
    
    high_residence = []                                     # Initializing high priority residence time array
    Low_residence = []                                      # Initializing low priority residence time array
    
    high_arraival = []                                      # Initializing hig priority arraiaval time array
    low_arraival = []                                       # Initializing Low priority arraiaval time array
    
    current_in_service = 0                                  # Initializing variable to keep track of current customers in service 
    
    e = Heap([(0.0,"arrival")])                             # Initializing heap for upcoming events, by storing first arrival 
    
    while((len(e.heap) > 0) and e.heap[0][0] < m_time):     # Simulation Loop:
        
        event = e.pop()                                     # pop event from heap 
        
        t = event[0]                                        # setting time, t to event time 
        
        if(event[1] == "arrival"):                          # Processing Arrivals
            e.insert(((rand_e(lam) + t),"arrival"))
            
            if(current_in_service == 0):                    # Testing to see if there are no current customers in service
                                                            # Process arrival within service 
                service_time = rand_e(s)
                e.insert(((service_time + t),"departure"))
                current_in_service = 1
                
                
                if(random() < f):                            # If customer is in the queue 
                    high_residence.append(service_time)      # Appending service times for high priority customers 
                else:
                    Low_residence.append(service_time)       # Appending service times for regular customers 
                        
            else:  
                
                if(random() < f):
                    high_arraival.append(t)
                else:
                    low_arraival.append(t)
                    
        else:        #Departures: 
            
            current_in_service = 0 
                                                             # Check for customers that have Fast Pass 
            if( len(high_arraival) > 0):                     # Proccess Fast_Pass customers
                
                service_time = rand_e(s)
                
                high_residence.append(service_time + (t - high_arraival.pop(0)))
                e.insert(((service_time + t),"departure"))
                current_in_service = 1
                
                                                             # Check for customers without Fast Pass 
            elif(len(low_arraival) > 0):                     # Proccess regular customers
                service_time = rand_e(s)
                Low_residence.append(service_time + (t - low_arraival.pop(0)))
                e.insert(((service_time + t), "departure"))
                current_in_service = 1
                
    return high_residence, Low_residence                     # Return Array contaning residence times 
                                                             # For high and low priority customers 
    
def p_f(utilization,fractions):                              # CALCULATE average wating time 
                                                             # For High and Low priority customers 
    averages = []
    
    for fraction in fractions:
        high = []
        low = []
            
        for i in range(20):                                 # Simulates 20 trials/fraction 
                                                            # Stores values 
                                                            # Saves values for each type of customers
            
            results = simulation(utilization, fraction)
            
            high.append(sum(results[0])/len(results[0]))
            low.append(sum(results[1]) / len(results[1]))
                                                            # Appending averages to list 
                                                            
        averages.append((fraction, sum(high) / 20, sum(low)/20))
         
         
    return averages                                         # Returning Averages 
    
    
def main():
    
    # PART 1 : 
    # Average residence time at utilization 0.95 
    # No Fast pass included 
    
    queue_1_Avg = []
    for i in range(100):
        queue_1 = simulation(.95)
        queue_1_results = queue_1[1]
        queue_1_Avg.append(sum(queue_1_results)/len(queue_1_results))
    q_1_Avg_ = sum(queue_1_Avg)/len(queue_1_Avg)
    
    #Plotting Figure Utilization 0.95 (No Fast_Passes)
    
    plt.figure()
    plt.boxplot(queue_1_Avg)
    plt.title("Average Residence Time, utilization = 0.95 (no Fast Pass)")
    plt.ylabel("Average Residence Time")
    plt.savefig("Part_1.pdf",bbox_inches = "tight")
    
    fractions  = [(i / 20) for i in range (1, 20)]
    
    # PART 2 : 
    # Utilization at 0.95
    
    queue_2 = p_f(.95, fractions)
    queue_2_high = [t[1] for t in queue_2]
    queue_2_low = [t[2] for t in queue_2]
    
    #Plotting for utilization 0.95
    plt.figure()
    plt.xlim(0,1)
    plt.title("Residence Times for Fast_Pass holders and regular customers\n Utilization at 0.95")
    plt.xlabel("Fast Pass to Regular Customer Ratio")
    plt.ylabel("Average Residence Time")
    plt.plot(fractions,queue_2_high,color="black",label="Fast Pass Customer")
    plt.plot(fractions,queue_2_low,color="red",label = "Regular Customer")
    plt.legend()
    plt.savefig("Part_2.pdf",bbox_inches="tight")
    
    
    #PART 3 
    # Utilization at 0.45
    
    queue_3 = p_f(0.45,fractions)
    queue_3_high = [t[0] for t in queue_3]
    queue_3_low = [t[1] for t in queue_3]
    
    #Plotting for utilization 0.45
    plt.figure()
    plt.xlim(0,1)
    plt.title("Residence Times for Fast Pass and Regular Customer\n Utilization at 0.45")
    plt.xlabel("Fast Pass to Regular Customer Ratio")
    plt.ylabel("Averages Residence Times")
    plt.plot(fractions,queue_3_high,color="black",label="Fast Pass Customer")
    plt.plot(fractions,queue_3_low,color="red",label="Reguler Customer")
    plt.legend
    plt.savefig("Part_3.pdf",bbox_inches="tight")
    
    
if(__name__=="__main__"):
    main()
    
    
    


        
    
    
    
        
        

           
            
        
    
    
    




