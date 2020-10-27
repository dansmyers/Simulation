#!/usr/bin/python3

"""
noah olmstead harvey
the ticket problem
21102020
this script calculates the chance the final passenger to board a train will get their assigned seat
"""

####  IMPORTS  #################################################################################################################

from random import random

####  FUNCTIONS  ###############################################################################################################

def randSeat(openSeats = [x for x in range(100)]):              ####  returns the index of an available seat  ##################
    return(openSeats[(int)(random()*len(openSeats))])           #  returns a random open seat

def boardTrain():                                               ####  main simulate func, returns train array with passangers  #
    passengers = [x for x in range(100)]                        #  an array of passengers 0-99
    openSeats = [x for x in range(100)]                         #  an array of open seats 0-99
    train = [0 for x in range(100)]                             #  an array representing the passengers on the train, init to 0s
    passenger1 = randSeat(openSeats)                            #  the first passenger takes a random seat
    passengers.remove(0)                                        #  the first passenger is removed from the array of passengers
    train[passenger1] = 0                                       #  sets the first passenger's seat to 0 (for consistency)
    openSeats.remove(passenger1)                                #  removes the first passenger's seat from the open seats array
    #print(f"Passenger: 1  Seat:  {(passenger1+1)}")                                                           ##  DEBUGGING  ##
    for passenger in passengers:                                #  iterate through the remaining passengers 1-99
        if(passenger in openSeats):                             #  if their seat is open...
            train[passenger] = passenger                        #  ...add passenger to the train array at their original seat
            openSeats.remove(passenger)                         #  ...remove passenger's original seat from the open seats array
            #print(f"Passenger: {(passenger+1)}  Seat: {(passenger+1)}")                                       ##  DEBUGGING  ##
        else:                                                   #  if their seat is already taken...
            newSeat = randSeat(openSeats)                       #  ...find a random open seat
            train[newSeat] = passenger                          #  ...add passenger to the train array at their new seat
            openSeats.remove(newSeat)                           #  ...remove passenger's new seat from the open seats array
            #print(f"Passenger: {(passenger+1)}  Seat: {(newSeat+1)}")                                         ##  DEBUGGING  ##
    return(train)                                               #  return the train array, passengers (value) in seat (index)

####  MAIN  ####################################################################################################################

def main():                                                     ####  main  ####################################################
    lastPassenger = []                                          #  boolean array, last passenger got their assigned seat
    for i in range(10000):                                      #  runs the boarding simulation 10,000 times
        lastPassenger.append((boardTrain()[-1]==99))            #  chacks if the last seat has the final passenger (99)
    print(f"the last pasenger gets their original seat with a probability of: {(sum(lastPassenger)/len(lastPassenger))}")

if(__name__=="__main__"): main()                                ####  runs main when executed from cli  ########################
