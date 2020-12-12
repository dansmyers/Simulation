import random
from random import randint
cards =[]
started = 0




def populate_deck():
    global cards
    global started
    
    if started == 0:
        started = 1 
    else:
        cards = []
 
    #Populate values for non face cards and aces
    #4 of each value, suit is irrelevant
  
    
    for j in range (0, 8):
     for i in range(1,10):
        cards.append(i)
        cards.append(i)
        cards.append(i)
        cards.append(i)
    
    #Populate values (0's) for all face cards and 10's
     for i in range(0,13):
        cards.append(0)
       
#Return 1 if player wins, 0 if banker wins
def simulate():
    banker = 0
    player = 0
    
    #Give banker and player 2 cards to start
    for i in range(0, 3):
         card = randint(0, len(cards) - 1);
         if i % 2 == 0:
             banker += cards[card]
         else:
              player += cards[card]
         cards.pop(card)     
    

    #See if there were naturals
    if(player % 10 == 8 or player % 10 == 9):
        if(banker % 10 == 8 or banker % 10 == 9):
            return 2;
        else:
            return 1;
    elif(banker % 10 == 8 or banker % 10 == 9):
        if(player % 10 == 8 or player % 10 == 9):
            return 2;
        else:
            return 0;
    
    
    #Check if the player gets another card
    #If yes, keep track of the value of the card 
    stood = 0 
    third_card = 0
    if (player % 10 == 6 or player % 10 == 7):
        player = player % 10
    else:
        card = randint(0, len(cards) - 1);
        third_card = cards[card]
        player += cards[card]
        cards.pop(card)
        player = player % 10
        stood = 1
    
    
    #If the player stood, execute the banker's hand
    if stood == 0:
        if (banker % 10 == 6 or banker % 10 == 7):
            banker = banker % 10
        else:
            card = randint(0, len(cards) - 1);
            banker += cards[card]
            cards.pop(card)
            banker = banker % 10
    #Excecute banker rules if they took another card
    else:
        if banker % 10 == 2:
            card = randint(0, len(cards) - 1);
            banker += cards[card]
            cards.pop(card)
            banker = banker % 10
        elif banker % 10 == 3 and third_card != 8:
            card = randint(0, len(cards) - 1);
            banker += cards[card]
            cards.pop(card)
            banker = banker % 10
        elif banker % 10 == 4 and third_card != 10 or 9 or 8 or 1 or 0:
            card = randint(0, len(cards) - 1);
            banker += cards[card]
            cards.pop(card)
            banker = banker % 10
        elif banker % 10 == 5 and third_card == 4 or 5 or 6 or 7:
            card = randint(0, len(cards) - 1);
            banker += cards[card]
            cards.pop(card)
            banker = banker % 10
        elif banker % 10 == 6 and third_card == 6 or 7:
            card = randint(0, len(cards) - 1);
            banker += cards[card]
            cards.pop(card)
            banker = banker % 10
        else:
            banker = banker % 10
   
    
    if(banker % 10 > player % 10):
        return 0
    elif(banker % 10 < player % 10):
        return 1
    else:
        return 2
        

def main():
    player_wins = 0 
    banker_wins = 0
    tie = 0
    

    
    for i in range(0,10000):
        populate_deck()
        outcome = simulate()
        if outcome == 0:
            banker_wins += 1
           
        elif outcome == 1:
            player_wins += 1
           
        else: 
            tie += 1 
            tie += 10
            
    banker_bets = .95 * banker_wins
   
    print("Winnings over 10000 trials:")
    print("Player bet winnings:" , player_wins)
    print("Banker bet winnings: " , banker_bets)

   
    
    
if __name__ == '__main__':
    main()