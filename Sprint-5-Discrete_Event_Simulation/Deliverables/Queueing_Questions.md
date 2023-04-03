# Queueing Questions

Complete the following questions, which are all based on the theory we used in class to derive the residence time equation for M/M/1.

## M/M/1 Calculation Practice

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


## Power Management in Datacenters

There has been a large amount of recent research on reducing the economic and environmental impact caused
by the energy demands of modern datacenters. One of the most basic strategies for conserving energy is **dynamic voltage scaling** (DVS). By reducing the operating voltage of a processor, we can its reduce energy consumption in exchange for decreased performance.

Suppose we have a set of *k* servers, each operating as an M/M/1 queue capable of running at a maximum
rate *µ*. The total arrival rate to the entire set of servers is *λ*. Assume the service rate of each server scales
linearly with its power consumption (this is probably not realistic). Consider two basic operating strategies:

- Turn on all *k* servers, each running at a fraction 1 / *k* of its maximum power. In this scenario, the arrival rate at each queue is *λ* / *k* and the each queue’s service rate is *µ* / *k*.

- Turn on one server at full power. The server receives all arrivals at rate *λ* and has service rate *µ*.

Of these two strategies – multiple slow servers or one fast server – which one minimizes customer residence
time? By how much? Can you provide an intuitive explanation for this result?

Tip: Don't be intimidated by the fact that there are no numbers! Use the M/M/1 residence time equation and calculate the residence time for each scenario in terms of the given variables.

## M/D/1

The M/D/1 queue has Poisson arrivals and **deterministic** service times. Every customer receives the same service time of *s*, with no variability.

Derive the expected residence time in the M/D/1 queue given *s* and the arrival rate *λ*. How does M/D/1 compare to M/M/1?

Tip: Consider a customer that arrives at a random moment in time and finds the server occupied. On average, the new customer arrives **halfway** through the service period, so the expected residual life is *s* / 2.
