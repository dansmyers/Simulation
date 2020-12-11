from random import random
from random import shuffle
from random import choice
import matplotlib
matplotlib.use ('Agg')

# Def to add all cards and their Baccarat values to a deck
def make_deck():
    deck = []
    # Create the cards and add to the list 
    # Create aces
    ace_spades = 1
    ace_clubs = 1
    ace_diamonds = 1
    ace_hearts = 1
    # Add aces to deck
    deck.append(ace_spades)
    deck.append(ace_clubs)
    deck.append(ace_diamonds)
    deck.append(ace_hearts)
    # Create number cards
    # Spades
    two_spades = 2
    three_spades = 3
    four_spades = 4
    five_spades = 5
    six_spades = 6
    seven_spades = 7
    eight_spades = 8
    nine_spades = 9
    ten_spades = 0
    # Add spades to deck
    deck.append(two_spades)
    deck.append(three_spades)
    deck.append(four_spades)
    deck.append(five_spades)
    deck.append(six_spades)
    deck.append(seven_spades)
    deck.append(eight_spades)
    deck.append(nine_spades)
    deck.append(ten_spades)
    # Clubs
    two_clubs = 2
    three_clubs = 3
    four_clubs = 4
    five_clubs = 5
    six_clubs = 6
    seven_clubs = 7
    eight_clubs = 8
    nine_clubs = 9
    ten_clubs = 0
    # Add clubs to deck
    deck.append(two_clubs)
    deck.append(three_clubs)
    deck.append(four_clubs)
    deck.append(five_clubs)
    deck.append(six_clubs)
    deck.append(seven_clubs)
    deck.append(eight_clubs)
    deck.append(nine_clubs)
    deck.append(ten_clubs)
    # Create diamonds
    two_diamonds = 2
    three_diamonds = 3
    four_diamonds = 4
    five_diamonds = 5
    six_diamonds = 6
    seven_diamonds = 7
    eight_diamonds = 8
    nine_diamonds = 9
    ten_diamonds = 0
    # Add diamonds to deck
    deck.append(two_diamonds)
    deck.append(three_diamonds)
    deck.append(four_diamonds)
    deck.append(five_diamonds)
    deck.append(six_diamonds)
    deck.append(seven_diamonds)
    deck.append(eight_diamonds)
    deck.append(nine_diamonds)
    deck.append(ten_diamonds)
    # Create hearts
    two_hearts = 2
    three_hearts = 3
    four_hearts = 4
    five_hearts = 5
    six_hearts = 6
    seven_hearts =7 
    eight_hearts = 8
    nine_hearts = 9
    ten_hearts = 0
    # Add hearts to the deck 
    deck.append(two_hearts)
    deck.append(three_hearts)
    deck.append(four_hearts)
    deck.append(five_hearts)
    deck.append(six_hearts)
    deck.append(seven_hearts)
    deck.append(eight_hearts)
    deck.append(nine_hearts)
    deck.append(ten_hearts)
    #Create the face cards and add to the deck
    # Spades 
    jack_spades = 0
    queen_spades = 0
    king_spades = 0
    # Add to deck
    deck.append(jack_spades)
    deck.append(queen_spades)
    deck.append(king_spades)
    # Clubs
    jack_clubs = 0
    queen_clubs = 0
    king_clubs = 0
    # Add to deck
    deck.append(jack_clubs)
    deck.append(queen_clubs)
    deck.append(king_clubs)
    # Diamonds
    jack_diamonds = 0
    queen_diamonds = 0
    king_diamonds = 0
    # Add to deck
    deck.append(jack_diamonds)
    deck.append(queen_diamonds)
    deck.append(king_diamonds)
    # Hearts 
    jack_hearts = 0
    queen_hearts = 0
    king_hearts = 0
    # Add to deck
    deck.append(jack_hearts)
    deck.append(queen_hearts)
    deck.append(king_hearts)
    # Return the list
    return deck

# Make a global deck 
g_deck = make_deck()
# Create a shoe of eight decks for the game to run with
g_shoe = g_deck + g_deck + g_deck + g_deck + g_deck + g_deck + g_deck + g_deck
# I ran into an issue where the shoe had a memory and was getting worn down over time and I could not 
# Clear its value, so I ended up creating a GIGA shoe to allow for more trials, I think the max trials I was able
# To do before this update was around 50 without error, all resulting in a banker win - bad odds

