"""
Randy Springer
CMS 380 Sprint 1
Use enrollment data to understand campus connectivity
"""

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv

# Calculate the mean of the class size
def mean(x):
  
  return(sum(x) / len(x)) 
  
  
# Calculate the median of the class size
def median(x):

  # Sort the list
  y = sorted(x)
  
  if len(y) % 2 == 0:
    return ((y[len(y)//2] + y[len(y)//2 + 1]) / 2)
  else:
    return (y[(len(y)//2) + 1])
  

# Create a dictionary to store the cids for each student
courses_per_student = {}

# Create a second dictonary to store the students in each course
students_per_course = {}

# Open the file and create a csv reader
f = open('enrollments.csv', 'r')
reader = csv.reader(f)

# Use the for loop to step through all lines in the file
for line in reader:
  r_number = line[0]
  cid = line[1]
  
  # If this is the first time we've seen the student r_number,
  # make an entry for it in the dictionary
  if r_number not in courses_per_student:
    courses_per_student[r_number] = []
  
  # Append the cid to the student's list of courses
  courses_per_student[r_number].append(cid)
  
  # Add two more statements to populate the 
  # students_per_course
  if cid not in students_per_course:
    students_per_course[cid] = []
    
  students_per_course[cid].append(r_number)

# make a new list to hold class sizes
size = []

# add the class sizes to the list
for cid in students_per_course:
  size.append(float(len(students_per_course[cid])))

print("The mean of the class sizes is", mean(size))
print("The median of the class sizes is", median(size))

# Plot the histogram
plt.figure()
plt.hist(size, 20)
plt.xlabel('Students')
plt.ylabel('Course')

plt.savefig('Campus_Connections_Class_Size.pdf', bbox_inches='tight')


# Interactions
# Determine the number of unique connections
# for every student in the data set
interactions = {}
for r_number in courses_per_student:
  
  # add the r_number to the dictionary if it does not exist
  if r_number not in interactions:
    interactions[r_number] = []
  
  # iterate over the courses the student is in,
  # then iterate over the course to get the students in it,
  # if the student isn't in the dictionary add them
  for i in courses_per_student[r_number]:
    for i in students_per_course[i]:
      if i not in interactions[r_number]:
        interactions[r_number].append(i)

# create new list to hold number of interactions
new_size = []

# add the interactions to the list
for r_number in interactions:
  new_size.append(float(len(interactions[r_number])))

print("The average of the interactions is", mean(new_size))

# Plot the histogram
plt.figure()
plt.hist(new_size, 20)
plt.xlabel('Interactions')
plt.ylabel('Students')

plt.savefig('Campus_Connections_Interactions.pdf', bbox_inches='tight')








