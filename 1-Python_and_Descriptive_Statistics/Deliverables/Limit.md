# Take It to the Central Limit

<img src="https://www.thisisdig.com/wp-content/uploads/2023/11/the-eagles-812x609.jpg" width="300px" />

*We stan our long-haired 70s boomer country-soft rock overlords. The first song I learned to play on the guitar was "Take It Easy". [Article from Dig!](https://www.thisisdig.com/feature/take-it-to-the-limit-eagles-song-story/)*

## Overview

Recall that the Central Limit Theorem states that the distribution of the sample mean tends toward being normally distributed when the sample size is "sufficiently large". This rule is important because it applies regardless of the underlying distribution of the random variable, which **does not** have to be normally distributed or even particularly symmetric.

We're going to investigate this behavior emprically.

The exponential distribution is one of the best distributions. We'll use it extensively later in the semester for modeling random events in time. The exponential PDF has one parameter *λ* and is given by

*f*(*x*) = λ*e*<sup>-*λx*</sup> 

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Exponential_distribution_pdf_-_public_domain.svg/1920px-Exponential_distribution_pdf_-_public_domain.svg.png" width="300px" />

Observe that this distribution is not anywhere close to the same shape as the normal distribution.

## Question

Generate samples from the exponential distribution with *λ* = 1. Use increasing sample sizes of *n* = 3, 30, 300, 3000, 30000.

For each value of *n*, generate 1000 trials, each consisting of *n* random samples. Calculate the mean of each of the 1000 trials. Plot the histogram of the sample means and report the overall mean of the sample means (the "grand mean") and the standard deviation of the sample means.

You should see that the histograms become more and more normally distributed as *n* increases, the grand mean tends toward 1, and the standard deviation is approximately 1 / sqrt(*n*).

## Generating random variables

Here's one way of generating exponentially distributed random variates using `numpy`.

```
import numpy as np

# Generate n samples
n = 3

# Rate parameter
lambda_param = 1.0

# The numpy function uses the "scale", which is defined to be 1/lambda
samples = np.random.exponential(scale=1/lambda_param, size=n)
```
