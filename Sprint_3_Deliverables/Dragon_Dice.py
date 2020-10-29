"""
Simulate the probability of winning at Dragon Dice
"""
#Imports:

from random import randint
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def simulate():
    guess = randint(1,6)
    dice_1 = randint(1,6)
    dice_2 = randint(1,6)
    dice_3 = randint(1,6)
    
    if guess == dice_1 or guess == dice_2 or guess == dice_3:
        return True
        

def main():
    max_trials = 1000
    num_succeses = 10
    
    for trail in range(max_trials):
        result = simulate()
        
        if result == True:
            num_succeses += 1

    
    frac_success = num_succeses/max_trials
    return frac_success

if __name__ == '__main__':
    results =[]
    expected_value = 0 
    for i in range(20000):
        results.append(main())
      
plt.hist(results,25)
plt.title("Dragon_Dice")
plt.xlabel("probability of Winning")
plt.ylabel("size")
plt.savefig("Dragon_Dice,000 Trials Distribution.pdf",bbox_inches='tight')
    