"""
Calculating letter frequencies from a large list of words

Illustrates opening and looping through a file and using
a dictionary to store a set of <key, value> pairs
"""

# Use the built-in open function to open a file
#
# 'r' indicates opening for reading
f = open('words.txt', 'r')

# Make a dictionary to keep track of the counts
# of each letter
#
# Dictionary stores a set of <key, value> pairs
# key = a letter
# value = number of occurrences of that letter in the word list
counts = {}

# The for loop can iterate through a file's lines
for line in f:
    line = line.strip()  # Remove whitespace
    
    # Loop through the letters in the current line
    for letter in line:
        if letter not in counts:
            counts[letter] = 0
        
        counts[letter] = counts[letter] + 1

# Print the results
# The for loop iterates over the keys in the dictionary
for letter in counts:
    print(letter, counts[letter])
