"""
use enrollment data to understand campus connectivity
"""

import csv

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


#create a dictionary to store the cids for each student
courses_per_student = {}

#create a second dictionary to store the students in each course
students_per_course = {}


#open enrollments.csv filter
f = open('enrollments.csv', 'r')

#create a csv reader to proccess the filter
reader = csv.reader(f)

#use the for loop to step through all the lines
for line in reader:
    r_number = line[0]
    cid = line[1]
    

    #if this is the first time weve seen the student r number make an entry for it
    if r_number not in courses_per_student:
        courses_per_student[r_number] = []
    
    #append the cid to the students list of courses
    courses_per_student[r_number].append(cid)
    
    #if this is the first time weve seen the course id number make an entry for it
    if cid not in students_per_course:
        students_per_course[cid] = []
    
    #append the r-nuber to the cid list of students
    students_per_course[cid].append(r_number)
    


#number of students per course id
num_students = {} #dictionary that stores the class number key and the number of students in that class
num_stud = [] #array that stores the number of students per couse

for cid in students_per_course:
    if cid not in num_students:
        num_students[cid] = []
    
    #append the number of students
    num_students[cid] = len(students_per_course[cid]);
    num_stud.append(len(students_per_course[cid]))


#--------------------------------------------------
#Mean and median functions:
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
    tempo = []
    for i in x:
        tempo.append(float(i))

    while len(tempo) > 1:
        tempo.remove(min(tempo))
        tempo.remove(max(tempo))
        if (len(tempo) == 2):
            return mean(tempo)
    
    return tempo[0]


def mean(x):
    sum = 0.0
    num = 0.0
    for i in x:
        sum += i
        num += 1.0
    return sum/num


#----------------------------------
print('Mean: ')
print(mean(num_stud))
print('Median: ')
print(median(num_stud))



#create a new figure -- always do this before calling a plotting fuunction
#histogram
plt.figure()

#plot a histogram of the data with 15 bins
plt.hist(num_stud, 15)


#set title and axis labels
plt.title('Students per Course')
plt.xlabel('courses')
plt.ylabel('number of students')

#save the figure to a file 
plt.savefig('students_per_course.pdf', bbox_inches = 'tight')


#boxplot
plt.figure()
plt.boxplot(num_stud, vert = 0, labels = ['#ofStud.'])
plt.title('Students_per_course.bxplt')
plt.savefig('studentspercourseboxplot.pdf')


##unique classmates per student

classmates_per_student = {} #dictionary: students r number is the key and the values are rnumber sof their unique classmates

for r_number in courses_per_student:
    
    studentsclasses = []#temporary array of the current students courses
    classesstudents = []#temporary array of the current courses students

    classmates_per_student[r_number] = []
        
    studentsclasses = courses_per_student[r_number]

    for classnumb in studentsclasses:#iterate through classes of the current student
        classesstudents = students_per_course[classnumb]
        for studentnum in classesstudents:
            if (studentnum not in classmates_per_student[r_number]) and (studentnum != r_number):
                #checks the current r_number and adds it only if it is not the current student or if it is already added
                classmates_per_student[r_number].append(studentnum)


        
unique_connections_per_student = {}#dict of number of unique classmates each r number has
classmates_student = [];#array of number of classmates

for r_number in classmates_per_student:
    unique_connections_per_student[r_number] = []
    unique_connections_per_student[r_number].append(len(classmates_per_student[r_number]))
    classmates_student.append(len(classmates_per_student[r_number]))

print(unique_connections_per_student)

print('Mean: ')
print(mean(classmates_student))
print('Median: ')
print(median(classmates_student))

#create a new figure -- always do this before calling a plotting fuunction
#histogram
plt.figure()

#plot a histogram of the data with 20 bins
plt.hist(classmates_student, 20)


#set title and axis labels
plt.title('Classmates per Student')
plt.xlabel('Student')
plt.ylabel('number of classmates')

#save the figure to a file 
plt.savefig('classmates_per_student.pdf', bbox_inches = 'tight')


#boxplot
plt.figure()
plt.boxplot(classmates_student, vert = 0)
plt.title('classmates_per_student.bxplt')
plt.savefig('classmates_per_student_boxplot.pdf')

