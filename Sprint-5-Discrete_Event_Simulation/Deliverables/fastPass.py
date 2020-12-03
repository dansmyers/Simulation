#!/usr/bin/python3

"""
noah olmstead harvey
simulating disney's fastpass+ system
27112020
this script simulates 
"""

####  IMPORTS  #################################################################################################################

from heap import Heap
from math import log
from math import sqrt
from random import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

####  FUNCTIONS  ###############################################################################################################

def randExponential(rate):                                      ####  returns exponential 
    return(-log(random())/rate)

def simulate(lam,freq=0.0,service=1.0,maxT=9999.9):             ####  simulates arrival/departure events for max time
    highResTimes = []                                           #  array to hold residence times of high priority customers
    lowResTimes = []                                            #  array to hold residence times of low priority customers
    highQueue = []                                              #  array to hold arrival times of high priority customers
    lowQueue = []                                               #  array to hold arrival times of low priority customers
    time = 0.0                                                  #  current simulation time
    inService = 0                                               #  number of customers in service (should be 1 or 0)
    futureEvents = Heap([(0.0,"arrival")])                      #  initialize FEL with first arrival
    while((len(futureEvents.heap) > 0) and (futureEvents.heap[0][0] < maxT)):           ##  SIMULATION LOOP  ###################
        event = futureEvents.pop()                              #  pop the event out of the FEL
        time = event[0]                                         #  set time to event time
        #print(inService,event)                                 #                                              ##  DEBUGGING  ##
        if(event[1] == "arrival"):                              ##  ARRIVAL  ###################################################
            futureEvents.insert(((randExponential(lam) + time),"arrival"))  #  add a new arrival to the FEL
            if(inService == 0):                                 #  if there are no customers in service - serve arrival
                sTime = randExponential(service)                #  service time is exponentially distributed
                futureEvents.insert(((sTime + time),"departure"))           #  add a new departure to the FEL
                inService += 1                                  #  add a customer to the inService variable
                if(random() < freq):                            #  if there is a customer in either queue
                    highResTimes.append(sTime)                  #  add service time to high priority residence time list
                else:                                           #  else
                    lowResTimes.append(sTime)                   #  add service time to low priority residence time list
            else:                                               #  if there is a customer in either queue
                if(random() < freq):                            #  if [0 - 1.0) < freq of passes
                    highQueue.append(time)                      #  append time to high priority queue
                else:                                           #  else
                    lowQueue.append(time)                       #  append time to low priority queue
        else:                                                   ##  DEPARTURE  #################################################
            inService -= 1                                      #  remove customer from inService variable (return it to 0)
            if(len(highQueue) > 0):                             #  if there are customers in the high priority queue
                sTime = randExponential(service)                #  service time is exponentially distributed
                highResTimes.append((sTime + (time - highQueue.pop(0))))    #  append (serviceT + (time - oldest highPri time))
                futureEvents.insert(((sTime + time),"departure"))           #  add a new departure to the FEL
                inService += 1                                  #  add a customer to the inService variable
            elif(len(lowQueue) > 0):                            #  else if there are customers in the low priority queue
                sTime = randExponential(service)                #  service time is exponentially distributed
                lowResTimes.append((sTime + (time - lowQueue.pop(0))))      #  append (serviceT + (time - oldest lowPri time))
                futureEvents.insert(((sTime + time),"departure"))           #  add a new departure to the FEL
                inService += 1                                  #  add a customer to the inService variable
    return(highResTimes,lowResTimes)                            #  return the arrays of simulation residence times for customers

def calcPassFractions(util,fracList):                           ####  returns a list of tuples: (fraction, high avg, low avg)
    returnAvgs = []                                             #  list of average wait times at specified frequencies
    for fraction in fracList:                                   #  for each fraction of passes in the list of fractions
        high,low = [],[]                                        #  lists for individual run high/low residence times
        for i in range(10):                                     #  ten runs at each pass fraction
            run = simulate(util,fraction)                       #  store result of simulation
            high.append(sum(run[0]) / len(run[0]))              #  add individual averge high residence time
            low.append(sum(run[1]) / len(run[1]))               #  add individual average low residence time
        returnAvgs.append((fraction,(sum(high) / 10),(sum(low) / 10)))      #  add ten run high/low averge to list to return
    return(returnAvgs)                                          #  return a list of tuples: (fraction, high avg, low avg)

def main():                                                     ####  MAIN  ####################################################

    q1avgs = []
    for i in range(100):
        q1 = simulate(.95)
        q1res = q1[1]
        q1avgs.append(sum(q1res) / len(q1res))

    plt.figure()
    plt.boxplot(q1avgs)
    plt.title("Average Residence Time:\n.95 Utilization - No Passes")
    plt.xlabel(f"No Fast Pass\n{(sum(q1avgs) / len(q1avgs))}")
    plt.ylabel("Average Residence Time")
    plt.savefig("noFastPasses.pdf",bbox_inches="tight")

    passFractions = [(i/20) for i in range(1,20)]

    q2 = calcPassFractions(.95,passFractions)
    q2high = [t[1] for t in q2]
    q2low = [t[2] for t in q2]

    plt.figure()
    plt.xlim(0,1)
    plt.title("Residence Times for Given Fraction of Fast Passes\n.95 Utilization")
    plt.xlabel("Fast Pass Fraction")
    plt.ylabel("Average Residence Time")
    plt.plot(passFractions,q2high,color="blue",label="FastPass")
    plt.plot(passFractions,q2low,color="red",label="No Pass")
    plt.legend()
    plt.savefig("passFraction95util.pdf",bbox_inches="tight")

    q3 = calcPassFractions(.5,passFractions)
    q3high = [t[1] for t in q3]
    q3low = [t[2] for t in q3]

    plt.figure()
    plt.xlim(0,1)
    plt.title("Residence Times for Given Fraction of Fast Passes\n.5 Utilization")
    plt.xlabel("Fast Pass Fraction")
    plt.ylabel("Average Residence Time")
    plt.plot(passFractions,q3high,color="blue",label="Fast Pass")
    plt.plot(passFractions,q3low,color="red",label="No Pass")
    plt.legend()
    plt.savefig("passFraction50util.pdf",bbox_inches="tight")

####  MAIN  ####################################################################################################################

if(__name__=="__main__"): main()                                ####  runs main when executed from cli  ########################
