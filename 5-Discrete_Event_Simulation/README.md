# Sprint 5 &ndash; Discrete-Event Simulation

<img src="https://i.imgur.com/YXOi1NJ.png" width="50%" />

## Due Monday, 4/21

## Overview 

This unit will focus on completing a larger simulation modeling project. In doing so, we're going to introduce an important strategy for designing simulation programs:
the **discrete-event** approach.

A discrete-event simulation models the system under consideration as a sequence of **events** where the **timing** of the events is meaningful. Consider, for example, the model of the M/M/1 queue you built in the last sprint. The events for the queue were the sequences of arrivals and departures
that occurred over the life of the system. The relative timing of the arrivals and departures is important, as we've seen, because the statistical properties of the 
interarrival and service time distributions determine the properties of the queue. Therefore, any model of queueing system must include the timing of its events as an 
important element.

Note that this is a different problem that the ones we considered in the earlier unit on Monte Carlo simulation. In those problems, we might have modeled a sequence of events
(like die rolls or roulette spins) but we **did not** have to model any concept of the time between events.

In this unit, you're going to use the discrete-event strategy to build a **priority queueing** model inspired by Disney's FastPass+ system and then use it to answer some 
design questions. At the end of this project, you'll be familiar with

- The discrete-event time-advance strategy for building simulation programs
- Using heaps to implement priority queues as a useful data structure for storing an ordered sequence of events
- Priority queueing

## Resources

The `Notes` and 'Examples' directories contains documents describing the basics of the event-based time-advance simulation strategy and an example of using it to implement a queueing model. This will be a helpful starting point for you as you start working on the FastPass+ project. Look at the other notes in Project 4 if you need to review the PASTA property, M/M/1 or any of the other foundational queueing material.

For background on heaps, which the example program uses, I recommend this article: https://medium.com/basecs/learning-to-love-heaps-cef2b273a238.
