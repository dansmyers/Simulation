"""
Alejandra De Osma 
CMS_380 
Dr.Myers   Fall 2020

Sprint_1 / Interactions

"""
#Imports:

import csv
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from math import sqrt


# Declaring dictionaries 

students_per_course = {}
courses_per_students = {}


# Open the file and create a csv reader
f = open('enrollments.csv', 'r') 

# Creating a csv reader that processes file f
reader = csv.reader(f)

# Reader automatically iterates through the lines in the file


# csv reader automatically turns the line into a list of fields
for line in reader:

    student_id = line[0]
    course_id = line[1]
    
# This if statement checks if we have previously seen that student id
# Registers it in the directory
# Append the course_id to the students courses list 

    if student_id not in courses_per_students:
        
        courses_per_students[student_id]=[]
    courses_per_students[student_id].append(course_id)
        
        
# This if statement checks if we have previously seen that course_id
# Registers it in the directory
# Append the student_id to the spesific courses list of students 
    if course_id not in students_per_course:
        
        students_per_course[course_id]= []
    students_per_course[course_id].append(student_id)
    
"""
Connections
  
"""
#create connections dictionary to store student connections
connections = {}

# Iterate through the students 
for student in courses_per_students:
    # register student in the connections dictionary
    connections[student]=[]
    
    #iterate throught the courses_per_students dictionary
    for course in courses_per_students[student]:

        for classmate in students_per_course[course]:
            #check for unique connections between classmate
            if(classmate not in connections[student] and classmate != student):
                #append classmaate to the connections dictionary
                connections[student].append(classmate)
     
size_of_connections = [len(connections[student])for student in connections]
    

""" 
Calculation functions

"""
#calculate the mean of the input list x
def mean(x):
    return (sum(x)/len(x))
    
    
#calculate the median of the input list x    
def median(x):
    x.sort()
    if(len(x) % 2 == 0):
        x1 = x[int(len(x) / 2)]
        x2 = x[int(len(x) / 2 -1)]
        
        return ((x1+x2) / 2)
        
#calculate the variance of the input list x
def variance(x):
    mean_of_x = mean(x)
    variance_of_x = [((i-mean_of_x)**2) for i in x]
    return mean(variance_of_x)
    
    
#calculate the Standard_Deviation of the input list x
def Standard_Deviation(x):
    return sqrt(variance(x)) 
    
def Average(x):
    return (sum(x) / len(x))
    
 
"""
Completing calculations

""" 
#Store the calculated values in variables

calculated_mean = mean(size_of_connections)
calculated_median = mean(size_of_connections)
calculated_variance = variance(size_of_connections)
calculated_sd = Standard_Deviation(size_of_connections)
calculated_average = Average(size_of_connections)


print(" \nConnections Data:\nMean: %5.3f\nAverage: %5.3f\nMedian: %5.3f\nVariance: %5.3f\nStandard Deviation: %5.3f\n" % (calculated_mean,calculated_average,calculated_median,calculated_variance,calculated_sd))

    
 #Utilize the matplot function to generate the boxplot 
 
plt.hist(size_of_connections,60)
plt.title("Interactions Problem")
plt.xlabel("Number of Unique Interactions")
plt.ylabel("Size")
 
plt.savefig("Interactions_Histogram.pdf",bbox_inches="tight")
 
 
    
    
    
    
    
    
    
    
    
    
    
    
    