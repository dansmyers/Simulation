""" 
Show that the Poisson distribution is a good approximation for the binomial under the given conditions.

CMS 380, Fall 2020 
Maria Morales 
"""
# Import the random module to generate random numbers for the simulation 
import random
# Import the math module for calculations
import math 

# Set up matplotlib and configure it to be used on Mimir 
import matplotlib
matplotlib.use('Agg') # Required because we are using a remote environment
from matplotlib import pyplot  as plt 

 

def flip_coin():
    """
    Simulate flipping a coin that comes up heads with a probability 0.025
    inputs: no 
    outputs: True if the random value is <= 0.025, False otherwise 
    """
    
    # random.random() returns a floating point number in the range [0.0, 1.0)
    coin = random.random()
    
    return coin <= 0.025
    
    
def  simulation():
    """
    Calls  flip_coin a large number of times and reports the number of successes,  where success is the coin landing as heads
    inputs: no
    outputs: number of successes/heads
    """
    # Number of times we'll flip the coin
    n_trials = 1000
    # Counts the number of successes
    num_heads = 0
    
    # Simulate flipping a biased coin 1000 times and count the number of times it
    # comes up heads
    for trial in range(n_trials):
        result = flip_coin()
        
        if result == True:
            num_heads += 1
            
    return(num_heads)
    
    
def calculate_success_freq(x):
    """
    Counts the frequency of the numbers in the list.
    inputs: a list cointaing number of successes
    outputs: a dictionary mapping the success value to its count
    """
    successes_count = {}
    
    # Iterate through the list and count the number of times a value repeats
    for num in x:
        if num not in successes_count:
            successes_count[num] = 1
        else:
            successes_count[num] += 1
    
    return successes_count
    
def cal_poisson_pmf(x):
    """
    Calculate the Poisson probability mass function of the given values
    inputs: a dictionary containg values and their frequency
    outputs: a dictionary containg mapping values to their Poisson pmf
    """
    poisson_pmf = {}
    lambda_val = 25
    

    # Find the Poisson pmf for every value in the input dictionary
    for key in x:
        key = key * 1000
        value = (math.exp(- lambda_val) * (pow(lambda_val, (key)))) / (math.factorial(int(key)))
        
        poisson_pmf[key] = value
    
    return poisson_pmf
        
    
    
def main():
    """"
    Repeat the simulation 1000 times and plot the fraction of times each outcome occurs.
    Plot the Poisson pmf for the above simulation with lambda = 25.
    """
    # Every elment in this list represents the fraction of the total number of heads flipped in 1 simulation (1000 trials)
    results = []
    num_simulations = 1000
    
    # For each simulation of 1000 coin flips, append the fraction of the number of heads flipped to the results list
    for i in range(num_simulations):
        num_success = simulation()
        results.append(num_success / 1000)
        
    results.sort()
    
    
    # Calculate the frequency of each fraction
    success_freq = {}
    success_freq = calculate_success_freq(results)
    
    # fractions, x-axis
    fractions = list(success_freq.keys())

    # frequency of each fraction, y-axis
    frac_frequency = list(success_freq.values())
    
    # Calculate the Poisson pmf for the fraction of times each outcome occurs
    poisson_pmf = cal_poisson_pmf(success_freq)
    
    # poisson distribution X values, x-axis
    x_values = list(poisson_pmf.values())
    
    # Poisson K values, y-axis
    y_values = list(poisson_pmf.keys())
    
    # Create new figure
    plt.figure()
    # Plot the fraction of times each outcome occurs
    plt.plot(fractions, frac_frequency, label="Binomial distribution")
    
    # Sort x-values for the Poisson plot
    x_values.sort()
    # Plot the Poisson pmf
    plt.plot(x_values, frac_frequency, label="Poisson distribution")
    
    plt.title("Les Poisson Distribution of values")
    plt.ylabel("Frequency")
    plt.xlabel("Value")
    plt.legend()

    plt.savefig('Binomial_Poisson_Plots.pdf', bbox_inches='tight')
  
    
    
if __name__ == '__main__':
    main()

    