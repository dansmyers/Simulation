### Baccarat Simulator
#
#CMS 380
import random

def main():
 
# Initialize the deck and counts of winning hands
    shoe = shuffle()
    player_wins = 0
    banker_wins = 0
    ties = 0
    
    
    
# Run some number of rounds of Baccarat
    for i in range (100000):
        result = simulate(shoe)
        if result == 'player':
            player_wins += 1
        elif result == 'banker':
            banker_wins += 1
        else:
            ties += 1
        if len(shoe) < 16:
            shoe = []
            shoe = shuffle()

    print ('Player Wins = ' + str(player_wins/100000) + ', Banker Wins ' + str(banker_wins/100000) + ', Ties ' + str(ties/100000))


def shuffle():
    deck = []
    # The deck will contain only the point values of the cards.
    # By Baccarat rules, there are 4 aces worth 1 point, 16 face cards and tens
    # worth 0 point, and 32 other cards worth their numerical value.
    # 8 decks are suffled together to create a shoe.
    for n in range(8):
        for i in range (32):
            deck.append((i % 8) + 2)
    
        for i in range (16):
            deck.append(0)
    
        for i in range (4):
            deck.append(1)
    
    random.shuffle(deck)

    return deck
    
    
    
# Runs one round of Baccarat
def simulate(deck):
    
    # Initialize Banker and Player
    # player_third_card is initialized to -10 to signify that it doesn't exist.
    banker = 0
    player = 0
    player_third_card = -10
    
# Deal out two hands of two cards
    player = (player + deck.pop()) % 10
    player = (player + deck.pop()) % 10
    
    banker = (banker + deck.pop()) % 10
    banker = (banker + deck.pop()) % 10
    
# Check for natural
    if player >= 8 and banker >= 8:
        return 'tie'
    elif banker >= 8:
        return 'banker'
    elif player >= 8:
        return 'player'
    

# Run through Player hand
    if player <= 5:
        player_third_card = deck.pop()
        player = (player + player_third_card) % 10
        

# Run through Banker hand
        if player_third_card == -10 and banker < 6:
            banker = (banker + deck.pop()) % 10
        elif banker <= 2:
            banker = (banker + deck.pop()) % 10
        elif banker == 3 and player_third_card != 8:
            banker = (banker + deck.pop()) % 10
        elif banker == 4 and player_third_card >= 2 and player_third_card <=7:
            banker = (banker + deck.pop()) % 10
        elif banker == 5 and player_third_card >= 4 and player_third_card <=7:
            banker = (banker + deck.pop()) % 10
        elif banker == 6 and (player_third_card == 6 or player_third_card == 7):
            banker = (banker + deck.pop()) % 10
                
    
# Compare hands and return results
    if player > banker:
        return 'player'
    elif banker > player:
        return 'banker'
    else:
        return 'tie'

if __name__ == "__main__":
    main()
