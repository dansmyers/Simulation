"""
Alejandra De Osma 
CMS_380 
Dr.Myers   Fall 2020

Sprint_1 / class_size

"""
#Imports:

import csv
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


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
Calculation functions

"""
def mean_class_size(x):
    courses = []
    
    for student in x:
        courses.append(len(x[student]))
    return(sum(courses)/len(courses))
        
def median_class_size(x):
    courses=[]
    
    for student in x:
        courses.append(len(x[student]))
    courses.sort()
    if( len(courses) % 2==0):
        c1 = courses[int(len(courses) / 2)]
        c2 = courses[int(len(courses)/2 -1)]
        return((c1 + c2) / 2) 
        
    else:
        c = courses[int(len(courses)/2)]
        
        return (c)
        
        
"""
Completing calculations

"""
class_mean = mean_class_size(students_per_course)
class_median = median_class_size(students_per_course)

class_size = [len(students_per_course[x]) for x in students_per_course]
        
        
        
"""
Using Matplot

"""
#First plot -> Box plot

plt.subplot(121)
plt.boxplot(class_size)
plt.title("Avarage Class Size")
plt.xlabel("Class")
plt.ylabel("Number of Students")

#Second plot -> Histogram
plt.subplot(122)
plt.hist(class_size)
plt.title("Class Size")
plt.xlabel("Class Size")
plt.ylabel("Number of Classes")

#Saving the plots in one file
plt.savefig("class_size_Matplot.pdf", bbox_inches="tight")
   