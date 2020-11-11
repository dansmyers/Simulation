import random
shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] * 4 * 8
random.shuffle(shoe)

def deal_two_cards():
    global shoe
    #print("Shoe before dealing 2: ", shoe)
    #print("Shoe len ", len(shoe))
    dealt = [shoe.pop(random.randrange(len(shoe))) for _ in range(2)]
    #print("Shoe after dealing 2: ", shoe)
    print("Shoe len after dealing 2\n ", len(shoe))
    print(dealt)
    
    return dealt

def deal_one_card():
    #print("Shoe before dealing 1: ", shoe)
    #print("Shoe len ", len(shoe))
    dealt = [shoe.pop(random.randrange(len(shoe))) for _ in range(1)]
    #print("Shoe after dealing 1: ", shoe)
    #print("Shoe len ", len(shoe))
    print(dealt)
    
def is_new_shoe_needed():
    # the dealer reshuffles a new shoe when the current one is almost empty
    global shoe
    if len(shoe) <= 16:
        shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] * 4 * 8
        random.shuffle(shoe)
        

for i in range(210):
    deal_two_cards()
    is_new_shoe_needed()
    
print("Shoe after 210 deals ", shoe)
print("Shoe len after dealing 210\n ", len(shoe))

player_wins = 0 
banker_wins = 0 
ties = 0 


"""
player = deal_two_cards()
banker  = deal_two_cards()

player_points = player % 10
banker_points = banker  % 10

if player_points or banker_points > 7 and <  10:
    # both hands stand 
    player_points = player_points
    banker_points = banker_points
elif player_points <= 5:
    # Draw one more card for the player hand 
    third_card = deal_one_card()
    player_points = player_points + third_card % 10
    if banker_points <= 2:
        new_card = deal_one_card()
        banker_points = banker_points + new_card % 10
    elif banker_points == 3 and third_card != 8:
        new_card = deal_one_card()
        banker_points = banker_points + new_card % 10
    elif banker_points == 4 and third_card > 1 and < 8:
        new_card = deal_one_card()
        banker_points = banker_points + new_card % 10
    elif banker_points == 5 and third_card > 3 and < 8:
        new_card = deal_one_card()
        banker_points = banker_points + new_card % 10
    elif banker_points == 7:
        banker_points = banker_points
elif player_points > 5 and < 8:
    player_points = player_points
    if banker_points <= 5:
        new_card = deal_one_card()
        banker_points = banker_points + new_card % 10
    elif banker_points > 5 and < 8:
        banker_points = banker_points """
    
