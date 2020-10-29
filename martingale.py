import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def simulate():
    spin = 1
    balance = 255
    bet = 1
    while spin <= 100 and bet < balance:
        flip = random.uniform(0, 1)
        if flip <= (18/36):
            balance += bet
            bet = 1
        else:
            balance -= bet
            bet = 2*bet
        spin += 1
    return balance

 

def main(): 
    outcomes = []
    for i in range(0, 1000):
        outcomes.append(simulate())
    print(outcomes)
    
    plt.hist(outcomes, bins = 400)
    plt.savefig('martingale_hist.pdf')

   

if __name__ == '__main__':

    main()
