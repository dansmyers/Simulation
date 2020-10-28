""" 
Deliverable Problem No.5 The ticket Problem

Objective: Simulate how first passnger taking a random seat would affect the last person's seating,
           and calculate the probability of last passenger successfully being able to be seated based on the simulation. 
The probability is about .50 

"""
# Importing the needed libraries
from random import randint

# Simulate function to simulate the problem 
def simulate():
    
    # each index represents passenger and value represents their seating
    seating = list()
    
    # first passenger lost their ticket so they took a seat at random between 1 and 100
    first_passenger = randint(1,100)
    # first passenger took the seat
    seating.append(first_passenger)
    
    # so now the rest of the seating depends on the first seating
    # we have 99 people left and we assume that second person have seat 2 and third person has 3 and so on. 
    for seat in range(2,101):
        
        if ( seat in seating):                  # if the seat was already taken
                                                # that person must take a random seatself.
            random_seat = randint(1, 100)

            while ( random_seat in seating):    # passenger must keep looking to find the random seat that is not taken yet. 
                random_seat = randint(1, 100)
            seating.append(random_seat)
        else:                                   # if the previous passengers did not take current passengers assigned seat, take the originally assigned seat. 
            seating.append(seat)
    
    return seating[len(seating)-1] == 100
    
def main():
    list_trial = []
    for trial in range(1000):
        success = simulate()
        list_trial.append(success)
    # Print out the 
    print("The probability of the last passenger successfully being able to take a seat is: ",list_trial.count(True)/len(list_trial))
    
# Execute only when this file was called and executed on command line. Calling Main
if __name__ == '__main__':
   main()