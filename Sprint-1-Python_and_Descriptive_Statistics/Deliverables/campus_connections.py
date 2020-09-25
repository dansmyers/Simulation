"""

<<<<<<< upstream/master
A program that measures the connectivity of the Rollins campus. The program reads a file called enrollments.csv and extracts student courseIds and RNumbers so that they can be inserted into dictionaries. One dictionary will function as a way to organize students per course(with courseID being the key). The other dictionary will function as a way to organize courses per student(with RNumber being the key).
=======
A program that measures the connectivity of the Rollins campus. The program reads a file called enrollments.csv and extracts student courseIds and RNumbers so that they can be inserted into dictionaries. One dictionary will function as a way to organize students per course(with courseID) being the key). 
>>>>>>> HEAD~2

Collaborated with Griffin

CMS380, Fall 2020

"""
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 

import csv


"""
	Function that calculates the average(mean) of a list of data values.

"""

def mean(values):
	
	# Find size of the data set
	count = len(values)
	total = 0
	
	# Sum the values in the data set together
	for i in values:
		total += i
	
	return total/count
	
"""
	Function that calculates the median of a list of data values. The function first sorts the list and then deals with two possible cases in which the length of the data is either even or odd.

"""


def median(values):
	
	# Find Size of data set
	
	count = len(values)
	
	# Sort the data set in order to find the median
	values = sorted(values)
	
	# Check if size of data set is divisible by 2(even size). If so, then the list indexes from 0 to n, where n is an odd number. If not, then the data set must be of an odd size and will index from 0 to n where n is an even number.
	
	if count % 2 == 0:
		# Subtract .5 and add .5 to the nth index(count - 1)/2 in order to find the two numbers that are needed for finding the median.
		
		number_1 = values[int(((count - 1) / 2) - (.5))]
		number_2 = values[int(((count - 1) / 2) + (.5))]
		return (number_1 + number_2)/ 2
	else:
		# The median can be found by just doing nth index/2 and finding the value at that index in the list.
		
		return (values[int((count - 1) / 2)])
		
"""
	build_histogram() uses the pyplot from matplotlib to create a histogram for a list of data values.

"""


def build_histogram(values):
	
	plt.figure()
	plt.hist(values, 20)

	plt.title("Unique Connections Histogram")
	plt.xlabel("Number of Unique Connections")
	plt.ylabel("Count")

	plt.savefig("Unique_Connections_Histogram.pdf", bbox_inches= "tight")
	

"""
	build_boxplot() uses the pyplot from matplotlib in order to create a boxplot for a list of data values.

"""
	
def build_boxplot(values):

	plt.figure()
	plt.boxplot(values)
	plt.xlabel('Data Set')
	plt.ylabel('Class size')
	plt.title('Class Size Boxplot')
	plt.savefig("Class_Size_Boxplot.pdf", bbox_inches= "tight")


"""
	Function that calculates the variance of a list of data values. 
	
"""

def variance(values):
	
	# Setup a variable for summation
	count = 0
	
	# Find size of data set
	
	length = len(values)
	
	# Find mean of the data set 
	
	average = mean(values)
	
	# iterate through the list and sum together (values[0] - mean)^2 ... (values[n] - mean)^2 where n is the last index in the list.
	
	for i in values:
		count += (i - average) ** 2
	
	return count/length


# MAIN



# Open file and create reader

file = open('enrollments.csv', 'r')
reader = csv.reader(file)


# Create a dictionary that will have courseID as the key and studentID as the value

students_per_course = {}

# Crate a dictionary that will have studentID as the key and courseID as the value

courses_per_student = {}

# Iterate through the lines in the file

for line in reader:
	student_ID = line[0]
	course_ID = line[1]
	
	# check to see if the course_ID is a key in the students_per_course dictionary
	if course_ID not in students_per_course:
		students_per_course[course_ID]= [];
		
	# check to see if the studentID is a key in the courses_per_student dictionary 
	
	if student_ID not in courses_per_student:
		courses_per_student[student_ID] = [];
	
	
	courses_per_student[student_ID].append(course_ID)
	students_per_course[course_ID].append(student_ID)

# List of class sizes
class_sizes = []



# Calculate the number of students per class and save each value per class to a list of class sizes
for course_ID in students_per_course:
	count = len(students_per_course[course_ID])
	class_sizes.append(count);


print("Mean of the class sizes: ", mean(class_sizes))
print("Median of the class sizes: ", median(class_sizes))
build_boxplot(class_sizes)
build_histogram(class_sizes)


# Find the number of relationships that each student has. Save it in a list

student_relationships = []

# Iterate through the students in the courses_per_student dictionary
for r_number in courses_per_student:
	
	# Create list that will save the relationships for this individual student
	
	individual_relationships = []
	
	for course in courses_per_student[r_number]:
	
		for student in students_per_course[course]:
		
		# check to see if the student is a new relationship 
		
			if student not in individual_relationships and student != r_number:
				
				individual_relationships.append(student)
			
	
	
	
	student_relationships.append(len(individual_relationships))
	

build_histogram(student_relationships)

print("Average number of unique student connections: ", mean(student_relationships))
print("Variance of unique student connections: " , variance(student_relationships))



	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	