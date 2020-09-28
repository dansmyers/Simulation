"""
(The part 1 hand calculations are in the readme)

Reads a set of data from the file 'data.txt' and calculates the mean, median, variance 
and standard deviation

"""

import math
import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot as plt

def mean(list):
	total = 0
	for i in list:
		total = total + i
	return total/len(list)

def median(list):
	median = 0
	index = len(list)/2
	if index%1 != 0:
		index = index-.5
		return list[int(index)]
	else:
		return (list[int(index)]+list[int(index-1)])/2

def variance(avg, list):
	ssd = 0
	for i in list:
		ssd = ssd + (i - avg)*(i - avg)
	return ssd/(len(list)-1)

sorted_list = []

f = open('data.txt', 'r')

#Could take a few seconds
print("Please wait...")

for line in f:
	
	l = float(line)

#Find the position that the element belongs in
	upper = 0
	lower = 0
	flag = True
	count = 0
	
	while flag:
		
		#In the case that there are no elments in the list, or line is larger than any element in the list
		if count == len(sorted_list):
			sorted_list.append(l)
			flag = False
		#If the line is not in the correct place in the list
		elif sorted_list[count] < l:
			count = count+1
		#if the line is in the correct place in the list
		else:
			sorted_list.insert(count, l)
			flag = False

#Perform Calculations
mean = mean(sorted_list)
median = median(sorted_list)
variance = variance(mean, sorted_list)
standard_deviation = math.sqrt(variance)

print("\nMean: ", mean, "\nMedian: ", median, "\nVariance: ", variance, "\nStandard Deviation: ", standard_deviation)

#Create Histogram
plt.figure()

plt.hist(sorted_list, 20)

plt.title('Histogram')
plt.xlabel('Data value')
plt.ylabel('Count')

plt.savefig('histogram.pdf', bbox_inches= 'tight')



