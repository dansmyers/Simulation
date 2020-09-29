"""
Fritz Stapfer Paz
Campus Connections - Interactions
09/30/2020


How many unique students does each Rollins student interact with in classes?
Determine the average and distribution of the number of unique connections 
    that each student experiences through classes.
"""

"""
Importing
"""
from math import sqrt               # Import Square Root for Standard Deviation Calculation
import csv                          # Used to read/parse csv
import matplotlib                   # Required setup for matplotlib
matplotlib.use('Agg')               # <-- Required on Mimir
from matplotlib import pyplot as plt


"""
Declare dictionaries
"""
courses_per_student = {}            # Create a dictionary to store the cids for each student
students_per_course = {}            # Second dictionary to store the students in each course


"""
Opening the file and populating dictionaries
"""
f = open('enrollments.csv', 'r')    # Open the enrollments.csv file


reader = csv.reader(f)              # Create a csv reader to process the file


for line in reader:                 # Use the for loop to step through all lines in the file
    r_number = line[0]
    cid = line[1]
    
    if r_number not in courses_per_student:     # If this is the first time we've seen the student r-number,
        courses_per_student[r_number] = []      # make an entry for it in the dictionary
    courses_per_student[r_number].append(cid)   # Append the cid to the student's list of courses

    if cid not in students_per_course:          # If this is the first time we've seen the student r-number,
        students_per_course[cid] = []           # make an entry for it in the dictionary
    students_per_course[cid].append(r_number)   # Append the r_number to the course's list of student


"""
Check for Connections
"""
connections = {}                                        # Create a dictionary to store the connections
for student in courses_per_student:                     # Iterate through every student
    connections[student] = []                           # and create a entry in connections for every student
    
    for course in courses_per_student[student]:         # Iterate through every course per student
        for peer in students_per_course[course]:        # Then get every student in that course
            if(peer not in connections[student] and peer != student):   # Check for unique connections
                connections[student].append(peer)       # Append peer to connections dictionary


"""
Create an array with the number of unique connections from connections dictionary
"""
number_of_connections = [len(connections[student]) for student in connections]


"""
Calculation helper functions
"""
def mean(x):                        # Calculate and return the mean of input list x
    return sum(x) / len(x)          # Return Mean (Sum / Length)

def median(x):                      # Calculate and return the median of input list x
    x.sort();                       # Sort x
    if(len(x) % 2 == 0):            # If x has even length, average both middle elements
        e_1 = x[int(len(x) / 2)]    # First Middle Element
        e_2 = x[int(len(x)/2 -1)]   # Second Middle Element
        e_sum = e_1 + e_2           # Add middle two elements
        return (e_sum / 2)          #Return Average of the Middle Elementss
    else:
        e = x[ int(len(x)/2)]       # Middle Element
        return (e)                  # Return Middle Element

def variance(x):                    # Calculate and return the variance of input list x
    m = mean(x)                     # Take the Mean
    sq = [(i-m)**2 for i in x]      # Uses list comprehension to get distance from mean
    
    return(sum(sq) / len(sq))       # Return Variance
    
def standard_deviation(x):          # Calculate and return the standard deviation of input list x
    return (sqrt(variance(x)))      # Return Standard Deviation (Square Root of Variance)


"""
Print Average, Mean, Median, Variance, and Standard Deviation of Unique Connections
"""
average = (sum(number_of_connections) / len(number_of_connections))
unique_mean = mean(number_of_connections)
unique_median = median(number_of_connections)
unique_variance = variance(number_of_connections)
unique_standard_deviation = standard_deviation(number_of_connections)

print(f'Average: {average}')
print(f'Mean: {unique_mean}')
print(f'Median: {unique_median}')
print(f'Variance: {unique_variance}')
print(f'Standard Deviation: {unique_standard_deviation}')


"""
Calculate and return the variance of input list x
""" 
def variance(x):
    m = mean(x)                     # Take the Mean
    sq = [(i-m)**2 for i in x]      # Uses list comprehension to get distance from mean
    
    return(sum(sq) / len(sq))       # Return Variance
    
"""
Calculate and return the standard deviation of input list x
""" 
def standard_deviation(x):
    return (sqrt(variance(x)))      # Return Standard Deviation (Square Root of Variance)


"""
Show distribution using MatPlotLib
"""
plt.hist(number_of_connections,50)
plt.title("Interactions")
plt.xlabel("Number of Interactions")
plt.ylabel("Count")

plt.savefig("interactions_distribution.pdf",bbox_inches="tight")