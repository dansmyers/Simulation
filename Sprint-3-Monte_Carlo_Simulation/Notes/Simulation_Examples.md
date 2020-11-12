# Simulation Examples

This write-up shows you how to implement some basic simulation programs using Python's `random` module. The examples are relevant to the 
deliverable problems.

## Cho-Han

A Japanese dice game, depicted in period movies featuring wandering samurai and Yakuzsa gangsters. The player rolls three dice and wagers on whether the sum will come up even or odd.

Let's write a program to predict the probability that three dice yield an even sum. The code below uses a `simulation` method with `randint` to simulate the dice rolls. A few details to point out:

- `simulate` returns `True` if the sum of the dice is even. Note that it just simulates one round of the game; we're not asking the user to actually *play* cho-han.

- Boolean values in Python are `True` and `False`. Capitalization is required.

- The `main` method keeps count of the number of `True` results.

```
# Cho-Han: use simulation to determine the probabilty that three dice give an even sum
# CMS 380

from random import randint

def simulate():

    """ Simulate one round of the game
        
        inputs: none
        outputs: True if the result is even, False otherwise
    """
    
    # Sum of three dice
    roll = randint(1, 6) + randint(1, 6) + randint(1, 6)
    
    if roll % 2 == 0:
       return True
    else:
        return False
        
        
def main():

    num_iterations = 1000  # Number of simulated trials 
    num_evens = 0  # Number of even results
    
    # Python for loop using range
    for trial in range(num_iterations):
    
        # simulate() returns True or False
        if simulate():
            num_evens += 1
      
    
    # Fraction of even rolls
    # Division is exact in Python 3, even if both inputs are integer
    frac_even = num_evens / num_iterations
      
    # Print using the %f format specifier
    print('The probability of an even roll on three dice is about %f.'% frac_even)
    
    
# __name__ is an internal variable
#
# If it has the value '__main__', then this script is running as the entry point
# of the program.
#
# This is a common way to get into a main function
if __name__ == '__main__':
    main()
```

## Sic Bo

A traditional Chinese dice game popular with Asian gamblers.

Bets in sic bo are based on the roll of three dice. The basic bets are called "big" and "little":

- The big bet wins if the sum is between 11 and 17 (inclusive) and not a triple.

- The little bet wins if the sum is 4 to 10 (again, inclusive) and not a triple.

Here is a program that simulates the probability of winning the big bet in sic bo. It uses the same structure as the previous example, with a `simulate` method that returns `True` or `False` based on the outcome of one round.

```
# Sic Bo: simluate the probability of winning the "big" bet
# CMS 380

from random import randint

def simulate():

    """ Simulate one round of the game
        
        inputs: none
        outputs: True if the result is greater than 10 and not a triple, False otherwise
    """
    
    # Sum of three dice
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die3 = randint(1, 6)
    
    # Test for triples
    # Python comparisons are pairwise, like in Java
    if die1 == die2 and die2 == die3 and die1 == die3:
        return False
        
    if die1 + die2 + die3 > 10:
        return True
    else:
        return False
        
def main():

    num_iterations = 1000  # Number of simulated trials 
    num_wins = 0  # Number of even results
    
    # Python for loop using range
    for trial in range(num_iterations):
    
        # simulate() returns True or False
        if simulate():
            num_wins += 1
      
    
    # Fraction of even rolls
    # Division is exact in Python 3, even if both inputs are integer
    frac_win = num_wins / num_iterations
      
    # Print using the %f format specifier
    print('The probability of winning the big bet in sic bo is about %f.'% frac_even)
    
    
# Call main() when this program runs
if __name__ == '__main__':
    main()
```
