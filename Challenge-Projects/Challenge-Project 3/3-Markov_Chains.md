# Challenge Project: Markov Chains

## Due December 11

## Description

These two problems will let you practice Markov Chain analysis of queueing systems with a couple of interesting models that are more complicated than the M/M/1 example we
did in class. Each problem asks you to set up a Markov chain model representing the number of customers in the system and then solve the balance equations to obtain a 
closed-form distribution for the number of customers in the system.


### M/M/1/*b*

The M/M/1/*b* queue is like an M/M/1 queue, but has limited capacity: it can hold only *b* customers (including the one in service). Any customers that arrive while *b* are
in the system will be **dropped** and are not allowed to enter the system.

Draw out a Markov chain for the M/M/1/*b* system, with states numbered 0 to *b*. The forward arcs will be labeled with *λ* and the backward arcs will be labeled with *μ*.

Set up and solve the global balance equations to find the queue length distribution for the M/M/1/*b* system.

Tip:

You'll need to deal with a geometric summation when it's time to solve for *π*<sub>0</sub>. You can look up the result that you need.

### M/M/*&infin;*

The M/M/*&infin;* model is an *infinite-server* queueing system: every customer that arrives gets to enter service immediately without ever needed to wait in a line. Its main application is modeling an exponential delay in a system, where customers pause before continuing. Any number of customers may be waiting at the same time.

Use Markov chain analysis to show that the distribution of the number of customers in the M/M/*Infinity* system is Poisson distributed:

<img src="poisson_dist.png" width="10%" />

Tips:

The arrival rate to the system is still *λ*, just like in the M/M/1 model. However, the service rate now scales with the number of customers:

- When there is only one customer in the system, the service rate is *μ*.
- When there are two, the service rate is *2μ*.
- When there are three, it's *3μ*.

and so forth.

Start by drawing out the Markov chain and labeling the arcs with the fixed arrival rate and variable service rates, then solve the global balance equations. 
Look out for the infinite series form of the exponential function, which will have a factorial term in the denominator..