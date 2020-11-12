import random

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

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
    
    plt.figure()
    plt.hist(outcomes)
    plt.savefig('outcomes.pdf', bbox_inches = 'tight')
    
if __name__ == '__main__':
    main()
