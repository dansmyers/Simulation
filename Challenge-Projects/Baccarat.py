""" 

Simulate the card game Baccarat
the winner of the game is represented as integers:
0: Player wins
1: Banker wins
2: Tie

***Little observation, because the third card rule changes the hands of both plaer and bankers
   it is very unlikely that the tie is the winning case. 

"""
# Import libraries needed.
from random import randint

<<<<<<< HEAD
# Helper functions
def show_hands(hands):
    print("The hand is:", hands)
=======

#########  Helper Functions  ########################################################################

# set_up_deck function: set up the deck for a game based on the number of deck we play
# input: number of deck, output: full deck in string representation

def set_up_deck(num_deck):
    ranks = "1234567890000"
    single_deck = ranks * 4
    
    if ( num_deck == 0 or num_deck ==1 ):
        return single_deck
    else:
        return (single_deck * num_deck)

# draw_card 
def draw_card(deck, num_deck = 0):
    
    # drawing a card from the deck
    card_Index = randint(0,len(deck) - 1)
    card = int(deck[card_Index])
    
    # if we were not using the infinite deck, we want to make sure to eliminate the deck
    if num_deck != 0:
        deck = (deck[:card_Index] + deck[card_Index:])
        
    return card

def show_hands(hands):
    print("The hand is:", hands)
    
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
def ending_round(player, banker):

    if ( player> banker ):          # when player wins
        return 0
    elif ( player < banker ):       # when banker wins
        return 1
    else:                           # when tied.
        return 2

<<<<<<< HEAD
def third_draw(hands):
=======
def third_draw(hands, game_deck, num_deck):
    """
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
    third_draw = randint(1, 13)
    if ( 10 <= third_draw <=13 ):
        hands.append(0)
    else:
        hands.append(third_draw)
<<<<<<< HEAD
    return hands


# Simulate the baccarat game, return 0 if player wins, 1 if banker wins and 2 if the game tied. 

def simulate():
=======
    """
    hands.append(draw_card(game_deck, num_deck))
    return hands




# Simulate the baccarat game, return 0 if player wins, 1 if banker wins and 2 if the game tied. 

def simulate(num_deck = 0):
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
    
    # list to keep their hands
    player_hands = []               # player's hands
    banker_hands = []               # banker's hands
    winner = 0                      # initializing winner which what simulate will return at the end
<<<<<<< HEAD
    for x in range(2):
        p_draw = randint(1, 13)
        b_draw = randint(1, 13)
        
        if ( 10 <=p_draw<= 13 ):
            p_draw = 0
        elif ( 10 <=p_draw<= 13 ):
            b_draw = 0
        player_hands.append(p_draw)
        banker_hands.append(b_draw)
            
=======
    game_deck = set_up_deck(num_deck)
    
    print(game_deck)                # debugging
    for x in range(2):

        player_hands.append(draw_card(game_deck, num_deck))
        banker_hands.append(draw_card(game_deck, num_deck))
        
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
    # Implementing third card rule 
    
    """
    IMPORTANT: we must apply the thrid card rule of player hands first not the bankers because bankers card rule is 
               is based on the player card values.
    """ 
    
    # we first need the hands value of both player and banker
    
    p_value = sum(player_hands) % 10
    b_value = sum(banker_hands) % 10
    
    # showing the hands
    print("The player's hands")
    show_hands(player_hands)
    print("The banker's hands")
    show_hands(banker_hands)
    
    # first rule if at least one of the hands acheive the value of 8 or 9 game immediately ends
    if ( (8 <= p_value <= 9) or (8 <= b_value <= 9) ):
        print("The natural was announced, end of this round")
        winner = ending_round(p_value, b_value)
        return winner
    
    # Let the third card distribution begin!
    if ( 0 <= p_value <=5 ):                # plaer's third card rule
        print("Player draws third card")
<<<<<<< HEAD
        player_hands = third_draw(player_hands)
=======
        player_hands = third_draw(player_hands, game_deck, num_deck)
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
       
       
    print("After third draw player's hands")
    show_hands(player_hands)
    p_value = sum(player_hands) % 10        # update the player's hand value
    
    if ( 0 <= b_value <= 2 ):                # if the banker's hand value is less than or equal 2 then draw third card
        print("Banker draws third card regardless")
<<<<<<< HEAD
        banker_hands = third_draw(banker_hands)

    elif ( (b_value == 3) and (player_hands[-1] != 8) ):
        print("Banker's third draw with hands value 3")
        banker_hands = third_draw(banker_hands)

    elif( (b_value == 4) and (2 <= player_hands[-1] <= 7) ):
        print("Banker's third draw with hands value 4")
        banker_hands = third_draw(banker_hands)

    elif ( (b_value == 5) and (4 <= player_hands[-1] <= 7) ):
        print("Banker's third draw with hands value 5")
        banker_hands = third_draw(banker_hands)

    elif ( (b_value == 6) and ( 5 <= player_hands[-1] <=7) ):
        print("Banker's third draw with hands value 6")
        banker_hands = third_draw(banker_hands)
=======
        banker_hands = third_draw(banker_hands, game_deck, num_deck)

    elif ( (b_value == 3) and (player_hands[-1] != 8) ):
        print("Banker's third draw with hands value 3")
        banker_hands = third_draw(banker_hands, game_deck, num_deck)

    elif( (b_value == 4) and (2 <= player_hands[-1] <= 7) ):
        print("Banker's third draw with hands value 4")
        banker_hands = third_draw(banker_hands, game_deck, num_deck)

    elif ( (b_value == 5) and (4 <= player_hands[-1] <= 7) ):
        print("Banker's third draw with hands value 5")
        banker_hands = third_draw(banker_hands, game_deck, num_deck)

    elif ( (b_value == 6) and ( 5 <= player_hands[-1] <=7) ):
        print("Banker's third draw with hands value 6")
        banker_hands = third_draw(banker_hands, game_deck, num_deck)
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
    
    # when the banker's hand value is 7, banker stands
    print("After third draw banker's hands")
    show_hands(banker_hands)
    b_value = sum(banker_hands) % 10
    
    # the end of the round
    
    winner = ending_round(p_value, b_value)
    
    return winner
    

if __name__ == '__main__':
    
<<<<<<< HEAD
    w = simulate()
    
    if ( w == 0):
        print("The winner of the first Baccarat round is: Player")
    elif (w == 1):
        print("The winner of the first Baccarat round is: Banker")
    else:
        print("The winner of the first Baccarat round is: Tie")
=======
    w = simulate(8)
    p,b,t = 0,0,0
    if ( w == 0):
        print("The winner of the first Baccarat round is: Player")
        p += 1
    elif (w == 1):
        print("The winner of the first Baccarat round is: Banker")
        b += 1
    else:
        print("The winner of the first Baccarat round is: Tie")
        t += 1
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
    