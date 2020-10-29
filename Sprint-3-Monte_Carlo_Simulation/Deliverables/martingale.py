# Import method to generate ranndom roulette spins
from random import randint

# Set up matplotlib and configure it to be used on Mimir 
import matplotlib
matplotlib.use('Agg') # Required because we are using a remote environment
from matplotlib import pyplot  as plt


def spin_roulette():
    """ 
    Simulate one roulette spin
    inputs: no 
    outputs: return 1 if the ball lands on black
    """
    spin = randint(1,38)
    color =''
    
    if (spin % 2 == 0) and spin <= 36:
        color = 'black'
    elif (spin % 2 == 1) and spin < 36:
        color = 'red'
    else:
        color = 'green'
    
    if color == 'black':
        return 1 
    else: 
        return 0

def simulate():
    """
    Simulate a gambler playing roulette, always betting on black and using the Martingale system.
    The initial money avaiable is $255.
    The game ends after playing 100 spins or if the gambler runs out of money to cover the size of the bet required by the Martingale system
    """
    
    bankroll = 255 
    count = 0
    bet = 1
    
    while count <= 100 and bet <= bankroll:
        outcome = spin_roulette()
        
        # if the ball lands on black continue betting $1
        # otherwise, double the bet and conitue playing with the conditions above
        if outcome == 1:
            bankroll += bet
            bet = 1
        else:
            bankroll -= bet
            bet = bet * 2
        count += 1

    
    return bankroll
    
def main():
    """
    Call simulate 1000 times and plot a histogram of the outcomes
    """
    n_trials = 1000
    
    # Holds the outcomes of each simulation
    outcomes =  []
    
    # RUn the simulation 1000 times and record the outcomes 
    for trial in range(n_trials):
        result = simulate()
        outcomes.append(result)
    
    # Create new figure
    plt.figure()
    plt.hist(outcomes, 30)
    plt.title("Martingale strategy distribution of outcomes")
    plt.ylabel("Frequency")
    plt.xlabel("Value")
    plt.savefig('Martingale_strategy_results.pdf')
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    