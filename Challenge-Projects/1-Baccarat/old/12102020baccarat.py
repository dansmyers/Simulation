#!/usr/bin/python3

"""
noah olmstead harvey
baccarat
12102020
this script calculates baccarat odds
"""

####  IMPORTS  #################################################################################################################

from random import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

####  FUNCTIONS  ###############################################################################################################

def compare(player, banker):                                    ####  returns (PLAYER,BANKER,TIE) 1=win 0=lose  ################
    if(player==banker):                                         #  if the players score and the bankers score are the same
        return(0,0,1)                                           #  ,,TIE
    elif(player>banker):                                        #  else if the players score is higher
        return(1,0,0)                                           #  PLAYER,,
    else:                                                       #  else
        return(0,1,0)                                           #  ,BANKER,

def getCard(cards = [0 for i in range(10)]):                    ####  returns a cards from given array of card numbers
    cardCount = sum(cards);                                     #  total number of cards in shoe
    value = ((int)(random()*cardCount))                         #  an "index" of a random card (weighted by given cards)
    for i,e in enumerate(cards):                                #  iterate through cards array values with a counter/index
        value-=i                                                #  subtract the cards of value i from value
        if(value<=0):                                           #  if value<=0 index of cards is value to return...
            value = e                                           #  ...store the correct index in value
            break                                               #  ...break out of for loop
    while(cardsLeft[value] <= 0):                               #  if there are no cards left in shoe of that value: redraw
        value = ((int)(random()*cardCount))                     #  an "index" of a random card (weighted by given cards)
        for i,e in enumerate(cards):                            #  iterate through cards array values with counter/index
            value-=i                                            #  subtract the cards of value i from value
            if(value<=0):                                       #  if value<=0 index of cards is value to return...
                value = e                                       #  ...store the correct index in value
                break                                           #  ...break out of for loop                          
    return(value)                                               #  return value of drawn card

def draw(cardsPlayed, decks = 0):                               ####  returns a card value based deck size and cards played  ###
                                                                ##     INFINITE DECK CASE (THE EASIEST)    #####################
    if(decks==0):                                               #  DEFAULT value (if the user doesnt pass a 2nd arg decks = 0)
        value=((int)(random()*13))                              #  value = (int cast)((0.0-.9999)*13) [0:13] (A-10,K,Q,J = 13)
        cardValue=(0 if value<=3 else (value-3))                #  K,Q,J,10 get new value of 0
        cardsPlayed[cardValue]+=1                               #  update cardsPlayed (not needed for infinite deck)
        return(cardsPlayed, cardValue)                          #  returns cardsPlayed and the value of the drawn card
    elif(decks==1):                                             ##    SLIGHTLY HARDER CASE    ##################################
        if(sum(cardsPlayed)>=36):                               #  resuffle when there are 16 cards left in shoe (pos cut card)
            cardsPlayed = [0 for i in range(10)]                #  resuffle if at end of shoe
        cardsLeft=[4-i for i in cardsPlayed]                    #  # of cards of index value
        cardsLeft[0]+=12                                        #  add extra zero value cards (1*4*(4-1))
        value = getCard(cardsLeft)                              #  get weighted random value of card given cards left
        cardsPlayed[value] += 1                                 #  keep track of cards played
        return(cardsPlayed, value)                              #  returns cardsList and the value of the drawn card
    elif(decks==8):                                             ##    BACCARAT STANDARD CASE    ################################
        if(sum(cardsPlayed)>=400):                              #  resuffle when there are 16 cards left in shoe (pos cut card)
            cardsPlayed = [0 for i in range(10)]                #  resuffle if at end of shoe
        cardsLeft=[32-i for i in cardsPlayed]                   #  # of cards of index value
        cardsLeft[0]+=96                                        #  add extra zero value cards (8*4*(4-1))
        value = getCard(cardsLeft)                              #  get weighted random value of card given cards left
        cardsPlayed[value]+=1                                   #  keep track of cards played
        return(cardsPlayed, value)                              #  returns cardsList and the value of the drawn card
    else:                                                       ##    DEFAULT CASE    ##########################################
        pass                                                    #  pass

