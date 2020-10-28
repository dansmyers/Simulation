"""
Use enrollment to underrstand campus connectivity

CMS380
"""
#Import csv reader
import csv

#Create a dictionary to store list of courses per student
courses_per_student = {}

#Second dictionary to record the students in each course
students_per_course = {}

#Open the enrollment file
f = open('enrollments.csv', 'rU')

#Create a csv reader
reader = csv.reader(f)

#Use for loop to stop through all the lines in the file
for line in reader:
    r_number = line[0]
    c_id = line[1]
    
    print(r_number, c_id)
    
    #If this is the first time you have seen the student
    if r_number not in courses_per_student:
        courses_per_student(r_number) = ()
        
    #Append the cid to the list of student courses
    courses_per_student(r_number).append(c_id)

print(courses_per_student)

#Add two more statements to populate students_per_course
#Similar to what you have now but reverse the numbers



    


