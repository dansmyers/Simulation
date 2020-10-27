"""
Fritz Stapfer Paz
Sprint 3 - Les Poissons! Les Poissons! How I Love les Poissons!
10/28/2020

Show how the Poisson distribution is a good approximation for the binomial distribution
under specific conditions
"""

# --------------------------------------------- Imports -----------------------------------------------

from math import e
from math import factorial

from random import random

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# --------------------------------------------- Functions ---------------------------------------------

def binomial():                     # return integer for number of heads
    counter = 0                     # count the number of heads that show up
    
    for event in range(1000):       # simulate binomial process with n = 1000 and p = .025
        if(random() <= 0.025):      # simulate coinflip with probability p
            counter += 1            # uncrement counter if coinflip succeeds
    
    return counter                  # return counter

# -----------------------------------------------------------------------------------------------------

def poisson():                      # return the poisson distribution
    return([((e**(-25))*(25)**(x))/factorial(x) for x in range(50)])

# -----------------------------------------------------------------------------------------------------

def run():                         # run the entire simulation
    binomial_sims = list()          # list with binomial distribution results
    poisson_sims = list()           # list with poisson distribution results
    
    for event in range(1000):       # run binomial distribution 1000 times
        b = binomial()              # run a binomial simulation
        binomial_sims.append(b)     # append it to list of results
    binomial_sims.sort()            # sort the results
    
    poisson_sims = poisson()        # simulate the poisson distribution
    
    # plotting data
    plt.figure()
    plt.hist(binomial_sims, bins = 25, density = True)
    plt.plot(poisson_sims, color = 'green', linewidth = '3')
    plt.title('Les Poissons!')
    plt.xlabel('heads per 1000 flips')
    plt.ylabel('frquency per 1000 flips')
    plt.savefig('poisson_binomial_simulation.pdf', bbox_inches='tight')
    
# -----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    run()