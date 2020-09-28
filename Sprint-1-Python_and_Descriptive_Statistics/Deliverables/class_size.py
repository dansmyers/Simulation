"""

Deliverable Problem No.3: Class size

Find out the mean, median class size at Rollins from the data enrollment.csv
    * Use csv library
    * Use dictionaries as hashmap to demonstrate relationship between students and courses_per_student
    * Use matplotlib to help us visualize the data
    * Use use sqrt from math

"""
# import libraries we need 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 
import csv
from math import sqrt


# Helper functions: mean, median, variance and standard standard deviation
def median(vs):
    
    vs.sort()
    
    if len(vs)%2==0:
        median = (vs[int((len(vs)/2)+1)] + vs[int((len(vs)/2)-1)])/2 
    else:
        median = vs[int(len(vs)/2)+1]
        
    return median
    
def mean(vs):

    return sum(vs)/len(vs)

def variance(vs):
    
    m = mean(vs)
    
    vs = [(x-m)**2 for x in vs]
    
    return sum(vs)/len(vs)

def std_deviation(vs):
    
    v = variance(vs)
    return sqrt(v)

# Create two dictionaries we will use as hashmap
students_per_course = dict()
courses_per_student = dict()

# Open the enrollment.csv file and read throught the file
with open('enrollments.csv','r') as f:
    
    reader = csv.reader(f)
    
    for line in reader:
        # getting the r_number and course_id of each student from each line
        r_number = line[0]
        course_id = line[1]
        
        # if we had not created 
        if(course_id not in students_per_course):
            students_per_course[course_id] = []
        if(r_number not in courses_per_student):
            courses_per_student[r_number] = []
            
        students_per_course[course_id].append(r_number)
        courses_per_student[r_number].append(course_id)
            

# Get the each class size in key-value pair 
# of course_id-number of student
size = dict()

# Getting the class size for each course
for course in students_per_course:
    
    class_size = len(students_per_course[course])
    
    
    size[course] = class_size
    
# For statistical summary purpose we only need numbers 
# Create a list to store the size of classes
# Using list comprehension to get class size of each course

size_list = [len(students_per_course[course]) for course in students_per_course]

print("The median class size is: %.2f" % median(size_list))
print("The mean class size is: %.2f" % mean(size_list))

# Create a Histogram
plt.figure()
plt.hist(size_list,25)
plt.title('Rollins Class Size Histogram')
plt.xlabel('Size of a Class')
plt.ylabel('Number of Students')
plt.savefig('class_size_hist.pdf',bbox_inches='tight')

# Create a boxplot
plt.figure()
plt.boxplot(size_list,vert=False)
plt.title('Rollins Class Size Boxplot')
plt.xlabel('Size of a Class')
plt.savefig('class_size_boxplot.pdf',bbox_inches='tight')
