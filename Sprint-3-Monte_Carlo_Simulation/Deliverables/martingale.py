'''
CMS 380
Write a simulation to evaluate the Martingale strategy
'''

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 

from random import randint

money = 255

def simulate(bet):
    global money
    wins = True
    
    spin_num = randint(1,38)
    if spin_num <= 18:
        money = bet + money
    else:
        money = money - bet
        wins = False
    return wins

def main():
    global money
    spins = []
    max_trials = 10
    
    for i in range(max_trials):
        bet = 1
        num_games = 0 
        while money > bet and num_games <= 100:
            if simulate(bet):
                bet = 1
            else:
                bet = bet * 2
            num_games += 1
        spins.append(money)
        money = 255
    
    
    #create a new figure, always do before calling plotting function
    plt.figure()


    plt.hist(spins,50)

    #Set title and axis labels
    plt.title("Martingale Strategy")
    plt.xlabel("Money Left")
    plt.ylabel("Count")

    #save figure to a filter
    plt.savefig("Martingale.pdf", bbox_inches='tight')
    
if __name__ == '__main__':
    main()
