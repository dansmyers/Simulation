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

    print("Matt")
    

    
    
# Call main() when this program runs
if __name__ == '__main__':
    main()
