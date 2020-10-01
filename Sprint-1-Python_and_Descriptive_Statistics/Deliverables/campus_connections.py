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
import statistics

# csv module makes it easy to process delimited text files
import csv

def avg(x):
    total = 0
    for line in x:
        total = total + line
    div = len(x)
    return total/div

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
num_students = []
# Here's an example of how to iterate through the keys in a dictionary
# Print the students in each course
for course_id in students_per_course:
    student_list = students_per_course[course_id]
    num = len(student_list)
    num_students.append(num)
   #print(course_id + ': ' + str(student_list))

num_courses = []
for student_id in courses_per_student:
    course_list = courses_per_student[student_id]
    num2 = len(course_list)
    num_courses.append(num2)
   # print(student_id + ': ' + str(course_list))
   
# Get Average number of students in each class:
avg_students = avg(num_students)
print("This is the average number of students per class:", "{:.2f}".format(avg_students))

# Get median of class sizes
print("The median is:", statistics.median(num_students))

# Get avg connections
unique_connections = []
num_connections= []
for student in courses_per_student:
    courses = courses_per_student[student]
    for course in courses:
        students = students_per_course[course]
        for person in students:
            if person not in unique_connections:
                unique_connections.append(person)
                x = len(unique_connections)
    num_connections.append(x - 1)
    unique_connections.clear()
        
avg_connections = avg(num_connections)
print("The average number of unique connections: ", avg_connections)
"""
    ****FIX PLOT FORMAT ********
"""
   
plt.figure()
plt.hist(num_connections)
plt.xlabel('Num of Connections')
plt.ylabel('Count of Students')
plt.savefig('unique_connections.pdf', bbox_inches='tight')


# Create a box plot

fig = plt.figure()
plt.boxplot(num_connections)
plt.xlabel("Class size")

plt.savefig('box_course.pdf')
    