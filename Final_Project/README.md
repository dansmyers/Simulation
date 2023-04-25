# Final Project: Erlang's Formulas

## Overview

Agner Erlang was a Danish mathematician, statistician and engineer, who invented the fields of traffic engineering and queueing theory. He worked for the Copenhagen Telephone Company from 1908 to 1929 and developed methods to analyze the use of telephone circuits and operators. The Erlang distribution and the Erlang unit, used to measure load in telecom systems, are both named after him.

Consider a telephone system with the following characteristics:

- Customers arrive according to a Poisson process at rate *λ*. The length of each call is exponentially distributed with average *s*.

- There are *c* identical servers available to process calls.

- There is *no* additional capacity for waiting customers. A newly arriving customer is either accepted by one of the *c* servers and processed immediately, or **dropped** because there is no additional capacity.

In modern queueing notation, this system is called the M/M/*c*/*c* queue: there are *c* servers and the system can have a maximum of *c* customers. In an old-style telephone system, the servers of the model corresponded to available switchboard lines that could carry incoming calls. If all lines were occupied, an incoming calls would be rejected.

A key quantity of interest in the M/M/*c*/*c* is the **blocking probability**, the probability that an arbitrary call is rejected because the system is full. Engineers would typically like to adjust the capacity of the system to keep the blocking probability below an acceptable threshold. In 1917, Erlang derived a formula for the blocking probability in the M/M/*c*/*c* queue, which is now know as the Erlang-B formula.

(There are also Erlang-A and Erlang-C formulas. Erlang-C gives the estimated residence time for a customer in an M/M/*c* system with infinite capacity. Erlang-A is similar to M/M/*c*, but adds the idea of **abandoned calls**; customers may give up leave the system before receiving service if their patience is exhausted.

In this, the final project, you're going to write a simulation program that estimates blocking probabilities, compare it to the results predicted by the Erlang-B formula and the use your results to do a little capacity planning for an example telecom system.

## Erlang's-B formula

Start by doing a little bit of research on the Erlang-B formula. Here's one representation of the formula:

<img src="https://www.mbaskool.com/images/stories/business_concepts/erlang_b.png" width="25%" />

