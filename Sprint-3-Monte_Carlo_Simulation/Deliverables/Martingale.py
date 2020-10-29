"""
Hiroki Sato 
10/25/20

Deliverable problem No. 6: Martingale Simulation

Objective: Simulate the Roulette and Martingale strategy used in Roulette

As a result of the simulation, there is higher likelihood of which they lose money at the end of the spin rather than gain money on average, 
but when you look at the histogram, we either win some money about 50 dollars or lose tons of money than where you started -250 and end up losing the enire bankroll, 
"""
from random import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
 
# Creating a wheel
wheel = [True if(x<18) else False for x in range(38) ]


# plot function to plot the simulation outcome as histogram. 
def plot(records):
    plt.figure()
    plt.hist(records,255,density=True)
    plt.title("The Margingale Simulation")
    plt.xlabel(f"Amount\nAverage Winnings: {sum(records)/len(records)}")
    plt.ylabel("Fraction of event")
    plt.savefig('martingale_simulation.pdf', bbox_inches='tight')
    
# Martingale function 
def Martingale(bankroll = 255):
    # we want to keep track of spins because the player stops after playing 100 spins and we start the bet from 1
    spins = 0                               # 
    bet = 1
    while(spins < 100 and bankroll >= bet):
        spins +=1                           #placing the bet for a spin
        # Debugging lines
        #print("Num Spin",spins)
        #print("The current Bankroll:",bankroll)
        #print("Size of bet",bet)
        \
        spin = wheel[int(random()*38)]      # Producing the outcome of the spin
        if spin:                            # if spin is true, and won the spin, you gain bankroll
            bankroll = bankroll + bet
            bet = 1                         # Because we do not want to risk losing any money, start back from $1 bet
        else:
            bankroll = bankroll - bet       # if lost, we lose money...
            bet = bet*2                     # but to earn those lost money back, double the bet for the next spin

    bankroll = bankroll - 255               # Subtracting 255 which was the starting point because we are interested in how much money they gained or lost. 
    return bankroll

def simulate():
    # As deliverable problem explained. player starts with $255 
    records=[]
    for x in range(1000):
        gain = Martingale()
        records.append(gain)
    
    plot(records)
    

if __name__ == '__main__':

    simulate()