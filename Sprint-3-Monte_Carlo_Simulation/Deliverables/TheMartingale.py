"""
Christian Huber
CMS 380, Fall 2020 / Sprint 3 / The Ticket Problem
This script simulates using the Martingale stratgey
in roulette and estimates the winnings.
"""
​
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

from random import random
​

# Create Roulette Wheel as array of 18 True, 20 False values
wheel = [True if(x<18) else False for x in range(38)]
​

### FUNCTIONS ###
​
def martingale(budget, spins):
    bet = 1
    while(budget >= bet or spins > 0):
        spins -= 1
        win = wheel[(int)(random()*38)]
        if(win == True):
            budget += bet
            bet = 1
        else:
            budget -= bet
            bet = bet*2
    return(budget)


def plot(winnings)
    plt.figure()
    plt.hist(winnings, bins = 256, density = "True")
    plt.title("Winnings After Playing The Martingale Strategy In Roulette")
    plt.xlabel("Winnings (in USD)")
    plt.ylabel("Count")
    plt.savefig("Martingale_hist.pdf", bbox_inches = 'tight')


### MAIN ###

def main():
    winnings = []

    # Save winnings from each of the 1000 trials to winnings array
    for x in range(1000):

        # Simulate one full round of Martingale strategy
        # and calculate winnings by subtracting entry budget
        round_winnings = martingale(255, 100)-255
        
        winnings.append(round_winnings)
    plot(winnings)


if __name__ == '__main__':
   main()
