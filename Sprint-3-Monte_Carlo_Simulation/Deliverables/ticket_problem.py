'''
CMS 380 
Ticket problem
Write a simulation program to determine the probability that
passenger 100 gets to sit in originally assigned setattr
'''
# random number generator
from random import randint

assign_seats = []

# Check to see if the seat is already taken 
def taken(seat_num):
    global assign_seats
    taken = True
    for ticket_num in range(len(assign_seats)-1):
        if assign_seats[ticket_num] == seat_num:
            assign_seats.pop(ticket_num)
            taken = False
    return taken
 

# Simulation for one trial
def simulate():
    global assign_seats
    for i in range(1,101):
       assign_seats.append(i)
    
    # Person 1 takes a random seat
    person_1 = randint(1,100)
    
    # Take that random seat out of the assigned seats 
    assign_seats.pop(person_1 - 1)
    
    # all indeces shift down/left
    
    # Put the rest of the passengers into their seats 
    for person in range(1,99):
        if taken(person):
            # Get a new random number, then remove it from the
            # list of assigned seats.
            seat_num = randint(0, len(assign_seats) - 1)
            assign_seats.pop(seat_num)
    return assign_seats[0]
    

def main():
    max_trials = 1000
    count_hundred = 0
    for i in range(max_trials):
       if simulate() == 100:
           count_hundred += 1
    prob = (count_hundred/1000)
    print("Probability is: ", prob)
    
# Code to run main
if __name__ == '__main__':
    main()
    