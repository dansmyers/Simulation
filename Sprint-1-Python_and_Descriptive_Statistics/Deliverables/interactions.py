#!/usr/bin/python3

"""
noah olmstead harvey
interactions
17092020
this script calculates the total number of unique students each student interacts with across their classes given anonymized registration data
"""

from math import sqrt
import matplotlib                                               #  NOTE:  deliverables do not mention creating a plot with this data but...
matplotlib.use("Agg")
from matplotlib import pyplot as plt

def mean(l):                                                    #  copied from moreCalculations.py
    return(sum(l)/len(l))

def median(l):                                                  #  copied from moreCalculations.py
    l.sort()
    if(len(l)%2==0):
        return((l[int(len(l)/2)]+l[int(len(l)/2)-1])/2)
    else:
        return(l[int(len(l)/2)])

def variance(l):                                                #  copied from moreCalculations.py
    m = mean(l)
    sq = [(i-m)**2 for i in l]
    return(sum(sq)/(len(sq)-1))                                 #  changed variance from POPULATION to SAMPLE (/n, /n-1)

def standardDeviation(l):                                       #  copied from moreCalculations.py
    return(sqrt(variance(l)))

with open("enrollments.csv") as f:
    data = f.readlines()

courses = {}                                                    #  course: [STUDENTS]
students = {}                                                   #  student: [COURSES]

for line in data:
    line = line.strip()
    column = line.split(',')
    if(column[1] in courses):                                   #  same logic as classSize.py, but with two dictionaries
        courses[column[1]].append(column[0])
    else:
        courses[column[1]] = [column[0]]
    if(column[0] in students):
        students[column[0]].append(column[1])
    else:
        students[column[0]] = [column[1]]
            
connections = {}                                                #  student: [PEERS]

for student in students:                                        #  this loop adds students as keys to connections with the values being a list of unique peers
    connections[student] = []                                   #  creates a key(student) in connections dictionary
    # for course in students[student]:                            #  iterates through the courses each student is signed-up for
    #     for peer in courses[course]:                            #  iterates through the students in that course
    #         if(peer not in connections[student] and peer != student):   #  if a student(courses value) is not already a peer, and is not the student(connections key)...
    #             connections[student].append(peer)               #  ...append the student(courses value) to the list of peers(connections value)
    [[connections[student].append(peer) for peer in courses[course] if(peer not in connections[student] and peer != student)] for course in students[student]]  #  ^^ SAME AS COMMENTED OUT^^

numberConnections = [len(connections[x]) for x in connections]  #  this creates an array of the numbers of unique connections (an array of the len() of the connections dictionary values)

print(f"MEAN: {mean(numberConnections)}\nMEDIAN: {median(numberConnections)}\nVARIANCE: {variance(numberConnections)}\nSTANDARD DEVIATION: {standardDeviation(numberConnections)}")

plt.figure()
plt.hist(numberConnections,50)                                  #  plot for data
plt.title("Interactions")
plt.xlabel(f"Number of Interactions\n\nAverage: {mean(numberConnections)}\nStandard Deviation: {standardDeviation(numberConnections)}")
plt.ylabel("Count")
plt.savefig("interactionsHistogram.pdf",bbox_inches="tight")