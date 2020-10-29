
import random

def simulate():
    #list[0] = random.randint(1, 101)
    passengers = []
    availableSeats = []
    for i in range(1, 100):
        availableSeats.append(i)
    
    r = random.randint(0, len(availableSeats))
    
    passengers.append(availableSeats[r])
    availableSeats.remove(availableSeats[r])
    
    for i in range(1, 100):
        if i in availableSeats:
            passengers.append(i)
            availableSeats.remove(i)
        
        else:
            x = random.randint(0, len(availableSeats) - 1)
            passengers.append(availableSeats[x])
            availableSeats.remove(availableSeats[x])
    
    return passengers[-1]
    
    
            
#main- run 1000 times and find prob 
numSuccesses = 0

for i in range(1000):
    trial = simulate()
    if trial == 99:
        numSuccesses += 1




prob = numSuccesses / 1000
print('Probability the last passenger will sit in their assigned seat: ')
print(prob)
