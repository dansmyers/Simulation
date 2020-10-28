"""
Simulate a bionomial process
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
  Simulate rolling a die with prob 1/40
  
  inputs: no
  output: True if die1 = 1, False otherwise
  """
  
  # Simulate the roll a die
  # randint(1,40) generates an int in the range of 1 to 40, inclusive
  die1 = randint(1,40)

  return die1 == 1
  

def main():  
  """
  Call simulate a large number of times and report the fraction of successes
  """
  
  max_trials = 1000
  num_sucesses = 0
  
  for trial in range(max_trials):
    result = simulate()
    
    if result == True:
      num_sucesses += 1
  
  # Report the fraction of trials that yeilded success
  frac_success = num_sucesses / max_trials
  # print(frac_success)
  return frac_success
  

if __name__ == '__main__':
  results = []
  
  # run a large number of simulated trials and collect the results in a list
  for i in range(1000):
    frac_success = main()
    results.append(frac_success * 1000)


  plt.figure()
  plt.title("Les Poissons Histogram")
  plt.xlabel("Number of Heads Occur")
  plt.ylabel("Number of Trials")
  plt.hist(results, 25)
  plt.savefig('les_poissons.pdf', )  
    
   