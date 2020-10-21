#!/usr/bin/python3

"""
noah olmstead harvey
baccarat
21102020
this script calculates baccarat odds
"""

####  IMPORTS  #################################################################################################################

from random import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

####  GLOBALS  #################################################################################################################

tableau = [True,True,True,True,True,True,True,True,True,True,   ####  8x10  T/F array for banker 3rd draw  #####################
           True,True,True,True,True,True,True,True,True,True,
           True,True,True,True,True,True,True,True,True,True,
           True,True,True,True,True,True,True,True,False,True,
           False,False,True,True,True,True,True,True,False,False,
           False,False,False,False,True,True,True,True,False,False,
           False,False,False,False,False,False,True,True,False,False,
           False,False,False,False,False,False,False,False,False,False]

####  FUNCTIONS  ###############################################################################################################

def buildShoe(numDecks = 0):                                    ####  outputs a string with card values given number of decks  #
    suite = "0000987654321"                                     #  K,Q,J,10 = 0 and A = 1, suite as a string
    deck = (suite*4)                                            #  python string multiplication to create a deck of 4 suites
    if(numDecks==0 or numDecks==1):                             #  if there is a single deck or an infinate deck...
        return(deck)                                            #  ...return the deck (string)
    elif(numDecks==8):                                          #  if there are eight decks (baccarat standard)...
        return((deck*8))                                        #  ...return the deck (string) multiplied by 8
    else:                                                       #  if there is an unexpected number of decks...
        print("Unexpected number of decks in shoe...")          #  ...print a message to stdout
        return((deck*numDecks))                                 #  ...return the deck (string) multiplied by given number

def drawCard(deck = ("0000987654321"*4), numDecks = 0):         ####  outputs a card value and the updated deck string  ########
    cardIndex = (int)(random()*len(deck))                       #  cast to int a random num[.0-1) multiplied by deck size
    cardValue = int(deck[cardIndex])                            #  conevert to int the char at the random index in deck string
    if(numDecks!=0):                                            #  if it is not an infinite deck game...
        deck = (deck[:cardIndex]+deck[(cardIndex+1):])          #  ...use python string splicing to update the deck string
    return(cardValue, deck)                                     #  return the card value (int) and the updated deck (string)

def compare(p, b):                                              ####  outputs a tuple (P,B,T) with 1=win 0=loss  ###############
    if(p==b):                                                   #  if the player and the banker have the same score...
        return(0,0,1)                                           #  ...return 0,0,1 (tuple) TIE
    elif(p>b):                                                  #  if the player has a greater score than the banker...
        return(1,0,0)                                           #  ...return 1,0,0 (tuple) PLAYER
    else:                                                       #  if the banker has a greater score than the player...
        return(0,1,0)                                           #  ...return 0,1,0 (tuple) BANKER

def playRound(shoe = ("0000987654321"*4), numDecks = 0):        ####  outputs the updated deck and the round's result  #########
    if(len(shoe)<=16):                                          #  if the shoe has 16 or fewer cards...
        shoe = buildShoe(numDecks)                              #  ...rebuild the shoe
    pCardOne, shoe = drawCard(shoe,numDecks)                    #  draw player's 1st card and update the shoe
    pCardTwo, shoe = drawCard(shoe,numDecks)                    #  draw player's 2nd card and update the shoe
    bCardOne, shoe = drawCard(shoe,numDecks)                    #  draw banker's 1st card and update the shoe
    bCardTwo, shoe = drawCard(shoe,numDecks)                    #  draw banker's 2nd card and update the shoe
    #print(f"{pCardOne} {pCardTwo} ",end='')                                                                   ##  DEBUGGING  ##
    player = ((pCardOne+pCardTwo)%10)                           #  calculate player's score
    banker = ((bCardOne+bCardTwo)%10)                           #  calculate banker's score
    if(8<=player<=9 or 8<=banker<=9):                           #  if either player has a "natural" 8,9...
        #print(f"|{player}| {bCardOne} {bCardTwo} |{banker}|",end='')                                          ##  DEBUGGING  ##
        pass                                                    #  ...skip the rest of the checks
    elif(player<=5):                                            #  elif player has a score of 5 or less...
        pCardThree, shoe = drawCard(shoe,numDecks)              #  ...draw player's 3rd card and update shoe
        player = ((player+pCardThree)%10)                       #  ...recalculate player's score
        #print(f"{pCardThree} |{player}| {bCardOne} {bCardTwo} |{banker}|",end='')                             ##  DEBUGGING  ##
        if(tableau[((banker*10)+pCardThree)]):                  #  ...if the tableau says so...
            bCardThree, shoe = drawCard(shoe,numDecks)          #  ......draw banker's 3rd card and update shoe
            banker = ((banker+bCardThree)%10)                   #  ......recalculate banker's score
            #print(f" {bCardThree} |{banker}|",end='')                                                         ##  DEBUGGING  ##
    elif(banker<=5):                                            #  elif banker has a score of 5 or less...
        bCardThree, shoe = drawCard(shoe,numDecks)              #  ...draw banker's 3rd card and update shoe
        banker = ((banker+bCardThree)%10)                       #  ...recalculate banker's score
        #print(f"| {bCardOne} {bCardTwo} {bCardThree} |{banker}|",end='')                                      ##  DEBUGGING  ##
    #else: print(f"| {bCardOne} {bCardTwo} |{banker}|",end='')                                                 ##  DEBUGGING  ##
    #print(f" ||{len(shoe)}|| {shoe}")                                                                         ##  DEBUGGING  ##
    return(shoe, compare(player,banker))                        #  returns shoe (string) and the results of the round (tuple)

def playGame(numRounds = 1000, numDecks = 0):                   ####  outputs the player, banker, and tie win ratios  ##########
    p,b,t = 0,0,0                                               #  initialize player, banker, and tie variables
    shoe = buildShoe(numDecks)                                  #  create a shoe for the game given the number of decks used
    for i in range(numRounds):                                  #  iterate through the given number of rounds
        shoe,results = playRound(shoe,numDecks)                 #  update the shoe and the results after the round is played
        p += results[0]                                         #  update the player variable based on the results tuple
        b += results[1]                                         #  update the banker variable based on the results tuple
        t += results[2]                                         #  update the tie variable based on the results tuple
    return((p/numRounds),(b/numRounds),(t/numRounds))           #  return player, banker, and tie win ratios (tuple)

####  MAIN  ####################################################################################################################

p8,b8,t8=[],[],[]
for i in range(1000):
    results = playGame(10000,8)
    p8.append(results[0])
    b8.append(results[1])
    t8.append(results[2])
print(f"\nPLAYER(8):  {(sum(p8)/len(p8))}\nBANKER(8):  {(sum(b8)/len(b8))}\nTIE(8):     {(sum(t8)/len(t8))}\n")

plt.figure(figsize=(16,6))
plt.boxplot([t8,b8,p8],labels=["TIE","BANKER","PLAYER"],vert=False)
plt.title("STANDARD BACCARAT PROBABILITIES")
plt.xlabel(f"\nPLAYER: {(sum(p8)/len(p8))}\nBANKER: {(sum(b8)/len(b8))}\n   TIE: {(sum(t8)/len(t8))}")
plt.savefig("baccaratResults.pdf",bbox_inches="tight")
