"""
Use enrollment data to understand campus connectivity
"""

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import csv

#Same median function as part 2
def median(l):
	median = 0
	index = len(l)/2
	if index%1 != 0:
		index = index-.5
		return l[int(index)]
	else:
		return (l[int(index)]+l[int(index-1)])/2

#Open file
f = open('enrollments.csv', 'r')

#Define dictionaries. Also it's easier to figure out the total enrollements and connections as you go along
courses_per_student = {}
students_per_course = {}
connections_per_student = {}
total_class_enrollments = 0
total_connections = 0;

reader = csv.reader(f)


for line in reader:
	
    student_id = line[0]
    course_id = line[1]
    
    #Populate the course and student dictionaries
    if course_id not in students_per_course:
        students_per_course[course_id] = []
        
    students_per_course[course_id].append(student_id)
    
    
    if student_id not in courses_per_student:
    	courses_per_student[student_id] = []
    
    courses_per_student[student_id].append(course_id)
    
    #define an empty list for each student in the connections per student dictionary
    connections_per_student[student_id] = []
    
    total_class_enrollments = total_class_enrollments + 1
    
#figure out all of the connections
for student in courses_per_student:
	for course in courses_per_student[student]:
		for classmate in students_per_course[course]:
			if classmate not in connections_per_student[student] and classmate != student:
				connections_per_student[student].append(classmate)
				total_connections = total_connections + 1

#get the last two reqired totals and get the averages
total_classes = len(students_per_course)
total_students = len(courses_per_student)

average_connections = total_connections/total_students
average_class_size = total_class_enrollments/total_classes

#turn the course and connection data in the lists. We just need the amount of students or connections 
#respectively for each dict item, the corse or student the numbers correspond to are irrelevant. We need
#the lists for the histogram
courses_list = []
connections_list = []

for i in students_per_course:
	courses_list.append(len(students_per_course[i]))
	
#I looked up this method.
courses_list.sort()

for i in connections_per_student:
	connections_list.append(len(connections_per_student[i]))

#much easier ot find median with a list as opposed to a dict
class_size_median = median(courses_list)

#create the histograms
print("Average Connections: ", average_connections)
print("Average Class Size: ", average_class_size)
print("Median Class Size: ", class_size_median)

plt.figure()

plt.hist(connections_list, 40)

plt.title('Number of connections per student')
plt.xlabel('Amount of Connections')
plt.ylabel('Count')

plt.savefig('connections.pdf', bbox_inches= 'tight')



plt.figure()

plt.hist(courses_list, 25)

plt.title('Number of students in per class')
plt.xlabel('Amount of Students')
plt.ylabel('Count')

plt.savefig('courses.pdf', bbox_inches= 'tight')
