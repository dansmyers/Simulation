"""
Fritz Stapfer Paz
Campus Connections - Class Size
09/30/2020


Use the data to find the mean and median class sizes. 
Create a box plot and a histogram to show the distribution of class sizes. 
Make sure to label the axes of your plots.
"""

# Used to read/parse csv
import csv
# Required setup for matplotlib
import matplotlib
matplotlib.use('Agg')               # <-- Required on Mimir
from matplotlib import pyplot as plt


# Create a dictionary to store the cids for each student
courses_per_student = {}

# Second dictionary to store the students in each course
students_per_course = {}


# Open the enrollments.csv file
f = open('enrollments.csv', 'r')

# Create a csv reader to process the file
reader = csv.reader(f)

# Use the for loop to step through all lines in the file
for line in reader:
    r_number = line[0]
    cid = line[1]
    
    # If this is the first time we've seen the student r-number,
    # make an entry for it in the dictionary
    if r_number not in courses_per_student:
        courses_per_student[r_number] = []
    # Append the cid to the student's list of courses
    courses_per_student[r_number].append(cid)
    
    
    # If this is the first time we've seen the student r-number,
    # make an entry for it in the dictionary
    if cid not in students_per_course:
        students_per_course[cid] = []
    # Append the r_number to the course's list of student
    students_per_course[cid].append(r_number)


#Helper Functions to Calculate Mean and Median
def mean_class_size(x):                         # Pass students_per_course as x
    classes = []                                # Array that will hold the number of students per class
    for student in x:                           # For each student in x
        classes.append(len(x[student])) 
        
    return(sum(classes)/len(classes))           # Return mean
    
def median_class_size(x):                         # Pass students_per_course as x
    classes = []
    for student in x:
        classes.append(len(x[student]))
        
    classes.sort()
    
    if(len(classes) % 2 == 0):                  # Calculate median
        e_1 = classes[int(len(classes) / 2)]    # First Middle Element
        e_2 = classes[int(len(classes)/2 -1)]   # Second Middle Element
        e_sum = e_1 + e_2                       # Add middle two elements

        return (e_sum / 2)                      #Return Average of the Middle Elementss
    else:
        e = classes[int(len(classes)/2)]        # Middle Element
        return (e)                              # Return Middle Element


# Perform Calculations
mean = mean_class_size(students_per_course)
median = median_class_size(students_per_course)
class_size = [len(students_per_course[x]) for x in students_per_course]  


# NatPlotLib stuff goes here
# Noah figured out how to put two plots in a single pdf, so I am using his code for this

plt.subplot(121)                                # First Subplot
plt.boxplot(class_size)
plt.title("Average Class Size")
plt.xlabel("Class")
plt.ylabel("Number of Students")

plt.subplot(122)                                # Second Subplot
plt.hist(class_size)
plt.title("Class Size")
plt.xlabel("Class Size")
plt.ylabel("Number of Classes")

plt.savefig("class_size.pdf",bbox_inches="tight")
