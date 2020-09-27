#!/usr/bin/python3

"""
noah olmstead harvey
class size
17092020
this script finds mean and median class sizes given anonymized registration data
"""

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

def meanClassSize(d):
    l = [len(d[key]) for key in d]                              #  creates an array of the number of students (len(value)) for each key(course) in the dictionary
    return(sum(l)/len(l))

def medianClassSize(d):
    l = [len(d[key]) for key in d]
    l.sort()
    if(len(l)%2==0):
        return((l[int(len(l)/2)]+l[int(len(l)/2)-1])/2)         #  uses len func to reference indexes of the middle two elements
    else:
        return(l[int(len(l)/2)])                                #  uses len func and a cast to int (floor) to reference the index of the middle element

with open("enrollments.csv") as f:                              #  stores enrollments as an array of lines in data
    data = f.readlines()

courses = {}                                                    #  COURSE: [STUDENTS]

for line in data:
    line = line.strip()
    column = line.split(',')                                    #  using built-in split() instead of csv reader
    if(column[1] in courses):                                   #  if the course is already a key in dictionary...
        courses[column[1]].append(column[0])                    #  ...reference the key, and append a new student
    else:                                                       #  if the course is NOT already a key in dictionary...
        courses[column[1]] = [column[0]]                        #  ...create dictionary entry for key(course) with a value of [student]

classSize = [len(courses[x]) for x in courses]                  #  an array containing the length of the values in the courses dictionary (class size)

plt.figure()
plt.subplot(121)                                                #  .subplot(rows,columns,index) (referencing the first subplot)
plt.boxplot(classSize)
plt.title("Class Size Box-Plot")
plt.xlabel(f"Class\n\nAverage: {meanClassSize(courses)}")       #  use python3 fString to add calculated mean/median to plot
plt.ylabel("Number of Students")
plt.subplot(122)                                                #  reference second subplot and set param
plt.hist(classSize)
plt.title("Class Size Histogram")
plt.xlabel(f"Number of Students\n\nMedian: {medianClassSize(courses)}")
plt.ylabel("Number of Classes")

plt.savefig("classSizeBoxPlotAndHistogram.pdf",bbox_inches="tight")