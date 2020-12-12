import random
import math
shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] * 4 * 8
random.shuffle(shoe)

def deal_two_cards():
    global shoe
    
     # Check if the current shoe needs to be reshuffled
    is_new_shoe_needed()
    
    dealt = [shoe.pop(random.randrange(len(shoe))) for _ in range(2)]
    val = dealt[0] + dealt[1]
    
    return val

def deal_one_card():
    # Check if the current shoe needs to be reshuffled
    is_new_shoe_needed()

    dealt = [shoe.pop(random.randrange(len(shoe))) for _ in range(1)]
    val = dealt[0]
    
    return val
    
    
def is_new_shoe_needed():
    # the dealer reshuffles a new shoe when the current one is almost empty
    global shoe
    if len(shoe) <= 16:
        shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] * 4 * 8
        random.shuffle(shoe)
        
        
def declare_winner(p_hand, b_hand):
    if p_hand > b_hand:
        # Player wins, return 1
        return 1
    elif b_hand > p_hand:
        # Banker wins, return 2 
        return 2
    elif b_hand == p_hand:
        # It's a tie, return 3
        return 3


def simulate():
    # Returns 1 if player wins,
    # 2 if banker wins, 
    # 3 if it's a tie
    winner = 0
    
    
    
    player = deal_two_cards()
    banker  = deal_two_cards()
    
    player_points = player % 10
    banker_points = banker  % 10
    

    
    
    if (player_points == 8 or player_points == 9) and (banker_points != 8 and banker_points != 9):
        # Both hands stand, round ends, player wins 
        winner = 1
        return winner
    elif (player_points != 8 and player_points != 9) and (banker_points == 8 or banker_points == 9):
        # Both  hands stand, round ends, banker wins
        winner = 2
        return winner
    elif (player_points == 8 or player_points == 9) and (banker_points == 8 or banker_points == 9):
        # Both hands stand, rond ends with a tie
        winner = 3
        return winner
        
    elif player_points <= 5:
         
        # Draw one more card for the player hand 
        third_card = deal_one_card()
        player_points = (player_points + third_card) % 10
         
        if banker_points <= 2:
            new_card = deal_one_card()
            
            banker_points = (banker_points + new_card) % 10
             
        elif banker_points == 3 and third_card != 8:
            
            new_card = deal_one_card()
            banker_points = (banker_points + new_card) % 10
            
        elif banker_points == 4 and ( 1 < third_card < 8):
            
            new_card = deal_one_card()
            banker_points = (banker_points + new_card) % 10
            
            
        elif banker_points == 5 and (3 < third_card < 8):
            
            new_card = deal_one_card()
            banker_points = (banker_points + new_card) % 10
            
            
        elif banker_points == 6 and (5 < third_card < 8):
            
            new_card = deal_one_card()
            banker_points = (banker_points + new_card) % 10
            
            
        elif banker_points == 7:
            
            # Banker stands
            banker_points = banker_points
            
    elif 5 < player_points < 8:
        
        # Player hand stands on a 6 or a 7
        player_points = player_points
        # If player stands with 2 cards, banker follows
        # the same rules as the player
        if banker_points <= 5:
            
            new_card = deal_one_card()
            banker_points = (banker_points + new_card) % 10
            
        elif 5 < banker_points < 8:
            
            banker_points = banker_points 
            
            
    winner = declare_winner(player_points, banker_points)
    
    
    return winner
    
def main():
    """ 
    Call simulate 1000 times and report the fraction of outcomes for each hand
    """
    
    max_simulations = 1000000
    player_wins = 0 
    banker_wins = 0 
    ties = 0 
    
    player_fraction_of_wins = 0 
    banker_fraction_of_wins = 0 
    fraction_of_ties = 0 
    
    player_hand_house_edge = 0 
    banker_hand_house_edge = 0 
    tied_hand_house_edge = 0
    
    for game in range(max_simulations):
        
        result = simulate()
        
        if result == 1:
            player_wins += 1
        elif result == 2:
            banker_wins += 1
        elif result == 3:
            ties += 1
        else:
            print("Nope")
            
    player_fraction_of_wins = player_wins / max_simulations
    
    banker_fraction_of_wins = banker_wins / max_simulations
    
    fraction_of_ties = ties / max_simulations
    
    
            
    print("Fraction of wins for player hand: " , player_fraction_of_wins)
    print("Fraction of wins for banker hand: ", banker_fraction_of_wins)
    print("Fraction of games tied: ", fraction_of_ties)
 
    
    
    
    
if __name__ == "__main__":
	main()







    
