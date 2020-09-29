"""
Use enrollment to understand campus connectivity

CMS380 Fall 2020
"""

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#Import csv reader
import csv

#Create an empty dictionary to record the students in each course
students_per_course = {}

#Create an empty disctionary to record the students courses
courses_per_student = {}

#Open the enrollment file and create csv reader
f = open('enrollments.csv', 'r')
reader = csv.reader(f)

#Use for loop to stop through all the lines in the file
for line in reader:
    r_number = line[0]
    c_id = line[1]
    
    #If this is the first time you have seen the course
    if c_id not in students_per_course:
        students_per_course[c_id] = [r_number]
        
    #Append the student to the list of courses
    students_per_course[c_id].append(r_number)
    
    #If this is the first time you have seen the student
    if r_number not in courses_per_student:
        courses_per_student[r_number] = [c_id]
    
    #Append the course to the student
    courses_per_student[r_number].append(c_id)

#Create an empty list to store number of students per course
length_list = []

#Loop through courses storing number of students per course in list
for c_id in students_per_course:
    student_list = students_per_course[c_id]
    number_of_students = len(student_list) - 1
    length_list.append(number_of_students)
    

#Visualization purposes
#print(sorted(length_list))
#print(len(length_list))

#Calculates the mean or average of a list
def mean(x):
    """
    Calculate and return the mean of input list x
    """
    
    return sum(x) / len(x)


#Median function calculates the median value given a list
def median(x):
    """
    Calculate and return the median of input list x
    """
    # Sort the list
    sorted(x)
    
    # Get the length
    n = len(x)
    
    # if even the median is in the middle
    if n % 2 != 0: 
        return float(x[int(n / 2)]) 
    
    # If its odd average two numbers in the middle    
    return float((x[int((n-1)/ 2 )] + x[int(n / 2)]) / 2)

# Print the median and average of class sizes 
print('The median class size is: ', median(length_list))
print('The average class size is: ', mean(length_list))


# Find the number of unique students met for each individual student

#Create an empty list to store number of unique students per student
unique_students_list = []

#Loop through students to get course list
for r_number in courses_per_student:
    course_list = courses_per_student[r_number]
    #Create an empty list to store unique students
    unique_students = []
        
    #Loop through the students courses to get classes
    for c_id in course_list:
        student_list = students_per_course[c_id]
        
        for student in student_list:
            #Check if student has been seen
            if student not in unique_students:
                unique_students.append(student)
            
    temp = len(unique_students)
    unique_students_list.append(temp)

#Print the mean and median of Unique students
print('The median number of unique students meet: ', median(unique_students_list))
print('The average number of unique students meet: ', mean(unique_students_list))


# Create a new figure
plt.figure()

# Create a histogram
plt.hist(length_list, 18)

# Title and axis labels
plt.title('Class Size Distribution')
plt.xlabel('Class Size')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('class_size_histo.pdf', bbox_inches='tight')

#Make a new figure
plt.figure() 

# Creating plot 
plt.boxplot(length_list)

# Title and axis labels
plt.title('Class Size Distribution')
plt.xlabel('Class Size')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('class_size_boxplot.pdf', bbox_inches='tight')
