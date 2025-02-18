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

Here's one of the simplest tests for randomness: Generate a large number of random values from the generator and group them into bins, like a histogram. The distribution should be uniform, with no bin having significantly more or less entries than any other. Here's some example code that generates a list of numbers and plots their histogram. Experiment with some different small parameter choices and see what you obtain. 

```
# Generate sequence
numbers = [lcg.next() for _ in range(1000)]

plt.figure()
plt.hist(numbers)
plt.savefig('test.png')    
```
