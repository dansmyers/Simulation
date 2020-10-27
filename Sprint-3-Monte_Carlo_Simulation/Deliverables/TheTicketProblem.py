"""
Christian Huber
CMS 380, Fall 2020 / Sprint 3 / The Ticket Problem
This script simulates the boarding process for a train. The
goal is to find out how the first passenger's seat selection
affects the last passenger's seating.
"""

from random import randint

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


### FUNCTIONS ###
​def simulate():
    
    # Every Passenger-Index has a Seat-Value
    seats = list()

    
    # Random seat assignment for first passenger
    seats.append(randint(1, 100))

    
    # Assign 99 passengers to remaining seats using ascending
    # seat order (1, 2, 3,...). If target seat is taken, assign
    # random seat.
    for seat in range(2,101):

        # if seat is taken, assign random unoccupied seat
        if ( seat in seats):
            random_seat = randint(1, 100)
            while ( random_seat in seats): 
                random_seat = randint(1, 100)
            seats.append(random_seat)

        # if not, assign following seat
        else: 
            seats.append(seat)
    
    return seats[len(seats)-1] == 100


if __name__ == '__main__':
    list_trial = []
    for trial in range(2000):
        
        success = simulate()
        list_trial.append(success)
    print(list_trial.count(True))
