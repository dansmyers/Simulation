"""
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
Hiroki Sato 
09/29/20

Deliverable Problem No.2: More Calculation
<<<<<<< HEAD
=======
Deliverable Problem No.1: More calculation
>>>>>>> Commit the modifications
=======
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498

Open the data.txt file and calculate mean, median, variance, and standard deviation of the data
    * Use of with open & file reading
    * Use matplotlib
    * Use sqrt from math
    
"""
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from math import sqrt

<<<<<<< HEAD
<<<<<<< HEAD
# Opening a file here and argument 'r' specifying that we are reading this file 
=======
#opening a file here and argument 'r' specifying that we are reading this file 
>>>>>>> Commit the modifications
=======
# Opening a file here and argument 'r' specifying that we are reading this file 
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
with open ('data.txt','r') as f: 
    
    values =[float(x.strip()) for x in f]
   
<<<<<<< HEAD
<<<<<<< HEAD
# Calculate mean by using len and sum function
=======
# calculating mean by using len and sum function
>>>>>>> Commit the modifications
=======
# Calculate mean by using len and sum function
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
def mean(vs):

    return sum(vs)/len(vs)
    

<<<<<<< HEAD
<<<<<<< HEAD
# Calculate median for the data
=======
# calculating median for the data
>>>>>>> Commit the modifications
=======
# Calculate median for the data
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
def median(vs):
    
    vs.sort()
    if len(vs)%2==0:
        median = (vs[int((len(vs)/2)+1)] + vs[int((len(vs)/2)-1)])/2 
    else:
        median = vs[int(len(vs)/2)+1]
        
    return median
    
<<<<<<< HEAD
<<<<<<< HEAD
# Calculate variance of the data
=======
#Calculating variance of the data
>>>>>>> Commit the modifications
=======
# Calculate variance of the data
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
def variance(vs):
    
    m = mean(vs)
    
    vs = [(x-m)**2 for x in vs]
    
    return sum(vs)/len(vs)

<<<<<<< HEAD
<<<<<<< HEAD
# Calculate standard deviation
=======
>>>>>>> Commit the modifications
=======
# Calculate standard deviation
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
def std_deviation(vs):
    
    v = variance(vs)
    return sqrt(v)
    
    
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
# Printing out the mean, median, variance and standard deviation
print("Mean: %.3f" % mean(values))
print("Median: %.3f" % median(values))
print("Variance: %.3f" % variance(values))
print("Standard deviation: %.3f" % std_deviation(values))

# Creating boxplot and histogram
# We use fig function to initialize the plot
# Creating a boxplot, the vert is a parameter which takes boolean values in, to 
# specify whether the matplotlib is going to create a vertical or horizontal boxplot.
plt.figure()
plt.boxplot(values,vert=False)
plt.title('data.txt Boxplot')
plt.xlabel('Value')
plt.savefig('calculation_boxplot.pdf',bbox_inches='tight')

# Creating a histogram with 20 bins 
# and save the plot figure as pdf
<<<<<<< HEAD
=======
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
plt.title('Deliverable First plot')
plt.xlabel('Values')
plt.savefig('Deliverable_boxplot1.pdf',bbox_inches='tight')

# Creating a histogram with 20 bins 
>>>>>>> Commit the modifications
=======
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
# First we are not overwriting on top of the boxplot 
# so we call figure() and create brand new plot

plt.figure()
plt.hist(values,20)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498
plt.title('data.txt  histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.savefig('calculation_histogram.pdf',bbox_inches='tight')
<<<<<<< HEAD
=======
plt.title('Deliverable Second plot')
plt.xlabel('Values')
plt.ylabel('Count')
plt.savefig('Deliverable_histogram1.pdf',bbox_inches='tight')
>>>>>>> Commit the modifications
=======
>>>>>>> 53bc716e619a20ed752dbb534be33d9748bcd498

