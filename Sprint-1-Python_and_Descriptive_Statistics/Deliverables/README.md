# Sprint 1 &ndash; Deliverables

## Honor Code

Edit this section to include a statement of the Honor Code. i Promise not to cheat to much on purpose

## Team Members

List the other members of your team here.

## I Promise I'll Only Make You Do This One Time

Calculate, **by hand**, the five number summary and variance of the following data set:

```
3.5
9.1
9.5
8.3
8.2
8.7
4.4
6.7
2.5
4.4
6.7
```

Disclaimer: I may also ask you to do something like this on the quiz.

## More Calculations

Write a Python script to open the file `data.txt` and read through its values. Calculate and print the mean, median, variance, and standard deviation. Save (as PDFs) a box plot and a 20-bin histogram calculated from the values.

Tip: read the values into a list first. The easiest way to add an item to a list is with the `append` method:

```
# Add code here to open the file

# Declare an empty list
values = []

for line in f:
    line = line.strip()  # Remove whitespace
    
    # Cast to a float and then append to the list
    values.append(float(line))
    
    
# Now you calculate answers using the values list
```

Tip-tip: I recommend writing functions to calculate each one of the outputs. For example,

```
def mean(x):
    """
    Calculate and return the mean of input list x
    """
    
    return sum(x) / len(x)
```

## Campus Connections

How densely connected is the Rollins campus?

The file `enrollments.csv` contains course enrollment information from a previous semester that Dr. Yellen and I used for our course scheduling research project. Each line records one (anonymized) course enrollment for one student. For example, the beginning of the file has the lines

```
R460039483,703420369
R460039483,174689884
R460039483,677349699
R460039483,949748586
R680596214,454195846
R680596214,422498631
R680596214,80217700
R680596214,474708885
```

The first line indicates that the student with (anonymized) id number `R460039483` was enrolled in course `703420369` (again, this is an anonymized id number). The next lines report three more course enrollments for `R460039483`, followed by four courses for `R680596214`.

I've pre-filtered the course list to eliminate both unusually small classes (like independent studies and honors research) and large classes (like RCC peer mentor training or PE courses).

### Class Size

Use the data to find the mean and median class sizes. Create a box plot and a histogram to show the distribution of class sizes. Make sure to label the axes of your plots.

The basic challenge is mapping each course to a list of the students in contains. Here's a code excerpt that will help you do this, and also illustrates the use of the `csv`
module for working with structured text files.

```
# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv

# Create an empty dictionary to record which students are in each course
students_per_course = {}

# Open the file and create a csv reader
f = open('enrollments.csv', 'rU')
reader = csv.reader(f)

# Reader automatically iterates through the lines in the file
for line in reader:
    
    # csv reader automatically turns the line into a list of fields
    student_id = line[0]
    course_id = line[1]
    
    if course_id not in students_per_course:
        students_per_course = []
        
    students_per_course[course_id].append(student_id)
    
# Here's an example of how to iterate through the keys in a dictionary
# Print the students in each course
for course_id in students_per_course:
    student_list = students_per_course[course_id]
    print(course_id + ': ' + str(student_list)
```

Adapt this example to get the number of students in each course, then create the values and plots that you need.


### Interactions

Here's a second question: how many unique students does each Rollins student interact with in classes?

For example, suppose we have only two classes:

```
Underwater Basketweaving
------------------------
Daphne
Ernie
Fred
George
Harry

Early Pre-Modern Basketweaving: the Reed Period
-----------------------------------------------
Daphne
Ernie
Filius
Gilderoy
Harry
```

Daphne is in classes with six unique students: Ernie, Fred, George, Harry, Filius, and Gilderoy.

Determine the average and distribution of the number of unique connections that each student experiences through classes. Here is a general strategy:

1. Use the example above to read `enrollments.csv` and create dictionaries that record `students_per_course` and `courses_per_student`.

2. For each student, look up his or her list of courses, then iterate through the students in each course. This step requires using both dictionaries.

3. As you loop through the lists of students in each course, keep track of the number of unique student ids.

4. Record the number of unique students.

5. Keep repeating steps 2, 3, and 4 until you've determined the number of unique connections for every student in the data set.
