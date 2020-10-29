import random
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def playRound():
	rand = random.randint(1, 38)
	
	if (rand <= 16):
		return True
	else:
		return False


def simulate(num_sims):
	results = []
	
	for n in range(0, num_sims):
		
		bet = 1
		money = 255
		play_again = True
		spins = 0

		while play_again:
			spins = spins + 1
			result = playRound()
			
			if result == True:
				money = money + bet
				bet = 1
			else:
				money = money - bet
				bet = bet*2
				
			if bet > money or spins >= 100:
				play_again = False
	
		results.append(money)
	return results
	
	
results = simulate(1000)
print(results)




plt.hist(results, 50)
plt.title('Martingale outcomes distribution')
plt.ylabel('# of results')
plt.xlabel('Money earned')

plt.savefig('martingale.pdf', bbox_inches= 'tight')