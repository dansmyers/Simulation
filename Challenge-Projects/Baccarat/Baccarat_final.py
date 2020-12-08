"""
Christian Huber
CMS 380, Fall 2020 / Challenge Projects / Baccarat
This script simulates the game "Baccarat" in order to
estimate the probability of winning for the player and
banker bets.
(I also got some help from Noah regarding the String operations)
"""

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

from random import choice



### GLOBAL VARIABLES ###

# Create the Tableau as array of True (Hit) and False (Stand) values
#
# Pl. 3rd   0       1      2      3      4      5      6      7      8      9    Banker's Hand
tableau = [True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  # 0
           True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  # 1
           True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  # 2
           True,  True,  True,  True,  True,  True,  True,  True,  False, True,  # 3
           False, False, True,  True,  True,  True,  True,  True,  False, False, # 4
           False, False, False, False, True,  True,  True,  True,  False, False, # 5
           False, False, False, False, False, False, True,  True,  False, False, # 6
           False, False, False, False, False, False, False, False, False, False] # 7

# A suite of cards -> String is easiest to use
suite = "0000987654321"



###  FUNCTIONS  ###

### Returns the card values, depending on a given number of decks
def new_shoe(num_decks):

    # Mulitply suites to create a deck
    deck = suite * 4

    # Return number of decks asked for
    if(num_decks == 0 or num_decks == 1):
        return deck

    else:
        return deck * 8



### Returns a random card value and the new deck string after draw
def draw(deck, num_decks):

    # Use proprietary 'choice' and '.index' functions
    # to get value and index of a random card
    rand_val = int(choice(deck))
    i = deck.index(str(rand_val))

    # Splice the string to remove the drawn card
    deck = deck[:i] + deck[(i + 1):]

    return rand_val, deck



### Returns the tuple
#
# If player score > banker score: player wins
# Vice versa: banker wins
# Both Equal: Tie
#
# Noted as Win(1), Loss(0) in (Player, Banker, Tie)
def tple(p, b):
    if(p > b):
        return(1, 0, 0)

    elif(p < b):
        return(0, 1, 0)

    else:
        return(0, 0, 1)



### Simulates a coup (round) of baccarat and returns
### the coup results and the updated deck
def play_coup(shoe, num_decks):

    # Rebuild the shoe if it has <16 cards
    if(len(shoe) <= 16):
        shoe = new_shoe(num_decks)

    # Do the first two draws of player and banker and update
    # the shoe each time
    p1, shoe = draw(shoe, num_decks)
    p2, shoe = draw(shoe, num_decks)
    b1, shoe = draw(shoe, num_decks)
    b2, shoe = draw(shoe, num_decks)

    # Calculate respective scores using given formula
    p_score = (p1 + p2) % 10
    b_score = (b1 + b2) % 10

    # Check for naturals (guarantees direct win),
    # skip all other checks (pass) and directly return tuple
    if(8 <= p_score <= 9 or 8 <= b_score <= 9):
        pass

    # Check for a player score of <=5 and allow
    # the player to draw a third card
    elif(p_score <= 5):

        # Draw third card and update shoe
        p3, shoe = draw(shoe, num_decks)
        # Adjust player's score
        p_score = (p_score + p3) % 10

        # Consult the tableau about the banker's next step
        # by accessing the tableau value at the index given
        # the banker's total score and the player's 3rd draw
        #
        # If the value at this index is True, let the banker
        # draw a 3rd card and adjust her score
        if(tableau[(b_score * 10) + p3] == True):
            b3, shoe = draw(shoe, num_decks)
            b_score = (b_score + b3) % 10

    # Check for a banker score of <=5 and allow
    # her to draw a third card
    elif(b_score <= 5):

        # Draw third card and update shoe
        b3, shoe = draw(shoe, num_decks)
        # Adjust banker's score
        b_score = (b_score + b3)%10

    # Return the updated shoe and the tuple
    return shoe, tple(p_score, b_score)



### Simulates a number of coups
#
# Returns the win ratios for the three outcomes
# 1. Player Wins; 2. Banker Wins; 3. Tie
# of one game of Baccarat
def simulate(coups, num_decks):
    p = 0   # player array that will contain win ratios
    b = 0   # banker...
    t = 0   # tie...

    # Create new shoe given the requested number of decks
    shoe = new_shoe(num_decks)

    # Play baccarat for given amount of coups
    for i in range(coups):
        # Results and Shoe array must be updated after each coup
        shoe, results = play_coup(shoe, num_decks)

        # Update arrays with coup touples
        p += results[0]
        b += results[1]
        t += results[2]

    # Calculate and return win ratios from touples
    return(p/coups),(b/coups),(t/coups)



### MAIN ###

# Arrays to store results for each outcome
p = []  # player win ratios
b = []  # banker win ratios
t = []  # tie win ratios

# Simulate the plays of Baccarat
for i in range(1000):
    results = simulate(100,8)
    p.append(results[0])
    b.append(results[1])
    t.append(results[2])

# Print "averaged" probabilities of simulation with a formatted string
print("\nProbabilities of winning Baccarat:\nPlayer:   %2.2f%%\nBanker:   %2.2f%%\nTie:      %2.2f%%\n"
      % ((sum(p)/len(p))*100, (sum(b)/len(b))*100, (sum(t)/len(t))*100))
