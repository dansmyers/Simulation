""" Set of loops that prints Mario-style stairs of arbitrary  height"""

height = float(input('Enter desired stair height: '))

for n in range(0, height):
    for s in range(0, height -  1):
        