"""
Project Euler problem #1: find the sum of all multiples of 3 or 5 below 10000

Demonstrates the for loop and the range function
"""

# Python's for loop is more flexible than Java's and can be used to iterate
# over all kinds of sequences, including lists, strings, and files.
#
# The basic counting for loop uses the built-in range function.
#
# range(n) generates the sequence of integers from 0 to n - 1
#
# range(a, b) generates the sequence from a to b - 1

total = 0

for i in range(1, 10000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
      
print(total)
