"""
Alejandra De Osma 
CMS_380
Sprint 3 
Ticket Problem

"""
#IMPORTS
from random import random


def seat (empty_seat = [x for x in range(100)]):
#returning a random seating
    seat_1 = (int)(random() * len(empty_seat))
    #random number that selects a random spot in empty_seats
    #returns the seat
    return(empty_seat[seat_1])

def train_p():
    # This call generates a list of random passangers in rage 100
    passangers = [p for p in range(100)]
    # This call generates a list of available seats
    available_seats = [ s for s in range(100)]
    # this call generates a list or the occupied seats in the train 
    train_1 = [0 for x in range(100)]
    
    # assignning a random seat to the first passanger
    seat_p1 = seat(available_seats)
    # Locate and seat first passanger to seat
    train_1[seat_p1]= 0 
    # remove passanger 1 from the list of passangers
    passangers.remove(0)
    # remove seat that is now occupied by passanger 1
    available_seats.remove(seat_p1)
    
    # Iterating through the list of passangers
    for p in passangers:
        #Test to see if seat is taken
        if (p in available_seats):
            # If it is not taken assign that passenger to that seat
            train_1[p] = p 
            # Remove sear from seats list
            available_seats.remove(p)
            
        else:
            # Else generate a new random seat
            seat_2 = seat(available_seats)
            #Locate passanger to that seat
            train_1[seat_2] = p
            # remove that seat from the available seats
            available_seats.remove(seat_2)
            
    # Returning boolean value to see if passanger got a seat
    return(train_1[-1] == 99)
#main   
def main():
    # Using a list to store the results 
    results = list()
    # Running 1,000 trials 
    for trial in range(1000):
        #appending the train methods outputs to the list of results
         results.append(train_p())
         
    #Get length of list
    length = len(results)
    # get the sum of all the values in the results list 
    sum_r = sum(results)
    # Finging the probability 
    prob = sum_r/length
    
    #printing results and the probability value 
    print('\nProbability of last passenger gettig seat assignment:%6f\n' % prob)
    
    
# Final call to main 
if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    