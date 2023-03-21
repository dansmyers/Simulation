# Sprint 4 &ndash; Continuous Probability and an Intro to Queueing Theory

<img src="https://imgs.xkcd.com/comics/academia_vs_business.png" width="75%" />


## Overview and Metaness

We've spent the last two weeks refining your command of discrete probability and writing programs that use randomness. Now we're going to introduce the key concepts of
queueing theory, which we'll continue to study for the rest of the semester.

This sprint has five parts:

1. Learning some words for things related to queues.
2. Learning Little's Law, the most important formula in all of systems analysis. What *F = ma* is to physics, Little's Law is to waiting in lines.
3. The exponential distribution and its special memoryless property.
4. Techniques for generating random numbers and variables of different distributions in simulation programs.
5. Tying all this together to write a queueing simulator program in Python.


## List of Topics

- Queueing system terminology: residence time, throughput, arrival rate, service rate, utilization
- The Utilization Law
- Little's Law
- A little bit about PDFs, CDFs, and CCDFs
- The exponential distribution
- The memoryless property of the exponential
- Generating random variates using the inverse CDF method
- Writing a queueing simulator

## Resources

### Queueing Terminology and Little's Law

Take a look at my notes in `Queueing.pdf`, which introduces the important terminology and the fundamental laws. The main challenge with this section is simply getting
used to the number of new terms involved and their relationships. We'll talk through several examples in class.

### Continuous Probability and the Exponential Distribution

Start with my notes and these two videos:

- https://www.youtube.com/watch?v=IT-0oCOQrBY

- https://www.youtube.com/watch?v=bKkLYSi5XNE

The second video goes into some detail about the relationship between the exponential and Poisson distribution.

Key ideas:

- The concept of the CDF and CCDF. You don't need to do any calculus, but be able to state that the CDF is P(X <= x).
- The CDF and CCDF of the exponential distribution and using them to answer questions about lifetimes and the time between events.
- The memoryless property. This is probably the trickiest topic in this unit. Please read through the examples carefully, scan through the proof, then come back to the proof again after working through the example problems.

### Random Number Generation

We've already talked about the linear congruential generator. Now that we've introduced the exponential, we're ready to talk about generating random variates. We're going 
to focus on one technique, called the **inverse CDF method**. If you understand it, you can learn about other techniques you might come across in the future.

Start with my notes and then take a look at the first few slides of this presentation by Raj Jain at Washington-St. Louis:

https://www.cse.wustl.edu/~jain/cse567-08/ftp/k_28rvg.pdf

This video has another presentation of the inverse CDF idea:

https://www.youtube.com/watch?v=rnBbYsysPaU

