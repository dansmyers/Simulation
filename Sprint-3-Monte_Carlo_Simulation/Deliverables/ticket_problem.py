"""
Simulation program to determine the probability that passenger 100 gets to sit in her originally assigned seat.

CMS 380, Fall 2020
Maria Morales
"""

# Import the random module to generate random numbers for the simulation 
import random


def pick_random_seat(x):
    """ 
    Simulate a passanger picking a random avaiable seat
    input: list of avaiable seats 
    outputs: index of chosem seat
    """
    # Pick a random number between 0 and 1. Multiply times the number of avaiable seats and cast that to an integer
    seat = int(random.random() * len(x))
    
    # return the index of the chosen seat in list of avaiable seats x
    return seat
    
def simulate():
    """
    Simulates the process of 100 passangers picking random seats given that the first
    passanger lost his/her ticket.
    inputs: no
    outputs: returns 1 if the 100th passanger got his assigned seat
    """
    
    # Lists the seats avaiable from 1-100
    seats_available = []

    # Maps each passanger to the seat they chose
    seating_chart = {}

    for i in range(1,101):
        seats_available.append(i)
        

    #Let passanger 1 pick a random seat given that he lost his ticket
    p1_seat = seats_available[pick_random_seat(seats_available)]
    # remove chosen seat from the list of avaiable seats 
    seats_available.remove(p1_seat)
    # Map passanger 1 to the seat they chose
    seating_chart[1] =  p1_seat
    
    for passanger in range(2,101):
        
        # if the assigned seat of this passanger is avaiable remove it from the list
        # and update the seating chart
        if passanger in seats_available:
            seats_available.remove(passanger)
            seating_chart[passanger] = passanger
        else:
            new_seat = seats_available[pick_random_seat(seats_available)]
            seats_available.remove(new_seat)
            seating_chart[passanger] = new_seat
    
    if seating_chart[100] == 100:
        return 1 
    else:
        return 0 
    
    
def main():
    """
    Run the simulation 1000 times and determine the probability that 
    passanger 100 sits in her originally assigned seat.
    """
    n_trials = 1000
    num_successes = 0
    
    for trial in range(n_trials):
        num_successes += simulate()
        

    
    print("Probability that passanger 100 seats on her assigned assigned seat: ", (num_successes/1000))

if __name__ ==  '__main__':
    main()