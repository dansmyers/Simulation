'''
CMS 380
Les Poisson Question:

Show the Poisson distribution when n is large and p is small.
'''
import random
from scipy.stats import poisson
import numpy as np

import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot as plt

def simulate():
    heads = 0
    flip = 0
    for i in range(1000):
        flip = random.uniform(0,1)
        if flip <= .025:
            heads += 1
    return heads


def main():
    # Call simulate function a large number of times
    # Simulate is the coin flip
   
    trial_results = []
    
    max_trials = 1000
    
    # Insert results from the trial into 
    for trials in range(max_trials):
        num_heads = simulate()
        trial_results.append(num_heads)
   
    # print(trial_results)
    plt.figure()
    
    plt.hist(trial_results, 25)
    
    plt.title("Histogram of Results")
    plt.xlabel("Num of Trials")
    plt.ylabel("Count")
    
    plt.savefig("count_hist.pdf", bbox_inches='tight')
    x = []
    for z in range(1,101):
        x.append(z)
    points = []
    points2 = []
    
    for j in range(100):
        points.append(0)
        points2.append(j)
    for k in trial_results:
        points[k] = points[k] + 1
# Insert all of this into a histogram! And line plot
    plt.figure()
    plt.plot(points2, points)
    plt.plot(x, poisson.pmf(x,25)*1000)
    
    plt.savefig("overlay.pdf", bbox_inches='tight')
# Create a list of the num of simulations that yielded that outcome
    
# Code that runs main
if __name__=='__main__':
    main()
    
    