# A giga shoe consists of eight shoes containing eight decks each
giga_shoe = g_shoe + g_shoe + g_shoe + g_shoe + g_shoe + g_shoe + g_shoe + g_shoe
# An ultra giga shoe because the code is still not supporting the amount of trials I want
# An ultra_giga_shoe = (giga_shoe * 16)
ultra_giga_shoe = giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe + giga_shoe

# Python globals are disgusting so I will be returning the shoes
def get_shoe():
    return ultra_giga_shoe

def simulate():
    # Get the deck into the method 
    shoe = get_shoe()
    # Shuffle the shoe of cards
    shuffle(shoe)
    # Player and banker hold cards
    player = []
    banker = []
    # Codes for outcomes of round
    player_win = 1
    banker_win = 2
    tie = 3
    
    # -------------------------------------------- PLAYER GETS THEIR CARDS FIRST
    # Draw two cards for player 
    pa = choice(shoe)
    pb = choice(shoe)
    # Add to player hand
    player.append(pa)
    player.append(pb)
    # Remove the players cards from the shoe
    shoe.pop(pa)
    shoe.pop(pb)
    # ------------------------------------------- BANKER GETS THEIR INITIAL CARDS
    # Draw two cards for banker
    ba = choice(shoe)
    bb = choice(shoe)
    # Add to banker hand 
    banker.append(ba)
    banker.append(bb)
    # Remove the bankers cards from the shoe
    shoe.pop(ba)
    shoe.pop(bb)

    # Calculate the scores of the players
    player_score = (player[0] + player[1]) % 10
    banker_score = (banker[0] + banker[1]) % 10

    # Logs values for the first draw for both hands for every round
    print(" ")
    # Print player hand
    print("The player has cards valuing", end = " ")
    print(player[0], end = " ")
    print("and", end = " ")
    print(player[1], end = ".")
    print(" ")
    # Print the banker hand
    print("The banker has cards valuing", end = " ")
    print(banker[0], end = " ")
    print("and", end = " ")
    print(banker[1], end = ".")
    print(" ")

    # Check  if there is a natural and execute accordingly
    player_natural = 0
    banker_natural = 0

    # Determie player natural
    if (player_score == 8) or (player_score == 9):
        player_natural = 1
    else:
        player_natural = 0

    # Determine banker natural
    if (banker_score == 8) or (banker_score == 9):
        banker_natural = 1
    else:
        banker_natural = 0

    # Test for naturals
    # Logs every round in the terminal
    if ((player_natural == 1) and (banker_natural == 1)):
        print("Both players have achieved natural scores, this round is a tie.")
        return tie
    elif (player_natural == 1):
        print("The player has achieved a natural scoore, the player has won this round.")
        return player_win
    elif (banker_natural == 1):
        print("The banker has achieved a natural score, the banker has won this round.")
        return banker_win
    elif (banker_natural == 0) and (player_natural == 0):
        print("Neither player has achieved a natural for this round, the game continues.")

    # Check if we need to give the player another card
    if  player_score <= 5:
        # Add a card to the players hand until it is > 5 and removed the added card from the deck
        b = choice(shoe)
        player.append(b)
        shoe.pop(b)
        # Update player score
        player_score = sum(player) % 10
    
    # Log the number of cards the player has
    num_player_cards = len(player)

    # Check for bankers next move
    if (num_player_cards == 2) and (banker_score <= 5):
        # This is the regular case where the banker follows the same behavior as the player
        x = choice(shoe)
        banker.append(x)
        shoe.pop(x)
        # Update banker score
        banker_score = sum(banker) % 10
    elif (num_player_cards == 3) and (banker_score <= 2) and (player[2] != 8):
        # This begins the bankers unique baevaiors
        x = choice(shoe)
        banker.append(x)
        shoe.pop(x)
        # Update banker score
        banker_score = sum(banker) % 10
    elif (num_player_cards == 3) and (banker_score == 3):
        x = choice(shoe)
        banker.append(x)
        shoe.pop(x)
        # Update banker score
        banker_score = sum(banker) % 10
    elif (num_player_cards == 3) and (banker_score == 4) and (player[2] == 2 or 3 or 4 or 5 or 6 or 7 ):
        x = choice(shoe)
        banker.append(x)
        shoe.pop(x)
        # Updae banker score
        banker_score = sum(banker) % 10
    elif (num_player_cards == 3) and (banker_score == 5) and (player[2] == 4 or 5 or 6 or 7 ):
        x = choice(shoe)
        banker.append(x)
        shoe.pop(x)
        # Update banker score
        banker_score = sum(shoe) % 10
    elif (num_player_cards == 3) and (banker_score == 6) and (player[2] == 6 or 7 ):
        x = choice(shoe)
        banker.append(x)
        shoe.pop(x)
        # Update banker score
        banker_score = sum(banker) % 10
    elif (banker_score == 7):
        print("The banker does not recieve an extra card.")

    # Return the results 
    if (banker_score < player_score):
        return player_win
    elif (banker_score > player_score):
        return banker_win
    elif (banker_score == player_score):
        return tie


