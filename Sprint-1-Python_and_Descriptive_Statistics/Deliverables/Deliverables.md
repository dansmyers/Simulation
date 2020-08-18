# Sprint 1 &ndash; Deilverables

## Honor Code

Edit this section to include a statement of the Honor Code.

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
```
