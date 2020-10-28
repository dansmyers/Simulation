# Martingale Solution, Sprint 3
# CMS 380
# Matthew Trautmann Fall 2020

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from random import randint

def simulate():

    """ Simulate 100 rounds of playing roullete
        
        inputs: none
        outputs: Returns amount in players bank after either 100 rounds
        or until they cannot bet anymore
    """
    bank = 255
    bet = 1
    win = True
    spins = 0
    
    # Repeat spin until you reach 100 or can't afford bet
    while bank - bet > 0 and spins < 100:
        # If you won previous roll
        if win == True:
            spin = randint(1, 38)
            
            # If you win this spin, add money
            if spin <= 18:
                bank = bank + bet
                spins = spins + 1
            
            # If you lose spin, double next bet
            else:
                win = False
                bank = bank - bet
                bet = bet * 2
                spins = spins + 1
                
        # If you lost the last roll
        else:
            spin = randint(1, 38)
            
            # If you win this spin, add money
            if spin <= 18:
                win = True
                spins = spins + 1
                
            # If you lose this spin, double the bet
            else:
                bank = bank - bet
                bet = bet * 2
                spins = spins + 1
                
    return bank
    
        
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
    plt.title('Money after 100 Spins')
    plt.xlabel('Bank Amount')
    plt.ylabel('Count')

    # Save the figure to a file
    plt.savefig('martingale_histo.pdf', bbox_inches='tight')
    
# Call main() when this program runs
if __name__ == '__main__':
    main()