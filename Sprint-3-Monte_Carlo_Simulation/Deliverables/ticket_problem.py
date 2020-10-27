"""
Fritz Stapfer Paz
Sprint 3 - The Ticket Problem
10/28/2020

Simulate the ticket problem with 100 passengers and determine the probability that 
passenger 100 gets to sit in her originally assigned seat

"""

# --------------------------------------------- Imports -----------------------------------------------

from random import random

# --------------------------------------------- Functions ---------------------------------------------

def random_seat(open_seats = [x for x in range(100)]):                    # return a random seat
    seat = (int)(random() * len(open_seats))    # pick a random spot in open_seats
    return(open_seats[seat])                    # return the seat

# -----------------------------------------------------------------------------------------------------

def train_problem():
    passengers = [x for x in range(100)]        # generate list of passengers
    open_seats = [x for x in range(100)]        # generate list of open seats
    train = [0 for x in range(100)]             # generate list of the seated train
    
    p1_seat = random_seat(open_seats)           # assign passenger 1 to a random open seat
    train[p1_seat] = 0                          # seat 1st passenger to random open seat
    passengers.remove(0)                        # remove 1st passenger from passengers
    open_seats.remove(p1_seat)                  # remove seat 1st passenger took
    
    for p in passengers:
        if(p in open_seats):
            train[p] = p                        # if seat isn't taken place original passenger
            open_seats.remove(p)                # remove seat from open seats
        else:
            seat = random_seat(open_seats)      # else get a new random seat
            train[seat] = p                     # place passenger in random seat
            open_seats.remove(seat)                # remove seat from open seats
    
    return(train[-1] == 99)                     # return true or false if last passenger got his seat

# -----------------------------------------------------------------------------------------------------

def run():
    simulation_results = list()                 # list to store the results from all simulations
    for event in range (10000):                 # run 10000 simulations
        simulation_results.append(train_problem())   # append individual result to list
    
    # print result
    prob = sum(simulation_results)/len(simulation_results) 
    print('Probability of the last passenger getting his assigned seat: %.6f' % prob)
    
# -----------------------------------------------------------------------------------------------------
    
if __name__ == '__main__':
    run()
