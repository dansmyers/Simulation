"""
Christian Huber
CMS 380, Fall 2020 / Sprint 3 / The Ticket Problem
This script plots the results of a binomial process
and the poisson pmf for a series of coin flips
"""

from random import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from math import e
from math import factorial 


### FUNCTIONS ###

# Calculate poisson probability mass function for frequency of heads
# Takes highest numer of heads as argument
def ppmf(most_heads):
    pmf = [((e**(-25))*(25)**(x))/factorial(x) for x in range(most_heads)]
    return pmf


# Plot frequencies of head occurences and pmf in one histogram
def plot(num_heads, pmf):
    plt.figure()
    plt.hist(num_heads,bins=25,density=True)
    plt.plot(pmf)
    plt.title("Frequency of Event 'Heads' and Poisson PMF of Coin Flips")
    plt.xlabel("Frequency of Event 'Heads'")
    plt.savefig('les_poissons_hist_and_pmf.pdf', bbox_inches='tight')


# Simulate coin flips with binomial distribution
def binom():
    heads_count = 0
    
    for trial in range(1000): 
        flip = random()
        if (flip <= 0.025):
            heads_count = heads_count + 1
            
    return record

    
# Simulate the experiment
def simulate():
    heads = list()

    for trial in range(1000):
        flips = binom()
        heads.append(flips)
    heads.sort()
    poisson = list()
    poisson = ppmf(heads[-1])
    
    plot(heads, poisson)


if __name__ == '__main__':
    simulate()
