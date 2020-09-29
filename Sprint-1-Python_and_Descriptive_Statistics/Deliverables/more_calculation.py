"""
Hiroki Sato 
09/29/20

Deliverable Problem No.2: More Calculation

Open the data.txt file and calculate mean, median, variance, and standard deviation of the data
    * Use of with open & file reading
    * Use matplotlib
    * Use sqrt from math
    
"""
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from math import sqrt

#opening a file here and argument 'r' specifying that we are reading this file 
with open ('data.txt','r') as f: 
    
    values =[float(x.strip()) for x in f]
   
# calculating mean by using len and sum function
def mean(vs):

    return sum(vs)/len(vs)
    

# calculating median for the data
def median(vs):
    
    vs.sort()
    if len(vs)%2==0:
        median = (vs[int((len(vs)/2)+1)] + vs[int((len(vs)/2)-1)])/2 
    else:
        median = vs[int(len(vs)/2)+1]
        
    return median
    
#Calculating variance of the data
def variance(vs):
    
    m = mean(vs)
    
    vs = [(x-m)**2 for x in vs]
    
    return sum(vs)/len(vs)

def std_deviation(vs):
    
    v = variance(vs)
    return sqrt(v)
    
    
#Printing out the mean, median, variance and standard deviation
print("Mean : %.3f" % mean(values))
print("Median: %.3f" % median(values))
print("variance: %.3f" % variance(values))
print("Standard deviation: %.3f" % std_deviation(values))

#Creating boxplot and histogram
# we use fig function to initialize the plot
# Creating a boxplot, the vert is a parameter which takes boolean values in, to 
#specify whether the matplotlib is going to create a vertical or horizontal boxplot.
plt.figure()
plt.boxplot(values,vert=False)
plt.title('data.txt Boxplot')
plt.xlabel('Value')
plt.savefig('calculation_boxplot1.pdf',bbox_inches='tight')

# Creating a histogram with 20 bins 
# First we are not overwriting on top of the boxplot 
# so we call figure() and create brand new plot

plt.figure()
plt.hist(values,20)
plt.title('data.txt  histogram')
plt.xlabel('Values')
plt.ylabel('Count')
plt.savefig('calculation_histogram1.pdf',bbox_inches='tight')

