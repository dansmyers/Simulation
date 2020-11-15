"""

This program simulates the game of bacarat and finds the probability of each hand occurring. It also includes a calculation of house edges for each hand
Jacob Buckelew
CMS380 Fall 2020


"""

import random
import math

# Need a global list value that keeps track of all the cards in the shoe(416 total cards since there are 8 decks)
# This will be a list with 13 elements, each given the same value of 32 to represent 32 cards for each card value(2-10, J, K, Q, A)



shoe = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]
available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def reshuffle():
	"""
	
	The reshuffle method will be called once all cards in the shoe have been dealt.
	
	"""
	
	for i in range(len(shoe)):
		shoe[i] = 32
		available.append(i)


def return_card_value():
	
	"""
	
	This function will generate a random int that corresponds to one of the indices in the global shoe variable. 
	Instead of returning that specific card, the value of the card will be returned so it can be used in sums
	within the simulate function.
	Aces(shoe[0]) will return a 1
	Number cards(shoe[1]-->shoe[8]) return their face values
	Face cards(shoe[9]-->shoe[12]) return 0
	
	
	"""
	# check the status of the shoe variable
	if(shoe.count(0) == 13):
		reshuffle()
	j = random.choice(available)
	
	# update the global variable
	# consider the case when a number or face is no longer possible to get
	shoe[j] = shoe[j] - 1
	if(shoe[j] == 0):
		available.remove(j)
	
	if(j == 0):
		return 1
	elif(j == 9 or j == 10 or j == 11 or j == 12):
		return 0
	else:
		return j + 1


def simulate():
	"""
	
	Simulate() method runs one round of baccarat including the dealing of cards, calculation of hand values, applying tableau rules, and
	then deciding the winner of the round.
	
	"""
	
	# Dealer deals two hands of two cards
	# When dealing cards, the current state of the global shoe variable must be taken into account
	# We need to generate a random int, check if shoe[randint] != 0, and if it is equal to 0 , then we must keep generating until we 
	# generate one that will allow us to decrement another element in the array(meaning there are available cards). 
	
	# In an outer loop, generate the 4 cards. 
	# Inside the foor loop , use a while loop that we will only enter if the randomint continues to be at an index in the array thats element is 0.
	
	values = []
	result = ''
	
	for i in range(4):
		number = return_card_value()
		values.append(number)
	
	
	# The first two values can correspond to the player and second two correspond to the bank
	# Now we can save the sum of the two cards in each hand
	player = (values[0] + values[1]) % 10 
	bank = (values[2] + values[3]) % 10
	
	
	# check for a player getting a natural and the bank not getting a natural
	if(((player == 8) or (player == 9)) and ((bank != 8) and (bank!= 9))):
		result = 'P'
		return result
	# check for a banker getting a natural and player not getting a natural
	if(((bank == 8) or (bank == 9)) and ((player != 8) and (player != 9))):
		result = 'B'
		return result
	if(((bank == 8) or (bank == 9)) and ((player == 8) or (player == 9))):
		result = 'T'
		return result
	
	# Dealing the third card to the player depends on whether the player has a point value of 0-5
	# The player hand will always stand on a 6 or 7
	# Also, if the player picks a third card, then the bank must decided if it will picks a third
	# so there will need to be a nested if statement behavior here
	
	if( 0 <= player <= 5 ):
		
		player_third_card = return_card_value()
		
		
		player = (player + player_third_card) % 10
		
		# Figure out the banker's third card and add it to bank
		
		if(bank <= 2):
			bank = (bank + return_card_value()) % 10
		if(bank == 3 and player_third_card != 8 ):
			bank = (bank + return_card_value()) % 10
		if(bank == 4 and (2 <= player_third_card <= 7)):
			bank = (bank + return_card_value()) % 10
		if(bank == 5 and (4 <= player_third_card <= 7)):
			bank = (bank + return_card_value()) % 10
		if(bank == 6 and ((player_third_card == 6) or (player_third_card == 7))):
			bank = (bank + return_card_value()) % 10
	# Here is the case where the player stands at a 6 or 7. Now the banker must either hit on 0-5 or stand on 6-7	
	else:
		
		if(0 <= bank <= 5):
			bank = (bank + return_card_value()) % 10
	
	
	
	# decide the winner of the round now
	if(player > bank):
		result = 'P'
	elif(player < bank):
		result = 'B'
	else:
		result = 'T'
	
	return result	
	


def main():
	
	
	# run a large number of simulations
	
	MAX_TRIALS = 1000
	player_successes = []
	bank_successes = []
	tie_successes = []
	
	player_fractions = []
	bank_fractions = []
	tie_fractions = []
	house_edge_player_values = [0] * MAX_TRIALS
	house_edge_bank_values = [0] * MAX_TRIALS
	
	
	for i in range(1000):
		tie_fractions.append(0)
		bank_fractions.append(0)
		player_fractions.append(0)
		for trial in range(MAX_TRIALS):
			player_successes.append(0)
			bank_successes.append(0)
			tie_successes.append(0)
			outcome = simulate()
			if(outcome == 'T'):
				tie_successes[trial] = tie_successes[trial] + 1
			elif(outcome == 'B'):
				bank_successes[trial] = bank_successes[trial] + 1
			else:
				player_successes[trial] = player_successes[trial] + 1
		
		#house_edge_player_values[i] = (((sum(bank_successes))/((MAX_TRIALS - sum(tie_successes)))) - ((sum(player_successes))/(MAX_TRIALS - sum(tie_successes)))) * 100
		#print(house_edge_player_values)
		house_edge_player_values[i] = sum(player_successes) / (MAX_TRIALS - sum(tie_successes))
		house_edge_bank_values[i] = sum(bank_successes) / (MAX_TRIALS - sum(tie_successes))
		player_fractions[i] = sum(player_successes) / (MAX_TRIALS)
		bank_fractions[i] = sum(bank_successes) / MAX_TRIALS
		tie_fractions[i] = sum(tie_successes) / MAX_TRIALS
		player_successes = []
		bank_successes = []
		tie_successes = []
		
	player_house_edge = ((sum(house_edge_bank_values)/1000)- (sum(house_edge_player_values)/1000)) * 100
	bank_house_edge = ((sum(house_edge_player_values)/1000)- ((sum(house_edge_bank_values)/1000) * .95)) * 100
	average_player_fraction = (sum(player_fractions)/1000)
	average_bank_fraction = (sum(bank_fractions)/1000)
	average_tie_fraction = (sum(tie_fractions)/1000)
	tie_house_edge = ((1 / (average_tie_fraction)) - ((1 / (average_tie_fraction)) - 1))/(1 / (average_tie_fraction))
	print("Player Fraction: ", average_player_fraction)
	print("Bank Fraction: ", average_bank_fraction)
	print("Tie Fraction: ", average_tie_fraction)
	print("Player House Edge: ", player_house_edge)
	print("Bank House Edge: ", bank_house_edge)
	print("Tie House Edge: ", tie_house_edge)
	
	


if __name__ == "__main__":
	main()


