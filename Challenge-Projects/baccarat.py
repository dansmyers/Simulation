# Baccarat Simulation 
# CMS 380
# Matthew Trautmann Fall 2020

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from random import randint

def simulate():

    """ Simulate method simulates 1 round of baccarat
    
    
    """

        
def main():
    
    num_iterations = 1000  # Number of simulated trials 
    
    session_list = []
    
    # Python for loop using range
    for sessions in range(num_iterations):
        # Simulate 1 session
        temp = simulate()  # Simulate number of heads
        
        # Add session to list of sessions
        session_list.append(temp)
    
    # Create a new figure
    plt.figure()

    # Create a histogram
    plt.hist(session_list, 100)

    # Title and axis labels
    plt.title('Baccarat Simulation')
    plt.xlabel('Rounds played')
    plt.ylabel('Amount of Money')

    # Save the figure to a file
    # plt.savefig('baccarat.pdf', bbox_inches='tight')
    
# Call main() when this program runs
if __name__ == '__main__':
    main()