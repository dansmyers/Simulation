# Final Project: Erlang's Formulas

## Due Monday, May 8 (the day that would have been our final exam)

## Overview

Agner Erlang was a Danish mathematician, statistician and engineer, who invented the fields of traffic engineering and queueing theory. He worked for the Copenhagen Telephone Company from 1908 to 1929 and developed methods to analyze the use of telephone circuits and operators. The Erlang distribution and the Erlang unit, used to measure load in telecom systems, are both named after him.

Consider a telephone system with the following characteristics:

- Customers arrive according to a Poisson process at rate *λ*. The length of each call is exponentially distributed with average *s*. These assumptions are the same as the M/M/1 queue and our other models.

- There are *c* identical servers available to process calls.

- There is *no* additional capacity for waiting customers. A newly arriving customer is either accepted by one of the *c* servers and processed immediately, or **dropped** because there is no additional capacity.

In modern queueing notation, this system is called the M/M/*c*/*c* queue: there are *c* servers and the system can have a maximum of *c* customers. In an old-style telephone system, the servers of the model corresponded to available switchboard lines that could carry incoming calls. If all lines were occupied, an incoming calls would be rejected.

A key quantity of interest in the M/M/*c*/*c* is the **blocking probability**, the probability that an arbitrary call is rejected because the system is full. Engineers would typically like to adjust the capacity of the system to keep the blocking probability below an acceptable threshold. In 1917, Erlang derived a formula for the blocking probability in the M/M/*c*/*c* queue, which is now know as the Erlang-B formula.

There are also Erlang-A and Erlang-C formulas. Erlang-C gives the estimated residence time for a customer in an M/M/*c* system with infinite capacity. Erlang-A is similar to M/M/*c*, but adds the idea of **abandoned calls**; customers may give up leave the system before receiving service if their patience is exhausted.

In this, the final project, you're going to write a simulation program that estimates blocking probabilities, compare it to the results predicted by the Erlang-B formula and the use your results to do a little capacity planning for an example telecom system.

## Erlang's-B formula

Start by doing a little bit of research on the Erlang-B formula. Here's one representation of the formula:

<img src="https://www.mbaskool.com/images/stories/business_concepts/erlang_b.png" width="12%" />

Here, *m* is the number of servers and *E* is the **offered load**, given by

*E* = *λs*

Notice that the formula for *E* has the same form as the utilization law. In a single server system, the offered load is equivalent to the utilization. However, in a multi-server system, which we're dealing with here, the load can be greater than 1, because it can now be shared across the *m* servers. The expected utilization of each individual server is

*U* = *λs* / *m*

Consider a system with an offered load of 10. How many servers are required to keep the blocking probability

- Under 10%?

- Under 1%?

- Under .1%?

Tip: write a method that implements the Erlang-B formula. Look up how to do factorials in Python. The denominator of the formula looks weird, but it has a finite number of terms so you can calculate it using a simple loop. Use a binary search to find the value of *m* that satisfies the constraint.

Note that choosing to call the number of servers *c* or *m* doesn't make any difference to the model, nor is one notation more traditional than the other. Personally, I think writing about the M/M/*m*/*m* queue [seems ridiculous](https://www.youtube.com/watch?v=eTeg1txDv8w), but others may have different opinions.

## Simulate

Now, let's write a simulator to predict blocking probabilities. 

Implement a Python program that predicts the blocking probability for an M/M/*c*/*c* system. The inputs to your model are:

- The constant arrival rate and average exponentially-distributed service time. Set the arrival rate to 10 and the average service time to 1.

- The number of servers.

Use the discrete-event simulation approach, keeping track of arrivals and departure events and the number of customers currently in the system. If an arrival comes, but the system is full, record it as a dropped arrival and don't add it to the system. The blocking probability is the fraction of total arrivals that are dropped.

Use your simulator to verify the results from the previous section. Show that your recommended number of servers results in blocking probabilities close to those predicted by the Erlang-B formula.

Tips:

- Use the M/M/1 discrete event sim model as a reference and think about how to adapt it.

- You'll need to generate exponentially distributed interarrival and service times.

- Run five trials for each number of servers and report the average blocking probability in each case.


## I heard you like Erlang

Modify your simulator to use service times drawn from the **two-stage Erlang distribution**. A two-stage Erlang variable is generated by adding two independent and identically distributed exponential random variables.

Keep the arrival rate set to 10 and generate each Erlang-distributed service time by adding two independent exponential random variables, each with mean .5.

How many servers are required to keep the blocking probability below 1% if the service times are Erlang distributed? How does that compare to the original case of exponentially distributed service times?
