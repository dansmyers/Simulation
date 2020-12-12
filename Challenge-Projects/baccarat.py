'''
Ryan King, Challenge Project 1

Plays baccarat many times and gets the number of banker wins, player wins and ties. It then calculates 
the house edge. 

Many print statements have been commented out to allow the program to run faster.
'''
import random

def get_points(hand):
	total = 0
	for card in hand:
		if(card < 10):
			total = total + card
	return total%10

def check_natural(hand):
	
	if (get_points(hand) == 8 or get_points(hand) == 9):
			return True
	return False

def simulate(num_trials):
	num_player = 0;
	num_banker = 0;
	num_tie = 0;
	
	for i in range(1, num_trials):
		player_hand = []
		player_hand.append(random.randint(1, 13))
		player_hand.append(random.randint(1, 13))
		
		player_points = get_points(player_hand)
		player_natural = check_natural(player_hand)
		
		banker_hand = []
		banker_hand.append(random.randint(1, 13))
		banker_hand.append(random.randint(1, 13))
		
		banker_points = get_points(banker_hand)
		banker_natural = check_natural(banker_hand)
		
		if(player_natural and banker_natural):
			#print("\nGame #", i)
			#print("Player Hand:", player_hand, "\nPlayer Points: ", player_points)
			#print("Banker Hand:", banker_hand, "\nBanker Points: ", banker_points)
			
			num_tie = num_tie + 1
			#print("Tie")
			
		elif(player_natural):
			#print("\nGame #", i)
			#print("Player Hand:", player_hand, "\nPlayer Points: ", player_points)
			#print("Banker Hand:", banker_hand, "\nBanker Points: ", banker_points)
			
			num_player = num_player + 1
			#print("Player Wins")
			
		elif(banker_natural):
			#print("\nGame #", i)
			#print("Player Hand:", player_hand, "\nPlayer Points: ", player_points)
			#print("Banker Hand:", banker_hand, "\nBanker Points: ", banker_points)
			
			num_banker = num_banker + 1
			#print("Banker Wins")
			
		else:
			if(player_points < 6):
				player_hand.append(random.randint(1, 13))
				
				if(banker_points <= 2):
					banker_hand.append(random.randint(1,13))
				elif(banker_points == 3 and player_hand[2] != 8):
					banker_hand.append(random.randint(1, 13))
				elif(banker_points == 4 and player_hand[2] > 1 and player_hand[2] < 8):
					banker_hand.append(random.randint(1, 13))
				elif(banker_points == 5 and player_hand[2] > 3 and player_hand[2] < 8):
					banker_hand.append(random.randint(1, 13))
				elif(banker_points == 6 and (player_hand[2] == 6 or player_hand[2] == 7)):
					banker_hand.append(random.randint(1, 13))
			else:
				if(banker_points < 6):
					banker_hand.append(random.randint(1, 13))
		
			player_points = get_points(player_hand)
			banker_points = get_points(banker_hand)
		
			#print("\nGame #", i)
			#print("Player Hand:", player_hand, "\nPlayer Points: ", player_points)
			#print("Banker Hand:", banker_hand, "\nBanker Points: ", banker_points)
			if(player_points == banker_points):
				num_tie = num_tie + 1
				#print("Tie")
			elif(player_points > banker_points):
				num_player = num_player + 1
				#print("Player Wins")
			else:
				num_banker = num_banker + 1
				#print("Banker Wins")
	print("\nPlayer Wins: ", num_player, "\nBanker Wins:", num_banker, "\nTies:", num_tie)
	
	print("\nPlayer bet house edge", (-1)*(num_player/(num_banker+num_player)) + num_banker/(num_banker+num_player))
	print("Banker bet house edge", ((-19/20)*(num_banker/(num_banker+num_player)))+num_player/(num_banker+num_player))
	
trials = 500000
	
simulate(trials)