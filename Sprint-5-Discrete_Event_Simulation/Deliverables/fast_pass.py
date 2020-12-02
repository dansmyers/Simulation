"""
Fritz Stapfer Paz
12/2/2020 - Sprint 5

Simulate an M/M/1 queue with two different priority arrivals, and determine the ideal number of arrivals.
"""

# imports ======================================================================

from heap import Heap
from math import log
from math import sqrt
from random import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt


# main =========================================================================

def rand_exp(mu):                                               # random exponential time in service
    return -log(random())/mu

def simulate(lam,freq=0.0,service=1.0,max_time=10000):
    fel = Heap([(0.0,"arrival")])
    time = 0.0                                                  # simulation time
    in_service = False                                          # customers in service (0 or 1)
    
    lowpriority_rt = []                                         # low priority residence times
    highpriority_rt = []                                        # high priority residence times
    low_priority = []                                           # list holds low priority queue
    high_priority = []                                          # list holds high priority queue
    
    # simulation - while there are events to be executed, and time is within threshold
    while((len(fel.heap) > 0) and (fel.heap[0][0] < max_time)):
        event = fel.pop()                                       # pop the event out of the FEL
        time = event[0]                                         # set time to event time
        
        if(event[1] == "arrival"):                              # arrivals
            fel.insert(((rand_exp(lam) + time), "arrival"))     # add arrival to fel
            
            if(not in_service):                                 # if there is no one in service, process arrival
                service_time = rand_exp(service)                # service time is exponentially distributed
                fel.insert(((service_time + time),"departure")) # add a new departure to the FEL
                in_service = True                               # add a customer in service
                if(random() < freq):                            # if customer is high priorty
                    highpriority_rt.append(service_time)        # add service time to high priority residence time list
                else:
                    lowpriority_rt.append(service_time)         # add service time to high priority residence time list
            else:                                               # if there is a customer in either queue
                if(random() < freq):                            # if customer is high priority
                    high_priority.append(time)                  #   append time to high priority queue
                else:                                           # if customer is low priority
                    low_priority.append(time)                   #   append time to low priority queue

        else:                                                   # departures
            in_service = False                                  # remove customer in service
            
            if(len(high_priority) > 0):                         # process high priority customers
                service_time = rand_exp(service)                # service time is exponentially distributed
                pop = high_priority.pop(0)
                highpriority_rt.append(                         # append to residence time:
                    (service_time + (time - pop)))              # service_time + (time - oldest customer in low priority queue) priority queue)
                fel.insert(((service_time + time),"departure")) # add a new departure to the FEL
                in_service = True                               # add a customer in service
            elif(len(low_priority) > 0):                        # process low priority customer only if no high priority customers are left
                service_time = rand_exp(service)                # service time is exponentially distributed
                pop = low_priority.pop(0)
                lowpriority_rt.append(                          # append to residence time:
                    (service_time + (time - pop)))              # service_time + (time - oldest customer in low priority queue)n low priority queue)
                fel.insert(((service_time + time),"departure")) #  add a new departure to the FEL
                in_service = True                               # add a customer in service
                
    return(highpriority_rt,lowpriority_rt)                      # end the simulation and return the residence times array


def get_simulation_averages(lam,freq):                          # return tuple with fraction, avg rt, avg high rt, avg low rt
    avgs = []                                                   # list to store tuple
    for f in freq:                                              # loop through fastpass rates
        hrt, lrt = [],[]                                        # list of different averages
        for s in range(100):
            sim = simulate(lam, f)                              # run simulations with selected rate
            hrt.append(sum(sim[0]) / len(sim[0]))               # append simulation result from high restimes
            lrt.append(sum(sim[1]) / len(sim[1]))               # append simulation result from low restimes
        avgs.append((f, sum(hrt)/100, sum(lrt)/100))              # append average for the 10 simulations run
    return(avgs)                                                # return tuple
    
def main():
    # Run Simulations with No Fast Passes at 95% Utilization
    avgs_nopass_hu = []
    for i in range(100):
        nopass_hu = simulate(.95)
        nopass_hu_res = nopass_hu[1]
        avgs_nopass_hu.append(sum(nopass_hu_res) / len(nopass_hu_res))
    avg_nopass_hu = (sum(avgs_nopass_hu) / len(avgs_nopass_hu))

    plt.figure()
    plt.boxplot(avgs_nopass_hu)
    plt.title("Average Residence Time:\n.95 Utilization - No Passes")
    plt.xlabel(f"No Fast Pass\n{avg_nopass_hu}")
    plt.ylabel("Average Residence Time")
    plt.savefig("noFastPasses95util.pdf",bbox_inches="tight")
    
    # Run Simulations with No Fast Passes at 50% Utilization
    avgs_nopass_lu = []
    for i in range(100):
        nopass_lu = simulate(.95)
        nopass_lu_res = nopass_lu[1]
        avgs_nopass_lu.append(sum(nopass_lu_res) / len(nopass_lu_res))
    avg_nopass_lu = (sum(avgs_nopass_lu) / len(avgs_nopass_lu))

    plt.figure()
    plt.boxplot(avgs_nopass_lu)
    plt.title("Average Residence Time:\n.50 Utilization - No Passes")
    plt.xlabel(f"No Fast Pass\n{avg_nopass_lu}")
    plt.ylabel("Average Residence Time")
    plt.savefig("noFastPasses50util.pdf",bbox_inches="tight")
    
    # Get different pass fractions
    passFractions = [(i/20) for i in range(1,20)]

    # Run Simulations with different fast pass fractions, and graph resulting residence times
    # At 95% Utilization
    highutil = get_simulation_averages(.95, passFractions)
    highutil_high_rt = [t[1] for t in highutil]
    highutil_low_rt = [t[2] for t in highutil]

    plt.figure()
    plt.xlim(0,1)
    plt.title("Residence Times for Given Fraction of Fast Passes\n.95 Utilization")
    plt.xlabel("Fast Pass Fraction")
    plt.ylabel("Average Residence Time")
    plt.plot(passFractions,highutil_high_rt,color="blue",label="high")
    plt.plot(passFractions,highutil_low_rt,color="red",label="low")
    plt.legend()
    plt.savefig("passFraction95util.pdf",bbox_inches="tight")

    # At 50% Utilization
    lowutil = get_simulation_averages(.5,passFractions)
    lowutil_high_rt = [t[1] for t in lowutil]
    lowutil_low_rt = [t[2] for t in lowutil]

    plt.figure()
    plt.xlim(0,1)
    plt.title("Residence Times for Given Fraction of Fast Passes\n.5 Utilization")
    plt.xlabel("Fast Pass Fraction")
    plt.ylabel("Average Residence Time")
    plt.plot(passFractions,lowutil_high_rt,color="blue",label="high")
    plt.plot(passFractions,lowutil_low_rt,color="red",label="low")
    plt.legend()
    plt.savefig("passFraction50util.pdf",bbox_inches="tight")


if(__name__=="__main__"): 
    main()