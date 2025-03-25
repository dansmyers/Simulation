# Queuestions

## Overview

Answer the following analytical questions about the fundamental queueing laws and the M/M/1 queue. For each question, write or type your answer in a clean legible document. 

Tips:

- Review the notes. A lot of the challenge of this material is learning the new terms.
- Pay attention to the units in your calculations.
- There are only a few key quantities you can reason about: throughput/arrival rate, service times, residence times, and utilizations are the main ones. Think about what quantity would help you answer the question you need and then how to calculate it from what you are given. The Utilization Law and Little's Law are the main tools for relating parameters to each other.
- Utilization must be less than 1.0 for the system to be stable.

## Fundamental Law Questions

### Check My Math

I measured a system with one disk for a long period of time and collected the following data:

- Average service time for a disk access = 5 ms
- Average number of disk accesses per job = 2
- Average number of jobs in the system at any moment = 120
- Average residence time of a job in the system = 1 second

Did I make a mistake?

Tip: use Little's Law to derive the system throughput, calculate the disk throughput using the forced-flow law, then check the utilization at the disk using the Utilization Law.

Answer: Yes, I did. The number you're looking for is 1.2.


### Unbalanced Server Loads

There are two servers, A and B, in a system that receives arrivals at rate λ. Suppose that A receives 60% of the arrivals and B receives 40%, and that A runs at a utilization of 80% and B at a utilization of 60%.

B can process one request in an average of 250 µs. Calculate the average service time at server A.

Tip: Start by calculating the throughput at server B using the Utilization Law.

The answer should be about 222 µs.

## M/M/1 Questions


### M/M/1 Calculation Practice

Given an M/M/1 queue with *λ* = 10 arrivals per second and *s* = 75 ms, calculate the following quantities:

- The utilization, *U*
- The probability that an arriving customer finds the queue idle
- The average residence time, *R*
- The average waiting time, *W*
- The average number in the queue, *Q*
- The average number in the queue at an arrival instant
- The average number waiting and not being served
- The average number waiting and not being served at an arrival instant

Suppose we keep *λ* fixed at 10 arrivals per second. What value of *s* is required to achieve an average residence
time of .10 seconds?

What value of *s* is required to keep *Q* ≤ 2?

If *s* must stay fixed at 75 ms, what is the maximum arrival rate we can sustain while keeping *R* ≤ 1 second?


### Power Management in Datacenters

There has been a large amount of recent research on reducing the economic and environmental impact caused
by the energy demands of modern datacenters. One of the most basic strategies for conserving energy is **dynamic voltage scaling** (DVS). By reducing the operating voltage of a processor, we can its reduce energy consumption in exchange for decreased performance.

Suppose we have a set of *k* servers, each operating as an M/M/1 queue capable of running at a maximum
rate *µ*. The total arrival rate to the entire set of servers is *λ*. Assume the service rate of each server scales
linearly with its power consumption (this is probably not realistic). Consider two basic operating strategies:

- Turn on all *k* servers, each running at a fraction 1 / *k* of its maximum power. In this scenario, the arrival rate at each queue is *λ* / *k* and the each queue’s service rate is *µ* / *k*.

- Turn on one server at full power. The server receives all arrivals at rate *λ* and has service rate *µ*.

Of these two strategies – multiple slow servers or one fast server – which one minimizes customer residence time? By how much? Can you provide an intuitive explanation for this result?

Tip: Don't be intimidated by the fact that there are no numbers! Use the M/M/1 residence time equation and calculate the residence time for each scenario in terms of the given variables.


### M/D/1

The M/D/1 queue has Poisson arrivals and **deterministic** service times. Every customer receives the same service time of *s*, with no variability.

Derive the expected residence time in the M/D/1 queue given *s* and the arrival rate *λ*. How does M/D/1 compare to M/M/1?

Tip: Consider a customer that arrives at a random moment in time and finds the server occupied. On average, the new customer arrives **halfway** through the service period, so the expected residual life is *s* / 2.


