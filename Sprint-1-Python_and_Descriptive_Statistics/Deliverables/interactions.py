"""
Fritz Stapfer Paz
Campus Connections - Interactions
09/30/2020


How many unique students does each Rollins student interact with in classes?
Determine the average and distribution of the number of unique connections 
    that each student experiences through classes.
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


# Check for Connections
connections = {}                                        # Create a dictionary to store the connections
for student in courses_per_student:                     # Iterate through every student
    connections[student] = []                           # and create a entry in connections for every student
    
    for course in courses_per_student[student]:         # Iterate through every course per student
        for peer in students_per_course[course]:        # Then get every student in that course
            if(peer not in connections[student] and peer != student):   # Check for unique connections
                connections[student].append(peer)       # Append peer to connections dictionary

# Create an array with the number of unique connections from connections dictionary
number_of_connections = [len(connections[student]) for student in connections]


# Print Average of Unique Connections
average = (sum(number_of_connections) / len(number_of_connections))
print(f'Each student has on average {average} unique connections.')


# Show distribution 

# MatPlotLib stuff goes here
plt.hist(number_of_connections,50)
plt.title("Interactions")
plt.xlabel("Number of Interactions")
plt.ylabel("Count")

plt.savefig("interactions_distribution.pdf",bbox_inches="tight")