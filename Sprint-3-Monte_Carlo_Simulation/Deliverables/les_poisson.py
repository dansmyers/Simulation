""""
Hiroki Sato 
10/25/20

Deliverable problem No. 4: Les Poissons! Les Poissons! How I Love les Poissons!

Simulate Coin Flips using Binomial Distribution and then plot them to compare

Important:
    * To plot both of them on the same scale, use the matplotlib's histogram's argument: density
      this way we can plot the binomial process and poisson distribution without any manual scaling. 

"""
# Importing needed libraries
from random import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from math import e
from math import factorial 

# Helper functions
#1. Calculate the poisson pmf based of the number of heads occurrence
def poisson_pmf(num_event): # the argument passed is the highest number of heads occurence after heads list is being sorted to fewest to the most occurence
    poisson = [((e**(-25))*(25)**(x))/factorial(x) for x in range(num_event)]
    return poisson

#2. plot the histogram of binomial process and the poisson distribution on the same plot
def plot(heads, poisson):
    
    plt.figure()
    plt.hist(heads,bins=25,density=True)
    plt.plot(poisson)
    plt.title("The Coin Flip Simulation")
    plt.xlabel('Number of Heads')
    plt.ylabel('The frequency/fraction of occurence')
    plt.savefig('coin_flip_simulation.pdf', bbox_inches='tight')

#3. Demonstrate the binomial process the coin flips
def binomial_process():
    # we will only have to keep track of the number of heads
    record = 0
    
    for trial in range(1000): 

        coin_flip = random()
        
        if ( coin_flip <= 0.025 ):
            record = record + 1
                
    return record
    
# This function will call of of the needed functions to demonstrate the coinflips and calculate the poisson distribution
# based on that and will plot both of them. 
def simulate():

    heads = list()

    for trial in range(1000):

        # simulation of the 1000 coin flips
        coin_flips = binomial_process()
        heads.append(coin_flips)
    heads.sort()
    poisson = list()
    poisson = poisson_pmf(heads[-1])
    
    plot(heads, poisson)

if __name__ == '__main__':

    simulate()
    
    