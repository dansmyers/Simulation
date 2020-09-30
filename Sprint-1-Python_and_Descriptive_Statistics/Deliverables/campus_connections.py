"""
Mariah Haskell
CMS 380

How densely connected is Rollins campus? 
Determine the average and distribution of the number of unique connections that each student experiences through classes
"""

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv

# Create an empty dictionary to record which students are in each course
students_per_course = {}
courses_per_student = {}

# Open the file and create a csv reader
f = open('enrollments.csv', 'r')
reader = csv.reader(f)

# Reader automatically iterates through the lines in the file
for line in reader:
    
    # csv reader automatically turns the line into a list of fields
    student_id = line[0]
    course_id = line[1]
    
    if course_id not in students_per_course:
        # Makes a new empty list for each new student
        students_per_course[course_id] = []
    students_per_course[course_id].append(student_id)
    
    if student_id not in courses_per_student:
        courses_per_student[student_id] = []
    courses_per_student[student_id].append(course_id)
    
# Here's an example of how to iterate through the keys in a dictionary
# Print the students in each course
for course_id in students_per_course:
    student_list = students_per_course[course_id]
   #print(course_id + ': ' + str(student_list))


for student_id in courses_per_student:
    course_list = courses_per_student[student_id]
   # print(student_id + ': ' + str(course_list))
plt.figure()
plt.hist(course_list)
plt.xlabel('Student')
plt.ylabel('Num of Courses')

# Create a box plot
    
    