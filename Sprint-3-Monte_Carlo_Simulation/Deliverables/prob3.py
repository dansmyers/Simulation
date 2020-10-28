#random.randint -- generate random integers in a range 
import random
from scipy.stats import poisson
import numpy as np 

import math 

import matplotlib
matplotlib.use('Agg')
#needed to access in remote environment like mimir

from matplotlib import pyplot as plt
#plt is alias, we renamed and can run them as such

def simulate():
    """
    simulate one round of passe findIdx
    no inputs 
    output is true or false 
    """
    
    count = 0;
    
    for i in range(1000):
        num = random.uniform(0,1)
        if num <= .025:
            count+=1
        
    return count
    
def possion():
    x = 1000
    num = 25
    e = 2.71828
    
    denom = math.factorial(x)
    
    equation = pow(e,-num) * pow(num,x) / denom
    print(equation)
    

def main():
    """
    call simulate a large # of times and return 
    fraction of successes
    """
    
    #make a data structure to hold 1000 outcomes
    data = []
    max_trials = 1000
    num_successes = 0
    
    for trial in range(max_trials):
        data.append(simulate())
     
    
    #create a new figure, always do before calling plotting function
    plt.figure()

    #plot the histogram onto the figure, 15 bins 
    plt.hist(data, 25)

    #Set title and axis labels
    plt.title("Histogram of coin flip # of heads")
    plt.xlabel("Number of Heads")
    plt.ylabel("count")

    #save figure to a filter
    plt.savefig("count_hist.pdf", bbox_inches='tight')
    
    
    
    #Use an array for th frequency of numbers
    #Make an array of all the possible numbers
    points =[]
    points2 = []
    for j in range(100):
        points.append(0)
        points2.append(j)
    
    for i in data:
        points[i] = points[i] + 1
    
    
    plt.figure();
    plt.plot(points2, points)
    plt.plot(x, poisson.pmf(x,25) * 1000)
    
    plt.savefig("overlay.pdf", bbox_inches='tight')
    

#Write some code that will call main when this program runs 

if __name__ == '__main__':
    main()