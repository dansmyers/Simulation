import random 

def computeScore(hand):
    total = 0
    for card in hand:
        if(card.rank < 10):
            total += card.rank
    return total % 10

def play(deck):
    random.shuffle(deck)
    
    player_hand = [
        deck.pop(0), deck.pop(0)
    ]
    banker_hand = [
        deck.pop(0), deck.pop(0)
    ]
    
    player_score = computeScore(player_hand)
    banker_score = computeScore(banker_hand)
    
    if player_score in [8, 9] or banker_score in [8, 9]:
        if player_score in [8, 9] and banker_score not in [8, 9]:
            #player win
            return 0
        elif banker_score in [8, 9] and player_score not in [8, 9]:
            #banker win
            return 1
        else:
            #tie
            return 2
            
    #check if player has low hand and give third card
    if player_score <= 5:
        player_hand.append(deck.pop(0))
        
        #check if banker needs third card 
        if (banker_score == 6 and player_hand[2].rank in [6, 7]) or (banker_score == 5 and player_hand[2].rank in [4, 5, 6, 7]) or  (banker_score == 4 and player_hand[2].rank in [2, 3, 4, 5, 6, 7]) or (banker_score == 3 and player_hand[2].rank != 8) or (banker_score <= 2):
            banker_hand.append(deck.pop(0))
            
    
    elif player_score in [6, 7]:
        if banker_score <= 5:
            banker_hand.append(deck.pop(0))
            
    player_score = computeScore(player_hand)
    
    banker_score = computeScore(banker_hand)
    
    
    if(player_score > banker_score):
        #player win
        return 0
    elif(banker_score > player_score):
        #banker win
        return 1
    else:
        #tie
        return 2
        
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

suits = ["HEARTS", "SPADES", "DIAMONDS", "CLUBS"]

total_player_wins = 0
total_banker_wins = 0
total_ties = 0
for i in range(1000):
    deck = [Card(rank, suit) for rank in range(1, 14) for suit in suits]
    result = play(deck)
    if(result == 0):
        total_player_wins += 1
    elif(result == 1):
        total_banker_wins += 1
    else:
        total_ties += 1
        

prob_player = total_player_wins / 1000
prob_banker = total_banker_wins / 1000
prob_tie = total_ties / 1000

print("P(player): " + str(prob_player))
print("P(banker): " + str(prob_banker))
print("P(tie): " + str(prob_tie))
