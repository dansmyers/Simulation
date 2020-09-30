# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv

# Create an empty dictionary to record which students are in each course and which courses each student is taking
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
        students_per_course[course_id] = []
        
    students_per_course[course_id].append(student_id)
    
    if student_id not in courses_per_student:
        courses_per_student[student_id] = []
    courses_per_student[student_id].append(course_id)
    
Num_unique_students = []

#Loop through the student dictionary and compare with the
#course dictionary to find unique student interactions
for student_id in courses_per_student:
    
    #Create a course list to loop through for each student
    #Inititalize a list to hold unique student ids
    course_list = courses_per_student[student_id]
    unique_students = []
    
    #Loops through each course to create a student list
    #Then loops through student list looking for unique
    #student ids
    for course in course_list:
        student_list = students_per_course[course]
        for student in student_list:
            if student not in unique_students:
                unique_students.append(student)
                
                
    #The number of unique students is the length of
    #unique_students - 1 since we do not want to count
    #students interacting with themselves
    Num_unique_students.append(len(unique_students) - 1)   
    
#Prints the average number of unique connections
sum = 0
for i in Num_unique_students:
    sum += i
mean = sum / len(Num_unique_students)
print("The average number of unique student connections is: " + str(mean))

#Creates a histogram of the data
plt.figure()
plt.hist(Num_unique_students, 20)
plt.title("Number of Unique Student Connections")
plt.xlabel("Number of Unique Connections")
plt.ylabel("Count of Students")
plt.savefig("histogram.pdf", bbox_inches= "tight")