def playRound(cardsPlayed = [0 for i in range(10)], decks = 0): ####  this function handles each round and returns counters  ###
    tableau = [True,True,True,True,True,True,True,True,True,    #  a "9x7" array of bools for when the banker draws a third card
               True,True,True,True,True,True,True,True,True,
               True,True,True,True,True,True,True,True,True,
               True,True,True,True,True,True,True,False,True,
               False,False,True,True,True,True,True,False,False,
               False,False,False,False,True,True,True,True,False,False,
               False,False,False,False,False,False,True,True,False,False,
               False,False,False,False,False,False,False,False,False,False,]

    cardsPlayed, playerCardOne = draw(cardsPlayed)              #  update cardsPlayed and draw players first card
    cardsPlayed, playerCardTwo = draw(cardsPlayed)              #  update cardsPlayed and draw players second card
    cardsPlayed, bankerCardOne = draw(cardsPlayed)              #  update cardsPlayed and draw bankers first card
    cardsPlayed, bankerCardTwo = draw(cardsPlayed)              #  update cardsPlayed and draw bankers second card
    #print(f"{playerCardOne} {playerCardTwo} ",end='')                                                         ##  DEBUGGING  ##
    player = ((playerCardOne+playerCardTwo)%10)                 #  calculate players score
    banker = ((bankerCardOne+bankerCardTwo)%10)                 #  calculate bankers score

    if(8<=player<=9 or 8<=banker<=9):                           #  natural check (player or banker has score of 8 or 9)
        #print(f"| {bankerCardOne} {bankerCardTwo}",end='\n')                                                  ##  DEBUGGING  ##
        return(cardsPlayed,compare(player,banker))              #  if either hand is natural the round is over

    if(player<=5):                                              #  players score  5 or less
        cardsPlayed, playerCardThree = draw(cardsPlayed)        #  update cardsPlayed and draw players third card
        #print(f"{playerCardThree} | {bankerCardOne} {bankerCardTwo}",end='')                                  ##  DEBUGGING  ##
        player = ((player+playerCardThree)%10)                  #  recalculate players score
        if(tableau[((banker*9)+playerCardThree)]):              #  check tableau to see if banker draws [rows+colomns]
            cardsPlayed, bankerCardThree = draw(cardsPlayed)    #  update cardsPlayed and draw bankers third card
            #print(f" {bankerCardThree}",end='')                                                               ##  DEBUGGING  ##
            banker = ((banker+bankerCardThree)%10)              #  recalculate bankers score
    elif(banker<=5):                                            #  player stood on 6/7 and bankers score <= 5
        cardsPlayed, bankerCardThree = draw(cardsPlayed)        #  update cardsPlayed and draw bankers third card
        #print(f"| {bankerCardOne} {bankerCardTwo} {bankerCardThree}",end='')                                  ##  DEBUGGING  ##
        banker = ((banker+bankerCardThree)%10)                  #  recalculate bankers score
    #else: print(f"| {bankerCardOne} {bankerCardTwo}",end='')                                                  ##  DEBUGGING  ##
    #print()                                                                                                   ##  DEBUGGING  ##
    return(cardsPlayed,compare(player,banker))                  #  return the result of comparing the scores

def playGame(rounds, decks = 0):                                ####  this function plays a given number of rounds  ############
    p,b,t = 0,0,0                                               #  ints to hold total wins
    shoe = [0 for i in range(10)]                               #  the number of each card value (updated as games are played)
    for i in range(rounds):                                     #  play a given number of rounds
        shoe,result = playRound(shoe, decks)                    #  store the result of the round and the cards left
        p += result[0]                                          #  update player wins
        b += result[1]                                          #  update banker wins
        t += result[2]                                          #  update tie wins
    return((p/rounds), (b/rounds), (t/rounds))                  #  return average player, banker, and tie wins

