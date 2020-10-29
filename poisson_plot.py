
import random
import math
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('Agg')

#coin flip... .025 chance of heads 
def simulate():
    head = 0
    n = 1000
    for i in range(n):
        flip = random.uniform(0,1)
        if flip <= .025:
            head = head + 1
    return head
    
    
outcomes = []

def poisson(x, len):
    output = []
    for i in range(1, x):
        temp1 = (((math.e) ** (-len) * (len ** i)))
        temp2 = temp1 / float(math.factorial(i))
        output.append(temp2)
    return output



def main():
    n = 1000
    fractions = [0] * 1000
    for i in range(1000):
        temp = simulate()
        outcomes.append(temp)
    occurrences = []
    for i in range(101):
        num = outcomes.count(i)
        frac = num / 1000
        occurrences.append(frac)
    poissonL = poisson(50, 25)
    plt.figure()
    plt.plot(poissonL)
    plt.plot(occurrences)
    plt.xlim(0, 60)
    plt.title('Les Poissons!')
    plt.xlabel('Fraction of Trials')
    plt.ylabel('Number of heads per 1000 trials')
    plt.savefig('plot_for_les_poissons.pdf', bbox_inches='tight')



if __name__ == "__main__":
    main()
