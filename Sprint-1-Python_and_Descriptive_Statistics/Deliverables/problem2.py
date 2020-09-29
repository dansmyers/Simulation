import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math


def mean(values):
    sum = 0
    for i in values:
        sum += i
    
    avg = sum / len(values)
    return avg
    
    
    
def median(values):
    sorted_list = sorted(values)
    mid_high = sorted_list[int((len(sorted_list) / 2))]
    mid_low = sorted_list[int((len(sorted_list) / 2) - 1)]
    if (len(sorted_list) % 2 == 0):
        mid = (mid_high + mid_low)/ 2
        return mid
    else:
        return mid_high
    
    
    
def variance(values):
    avg = mean(values)
    sum = 0
    for i in values:
        sum += (i - avg)**2
    return sum / len(values)
    
    
def std_dev(values):
    return math.sqrt(variance(values))



f = open("data.txt", "r")
# Declare an empty list
values = []

for line in f:
    line = line.strip()  # Remove whitespace
    
    # Cast to a float and then append to the list
    values.append(float(line))
    
    

print(mean(values))
print(median(values))
print(variance(values))
print(std_dev(values))

plt.figure()
plt.hist(values,20)
plt.savefig("histogram.pdf", bbox_inches= "tight")

plt.figure()
plt.boxplot(values)
plt.savefig("boxplot.pdf", bbox_inches = "tight")

    
