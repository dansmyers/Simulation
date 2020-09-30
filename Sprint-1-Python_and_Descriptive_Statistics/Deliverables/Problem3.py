# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv

# Create an empty dictionary to record which students are in each course
students_per_course = {}

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

#Initialize empty list to hold class sizes then loop through course dictionary
#Class sizes are measured by the length of each list in the dictionary
data = []

for course_id in students_per_course:
    student_list = students_per_course[course_id]
    data.append(len(student_list))
 
#Finds the average and median class sizes
data.sort()
sum = 0
for i in data:
    sum += i
    
avg = sum / len(data)
print("The average class size is : " + str(avg))    


mid_high = data[int((len(data) / 2))]
mid_low = data[int((len(data) / 2) - 1)]
if (len(data) % 2 == 0):
    mid = (mid_high + mid_low)/ 2
    print("The median class size is : " + str(mid))
else:
    print("The median class size is : " + str(mid_high))


#Create Histogram and Boxplot
plt.figure()
plt.hist(data,20)
plt.title("Rollins College Class Sizes")
plt.xlabel("Class size")
plt.ylabel("Number of Classes")
plt.savefig("histogram.pdf", bbox_inches= "tight")

plt.figure()
plt.boxplot(data)
plt.title("Rollins College Class Sizes")
plt.ylabel("Class Size")
plt.savefig("boxplot.pdf", bbox_inches = "tight")
