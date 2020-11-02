"""
	Baccarat Challenge Project
"""

# improt the random library
import random

# Card values mapped to a number for the deck array

ACE_OF_SPADES = 0
TWO_OF_SPADES = 1
THREE_OF_SPADES = 2
FOUR_OF_SPADES = 3
FIVE_OF_SPADES = 4
SIX_OF_SPADES = 5
SEVEN_OF_SPADES = 6
EIGHT_OF_SPADES = 7
NINE_OF_SPADES = 8
TEN_OF_SPADES = 9
JACK_OF_SPADES = 10
QUEEN_OF_SPADES = 11
KING_OF_SPADES = 12

ACE_OF_CLUBS = 13
TWO_OF_CLUBS = 14
THREE_OF_CLUBS = 15
FOUR_OF_CLUBS = 16
FIVE_OF_CLUBS = 17
SIX_OF_CLUBS = 18
SEVEN_OF_CLUBS = 19
EIGHT_OF_CLUBS = 20
NINE_OF_CLUBS = 21
TEN_OF_CLUBS = 22
JACK_OF_CLUBS = 23
QUEEN_OF_CLUBS = 24
KING_OF_CLUBS = 25

ACE_OF_HEARTS = 26
TWO_OF_HEARTS = 27
THREE_OF_HEARTS = 28
FOUR_OF_HEARTS = 29
FIVE_OF_HEARTS = 30
SIX_OF_HEARTS = 31
SEVEN_OF_HEARTS = 32
EIGHT_OF_HEARTS = 33
NINE_OF_HEARTS = 34
TEN_OF_HEARTS = 35
JACK_OF_HEARTS = 36
QUEEN_OF_HEARTS = 37
KING_OF_HEARTS = 38

ACE_OF_DIMONDS = 39
TWO_OF_DIMONDS = 40
THREE_OF_DIMONDS = 41
FOUR_OF_DIMONDS = 42
FIVE_OF_DIMONDS = 43
SIX_OF_DIMONDS = 44
SEVEN_OF_DIMONDS = 45
EIGHT_OF_DIMONDS = 46
NINE_OF_DIMONDS = 47
TEN_OF_DIMONDS = 48
JACK_OF_DIMONDS = 49
QUEEN_OF_DIMONDS = 50
KING_OF_DIMONDS = 51

# List hoding the amount of copies left of each card in the array
# The array is initialized with 8 copies of each card in the deck
deck = []

# List holding the points each card is worth
# indicies represent the same card defined in the index 
# of the deck list
card_points = []

# variable used to set the card_points List
# with the correct amount of points for each card
count = 1

for i in range(52):
	deck.append(8)
	
	if count < 10:
		card_points.append(count)
	else:
		card_points.append(0)
		
	if count == 13:
		count = 0
		
	count += 1 

def reshuffle_deck(deck):
	"""
		This function will reshuffle all of the cards back into the deck
		All cards will be reset to 8 copies
	"""
	
	for i in range(len(deck)):
		if(deck[i] != 8):
			deck[i] = 8
			
	return deck
	
def draw_cards(deck):
	"""
		Function will draw 4 cards out of the deck and will return them as a list
	"""
	
	card1 = int(random.random() * len(deck))
	
	while deck[card1] <= 0:
		card1 = int(random.random() * len(deck));
	deck[card1] -= 1
		
	card2 = int(random.random() * len(deck))
	
	while deck[card2] <= 0:
		card2 = int(random.random() * len(deck))
	deck[card2] -= 1
		
	card3 = int(random.random() * len(deck))
	
	while deck[card3] <= 0:
		card3 = int(random.random() * len(deck))
	deck[card3] -= 1
	
	card4 = int(random.random() * len(deck))
	
	while deck[card4] <= 0:
		card4 = int(random.random() * len(deck))
	deck[card4] -= 1
		
	card_values = [card1, card2, card3, card4]
	
	return card_values

def draw_one_card(deck):
	"""
		Draw one card from the deck
	"""
	
	card = int(random.random() * len(deck))
	
	while deck[card] <= 0:
		card = int(random.random() * len(deck))
	deck[card] -= 1
	
	return card

def check_for_empty_deck(deck):
	"""
		Checks to see if there are less than 6 cards left in the deck
		returns true if less than 6 cards are left false otherwise
	"""
	count = 0
	for i in deck:
		count += i
		
		if count  > 6:
			return False
			
	return True

def simulate():
	"""
		Run one round of Baccarat
	"""
	global deck
		
	# String that will return the winner of the round
	# Returns player for player wins
	# Returns banker for banker wins
	# Returns neither for all other possibilities
	outcome = ""
	
	# reshuffle deck if there are no cards remaining
	if check_for_empty_deck(deck) == True:
		deck = reshuffle_deck(deck)
		
	# Draw cards 
	cards_drawn = draw_cards(deck)
	
	player_hand = [cards_drawn[0], cards_drawn[1]]
	banker_hand = [cards_drawn[2], cards_drawn[3]]
	
	player_points = (card_points[player_hand[0]] + card_points[player_hand[1]]) % 10
	banker_points = (card_points[banker_hand[0]] + card_points[banker_hand[1]]) % 10
	
	if player_points >= 8 and banker_points >= 8:
		outcome = "neither"
		return outcome
	
	elif player_points >= 8:
		outcome = "player"
		return outcome
	
	elif banker_points > 8:
		outcome = "banker"
		return outcome
	
	if player_points <= 5:
		player_hand.append(draw_one_card(deck))
		
		player_points = (card_points[player_hand[0]] + card_points[player_hand[1]] + card_points[player_hand[2]]) % 10
	else:
		banker_hand.append(draw_one_card(deck))
		
		banker_points = (card_points[banker_hand[0]] + card_points[banker_hand[1]] + card_points[banker_hand[2]]) % 10
	
	
for i in range(500):
	simulate()
























































