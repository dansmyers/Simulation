# Sprint 4 &ndash; Continuous Probability and an Intro to Queueing Theory

<img src="https://imgs.xkcd.com/comics/academia_vs_business.png" width="75%" />


## Due 

## Overview

We've spent the first half of the course refining your command of probability and writing programs that use randomness. Now we're going to introduce the key concepts of
queueing theory, which we'll continue to study for the rest of the semester.

This unit has five topics:

1. Learning some words for things related to queues.
2. Little's Law, the most important formula in all of systems analysis. What *F = ma* is to physics, Little's Law is to waiting in lines.
3. The Poisson arrival process and the delicious PASTA property.
4. The properties of the M/M/1 queue, the canonical queueing model.
5. Tying all this together to write a queueing simulator program in Python.


## List of Topics

- Queueing system terminology: residence time, throughput, arrival rate, service rate, utilization
- The Utilization Law
- Little's Law
- Derivation of the residence time in the M/M/1 queue
- Interpreting the M/M/1 residence time equation
- Writing a queueing simulator

## Resources

### Queueing Terminology and Little's Law

Take a look at my notes in `Queueing.pdf`, which introduces the important terminology and the fundamental laws. The main challenge with this section is simply getting
used to the number of new terms involved and their relationships. We'll talk through several examples in class.

The other notes cover the Poisson process, PASTA, and M/M/1. These were written for an older course I taught at UW-Madison, so the format is different.

The Poisson process notes have some more technical results and derivations of its properties. You can read these, but don't stress about them.
