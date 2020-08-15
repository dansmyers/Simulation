"""
Convert a length in feet into units of Smoots

This is a docstring enclosed in triple quotes.

It's conventional for the beginning of the program and the
beginning of each function to have a descriptive docstring.
"""

# This is a regular comment.

# Read length in feet and convert it to a float type
#
# input() is the basic Python 3 input function.
#
# input() returns its result as a string type: float() converts to a
# real-valued number.
#
# The basic Python types are int, str, and float
# Python's float is equivalent to a Java double
length_in_feet = float(input('Enter a length in feet: '))

# Convert
#
# Python 3 division is always exact, even if both values are ints
length_in_smoots = length_in_feet / 5.5833

# Print to two decimal places
#
# Formatted printing is similar to C's printf
#
# %.2f prints the given variable as float with two decimal places
print('Length in Smoots: %.2f' % length_in_smoots)
