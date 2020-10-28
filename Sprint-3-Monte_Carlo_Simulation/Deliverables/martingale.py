"""
Simulate a game of Martingale
"""

# Import a method to generate random die rolls
#
# random.randint -- generate random integeters in a range
from random import randint

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def simulate():
  """
  Simulate landing on black on a roulette wheel
  
  inputs: no
  output: True if result is less than or equal to 18
  """
  
  # Simulate the roulette wheel
  # randint(1,38) generates an int in the range of 1 to 38, inclusive
  result = randint(1,38)

  return result <= 18
  

def main():  
  """
  Start with 255 cash, bet 1 dolllar, if fail double bet
  end when 100 plays or run out of cash to make a bet
  return cash on hand at end of play
  """
  
  max_plays = 100
  cash = 255
  bet = 1
  
  for play in range(max_plays):
    result = simulate()
    
    if result == True:
      cash += bet
      bet == 1
    
    if result == False:
      cash -= bet
      bet *= 2
      if cash < bet:
        break
  
  return cash
  

if __name__ == '__main__':
  results = []
  
  # run a large number of simulated trials and collect the results in a list
  for i in range(1000):
    cash_result = main()
    results.append(cash_result)

  plt.figure()
  plt.title("Martingale Histogram")
  plt.xlabel("Cash Remaining")
  plt.ylabel("Number of Games")  
  plt.hist(results, 50)
  plt.savefig('martingale.pdf', )  
    