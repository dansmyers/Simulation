""" 
Use enorllemt data to understand campus connetcivity
    
CMS 380, Fall 2020

Maria Morales
"""

import csv
from more_calculations import *

# Set up matplotlib and configure it to be used on Mimir 
import matplotlib
matplotlib.use('Agg') # Required because we are using a remote environment
from matplotlib import pyplot as plt

# create a dictionary to store the cids for each student
courses_per_student = {}

# Second dictionary to store the students in each course 
students_per_course = {}

# Create a list to store the total number of students in each course 
class_size = []

# open the enrollments.csv file
f = open('enrollments.csv', 'r')

# Cerate a csv reader to process the file
reader = csv.reader(f)

# Use the for loop to step through all lines in the file
for line in reader:
    r_number = line[0]
    cid = line[1]
    
    print (r_number, cid)
    
    # If this is the frist time we've seen the student r_number, make an entry for it in the dictionary
    if r_number not in courses_per_student:
        courses_per_student[r_number] = [] # Makes a brand new empyt lists of courses associated with this student
        
    # If this is the first time we've seen the course ID, make an entry for it in the  dictionary
    if cid not in students_per_course:
        students_per_course[cid] = [] # Makes a brand new empty lists of students associated with this course
    
    # Append the course id so that it adds to the list of courses associated with that student
    courses_per_student[r_number].append(cid)
    # Append the student ID so that it adds to the list of students associated with that course
    students_per_course[cid].append(r_number)
    
    # Add two more  statements to populate the students_per_course
    # Reverse the roles of r-number and cid 
#print(courses_per_student)

# Iterate through the keys
for r_number in courses_per_student:
    print(r_number, courses_per_student[r_number])
    
for cid in students_per_course:
    print("The course and the students in it are:", cid, students_per_course[cid])
    


# Count the total number of students in each course and append it to the list
for cid in students_per_course:
    class_size.append(len(students_per_course[cid]))

print(class_size)
print('The mean class size: ',calc_mean(class_size))
print('The median class size: ', calc_median(class_size))

# Create a new figure for the histogram
plt.figure()

# Plot a histogram of the data of total students per course 
plt.hist(class_size, 25)

# Set title and axes labels 
plt.title('Class size distribution')
plt.xlabel('Class size')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('class_size_histogram.pdf', bbox_inches='tight')

# Create a new figure for the  boxplot
plt.figure()

# Plot the boxplot of the data of total students per course
plt.boxplot(class_size)

# Set title
plt.title('Class size')

# Save the figure to a file
plt.savefig('class_size_boxplot.pdf', bbox_inches='tight')


