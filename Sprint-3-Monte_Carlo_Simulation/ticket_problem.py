from numpy import random
import matplotlib.pyplot as plt






def simulate():
    seats = [""] * 101
    
    for n in range(100):
        if n == 0:
            random_1 = random.randint(1,101)
            seats[random_1] = n
        elif seats[n] == "":
            seats[n] = n
        else:
            x = True
            while x:
                random_2 = random.randint(1,101)
                if seats[random_2] == "":
                    seats[random_2] = n
                    x = False

    if seats[100] == 99:
        return True
    else:
        return False
                    
total = 0
true = 0
for n in range (1000):
    total += 1
    if simulate():
        true += 1

print (true/total)
