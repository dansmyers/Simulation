"""
Fritz Stapfer Paz
11/12/2020 
CMS 380 - Challenge Project 1
Monte Carlo simulator for baccarat that estimates the expected winning probability for the two main bets
"""

# imports ===========================================================

import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt


# classes ===========================================================

class Card:                                                         # Card Object Class
    def __init__(self, value, suit):                                # Constructor
        self.value = value                                          # Card value (1,13)
        self.suit = suit                                            # Card suit
    
    def __str__(self):                                              # to string (return "suit value")
        s = ""                                                      # declare s as string
        s = s + self.suit + " " + str(self.value)                   # update s with card data
        return s                                                    # return Suit Value


# functions =========================================================

def new_deck():                                                     # create the standard 8 decks deck
    suits = ['heart', 'diamonds', 'spades', 'clubs']                # suits list
    deck = [Card(value, suit) for value in range(1, 14) for suit in suits for i in range(0,8)]
    random.shuffle(deck)                                            # shuffle deck
    return deck                                                     # return the deck of cards


def print_deck(deck):                                               # print an entire deck of cards
    s = ""                                                          # declare s as string
    for card in deck:                                               # loop through cards in deck
        s = s + str(card) + " | "                                   # update s with cards
    print(s)                                                        # print the deck


def calculate_score(hand):                                          # calculate the score of a hand
    score = 0;                                                      # declare score as 0
    for card in hand:                                               # loop through cards in hand
        value = card.value                                          # get card value
        if value == 1:                                              # ace is worth 1 point
            score += 1                                              
        elif 2 <= value <= 9:                                       # 2 to 9 are worth their face value
            score += value
    return score%10                                                 # return score (mod 10 of sum of points)


def simulate():                                                     # return who won (PLAYER, BANKER, TIE) where 1 = win
    deck = new_deck()                                               # create deck
    deck_i = 3                                                      # index for last card drawn from deck
    player = [deck[0], deck[2]]                                     # player hand
    banker = [deck[1], deck[3]]                                     # banker hand
    #print_deck(player)                                             # debugging
    #print_deck(banker)                                             # debugging
    p_score = calculate_score(player)                               # calculate score for player hand
    b_score = calculate_score(banker)                               # calculate score for banker hand

    if p_score >= 8 and b_score >= 8:                               # if both are naturals
        return (0,0,1)                                              #   return a tie
    elif(p_score >= 8):                                             # if only player has a natural
        return (1,0,0)                                              #   return player win
    elif(b_score >= 8):                                             # if only banker has a natural
        return (0,1,0)                                              #   return banker win
    else:                                                           # no naturals
        if p_score < 6:                                             # if the player has a score smaller than 5
            deck_i += 1                                                 # DRAW CARD
            player.append(deck[deck_i])                                 # DRAW CARD
            # PLAYER HAS 3 CARDS DRAW A CARD FOR BANKER WHEN
            if b_score <= 2:                                        # the banker has a score <= 2
                deck_i += 1                                             # DRAW CARD
                banker.append(deck[deck_i])                             # DRAW CARD
            elif b_score == 3 and player[2].value != 8:             # the banker has a score of 3 and player's third card not 8
                deck_i += 1                                             # DRAW CARD
                banker.append(deck[deck_i])                             # DRAW CARD
            elif b_score == 4 and 2 <= player[2].value <= 7:        # the banker has a score of 4 and player's third card between 2 and 7
                deck_i += 1                                             # DRAW CARD
                banker.append(deck[deck_i])                             # DRAW CARD
            elif b_score == 5 and 4 <= player[2].value <= 7:        # the banker has a score of 5 and player's third card between 4 and 7
                deck_i += 1                                             # DRAW CARD
                banker.append(deck[deck_i])                             # DRAW CARD
            elif b_score == 6 and 6 <= player[2].value <= 7:        # the banker has a score of 6 and player's third card between 6 and 7
                deck_i += 1                                             # DRAW CARD
                banker.append(deck[deck_i])                             # DRAW CARD
        else:                                                       # if the player has a score of 6 or 7 he stands
            if b_score < 6:                                         # the banker draws on scores smaller than 5
                deck_i += 1                                             # DRAW CARD
                banker.append(deck[deck_i])                             # DRAW CARD
    
    p_score = calculate_score(player)                               # recalculate the player score
    b_score = calculate_score(banker)                               # recalculate the banker score
    
    if(p_score > b_score):                                          # if player has a higher score than banker
        return (1,0,0)                                              # return a win for player
    elif(b_score > p_score):                                        # if banker has a higher score than player
        return (0,1,0)                                              # return a win for banker
    else:                                                           # if they tied
        return (0,0,1)                                              # return a tie


def play(rounds):                                                   # play several rounds and return average wins
    p,b,t = 0,0,0                                                   # ints to hold total wins
    for i in range(rounds):                                         # play a given number of rounds
        result = simulate()                                         # run individual simulation
        p += result[0]                                              # update player wins
        b += result[1]                                              # update banker wins
        t += result[2]                                              # update tie wins
    return((p/rounds), (b/rounds), (t/rounds))                      # return average player, banker, and tie wins


def main():
    rounds = 10000                                                  # number of rounds per game
    games = 64                                                      # number of games
    p_wins = [0 for i in range(games)]                              # player wins list
    b_wins = [0 for i in range(games)]                              # banker wins list
    t_wins = [0 for i in range(games)]                              # tie list
    
    for i in range(games):                                          # run simulation "games" times
        result = play(rounds)                                       # get average from "rounds" simulations
        p_wins[i] = result[0]                                       # update player wins
        b_wins[i] = result[1]                                       # update banker wins
        t_wins[i] = result[2]                                       # update tie wins
    
    print("Player Average Win: ", sum(p_wins)/len(p_wins))          # print average wins for player
    print("Banker Average Win: ", sum(b_wins)/len(b_wins))          # print average wins for player
    print("Ties Average Win: ", sum(t_wins)/len(t_wins))          # print average wins for player
    
    plt.figure(1)                                                   # plot the boxplot for the player wins
    plt.boxplot(p_wins)
    plt.title(f"Player Win Chance\nAverage: {(sum(p_wins)/len(p_wins))}")
    plt.xlabel("")
    plt.ylabel("Probability")
    plt.savefig("baccarat_player.pdf")
    
    plt.figure(2)                                                   # plot the boxplot for the banker wins
    plt.boxplot(b_wins)
    plt.title(f"Banker Win Chance\nAverage: {(sum(b_wins)/len(b_wins))}")
    plt.xlabel("")
    plt.ylabel("Probability")
    plt.savefig("baccarat_banker.pdf")
    
    plt.figure(3)                                                   # plot the boxplot for the ties wins
    plt.boxplot(t_wins)
    plt.title(f"Ties Change\nAverage: {(sum(t_wins)/len(t_wins))}")
    plt.xlabel("")
    plt.ylabel("Probability")
    plt.savefig("baccarat_ties.pdf")

# main ==============================================================
if(__name__=="__main__"): 
    main()