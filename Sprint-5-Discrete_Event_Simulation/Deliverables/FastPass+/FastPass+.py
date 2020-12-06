'''
Christian Huber
CMS 380, Fall 2020
This script simulates the FastPass+ system at Disney's theme parks
with the goal to find the optimal amount of FastPasses available during
different utilizations.
'''

#### IMPORTS ####

# Import Noah's Heap class
from heap import Heap

from math import log
from math import sqrt
from random import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt


#### FUNCTIONS ####

#--- Generate and return random exponential
def rand_exp(rate):
    return -log(random())/rate


#--- Simulate the arrivals and departures for a maximum amount of time
def simulate(lam, f = 0.0, s = 1.0, max_t = 9999.9):

    # Arrays for residence times of high and low priority customers
    hi_r = []
    lo_r = []

    # Arrays for arrival times of high and low priority customers
    hi_q = []
    lo_q = []

    # To keep track of time
    t = 0.0

    # Number of customers in service (either 1 or 0)
    in_service = 0

    # Initialize heap of future events with first arrival
    events = Heap([(0.0,"arrival")])


    #-- Actual simulation loop
    while((len(events.heap) > 0) and events.heap[0][0] < max_t):

        # Pop event out of heap
        event = events.pop()

        # set time = event time
        t = event[0]

        # For arrivals:
        if(event[1] == "arrival"):
            events.insert(((rand_exp(lam) + t), "arrival"))

            # Process arrival if no customers in service
            if(in_service == 0):
                s_t = rand_exp(s)
                events.insert(((s_t + t), "departure"))
                in_service = 1

                # If a customer is present in either queue
                if(random() < f):
                    hi_r.append(s_t)
                else:
                    lo_r.append(s_t)

            # If customer is in service, add time to either
            # queue depending on frequency of passes
            else:
                if(random() < f):
                    hi_q.append(t)
                else:
                    lo_q.append(t)

        # For departures:
        else:
            in_service = 0

            # Check for customers with FastPass
            # and process them
            if(len(hi_q) > 0):
                s_t = rand_exp(s)
                hi_r.append(s_t + (t - hi_q.pop(0)))
                events.insert(((s_t + t), "departure"))
                in_service = 1

            # Check for customers without FastPass
            # and process them
            elif(len(lo_q) > 0):
                s_t = rand_exp(s)
                lo_r.append(s_t + (t - lo_q.pop(0)))
                events.insert(((s_t + t), "departure"))
                in_service = 1

    # return the arrays containing residence times           
    return hi_r, lo_r



#--- Calculate and return the average waiting times for
#--- high and low priority customers
def pass_fractions(util, fractions):
    avgs = []
    for fraction in fractions:
        hi = []
        lo = []

        # Simulate 20 times for each fraction and store
        # results for both priorities
        for i in range(20):
            result = simulate(util, fraction)
            hi.append(sum(result[0]) / len(result[0]))
            lo.append(sum(result[1]) / len(result[1]))

        # Add averages to list
        avgs.append((fraction, sum(hi) / 20, sum(lo) / 20))

    # Return avgs, which contains tuples for each fraction
    return avgs



#### MAIN ####

def main():

    #-- Question 1:
    q1_avgs = []
    for i in range(100):
        q1 = simulate(.95)
        q1_result = q1[1]
        q1_avgs.append(sum(q1_result) / len(q1_result))
    q1_avg = sum(q1_avgs) / len(q1_avgs)

    # Plot average residence time at utilization .95 and no FastPasses
    plt.figure()
    plt.boxplot(q1_avgs)
    plt.title("Average Residence Time at 0.95 Utilization (no FastPass)")
    plt.ylabel("Average Residence Time")
    plt.savefig("no_FastPass.pdf",bbox_inches="tight")


    fractions = [(i / 20) for i in range(1, 20)]


    #-- Question 2:
    q2 = pass_fractions(.95, fractions)
    q2_hi = [t[1] for t in q2]
    q2_lo = [t[2] for t in q2]

    # Plot residence time for fractions at 0.95 utilization
    plt.figure()
    plt.xlim(0,1)
    plt.title("Residence Times for FastPass holders and regular customers\nat given fraction of issued FastPasses\nat 0.95 Utilization")
    plt.xlabel("Fast Pass to Regular Customer Ratio")
    plt.ylabel("Average Residence Time")
    plt.plot(fractions,q2_hi,color="blue",label="FastPass Customer")
    plt.plot(fractions,q2_lo,color="red",label="Regular Customer")
    plt.legend()
    plt.savefig("FastPass_0.5.pdf",bbox_inches="tight")


    #-- Question 3:
    q3 = pass_fractions(.5, fractions)
    q3_hi = [t[0] for t in q3]
    q3_lo = [t[1] for t in q3]

    # Plot residence time for fractions at 0.5 utilization
    plt.figure()
    plt.xlim(0,1)
    plt.title("Residence Times for FastPass holders and regular customers\nat given fraction of issued FastPasses\nat 0.50 Utilization")
    plt.xlabel("Fast Pass to Regular Customer Ratio")
    plt.ylabel("Average Residence Time")
    plt.plot(fractions,q3_hi,color="blue",label="FastPass Customer")
    plt.plot(fractions,q3_lo,color="red",label="Regular Customer")
    plt.legend()
    plt.savefig("FastPass_0.95.pdf",bbox_inches="tight")



#### RUN MAIN ####
if(__name__=="__main__"): main()
