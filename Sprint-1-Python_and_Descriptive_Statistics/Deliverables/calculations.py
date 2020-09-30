"""
Calculate mean, median, variance, and std deviation of hte data in data.txt. Create a box plot and a histogram of the data with 20 bins. 
"""

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

#Open a file

f = open('data.txt', 'r')


#Creat empty list 
values = []

#Use for loop to iterate in line of file
for line in f:
    line = line.strip() #get rid of extra line between data values
    
    #append values form file to data list
    values.append(float(line))
    
   
#Finding the mean
mean = sum(values)/len(values)
print("The mean is: {0}" .format(mean))

#Finding the median
values.sort()
median = values[len(values)//2]
print("The median is: {0}" .format(median)) 
#print(len(values))

#Find variance

variance = sum([((x - mean) ** 2) for x in values]) / len(values)
print("The variance is: {0}" .format(variance)) 

#Find the standard deviation
std_dev = variance **(1/2)
print("The standard deviation is: {0}" .format(std_dev))


 
#print("The sum of values is {0}".format(sum(values)))
    
#Plot Histogram
plt.figure()
plt.hist(values, 20)
plt.xlabel("data value")
plt.ylabel("count")
plt.savefig('data_hist.pdf', bbox_inches='tight')

#Plot box Plot
plt.figure()
plt.boxplot(values)
plt.ylabel("data value")
plt.savefig('data_box_plot.pdf', bbox_inches='tight')