####  MAIN  ####################################################################################################################

runs = 10000                                                    #  number of rounds to play (per game)
games = 64                                                      #  number of games
pResults0 = [0 for i in range(games)]
bResults0 = [0 for i in range(games)]
tResults0 = [0 for i in range(games)]
pResults1 = [0 for i in range(games)]
bResults1 = [0 for i in range(games)]
tResults1 = [0 for i in range(games)]
pResults8 = [0 for i in range(games)]
bResults8 = [0 for i in range(games)]
tResults8 = [0 for i in range(games)]
for i in range(games):                                          #  play (64) games with (10000) rounds each
    results = playGame(runs, 0)                                 #  infinite deck
    pResults0[i] = results[0]
    bResults0[i] = results[1]
    tResults0[i] = results[2]
    print(f"{pResults0[i]} {bResults0[i]} {tResults0[i]}\n")                                                   ##  DEBUGGING  ##
for i in range(games):                                          #  play (64) games with (10000) rounds each
    results = playGame(runs, 1)                                 #  one deck
    pResults1[i] = results[0]
    bResults1[i] = results[1]
    tResults1[i] = results[2]
    print(f"{pResults1[i]} {bResults1[i]} {tResults1[i]}\n")                                                   ##  DEBUGGING  ##
for i in range(games):                                          #  play (64) games with (10000) rounds each
    results = playGame(runs, 8)                                 #  eight decks (baccarat standard)
    pResults8[i] = results[0]
    bResults8[i] = results[1]
    tResults8[i] = results[2]
    print(f"{pResults8[i]} {bResults8[i]} {tResults8[i]}\n")                                                   ##  DEBUGGING  ##

plt.figure(1)
plt.boxplot(pResults0)
plt.title(f"Player Win Chance (Infinite Deck)\nAverage: {(sum(pResults0)/len(pResults0))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratPlayerInfiniteDeckResults.pdf")
plt.figure(2)
plt.boxplot(bResults0)
plt.title(f"Banker Win Chance (Infinite Deck)\nAverage: {(sum(bResults0)/len(bResults0))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratBankerInfiniteDeckResults.pdf")
plt.figure(3)
plt.boxplot(tResults0)
plt.title(f"Tie Game Chance (Infinite Deck)\nAverage: {(sum(tResults0)/len(tResults0))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratTieInfiniteDeckResults.pdf")
plt.figure(4)
plt.boxplot(pResults1)
plt.title(f"Player Win Chance (One Deck)\nAverage: {(sum(pResults1)/len(pResults1))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratPlayerOneDeckResults.pdf")
plt.figure(5)
plt.boxplot(bResults1)
plt.title(f"Banker Win Chance (One Deck)\nAverage: {(sum(bResults1)/len(bResults1))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratBankerOneDeckResults.pdf")
plt.figure(6)
plt.boxplot(tResults1)
plt.title(f"Tie Game Chance (One Deck)\nAverage: {(sum(tResults1)/len(tResults1))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratTieOneDeckResults.pdf")
plt.figure(7)
plt.boxplot(pResults8)
plt.title(f"Player Win Chance (Eight Decks)\nAverage: {(sum(pResults8)/len(pResults8))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratPlayerEightDeckResults.pdf")
plt.figure(8)
plt.boxplot(bResults8)
plt.title(f"Banker Win Chance (Eight Decks)\nAverage: {(sum(bResults8)/len(bResults8))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratBankerEightDeckResults.pdf")
plt.figure(9)
plt.boxplot(tResults8)
plt.title(f"Tie Game Chance (Eight Decks)\nAverage: {(sum(tResults8)/len(tResults8))}")
plt.xlabel("")
plt.ylabel("Probability")
plt.savefig("baccaratTieEightDeckResults.pdf")