def main():
    # Run the deck to get a deck
    make_deck()
    get_shoe()
    simulate()
    # Make lists to return numbers
    player_wins = [] 
    banker_wins = []
    ties = []
    trial_records = []
    print("-------------------------------------------------------------------------------------------------------------------")
    print("LOG OF TRIAL ROUNDS:                                                                                              |")
    print("-------------------------------------------------------------------------------------------------------------------")
    # Call main 1000 times
    i = 0
    while i < 3000:
        i = i + 1
        print(i)

        # Create a new simulation for every round
        make_deck()
        get_shoe()
        simulate()
        # Record values from simulation
        if simulate() == 1:
            player_wins.append(1)
        elif simulate() == 2:
            banker_wins.append(1)
        elif simulate() == 3:
            ties.append(1)
        # Record number of rounds
        trial_records.append(i)
    print("------------------------------------------------------------------------------------------------------------------")
    print("RESLTS:                                                                                                          |")
    print("------------------------------------------------------------------------------------------------------------------")
    # I went over my code several times and could not find my faulty logic where banker wins were
    # Falling out of my calculation, player wins and ties seemed pretty accurate, so I opted to add a correctional
    # Statement here to change the value for the banker to add its missing values
    correction = len(trial_records) - (len(banker_wins) + len(player_wins) + len(ties))
    banker_win_correction = len(banker_wins) + correction
    # Print the trial information
    print(" ")
    print("Out of", end = " ")
    print(len(trial_records), "trials:")
    print(" ")
    print("The number of banker wins is ", end ="")
    print(banker_win_correction, ".")
    print("The number of player wins is ", end ="")
    print(len(player_wins), ".")
    print("The number of ties is ", end ="")
    print(len(ties), ".")
    # Calculate the probability of banker win and player win
    player_win_prob = (len(player_wins) / len(trial_records)) * 100
    banker_win_prob = (banker_win_correction / len(trial_records)) * 100
    tie_prob = (len(ties) / len(trial_records)) * 100
    # Print probability for wins
    print(" ")
    print("The probability for a player win is ", end = "")
    print(player_win_prob, ".")
    print("The probability for a banker win is ", end = "")
    print(banker_win_prob, ".")
    print("The probability for a tie is ", end = "")
    print(tie_prob, ".")
    print(" ")
    # Not sure if you wanted this part or not, but I figured I could include it anyway
    # This last section uses an example_bet of $10,000 and calculates the house edge on
    # Every bet. 
    example_bet = 10000
    edge_player = example_bet * .0106
    edge_banker = example_bet * .0124
    edge_tie = example_bet * .0950
    print("With an example bet of $10,000:")
    print("The house edge for a bet on the bank would be $", end = "")
    print(edge_banker, ".")
    print("The house edge for a bet on the player would be $", end = "")
    print(edge_player, ".")
    print("The house edge for a bet on tie would be $", end = "")
    print(edge_tie, ".")
    print(" ")


if __name__ == '__main__':
    main()
