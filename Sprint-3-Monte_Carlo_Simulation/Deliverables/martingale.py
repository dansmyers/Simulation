"""
Fritz Stapfer Paz
Sprint 3 - The Martingale
10/28/2020

Show the result of the use of the Martingale strategy through the use of a simulation.
"""

# --------------------------------------------- Imports -----------------------------------------------

from random import random

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# --------------------------------------------- Functions ---------------------------------------------

def spin():
    return (int)(random() * 38) < 18                # spin the roulette
    
# -----------------------------------------------------------------------------------------------------

def martingale():                                   # do the martingale simulation
    budget = 255                                    # 255$ starting budger
    rounds = 100                                    # 100 rounds
    bet = 1                                         # 1$ starting bet
    
    while(bet <= budget and rounds > 0):            # run until stopping criteria is met
        rounds -= 1                                 # count round
        
        if(spin()):                                 # if you win
            budget += bet                           # process profits
            bet = 1                                 # restart betting at 1$
        else:                                       # if you lose
            budget -= bet                           # process loss
            bet = bet*2                             # increase betting amount
        
    return(budget)                                  # return total winnings

# -----------------------------------------------------------------------------------------------------

def run():                                          # run the entire simulation
    simulation_results = list()                     # list to store the results from all simulations
    for event in range (10000):                     # run 10000 simulations
        simulation_results.append(martingale())     # append individual result to list

    # plotting data
    plt.figure()
    plt.hist(simulation_results,bins=256,density='True')
    plt.title('The Martingale')
    plt.xlabel('amount won')
    plt.ylabel("frequency of winnings")
    plt.savefig('martingale_simulation.pdf', bbox_inches='tight')

    # print average
    prob = sum(simulation_results)/len(simulation_results) 
    print('Average winnings from martingale: %.6f' % prob)
    
# -----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    run()