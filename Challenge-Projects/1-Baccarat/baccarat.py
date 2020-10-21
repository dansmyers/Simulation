#!/usr/bin/python3

"""
noah olmstead harvey
baccarat
<<<<<<< HEAD
<<<<<<< HEAD
21102020
=======
12102020
>>>>>>> added sprint 2 deliverable and challenge1 solution
=======
21102020
>>>>>>> updated baccarat challenge to take advantage of python strings to simplify code and changed outputed plot of results
this script calculates baccarat odds
"""

####  IMPORTS  #################################################################################################################

from random import random
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
####  FUNCTIONS  ###############################################################################################################

def compare(player, banker):                                    ####  returns (PLAYER,BANKER,TIE) 1=win 0=lose  ################
    if(player==banker):                                         #  if the players score and the bankers score are the same
        return(0,0,1)                                           #  ,,TIE
    elif(player>banker):                                        #  else if the players score is higher
        return(1,0,0)                                           #  PLAYER,,
    else:                                                       #  else
        return(0,1,0)                                           #  ,BANKER,
=======
####  GLOBALS  #################################################################################################################
>>>>>>> updated baccarat challenge to take advantage of python strings to simplify code and changed outputed plot of results

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

<<<<<<< HEAD
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
>>>>>>> added sprint 2 deliverable and challenge1 solution
=======
plt.figure(figsize=(16,6))
plt.boxplot([t8,b8,p8],labels=["TIE","BANKER","PLAYER"],vert=False)
plt.title("STANDARD BACCARAT PROBABILITIES")
plt.xlabel(f"\nPLAYER: {(sum(p8)/len(p8))}\nBANKER: {(sum(b8)/len(b8))}\n   TIE: {(sum(t8)/len(t8))}")
plt.savefig("baccaratResults.pdf",bbox_inches="tight")
>>>>>>> updated baccarat challenge to take advantage of python strings to simplify code and changed outputed plot of results
