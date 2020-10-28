"""
Simulate the ticket problem
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
  Simulate finding a random seat out of 100
  
  inputs: no
  output: random seat between 1 and 100
  """
  
  # Simulate finding an open seat
  # randint(1,100) generates an int in the range of 1 to 38, inclusive
  result = randint(1,100)

  return result
  

def main():  
  """
  Check to see if the seat is open. If not, call simulate to find a
  random seat.  Keep doing this for all 100 passengers.  Return 0 if
  passenger 100 sits in another seat besides 100 and 1 otherwise.
  """
  
  passengers = 100
  seats = []
  next_seat = 0
  
  """
  random the first seat
  """
  result = simulate()
  if result == 100:
    return 0
  else: 
    seats.append(result)
  
  for j in range(passengers - 1):
    next_seat = j + 2
    if next_seat not in seats:
      seats.append(next_seat)
    else:
      next_seat = simulate()
      if next_seat == 100:
        return 0
      else:
        if next_seat not in seats:
          seats.append(next_seat)

  return 1
  

if __name__ == '__main__':
  results = []
  
  # run a large number of simulated trials and collect the results in a list
  for s in range(1000):
    seat_result = main()
    results.append(seat_result)

  plt.figure()
  plt.title("Ticket Problem Histogram")
  plt.xlabel("Successfully having passenger 100 sit in seat 100 (0 failure 1 success)")
  plt.ylabel("Number of Occurances")  
  plt.hist(results, 10)
  plt.savefig('ticket_problem.pdf', )  
    