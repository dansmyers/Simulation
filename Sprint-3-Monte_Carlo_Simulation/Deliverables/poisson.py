import random
import math
import matplotlib.pyplot as plt

def simulate(num_trails, results_list):
	heads = 0 
	for i in range(0, num_trails):
		r = random.randint(0, 1000)
		if r < 25:
			heads = heads + 1
		results_list.append(heads/(i+1))
	return heads/num_trails
	
results_list = []

s = simulate(1000, results_list)

poisson = []

for i in range(1, 1000):
	
	poisson.append(25/1000)
	


plt.plot(results_list)
plt.plot(poisson)

plt.title('Heads to tails ratio over time')
plt.ylabel('% Success')
plt.xlabel('Trials')

plt.savefig('binomial.pdf', bbox_inches= 'tight')

print("Probability", s)