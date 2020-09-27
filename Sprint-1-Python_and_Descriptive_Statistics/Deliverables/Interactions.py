"""
Christian Huber
CMS 380, Fall 2020 / Sprint 1 / Interactions
This script uses student registration data to determine
the average and distribution of the number of unique
connections that each student experiences through classes.
"""

import csv
from math import sqrt

def mean(x):
    """
    Calculate and return the mean of input list x
    """
    return sum(x) / len(x)


def variance(x):
    """
    Calculate and return the variance of input list x
    """
    m = mean(x)

    # Create an array with the value of each (element - mean)^2
    v = [((i-m)**2) for i in x]
    return mean(v)


def stDev(x):
    """
    Calculate and return the Standard Deviation
    of input list x
    """
    return sqrt(variance(x))


def coeffV(x):
    """
    Calculate and return the coefficient of variance
    """
    return stDev(x) / mean(x)


# Course dictionary containing student IDs per course
courses = {}

# Student dictionary containing course IDs per student
students = {}


f = open("enrollments.csv", "r")

# Process file with csv reader
reader = csv.reader(f)

for line in reader:
    
    # If course is already in courses{}, add student
    # to that course
    if(line[1] in courses):
        courses[line[1]].append(line[0])

    # If not, add course to dictionary, then add student
    else:
        courses[line[1]] = [line[0]]

    # Same for students{}:
    if(line[0] in students):
        students[line[0]].append(line[1])
    else:
        students[line[0]] = [line[1]]


# Dictionary containing unique peers per student
connections = {}


# Populate connections{} with students(key) and their
# unique peers(values)
for student in students:
    
# Creates new student key
    connections[student] = []
    
    # Loop through each student's courses
    for course in students[student]:

        # Loop through the students in those courses
        for peer in courses[course]:

            # If a student from courses{} is not already a
            # unique peer and is not the key student,
            # append that student to the connections{}values
            if(peer not in connections[student] and peer != student):
                connections[student].append(peer)
                

# Create an array containing the number of unique peers of every
# student by using the number of values per student in students{}
numberConnections = [len(connections[x]) for x in connections]

# Print mean and distribution measures
print("The mean number of connections per student is:", mean(numberConnections))
print("The variance across the number of connections per student is:", variance(numberConnections))
print("The standard deviation is:", stDev(numberConnections))
print("The coefficient of variance is:", coeffV(numberConnections))
