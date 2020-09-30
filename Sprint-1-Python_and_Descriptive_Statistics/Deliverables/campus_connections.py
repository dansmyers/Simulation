""" 
Use enrollement data to understand campus connectivity

CMS 380 Fall 2020
"""

import csv
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

#Create a dictionary to store c_ids for e/ student
courses_per_student = {}

#Second dictionary to store the students in e/ course
students_per_course = {}

# Open and read the enrollements csv file 
f = open('enrollments.csv', 'r')

#Create a csv reader to process file
reader = csv.reader(f)

#use for loop to step through every line of the file
for line in reader:
    r_number = line[0]
    c_id = line[1]
    
    #print(r_number, c_id)
    
    #If this is the first time we've seen the student r number 
    #make an entry for it in the dictionary
    if r_number not in courses_per_student:
        courses_per_student[r_number] = []
    
    #Append the cids to the student's list  of courses
    courses_per_student[r_number].append(c_id)
    
    #I need to add two more statements to populate students_per_course
    #Similar to what we have now, but we are gong to reverse r_number and c_id
    if c_id not in students_per_course:
        students_per_course[c_id] = []
        
    #Append the students to the cid's 
    students_per_course[c_id].append(r_number)
    
#This prints the student:c1, c2, c3    
#for r_number in courses_per_student: 
    #print(r_number, courses_per_student[r_number])

#This prints the class and the students in it
#for c_id in students_per_course: 
    #print(c_id, students_per_course[c_id])


#CLASS SIZES


#Now, find mean and median class sizes and Create a box plot and a histogram to show the distribution of class sizes. Make sure to label the axes of your plots.
class_size = 0
class_size_list = []
for c_id in students_per_course:
    #How many persons in e/ class
    class_size = len(students_per_course[c_id]) + class_size
    class_size_list.append(len(students_per_course[c_id]))

#how many classes
number_of_classes = len(students_per_course)
#print (len(students_per_course))

#find mean of class size
mean = class_size/number_of_classes
print("The mean class size is: {0}" .format(mean))

#find the median of the class sizes
class_size_list.sort()
median = class_size_list[len(class_size_list)//2]
print("The median class size is: {0}" .format(median)) 

#print(class_size_list)

#Plot Histogram for class sizes
plt.figure()
plt.hist(class_size_list, 20)
plt.xlabel("class sizes")
plt.ylabel("count")
plt.savefig('class_size_hist.pdf', bbox_inches='tight')

#Plot box Plot for class sizes
plt.figure()
plt.boxplot(class_size_list)
plt.ylabel("class sizes")
plt.savefig('class_sizes_box_plot.pdf', bbox_inches='tight')


#INTERACTIONS


#print(courses_per_student[r_number])#que me de un course num YES
#print(len(courses_per_student[r_number]))
#for key in students_per_course:
    #print(key)
number_of_unique_students = []
unique_students = []
#print(students_per_course[c_id])


i = 0 

for r_number in courses_per_student:
    #list of the classes the student has
    #access students first course   
    #print(courses_per_student[r_number])
    for c_id in students_per_course:
        if str(courses_per_student[r_number][i]) ==  c_id and i < (len(courses_per_student[r_number])):
            #print('ok')
            if students_per_course[c_id] not in unique_students:
                unique_students = list(students_per_course[c_id])
            i = 1 + i
        #reset i 
        i = 0
    #print(len(unique_students))
    number_of_unique_students.append(len(unique_students))
    #reset unique_students
    unique_students = []    
    
#print(number_of_unique_students)
number_of_students = len(number_of_unique_students)
total_interactions = sum(number_of_unique_students)

#find average number of unique connections that each student experiences
mean2 = total_interactions/number_of_students
print("The average number of unique connections that each student experiences is: {0}" .format(mean2))

#find the median number of unique connections that each student experiences
number_of_unique_students.sort()
median2 = number_of_unique_students[len(number_of_unique_students)//2]
print("The median number of unique connections that each student experiencesis: {0}" .format(median2))

#Plot Histogram for the number of unique connections that each student experiences
plt.figure()
plt.hist(number_of_unique_students, 20)
plt.xlabel("number of unique students")
plt.ylabel("count")
plt.savefig('unique_students_hist.pdf', bbox_inches='tight')

#Plot box Plot for class sizes the number of unique connections that each student experiences
plt.figure()
plt.boxplot(number_of_unique_students)
plt.ylabel("number of unique students")
plt.savefig('unique_students_box_plot.pdf', bbox_inches='tight')


    

    
    

        






    













