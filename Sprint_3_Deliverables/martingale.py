"""
Alejandra De Osma 
CMS_380
Sprint 3 
Martingale Problem 
"""
#Imports 
from random import random

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# This function simulates a single spin 
def single_spin():
    # checks to see if the random generated value is smaller that 18
    return (int)(random()*38)<18
    
#Martingale simulation     
def martingale():
    # Starting budget amount 
    budget_Amount = 255
    # Number of rounds 
    trials = 100
    # Initial bet is equal to 1 
    bet = 1
    
    # Loop that will continue until the conditions are met 
    while(bet <= budget_Amount and trials > 0):
        # Subtracting the number of trials per iteration of the game
        trials -= 1
        
        # If the single spin is true, or Successful
        if(single_spin()):
            # The the bet amount is added to your budget
            budget_Amount += bet
            # Restarts betting 
            bet = 1
        #If the spin is false, or unsuccessful
        else:
            #Then the bet is subtracted from your budget
            budget_Amount -= bet
            #And the bet is doubled 
            bet = bet*2
    # Returns your budget after the completed simulations
    return budget_Amount
    
#Main     
def main():
    # Creating a list to store the values of the Martingale simulation
    simulation = list()
    
    # Loop that will complete 1,000 simulations 
    for trial in range(1000):
        # Append the results of the martingale function the the list of results
        simulation.append(martingale())
        
    # Ploting the results using matplotlib
    # Creating a histogram to visually observe distribution
    plt.figure()
    plt.hist(simulation, bins = 240,density = 'True')
    plt.title('The Martingale Simulation')
    plt.xlabel('Quantity won')
    plt.ylabel("Frequency of Success")
    plt.savefig('Martingale_simulation.pdf', bbox_inches='tight')

    # Printing the values of simmulation
    # Finding the probability of the completed simulations 
    prob = sum(simulation)/len(simulation) 
    print('Average winnings from martingale: %.6f' % prob)

# Call to run main 
if __name__ == '__main__':
    main()
        
    
