""" 
Use enrollment data to understand campus connectivity
"""

# Open enrollements.csv

import csv
import math
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#Create a dictionary to store the cids for each student
courses_per_student = {}

#Create dictionary to share students per course 
students_per_course = {}

#Create dictionary to share unique students_per_course
unique_student_connection = {}

#data to make a list of the lengths of each item in the dictionary
data_class_size = []


f = open('enrollments.csv', 'r')

# Create a csv reader to process the file 
reader = csv.reader(f)

# Use the for loop to step through every line in the file
for line in reader:
    r_number = line[0]
    cid = line[1]

    # if this is the first time
    if r_number not in courses_per_student:
        courses_per_student[r_number] = []

    #append the cid to the student's list of courses 
    courses_per_student[r_number].append(cid)
    
    #Add two more statements to populate students_per_course
    if cid not in students_per_course:
        students_per_course[cid] = []
    
    #Append Student to course cid
    students_per_course[cid].append(r_number)
    
    if r_number not in unique_student_connection:
        unique_student_connection[r_number] = []
    
#make a list of the length of each item in the dictionary
def populate_num_class():
    for i in students_per_course:
        data_class_size.append(len(i))


    
def populate_unique(students_course, courses_per_student):

    #go through each index in student connection and make a temp 
    #list of their courses
    for i in unique_student_connection:
        courses_S = courses_per_student[i]
        #go through their list of courses and get the list of
        #students in the course
        for j in courses_S:
            student_L = students_per_course[j]
            #go through all the students and Add
            #students to key list if not in there
            for k in student_L:
                if k not in unique_student_connection[i] and k is not i:
                    unique_student_connection[i].append(k)
                
            
  
    
#Finds the mean by getting the length at each index of dictionary
def find_mean(values):
    total = 0;
    for i in values:
        total = len(values[i]) + total;
        
    return total/len(values)
 
 
def find_median(entered_list):
    length_of_items_list= []
    
    #make a new list of items that are the length per dictionary items
    for i in entered_list:
       length_of_items_list.append(len(entered_list[i]))
     
    s_list = sorted(length_of_items_list)
    
    num = len(s_list)
    
    #get the median from the list of ordered lengths
    index = math.floor(num/ 2)
    median = s_list[index]
    return median

   
def variance(x):
    var_total = 0
    m = find_mean(unique_student_connection)
    #for all the values, find the difference between the value and the mean and square it

    for i in x:
        var_total = var_total + (m - len(x[i]))**2
    #divide the sum of squares by n
    return (var_total/len(x))
    
def standard_deviation(var_num):
    #take the sqaure root of the variance
    return math.sqrt(var_num)



    
    
#class_total = students_per_course_nums(students_per_course)
#Print statements for class lengths and course per student
print("Mean Students per Course:", find_mean(students_per_course))
print("Median Students per Course:", find_median(students_per_course))
print("Mean Course for students:", find_mean(courses_per_student))


#Populate unique dictionary
populate_unique(students_per_course, courses_per_student)
#Print statements for unique students
print("Mean for Unique students:", find_mean(unique_student_connection))
print("Median for Unique students:", find_median(unique_student_connection))
print("Variance for Unique students:", variance(unique_student_connection))
var_uni = variance(unique_student_connection)
print("Standard Deviation Unique Students:", standard_deviation(var_uni))


#Figures
populate_num_class()
plt.figure()
plt.hist(data_class_size,8)
plt.xlabel('Number of Students')
plt.ylabel('Number of Occurances')
plt.savefig('histNumStudents.pdf', bbox_inches = 'tight')

plt.figure()
plt.boxplot(data_class_size)
plt.ylabel('Number of Students')
plt.savefig('boxpltNumStudents.pdf', bbox_inches = 'tight')

