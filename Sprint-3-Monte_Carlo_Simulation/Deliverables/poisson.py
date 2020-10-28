# Les Poisson Problem
# CMS 380
# Matthew Trautmann Fall 2020

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import math

from random import randint

def simulate():

    """ Simulate one trial for Les Poison
        
        inputs: none
        outputs: Number of times heads occured out of 1000
        with a probabilty of .025
    """
    num_trials = 1000
    num_of_heads = 0
    
    for trial in range(num_trials):
        
        temp = randint(1, 40)
        
        if temp == 1:
            num_of_heads += 1
            

    return num_of_heads

def poisson(x, l):
    """ 
        Poisson function, acts as the poisson pmf function
        inputs: x the number of events, and l, lambda value
        outputs: a list of values associated with x
    """
    
    output = []
    for i in range(1, x):
        temp1 = (((math.e) ** (-l)) * (l ** i))
        temp2 = temp1 / float(math.factorial(i))
        output.append(temp2)
    return output
        
    
    
def main():

    num_iterations = 1000  # Number of simulated trials 
    
    # Create the empty list
    frac_heads_list = [0] * 1000
    
    # Python for loop using range
    for iteration in range(num_iterations):
        num_heads = simulate()  # Simulate number of heads
        frac_heads_list[num_heads] = frac_heads_list[num_heads] + 1
    
    # Divide the occurences by total amount of outcomes  
    newList = [x / 1000 for x in frac_heads_list]

    poisson_list = poisson(50, 25)
    # Create a new figure
    plt.figure()

    # Create line plots for simulated data
    plt.plot(newList)
    plt.plot(poisson_list)
    
    # Limit the x range
    plt.xlim(0, 50)
    
    # Title and axis labels
    plt.title('Heads to tails ratio over time')
    plt.ylabel('% Success')
    plt.xlabel('Trials')

    # Save the figure to a file
    plt.savefig('poisson.pdf', bbox_inches='tight')
    

    
    
# Call main() when this program runs
if __name__ == '__main__':
    main()
