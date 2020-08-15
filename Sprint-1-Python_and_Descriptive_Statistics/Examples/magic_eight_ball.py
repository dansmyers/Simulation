"""
Magic Eight Ball: a fortune telling program

Demonstrates conditionals, random choices, and import statements
"""

# The import statement is the same as in Java: load an external module
#
# You can also use the from...import... form if you want to load only
# one function from a module
from math import random

# Read a question from the user
# This is just for flavor: it has no effect on the output
print('I AM THE MAGIC EIGHT BALL!")
question = input('Tell me your question: ')

# Generate a random number in [0, 1)
r = random()

# Use the value of r to select an output message
#
# Note: Python allows chained conditionals of the form a < b < c, but many other languages don't
if r <= .25:
    print('My sources say no.')
elif .25 < r <= .50
    print('It is decidedly so.')
elif .50 < r <= .75
    print('Concentrate and ask again.')
else:
    print('Signs point to yes.')
