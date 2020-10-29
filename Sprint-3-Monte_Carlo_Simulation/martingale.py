from numpy import random
import matplotlib.pyplot as plt






def simulate():
    bank = 255
    bet = 1
    wheel = []
    
    for n in range(18):
        wheel.append("red")
    for n in range (18):
        wheel.append("black")
    wheel.append("Green")
    wheel.append("Green")
    for n in range (100):
        spin = random.randint(0,38)
        if wheel[spin] == "red" or wheel[spin] == "Green":
            bank = bank - bet
            bet = bet * 2
        if wheel[spin] == "black":
            bank += bet
            bet = 1
        if bank < bet:
           return bank
        
    return bank
data = []
for n in range(100):
    data.append(simulate())

print (data)
plt.figure()
plt.hist(data, 25)
