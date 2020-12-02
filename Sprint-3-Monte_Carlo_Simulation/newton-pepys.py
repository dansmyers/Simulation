from math import factorial
#binomial distribution
def binomial_distribution(n, x, p):
    # x = Number of times for a specific outcome within n trials
    # n = Number of trials
    q = 1 - p
    choose = factorial(n) / (factorial(x) * (factorial(n-x)))
    return choose * (p ** x) * (q ** (n - x))
    
print('Six fair dice are tossed independently and at least one appears:')
print('%.6f\n' % binomial_distribution(6, 1, 1/6))

print('Twelve fair dice are tossed independently and at least two sixes appear:')
print('%.6f\n' % binomial_distribution(12, 2, 1/6))

print('Eighteen fair dice are tossed independently and at least three sixes appear:')
print('%.6f\n' % binomial_distribution(18, 3, 1/6))

print("The first outcome has the highest probability, therefore is the most likely.")