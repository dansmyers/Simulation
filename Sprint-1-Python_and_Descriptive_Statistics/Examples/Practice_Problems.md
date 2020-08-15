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
