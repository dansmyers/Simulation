"""
Christian Huber
CMS 380, Fall 2020 / Sprint 1 / classSize
This script finds mean and median class sizes and
visualizes the data in a boxplot and a histogram
"""

import csv

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

def meanSize(d):
    x = []
    for key in d:
        x.append(len(d[key]))
    return(sum(x)/len(x))

def medianSize(d):
    x = []
    for key in d:
        x.append(len(d[key]))
    x.sort()
    
    # Calculate mean for middle indexes of an even set
    # by averaging middle two indexes
    if(len(x)%2==0):
        return((x[int(len(x)/2)]+x[int(len(x)/2)-1])/2)

    else:
        return(x[int(len(x)/2)])
    

# Create dictionary that contains students per course
courses = {}

f = open("enrollments.csv", "r")

# Process file with csv reader
reader = csv.reader(f)

for line in reader:

    # Append student to course if course already
    # exists in dictionary
    if(line[1] in courses):
        courses[line[1]].append(line[0])

    # Add new course and student to dictionary
    else:
        courses[line[1]] = [line[0]]

mean = meanSize(courses)
median = medianSize(courses)

# Create an array that contains the class size for each course
classSize = [len(courses[x]) for x in courses]



# Plotting both graphs in one file with plt.subplot
# plt.subplot(rows-columns-index) with index 1 for boxplot
plt.subplot(121)
plt.boxplot(classSize)
plt.title("Average Class Size")
plt.xlabel("Class")
plt.ylabel("Number of Students")

# Index 2 for histogram
plt.subplot(122)

plt.hist(classSize)
plt.title("Class Size")
plt.xlabel("Class Size")
plt.ylabel("Number of Classes")

plt.savefig("classSizeBoxPlotAndHistogram.pdf",bbox_inches="tight")
