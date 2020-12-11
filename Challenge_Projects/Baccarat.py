"""
Alejandra De Osma 

CMS 380 
Challenge Projects: 
Project number 1 : Baccarat 

This program will simulate a game of Baccarat, which was a traditional gambling game played in the james bond movies.

"""
import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt 

import random 

"""
CLASSES ####################################################
"""
# This is the card class 
# Identifies that a card has a value and a suit
class Card:
    def __init__(x,value, suit):
        x.value = value
        x.suit = suit
    
    # Sets the string for the card 
    # Includes the suit of the card and the value
    def __str__(x):
        string = ""
        string = string + x.suit +""+str(s.value)
        return string
        

"""
FUNCTIONS  ####################################################
"""       
# This function generated a new deck
def n_deck():
    
    # Identifies all possible suits:
    suits = ['Hearts','Spades','Diamonds','Clubs']
    
    # generates a deck:
    deck_1 = [Card(value, suit) for value in range(1, 14) for suit in suits for i in range(0,8)]
    
    # After the deck is created 
    # We shuffle it to randomize the order of its cards
    random.shuffle(deck_1)
    
    # Returns the deck
    return deck_1
    
# This funcgion prints the deck 
def  print_d(deck):
    # Local variable string 
    string = ""
    # Iteratesd through every card in the deck
    for card in deck:
        # Adds the card as a string to the local string
        string = string + str(card) + "||"
        
    # Finally, Prints the complete string     
    print(string)
    
# Thie function calculates the scores for all player_Score
# Takes the players cards as an argument
def check_score(hand):
    # Local variable s keeps track of score
    s = 0 
    # Iterates though cards and updates score
    for card in hand:
        # gets the value of the individual card 
        v = card.value 
        if v == 1:
            # Score +1 if the value of the card is == to 1
            s += 1
        elif 2 <= v <= 9:
            # Score + the value of the card if the card's value is between 2 and 9 
            s += v
    # Returns the total score %10 
    return s%10 

# This fuction simulates a round of baccarat 
def Simulation():
    # Initializing decks:
    deck = n_deck()
    deck_1 = 3
    
    # Initializing player and banker:
    
    player = [deck[0], deck[2]]
    banker = [deck[1], deck[3]]
    
    # Initializing the score of both players:
    player_Score = check_score(player)
    banker_Score = check_score(banker)
    
    # Winning conditions: 
    
    # Conditions for a tie 
    if player_Score >= 8 and banker_Score >= 8:
        return (0,0,1) 
    
    # Conditions for a player win:
    elif(player_Score >= 8):
        return (1,0,0)
        
    # conditions for a banker win:
    elif(banker_Score >= 8): 
        return (0,1,0) 
        
    # Remaining conditions:
    else:
        if player_Score < 6 :
            # If the players current score is smaller than 6 then:
            deck_1 += 1 
            player.append(deck[deck_1])
            
            if banker_Score <= 2:
            # If banker score is smaller or equal to 2 deck_1 +1 
                deck_1 += 1
                # appending deck_1 to deck
                banker.append(deck[deck_1])
                    
            elif banker_Score == 3 and player[2].value !=8:
            # If banker score is == 3 and players card not equal to 8 deck_1 +1: 
                deck_1 += 1
                # appending to banker 
                banker.append(deck[deck_1])
                
            elif banker_Score == 4 and 2 <= player[2].value <= 7:
            # If bankers score is equal to 4 and players card is bigger than 2 and smaller or equal to 7:
                deck_1 += 1
                # appending to banker:
                banker.append(deck[deck_1])
                
            elif banker_Score == 5 and 4 <= player[2].value <=7:
            # If banker score is equal to 5 and players card is between 4 and 7:
                deck_1 += 1
                # Append to banker
                banker.append(deck[deck_1])
                
            elif banker_Score == 6 and 6 <= player[2].value <= 7:
                # If bankers score is equal to 6 and players card is either 6 or 7
                deck_1 += 1
                # Append to banker 
                banker.append(deck[deck_1])
                    
        else:
            # Remaining conditions:
            if banker_Score < 6:
                deck_1 += 1
                banker.append(deck[deck_1])
                
    # Update both scores of player and banker:
    player_Score = check_score(player)
    banker_Score= check_score(banker)
    
    # Difnie who won the round:
    
    # Player won:
    if (player_Score > banker_Score):
        return (1,0,0)
    # Banker won:
    elif(banker_Score > player_Score):
        return (0,1,0)
    # Tie between players:
    else:
        return (0,0,1)
        
        
# This function playes a certain number of rounds
# Tkaes the number of rounds wanted to played as an argument:
def play(rounds):
    # local variables keeps track of wins each round:
    
    # Player wins:
    p = 0
    # Banker wins:
    b = 0
    # Ties:
    t = 0
    
    #Runs simulation for a number or rounds:
    for i in range(rounds):
        result = Simulation()
        
        # based on the results adds them to each individual variable:
        p += result[0]
        b += result[1]
        t += result[2]
        
    # Returns the avarage (wins / rounds)
    return (p/rounds),(b/rounds),(t/rounds)
    
# main     
def main():
    
    # number of rounds to be simulated:
    rounds = 10000
    
    # played games:
    games = 64 
    
    player_wins = [0 for i in range(games)]
    
    banker_wins = [0 for i in range(games)]
    
    tie_wins = [0 for i in range(games)]
    
    for i in range(games):
        result = play(rounds)
        # appending each game results to each winner: 
        player_wins[i] = result[0]
        banker_wins[i] = result[1]
        tie_wins[i] = result[2]
     
    # Printing the average wins for each result:
    
    # Average player wins, adds wins diveds them by the length of array
    print("Player Average Win:",sum(player_wins)/len(player_wins))
    
    # Average banker wins, adds wins diveds them by the length of array
    print("Banker Average Win:",sum(banker_wins)/len(banker_wins))
    
    # Average ties, adds ties diveds them by the length of array
    print ("Ties Average Win:",sum(tie_wins)/len(tie_wins))

    """
    Plots
    """
    # Generating a box-plot to interprate the gathered data
    # Box plot for Average player wins:
    plt.figure(1)
    plt.boxplot(player_wins)
    plt.title(f"Player Winning Chance Averages:")
    plt.ylabel("Probability")
    plt.savefig("Baccarat_player_boxplt.pdf")

    # Figure 2, boxplot for banker average wins:
    plt.figure(2)
    plt.boxplot(banker_wins)
    plt.title(f"Banker Winning Chance Averages")
    plt.ylabel("Probability")
    plt.savefig("Baccarat_Banker_boxplt.pdf")

    # Figue 3, boxplot for average ties:
    plt.figure(3)
    plt.boxplot(tie_wins)
    plt.title("Chance of Tying Averages")
    plt.ylabel("Probability")
    plt.savefig("Baccarat_Ties_boxplt.pdf")

"""
Main
"""
# Main call, running program

if(__name__=="__main__"):
    main()
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
            
    
    