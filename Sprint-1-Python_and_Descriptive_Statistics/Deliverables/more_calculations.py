"""
Alejandra De Osma 
CMS_380 
Dr.Myers   Fall 2020

Sprint_1 / More_Calculations

"""
#Imports:

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from math import sqrt



# Add code here to open the file
f = open('data.txt','r')

# Declare an empty list
values = []

for line in f:
    line = line.strip()  
    
    # Cast to a float and then append to the list
    values.append(float(line))
    
    
"""
Calculation functions

"""

# Now you calculate answers using the values list


# Calculate and return the mean of input list x
def mean(x):
    
    return sum(x) / len(x)
    

 # Calculate and return the mean of input list x
def median(x):
    x.sort()
    
    if( len(x)%2 == 0):
        return ((x[int(len(x)/2)]+x[int(len(x)/2)-1])/2)
        
    else:
        return( x[(int(len(x)/2))])
        

#calculate the variance of the input list x
def variance(x):
    mean_of_x = mean(x)
    
    variance_of_x = [((i-mean_of_x)**2) for i in x]
    return mean(variance_of_x)
    
    
    
    
#calculate the variance of the input list x
def Standard_Deviation(x):
    return sqrt(variance(x))
    
    
#Store the calculated values in variables 
data_mean = mean(values)
data_median = median(values)
data_variance = variance(values)
data_standard_deviation = Standard_Deviation(values)

print(" \nData.txt values:\nMean: %5.3f\nMedian: %5.3f\nVariance: %5.3f\nStandard Deviation: %5.3f\n" % (data_mean,data_median,data_variance,data_standard_deviation))


#Utilize the matplot function to generate the boxplot 
plt.figure()
plt.boxplot(values)
plt.title("Data.txt Boxplot")
plt.xlabel("Data")
plt.ylabel("Values")

#Saving the plot in one file 
plt.savefig("More_Calculations_Boxplot.pdf", bbox_inches="tight")









