# The Ticket Problem Solution
# CMS 380
# Matthew Trautmann Fall 2020

from random import randint, choice

def simulate():

    """ Simulate one train trip
        
        inputs: none
        outputs: Returns true If passanger 99 got to sit in seat 99
    """
    
    # Make a list of passangers
    passangers = list(range(100))
    # Assign first passanger random seat
    passangers[0] = randint(0, 99)
    
    
    # Loop through the passangers
    for x in range(1, 100):
        # If their seat is taken assign them a random remaining seat
        if x in passangers[:x]:
            passangers[x] = randint(x+1, 101) % 100
    
    
    # Check if the last passanger is in their seat
    if passangers[99] == 99:
        final_seat_check = True
    else:
        final_seat_check = False


    return final_seat_check
def main():
    num_of_simulations = 1000
    # Make a list of simulation results
    results = []
    
    for x in range(1, num_of_simulations):
        temp = simulate()
        results.append(temp)
        
    num_of_positives = 0
    for result in results:
        if result == True:
            num_of_positives+=1
        
    
    probabilty = num_of_positives / num_of_simulations
    print(probabilty)
    
# Call main() when this program runs
if __name__ == '__main__':
    main()