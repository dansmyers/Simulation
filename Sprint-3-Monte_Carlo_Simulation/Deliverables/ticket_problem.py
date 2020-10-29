import random

def simulate():
	#Dictionary Key is seat #, value is the assigned seat of the person sitting there
	seatingDict = {}
	
	
	
	seatingDict[random.randint(1, 100)] = 1;
	
	for x in range(2, 101):
		if x not in seatingDict:
			seatingDict[x] = x
		else:
			foundEmptySeat = False
			while foundEmptySeat == False:
				r = random.randint(1,100)
				if r not in seatingDict:
					seatingDict[r] = x
					foundEmptySeat = True
	if seatingDict[100] == 100:
		return 1
	else:
		return 0

trials = 10000
sucesses = 0


for i in range(0, trials):
	sucesses = sucesses + simulate()
	
probability = sucesses/trials


print("Person 100 sat in seat 100", sucesses, "times out of", trials, "for a probability of", probability)