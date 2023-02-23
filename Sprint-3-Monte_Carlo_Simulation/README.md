# Sprint 3 &ndash; Jeu Monégasque

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Monaco_Monte_Carlo_1.jpg/2560px-Monaco_Monte_Carlo_1.jpg" width="100%" />

*Monte Carlo is a district of the small European principality of Monaco. It's the home of a famous casino and entertainment complex that has been in operation since the 1800s.*

## Starts Thursday, 2/23
## Deliverables and quiz are due on Wednesday 3/8

## Overview

After the last sprint, you should be starting to get comfortable with reasoning about probabilities and discrete random variables. In this sprint, we're going to build on these concepts by introducing two more important discrete distributions &ndash; the geometric and binomial &ndash; and applying all the concepts we've studied thus far to writing
simulation programs to estimate calculations that would be too complex to do by hand.

## Learning Outcomes

At the end of this sprint, you will be familiar with the following concepts.

1. The geometric, binomial, and Poisson distributions, their means, and their applications to modeling problems.

2. Random number generation using a linear congruential generator; the important of correctly parameterizing a random number generator.

3. Writing Monte Carlo simulation programs that use randomness as an alternative to complex calculations.

In some respects, this sprint has less material than the last one, but the problems will be more complex and time-consuming to complete.

## Deliverables

Complete the questions in the `Deliverables` directory.

Upload your code and solution files for the written problems into your repositoy (don't use a zip file) and send me a pull request for your submission.

## Topics

At the end of this sprint, you should be familiar with the following concepts and examples.

- The geometric distribution and its role in reasoning about sequences of true/false random events.

- Deriving the mean of the geometric distribution using a summation.

- The binomial distribution and its role in reasoning about "*k* successes out of *n* trials" problems.

- Deriving the mean of the binomial distribution.

- The Poisson distribution and its application to modeling the number of events in a period.

- Linear congruential random number generators, including the concepts of the seed and periods. Understand the challenges involved in 
corectly parameterizing a RNG and, therefore, the reasons why you should not try to write your own.

- Writing Python programs that use randomness to implement Monte Carlo simulations. These programs will mostly not require any new features, but will require
you to further develop your Python programming skills.

## Resources

### Discrete Distributions

Again, start with my notes on the `Notes` directory. Everything that's discussed there is a continuation of the topics of the last sprint, but the geometric and binomial
distributions are more complex. There are several examples in the notes: pay close attention to the worked ones and try the other ones for practice.

[This video](https://www.youtube.com/watch?v=8fqkQRjcR1M) discusses the derivation of the mean of the binomial distribution.

[This article](https://medium.com/@andrew.chamberlain/deriving-the-poisson-distribution-from-the-binomial-distribution-840cc1668239) provides additional information on 
deriving the Poisson distribution, starting from the binomial distribution.


### Random Number Generation

Take a look at my notes in the `Notes` directory, which will cover the basics of the linear congruential pseudorandom number generator.


### Monte Carlo Simulation

**Monte Carlo simulation** is a general term for any algorithm that uses randomness to estimate answers to complex deterministic calculations. Monte Carlo methods show up in physics, engineering, combinatorics, and other areas where interesting problems have answers that are too hard to calculate exactly.

The original idea for Monte Carlo simulation is credited to Stanislaw Ulam, a Polish scientist who came to America, worked on the Manhattan Project, and continued to be involved in nuclear research after World War II. While recuperating from an injury, he became interested in solitaire and decided to calculate the probability that an arbitrary game was winnable.

Despite his brilliance, the combinatorics of solitaire proved too challenging to work out exactly, so he hit up on the idea of using one of the very new computers to simply **simulate** a large number of solitaire games, keeping track of the percentage that could be won. Once Ulam explained his idea to his fellow scientists, it became clear that random sampling could be used to find answers to other complex calculations that were more directly related to nuclear research.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Casino_de_Monaco_%2850158785856%29.jpg/2880px-Casino_de_Monaco_%2850158785856%29.jpg" width="100%" />

*The Place du Casino.*


The `Notes` directory contains a file showing how to set up some example simulation programs. Use these as models for the homework problems.

Here is [an MIT lecture on Monte Carlo simulation](https://www.youtube.com/watch?v=OgO1gpXSUzU). The second half gets into some more complex material, but the first half is a good overview of the history and motivation for the method.

Finally, here's an example of using Monte Carlo simulation [to estimate pi](https://academo.org/demos/estimating-pi-monte-carlo/).

