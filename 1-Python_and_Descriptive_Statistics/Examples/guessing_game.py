"""
A number guessing game

Demonstrates the while loop and conditionals
"""

# randint is another random function that generates integers from a given range
from random import randint

# Pick a random target value
target = randint(1, 1000)

guesses_remaining = 10

while guesses_remaining > 0:
    
    # Prompt for a guess
    #
    # Recall: the int function casts the string input to an integer value
    guess = int(input('Guess a number between 1 and 1000: '))
    
    # Test if the guess is too high, too low, or correct
    if guess > target:
        print('Too high!')
        guesses_remaining = guesses_remaining - 1
        
    elif guess < target:
        print('Too low!')
        guesses_remaining = guesses_remaining - 1

    else:
        print('Correct!')
        break  # End the current loop immediately, proceed to the code after the loop
    
# Print a message based on whether the user found the correct answer
if guesses_remaining == 0:
    print('Better luck next time!')
else:
    print('Good job!')
