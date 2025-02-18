# Fun with the Linear Congruential Pseudorandom Number Generator

## Overview

This in-class activity has two parts:

1. Implementing a basic PRNG as a Python class
2. Experimenting with a few tests for randomness

## Class

Create a new file named `lcprng.py` on Codespaces.

Write a Python class that implements the basic linear congruential algorithm. Recall that the linear congruential generator chooses the next number in its random sequence using:
```
next = (a * current + c) % m 
```
where `a`, `c`, and `m` are the parameters of the model.

Here's some starting code:
```
"""
Linear congruential generator
"""

class LinearCongruentialGenerator:

    def __init__(self, seed=0):
        """
        Initialize the LCG with given parameters.
        
        Args:
            seed (int): Starting value for the sequence
            multiplier (int): Multiplier in the LCG formula
            increment (int): Increment in the LCG formula
            modulus (int): Modulus in the LCG formula
        """

        # The seed is the first number in the sequence
        self.current = seed

        # Fixed generator parameters
        self. a = 3
        self.c = 0
        self.m = 32


if __name__ == '__main__':
    lcg = LinearCongruentialGenerator(seed=1)

    # Generate sequence
    for _ in range(10):
        print(lcg.next())
```

Add the following methods to the generator:

- `next`: Generates the next value of `self.current` and returns it as the next number in the sequence
- `next_float`: Generates the next value of `self.current` and returns `self.currrent / self.m` as a float in [0, 1).
- `set_seed`: Takes a seed value as input and resets `self.current`

### Questions

- For the example code, what is the period of the generator?

- What happens if you set the seed to 0?

- Do some research and find examples of real-world generator parameters.

## A Couple of Tests

### Uniformity

Here's one of the simplest tests for randomness: Generate a large number of random values from the generator and group them into bins, like a histogram. The distribution should be uniform, with no bin having significantly more or less entries than any other.

You could think of this as the "balls in bins" model: throw a large number of balls into bins determined by the RNG output. If the output is good, every bin should have, on average, the same number of balls.  The formal test for this quality is the **Chi-Square test**, which is used to determine if the distributions in the bins are statistically different from what would be expected from a uniform distribution.


Here's some example code that generates a list of numbers and plots their histogram. Experiment with some different small parameter choices and see what you obtain. You'll need to import pyplot at the top of your script.
```
# Import at top of script
from matplotlib import pyplot as plt

# Generate sequence
numbers = [lcg.next() for _ in range(10000)]

plt.figure()
plt.hist(numbers, bins=lcg.m)
plt.savefig('test.png')    
```

### Bigger generators

Modify the problem to use values from a larger generator. Here are the parameters for one implementation called [MINSTD](https://en.wikipedia.org/wiki/Lehmer_random_number_generator#Parameters_in_common_use), used as a default in some systems including C++:
```
# MINSTD generator
self.a = 48271
self.c = 0
self.m = 2**31 - 1
```
Modify the histogram example to generate 1 million random values by calling the `next_float` method; they will all be in the range [0, 1). Histogram them into 100 bins.

Repeat with the parameters for the old-school RANDU generator used by 70s-era C:
```
# RANDU
self. a = 65539
self.c = 0
self.m = 2**31
```
Do you observe any obvious differences in the uniformity of the two implementations?

### Spectral test

The two generators appear to be similarly uniform (again, we haven't quantified this using a statistical test, but both would pass a basic test for uniformity).

It's still possible to observe some differences between the generators. The **spectral test** checks for correlations between consecutive generated values. If you have a series of random values:
```
[x_1, x_2, x_3, x_4, x_5, ...]
```
You can form points of consecutive values. For example, in three dimensions:
```
(x_1, x_2, x_3)
(x_2, x_3, x_4)
(x_3, x_4, x_5)
etc.
```
A basic property of the linear congruential generator is that, in high enough dimensions, these points will lie on a small number of distinct hyperplanes. The more separated the planes, the lower the quality of the generator.
 
Here's an example main section that constructs 3-D points from a sequence of random floats and then creates a 3-D scatter plot. Run it with the MINSTD and RANDU paramters. What differences do you observe?

```
if __name__ == '__main__':
    lcg = LinearCongruentialGenerator(seed=1)

    # Generate sequence
    numbers = [lcg.next_float() for _ in range(10000)]
    x = numbers[:len(numbers) - 2]
    y = numbers[1:len(numbers) - 1]
    z = numbers[2:len(numbers)]

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z)
    ax.view_init(elev=24, azim=-126)
    plt.savefig('test.png')    
  
```
