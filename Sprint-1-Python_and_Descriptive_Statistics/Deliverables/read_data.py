"""
Perform calculations on data.txt to find needed values
"""
import math
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

f = open('data.txt', 'r')

#r is reading mode, f is now the reference to the file 

values = []

for line in f:
    line = line.strip()
    
    values.append(float(line))
    
    


def mean(x):
    #mean is the sum of all the values over the length of the list
    return sum(x)/ len(x)

def median(x):
    #If list is even numbered, take the average of the middle values
    if len(x) % 2 == 0:
        return (x[math.floor(len(x)/2)] +x[math.ceil(len(x)/2)])/ 2
    else:
        #If not, get the middle value
        return [math.ceil(len(x)/2)]
        
def variance(x):
    var_total = 0
    m = mean(x)
    #for all the values, find the difference between the value and the mean and square it
    for i in x:
        var_total = var_total + (m - i)**2
    #divide the sum of squares by n
    return (var_total/len(x))
    
def standard_deviation(var_num):
    #take the sqaure root of the variance
    return math.sqrt(var_num)
    
    


print("Median", median(values))        
print("Mean", mean(values))
print("Variance", variance(values))
print("Standard Deviation", standard_deviation(variance(values)))

plt.figure()
plt.hist(values,20)
plt.xlabel('Data Value')
plt.ylabel('Count')
plt.savefig('20binhist.pdf', bbox_inches = 'tight')

plt.figure()
plt.boxplot(values)
plt.ylabel('Data Value')
plt.savefig('databoxplt.pdf', bbox_inches = 'tight')



