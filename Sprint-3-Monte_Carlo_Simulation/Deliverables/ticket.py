
import random

def simulate():
    
    passengers = []
    
    availableSeats = []
    for i in range(100):
        availableSeats.append(i)
    
    
    x = random.randint(0, len(availableSeats))
    passengers.append(availableSeats[x])
    availableSeats.remove(availableSeats[x])
    
    for i in range(1, 100):
        
        if i in availableSeats:
            passengers.append(i)
            availableSeats.remove(i)
        else:
            x = random.randint(0, (len(availableSeats) - 1))
            passengers.append(availableSeats[x])
            availableSeats.remove(availableSeats[x])

    return passengers[99]        


num = 0
for i in range(0, 100000):
    if simulate() == 99:
        num += 1;
print(num/100000)
