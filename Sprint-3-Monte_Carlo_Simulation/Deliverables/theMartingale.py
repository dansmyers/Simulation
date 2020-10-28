#!/usr/bin/python3

"""
noah olmstead harvey
the martingale
21102020
this script estimates winnings based on employing the martingale roulette strategy 
"""

####  IMPORTS  #################################################################################################################

from random import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

####  GLOBALS  #################################################################################################################

wheel = [True if(x<18) else False for x in range(38)]           ####  an array of 18T/20F to represent the roulette wheel  #####

####  FUNCTIONS  ###############################################################################################################

def martingale(budget = 255, rounds = 100):                     ####  returns the player's winnings  ###########################
    bet = 1                                                     #  player bet starts at 1
    while(budget>=bet and rounds > 0):                          #  while the player can afford the bet and less than 100 rounds
        rounds -= 1                                             #  decrement rounds
        win = wheel[(int)(random()*38)]                         #  spin the roulette wheel
        if(win):                                                #  if the player wins...
            budget += bet                                       #  ...add the bet to their winnings
            bet = 1                                             #  ...reset the bet amount to 1
        else:                                                   #  if the player loses...
            budget -= bet                                       #  ...subtract the bet from their winnings
            bet = bet*2                                         #  ...double the bet for the next round
        #print(budget, bet, win)                                                                               ##  DEBUGGING  ##
    return(budget)                                              #  return total winnings

####  MAIN  ####################################################################################################################

def main():
    results = [(martingale(255,100)-255) for x in range(1000)]  #  save (winnings - budget) for 1000 rounds in a results array
    plt.figure()
    plt.hist(results,bins=256,density="True")
    plt.title("Martingale Winnings")
    plt.xlabel(f"Amount\nAverage Winnings: {sum(results)/len(results)}")
    plt.ylabel("Frequency")
    plt.savefig("theMartingaleSimulation.pdf",bbox_inches="tight")

if(__name__=="__main__"): main()
