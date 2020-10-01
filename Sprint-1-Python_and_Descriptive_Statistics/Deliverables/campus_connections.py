"""
    Use enrollement data to understand campus connectivity
    
    CMS 380, Fall 2020
    Jay Jiranek
"""

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import csv
import statistics

#functions
def min(x):
    minimum = x[0]
    for i in x:
        if i < minimum:
            minimum = i
    return minimum
    
def max(x):
    maximum = x[0]
    for i in x:
        if i > maximum:
            maximum = i
    return maximum
def median(x):
    num = []
    for i in x:
        num.append(float(i))     
    while len(tempo) > 1:
        num.remove(min(num))
        num.remove(max(num))
    return num[0]
    
def mean(x):
    sum = 0.0
    count = 0.0
    for i in x:
        sum += i
        count += 1
    return sum/count


# create a dictionary to store the cids for each student
courses_per_student = {}

# second dictionary to store the students in each course
students_per_course = {}
# Open the enrollments.csv file 
f = open('enrollments.csv', 'r')

# Create a csv reader to process the file
reader = csv.reader(f)

# Use the for loop to step through all lines in the file
for line in reader:
    r_number = line[0]
    cid = line[1]
    
    # If this is the first time we've seen the student r-number, make an entry in dictionary
    if r_number not in courses_per_student:
        courses_per_student[r_number] = []
    
    # Append the cid to student's list of courses 
    courses_per_student[r_number].append(cid)
    
    #Add two more statements to populate the students per course
    # reverse roles of r_number and cid
    if cid not in students_per_course:
        students_per_course[cid] = []
        
    students_per_course[cid].append(r_number)

            

 #   print(r_number, courses_per_student[r_number])
number_of_students = []
for cid in students_per_course:
    if isinstance(students_per_course[cid], list):
        number_of_students.append(len(students_per_course[cid]))
print("Average students per course:", statistics.mean(number_of_students))
print("Median number of student per course:", median(number_of_students))

#create a new figure -- always do this before calling a plotting fuunction
plt.figure()
#plot a histogram of the data with 15 bins
plt.hist(number_of_students, 30)
#set title and axis labels
plt.title('Students per Course')
plt.xlabel('Courses')
plt.ylabel('Number of students')
#save the figure to a file 
plt.savefig('students_per_course.pdf', bbox_inches = 'tight')

#box plot 
plt.figure 
plt.boxplot(number_of_students, vert = 0)

plt.title("Students per course")
plt.xlabel("number of students in course")
plt.ylabel("course")

plt.savefig("students_per_course.pdf", bbox_inches = 'tight')

# Interactions

classmates = {}

for r_number in courses_per_student:
    student_classes = []
    classes_student =[]
    
    classmates[r_number] = []
    
    for classnum in classes_student:
        classes_student = students_per_course[classnum]
        for studentnum in classes_student:
            if studentnum not in classmates[r_number] and studentnum != r_number:
                classmates[r_number].append(studentnum)
    
    student_interactions = {}
    for r_number in classmates:
        student_interactions[r_number] = []
        student_interactions[r_number].append(classmates[r_number])
        
    print(student_interactions)
