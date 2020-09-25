"""
	This program finds how densely the Rollins community is connected.
"""
# import matplotlib to create the box plot and histogram
import matplotlib

#import the csv library to get a csv reader
import csv

# tell matplotlib we are using a virtual environment for our code
matplotlib.use("Agg")

# import pyplot as plt to use later in the histogram and box plot functions
from matplotlib import pyplot as plt


# function to caluclate the mean of a data set
def calculate_mean(values):
	num_values = len(values)
	value_sum = 0
	
	for number in values:
		value_sum += number
	
	mean = value_sum / num_values
	
	return mean
	
# function to calculate the median of a data set
def calculate_median(values):
	values = sorted(values)
	list_length = len(values)
	
	if len(values) % 2 == 0:
		
		middleElem1 = values[int(list_length / 2) - 1]
		middleElem2 = values[int(list_length / 2)]
		
		average = (middleElem1 + middleElem2) / 2 
		
		return average
		
	else:
		median = values[int(list_length / 2)]
		
		return median 

# function to caluclate the histogram of data 
def histogram_of_data(values):
	plt.figure()
	
	plt.hist(values, 20)
	
	plt.title("Rollins Class Sizes")
	plt.xlabel("Class Size")
	plt.ylabel("Count")
	
	plt.savefig("class_sizes_histogram.pdf", bbox_inches = "tight")
	
# function to caluclate a box plot of data
def box_plot_of_data(values):
	plt.figure()
	
	plt.boxplot(values)
	
	plt.title("Rollins Class Sizes")
	plt.xlabel("Class Size")
	plt.ylabel("Count")
	
	
	plt.savefig("class_sizes_box_plot.pdf", bbox_inches = "tight")

# open the file and save it into enrollments
enrollments = open("enrollments.csv", "r")

#create a csv reader and use it to read the information from the csv file
enrollment_reader = csv.reader(enrollments)

# dictionary mapping a student to a course 
courses_per_student = {} 

# dictionary mapping a course to a student 
students_per_course = {}

for x in enrollment_reader:
	student_id = x[0]
	course_id = x[1]
	
	if student_id not in courses_per_student:
		courses_per_student[student_id] = []
		
	if course_id not in students_per_course:
		students_per_course[course_id] = []
		
	courses_per_student[student_id].append(course_id)
	
	students_per_course[course_id].append(student_id)
	
# caluclate the total number of students in each course and save it to a list

# array holding the number of students in each course
class_sizes = []

for courses in students_per_course:
	
	class_sizes.append(len(students_per_course[courses]))

print("Mean of the class sizes is: ", calculate_mean(class_sizes))
print("Median of the class sizes is: ", calculate_median(class_sizes))


# keep track of unique student id's for the student
unique_students = []

# number of unique student unique_student_interactions
num_unique_students = [] 

for students in courses_per_student:
	courses = courses_per_student[students]
	unique_students.append(students)
	
	for course in courses:
		student = students_per_course[course]
		
		for y in student:
			if y not in unique_students:
				unique_students.append(y)
				
	num_unique_students.append(len(unique_students))
	unique_students.clear()
		
print("Average unique student connections: ", calculate_mean(num_unique_students))





	



















































































