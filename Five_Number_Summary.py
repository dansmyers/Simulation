# Add code here to open the file
f = open('data.txt', 'r')

# Declare an empty list
values = []

for line in f:
    line = line.strip()  # Remove whitespace
    
    # Cast to a float and then append to the list
    values.append(float(line))
print(values)
    
# Now you calculate answers using the values list


def min(x):
    minimum = x[0]
    for i in x:
        if i < minimum:
            minimum = i
    return minimum
print('Minumum: ')
print(min(values))

def max(x):
    maximum = x[0]
    for i in x:
        if i > maximum:
            maximum = i
    return maximum
print('Maximum: ')
print(max(values))

def median(x):
    tempo = []
    for i in x:
        tempo.append(float(i))

    while len(tempo) > 1:
        tempo.remove(min(tempo))
        tempo.remove(max(tempo))
    
    return tempo[0]
print('Median: ')
print(median(values))

def mean(x):
    sum = 0.0
    num = 0.0
    for i in x:
        sum += i
        num += 1.0
    return sum/num
print('Mean: ')
print(mean(values))

def variance(x):
    avg = mean(values)
    temp = 0.0
    templist = []
    for i in x:
        temp = avg - i
        templist.append(float(temp ** 2))
    for i in templist:
        temp += i
    return temp / avg
print('Variance: ')
print(variance(values))

def standev(x):
    return variance(x) ** 0.5
print('Standard Deviation: ')
print(standev(values))
