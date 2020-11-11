#!/usr/bin/python3

"""
noah olmstead harvey
simulating M/M/1
09112020
this script simulates a single-server queue and calculates its comfidence intervals
"""

####  IMPORTS  #################################################################################################################

from random import random
from math import log
from math import sqrt
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

####  FUNCTIONS  ###############################################################################################################

def randExponential(mu):                                        ##  given mu (lamda) calculates random exponential value
    return(-log(random())/mu)

def simulate(arrivalRate,averageServiceTime,n):                 ##  simulates a m/m/1 queue
    interarrivalTimes = [randExponential(arrivalRate) for i in range(n)]#  uses exponential distribution to get interarrival
    serviceTimes = [randExponential((1/averageServiceTime)) for i in range(n)]  #  uses inverse of interarrival for service time
    arrivalTimes = [sum(interarrivalTimes[:(i+1)]) for i in range(n)]   #  gets arrival times by summing previous interarrivals
    enterServiceTimes = [0]*n                                   #  initializes enter service times
    departureTimes = [0]*n                                      #  initializes departure times

    enterServiceTimes[0] = arrivalTimes[0]                      #  set enter service time for first customer
    departureTimes[0] = (enterServiceTimes[0]+serviceTimes[0])  #  set departure time for first customer
    for i in range(1,n):                                        #  iterate over the remaining customers
        enterServiceTimes[i] = max(arrivalTimes[i],departureTimes[i-1]) #  enter time either previous departure or arrival time
        departureTimes[i] = (enterServiceTimes[i]+serviceTimes[i])      #  departure time is enter time plus service time
    residenceTimes = [(departureTimes[i]-arrivalTimes[i]) for i in range(n)]    #  residence is departure minus arrival time
    
    return((sum(residenceTimes)/n))                             #  returns the average of the residence times

####  SIMULATING M/M/1  ########################################################################################################

def main():
    arrivalRates = [(i/20) for i in range(1,20)]                #  creates list of rates: [.05, .10, .15, ..., .95]
    averageResidenceTimes = [simulate(i,1.0,5000) for i in arrivalRates]        #  the average residence time for each rate
    utilization = [averageResidenceTimes[i]*arrivalRates[i] for i in range(19)] #  the server utilization for each rate

    plt.figure()
    plt.xlim(0,1)
    plt.ylim(0,20)
    plt.title("M/M/1 Queue")
    plt.xlabel("Server Utilization")
    plt.ylabel("Average Residence Times")
    plt.plot(arrivalRates,utilization,color="red",linewidth='2')
    plt.savefig("MM1queue.pdf",bbox_inches="tight")

####  CONFIDENCE INTERVALS  ####################################################################################################

    simulateMultiple = [[simulate(rate,1.0,1000) for i in range(5)] for rate in arrivalRates]   #  five samples of each rate
    yBar = [(sum(y)/5) for y in simulateMultiple]               #  average of samples
    s = [sqrt((sum([((y[ii]-yBar[i])**2) for ii in range(5)]))/4) for i,y in enumerate(simulateMultiple)]   #  stdDev of samples
    ucl = [(yBar[i]+(2.776*(s[i]/sqrt(5)))) for i in range(19)] #  upper 95% confidence limit (t-distribution)
    lcl = [(yBar[i]-(2.776*(s[i]/sqrt(5)))) for i in range(19)] #  lower 95% confidence limit (t-distribution)
    yBarUtilization = [yBar[i]*arrivalRates[i] for i in range(19)]  #  utilization of sample averages
    uclUtilization = [ucl[i]*arrivalRates[i] for i in range(19)]#  utilization of upper 95% confidence limit
    lclUtilization = [lcl[i]*arrivalRates[i] for i in range(19)]#  utilization of lower 95% confidence limit

    plt.figure()
    plt.xlim(0,1)
    plt.ylim(0,20)
    plt.title("M/M/1 Queue Confidence Intervals")
    plt.xlabel("Server Utilization")
    plt.ylabel("Average Residence Times")
    plt.plot(arrivalRates,uclUtilization,color="blue",label="UCL",linewidth='1')
    plt.plot(arrivalRates,yBarUtilization,color="green",label="AVG",linewidth='2')
    plt.plot(arrivalRates,lclUtilization,color="red",label="LCL",linewidth='1')
    plt.legend()
    plt.savefig("MM1confidenceIntervals.pdf",bbox_inches="tight")

####  MAIN  ####################################################################################################################

if(__name__=="__main__"): main()
