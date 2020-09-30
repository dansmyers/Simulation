#!/usr/bin/python3

"""
noah olmstead harvey
more calculations
17092020
this script calculates the mean, median, variance, and standard deviation for a given data file and then creates two plots of the data
"""

from math import sqrt
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

def mean(l):
    return(sum(l)/len(l))

def median(l):
    l.sort()                                                    #  moved sort() to relevent func (per fritz's note on friday)
    if(len(l)%2==0):
        return((l[int(len(l)/2)]+l[int(len(l)/2)-1])/2)         #  uses len func to reference indexes of the middle two elements
    else:
        return(l[int(len(l)/2)])                                #  uses len func and a cast to int (floor) to reference the index of the middle element

def variance(l):
    m = mean(l)
    sq = [(i-m)**2 for i in l]                                  #  uses list comprehension to create an array of each element minus the mean the result of which is squared
    return(sum(sq)/(len(sq)-1))                                 #  changed variance from POPULATION to SAMPLE (/n, /n-1)

def standardDeviation(l):
    return(sqrt(variance(l)))

with open("data.txt") as f:                                     #  opening file using "with" handles closing the file, the second argument defaults to 'r' (read) in the open func if not specified
    data = f.readlines()                                        #  creates an array containing lines from the file

values = []

[values.append(float(line.strip())) for line in data]           #  removes whitespace on each line, casts to a float value, and appends to the values array

print("MEAN: "+str(mean(values)),"MEDIAN: "+str(median(values)),"VARIANCE: "+str(variance(values)),"STANDARD DEVIATION: "+str(standardDeviation(values)),sep='\n')

plt.figure()
plt.boxplot(values)
plt.title("Data.txt Box-Plot")
plt.xlabel("Data")
plt.ylabel("Values")
plt.savefig("moreCalculationsBoxPlot.pdf",bbox_inches="tight")

plt.figure()
plt.hist(values,20)
plt.title("Data.txt Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("moreCalculationsHistogram.pdf",bbox_inches="tight")