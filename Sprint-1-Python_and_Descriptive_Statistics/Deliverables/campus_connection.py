"""
Hiroki Sato 
09/29/20

Deliverable problem No.4 : Campus connection

Find out the number of unique students are related to each student as they take classmethod
    * Use csv library
    * Use matplotlib
    * Use sqrt from math
    * Use dictionaries as hashmaps to demonstrate the relationship 
        between each student through courses they are registered.
        
    ** the helper functions, hashmaps, and how we open the file is identical to 
    the preious class size problem.
"""
#Import needed libraries
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 
import csv
from math import sqrt

# Helper functions: mean, median, variance and standard standard deviation
def median(vs):
    
    vs.sort()
    
    if len(vs)%2==0:
        median = (vs[int((len(vs)/2)+1)] + vs[int((len(vs)/2)-1)])/2 
    else:
        median = vs[int(len(vs)/2)+1]
        
    return median
    
def mean(vs):

    return sum(vs)/len(vs)

def variance(vs):
    
    m = mean(vs)
    
    vs = [(x-m)**2 for x in vs]
    
    return sum(vs)/len(vs)

def std_deviation(vs):
    
    v = variance(vs)
    return sqrt(v)

# Create three hashmaps using dictionaries 
students_per_course = dict()
courses_per_student = dict()
unique_students = dict()

# Opening csv file enrollment

with open('enrollments.csv','r') as f:
    
    reader = csv.reader(f)
    
    for line in reader:
        # getting the r_number and course_id of each student from each line
        r_number = line[0]
        course_id = line[1]
        
        # if we had not created 
        if(course_id not in students_per_course):
            students_per_course[course_id] = []
        if(r_number not in courses_per_student):
            courses_per_student[r_number] = []
            
        students_per_course[course_id].append(r_number)
        courses_per_student[r_number].append(course_id)
            

# After completing two dictionaries students_per_course and courses_per_student, 
# populate the unique_student dictionary 
for student in courses_per_student:
    
    schedule = courses_per_student[student]
    unique_students[student] = []
    
    for course in schedule:
        
        roster = students_per_course[course]
        
        for person in roster:
            
            if((person not in unique_students[student]) & (person != student)):
                unique_students[student].append(person)
                
                
        
        
# Taking the number of unique students interacted for each student using list comprehension as 
num_unique_student = [len(unique_students[s]) for s in unique_students]

# Perform basic statistical analysis and print them out
print("The median of the number of unique student to each individual student is: %.2f" %  median(num_unique_student))
print("The mean of the number of unique student to each individual student is: %.2f" % mean(num_unique_student))
print("The variance of the distribution of the number of unique student to each individual student is: %.2f" % variance(num_unique_student))
print("The standard deviation of the distribution of the number of student to eahc individual student is: %.2f" % std_deviation(num_unique_student))

# Create plots and save as pdf. Histogram & Boxplot
# 1. Creating a Histogram
plt.figure()
plt.hist(num_unique_student,50)
plt.title('Rollins Campus Connection Histogram')
plt.xlabel('Number of Unique Student')
plt.ylabel('Student Count')
plt.savefig('campus_connection_hist.pdf',bbox_inches='tight')