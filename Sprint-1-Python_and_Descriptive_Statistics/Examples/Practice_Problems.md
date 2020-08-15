# Python Practice Problems

Write Python programs for the following problems. These are for your own practice and will help you become comfortable with basic 
elements of Python programming. **You don't need to submit your answers for these.**

## Problems

### Smoots

Oliver R. Smoot is an MIT graduate and former head of the American National Standards Institute (ANSI) and the International Organization for Standards (ISO).

In 1958, as part of his initiation into ΛXA, Smoot and his brothers measured the entire length of Harvard Bridge over the Charles River in Cambridge, MA, using Smoot’s body as the ruler. He was at the time 170 cm tall (5 feet, 7 inches), and the bridge was declared to be 364.4 Smoots, "plus or minus one ear" (about 2035 feet or 650.7 meters). Since that time, the measurement of Harvard Bridge has always been denominated in Smoots, with the markings repainted each year by the incoming ΛXA pledge class at MIT. The Cambridge police use the Smoot markings to identify the location of accidents on the bridge.

<img src="https://alum.mit.edu/sites/default/files/styles/article_desktop/public/images/SMOOT.jpg?itok=jMC7rC_T" width="50%" />

Write a program that can take a bridge length measured in feet and convert it to units of Smoots. Your program should add the statement "plus or minus one ear" to the measurement it reports.

Tip: one Smoot is about 5.5833 feet.

Tip-tip: use Python's `input` function to read from the terminal.


### If They're the Super Mario Brothers, Does That Mean His Name is Mario Mario?

At the end of each level in the original *Super Mario Bros.*, Mario jumps up a stair like the following:

```
     ##
    ###
   ####
  #####
 ######
#######
```

Write a set of loops that print Mario-style stairs of arbitrary height.

Tip: the first line has `height - 1` spaces and 2 blocks. The second line has `height - 2` spaces and 3 blocks.

Tip-tip: use an outer `for` loop to iterate over the levels of the staircase; you can use inner loops to print the spaces and stars, or read about Python's 
**string multiplication** feature, which is very convenient for generating repeated strings.


### RPS

Write a rock-paper-scissors game. Use the template below as a starting point and fill in the rest of the sections.

```
"""
A Rock-Paper-Scissors game that plays one round of human vs. computer
"""

# Import the randint method
from random import randint

# Declare constant variables representing the three moves
# Map each move to a number, but refer to them by name in the rest of the program
#
# Using CAPITALIZATION to indicate constants is standard style, but Python
# doesn't have a way to enforce that a variable is constant
ROCK = 1
PAPER = 2
SCISSORS = 3

# Print the welcome message and list the three moves
print('Welcome, pathetic human, to Rock-Paper-Scissors.')
print()
print('1. ROCK')
print('2. PAPER')
print('3.SCISSORS')

# Read the user's move
move = int(input('Select a move to form with your clumsy and imprecise meat-hands: '))

# If the move is not ROCK, PAPER, or SCISSORS, exit the program

# Randomly generate the CPU's move using randint

# Print a message declaring the CPU's move

# Easy case: if the player and CPU's moves are the same, it's a tie

# Fill in the other cases

```

### 10001st Prime (Project Euler #7)

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Tips:

The basic strategy is something like this:

```
n = 2;
numPrimes = 0;

while True:
    if (isPrime(n)):
        numPrimes += 1
    
    if numPrimes == 10001:
        print(n)
        break
    else:
        n += 1
```

Think about how to test if a number is prime, then write an `is_prime(n)` function that returns `True` if the input number `n` is prime and `False` otherwise. The straightforward way is to test for divisibility by any numbers between 2 and `sqrt(n)`.

Tip: you can do a little better if you recognize that 2 is a special case as the only even prime. Start with 3 and then advance by 2 on each iteration.

Tip-tip: if you want to be even fancier (which, of course, you do), you could use a list to keep track of the primes you find. It's then sufficient to test for divisibility by the **primes** that are less than or equal to `sqrt(n)`, which will be much faster than grinding up through the sequential numbers.

You can try the straightforward solution first. If it runs for more than, say, a minute, try implementing the faster solution.
