#!/usr/bin/python3

"""
noah olmstead harvey
les poissons les poissons how i love les poissons
21102020
this script plots a binomial process and poisson distribution for flipping coins with p(head) = .025
"""

####  IMPORTS  #################################################################################################################

import math
from random import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

####  FUNCTIONS  ###############################################################################################################

def binomial(n = 1000, p = .025):                               ####  returns a boolean array representing the number of heads
    return([True if(random()<p) else False for x in range(n)])  #  T if random() < p and F otherwise

def binomialSimulation(rounds = 1000, n = 1000, p = .025):      ####  runs a given number of rounds and returns head frequency
    freq = []                                                   #  an array to store the results of the binomial process
    for i in range(rounds):                                     #  runs for the given number of rounds
        freq.append(sum(binomial(n,p)))                         #  adds the total number of heads each round to freq array
    return(freq)                                                #  returns the head frequency array

def poisson(k = 51, lam = 25):                                  ####  returns the poisson dist for values 0-50 with lam=25
    return([(((math.e**(-lam))*(lam**x))/math.factorial(x)) for x in range(k)])

####  MAIN  ####################################################################################################################

def main():                                                     ####  main  ####################################################
    bino = binomialSimulation()                                 #  calculate binomial (use default values)
    pois = poisson()                                            #  calculate poisson (use deafault values)
    plt.figure()
    plt.hist(bino,bins=25,density=True)                         #  add the binomial histogram to the plot
    plt.plot(pois,color="gold",linewidth="4")                   #  add the poisson function to the plot
    plt.title("Binomial/Poisson Coin Flip")
    plt.xlabel("Number of heads (per 1000 flips)")
    plt.ylabel("Frequency (in 1000 rounds)")
    plt.savefig("lesPoissonsSimulation.pdf",bbox_inches="tight")

if(__name__=="__main__"): main()                                ####  runs main when executed from cli  ########################
