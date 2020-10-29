"""
Alejandra De Osma 
CMS_380
Sprint 3
Les Poissons problem 
"""
#IMPORTS:
import math
from math import e
from math import factorial
from random import random

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# This function returns the number of heads 
# using n= 1000 trials and a probability of p = 0.025
def binomial():
    # This temporary variable will store the number of obtained heads
    temp = 0
    # Simulating trial 1,000 times 
    for event in range(1000):
        # Testing to see if the random generated decila is bigger that p or 0.025
        if(random() <= 0.025):
            # If so value of temp is incremented by one 
            temp += 1        
    # Return number of heads obtained in 1,000 trials
    return temp    
    
# This function simulates the poisson distribution
def poisson():
    return([((e**(-25))*(25)**(x))/factorial(x) for x in range(50)])

#Call to main 
def main():
    # Create a list of the binomial simulations
    binomial_s = list()
    # Create a list for the poisson returned values 
    poisson_s = list()
    
    # Completing 1,000 trials 
    for trial in range(1000):
        # Locally storing the value returned by the binomial function
        b_value = binomial()
        # Appending those values to the list of binomial simulations
        binomial_s.append(b_value)
        
    # Sotring the values within the list of results
    binomial_s.sort()
        
    # Storing the value of the possion distribution the the list 
    poisson_s = poisson()
    
    # Graphing the vslues obtained 
    plt.figure()
    plt.hist(binomial_s,bins = 25, density = True)                    
    plt.plot(poisson_s,color='black',linewidth='3') 
    plt.title("Binomial Possion")
    plt.xlabel("Number of heads (per 1000 flips)")
    plt.ylabel("Frequency / (1000 rounds)")
    plt.savefig("Le_Possions_Simulation.pdf",bbox_inches='tight')

# Final call to main
if(__name__=='__main__'):
    main()