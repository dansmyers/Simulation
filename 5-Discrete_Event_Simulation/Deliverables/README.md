# Simulating Disney's FastPass+ System

## Description

In this project, you'll use the *discrete-event simuation* strategy to model a version of Disney's FastPass+ virtual queueing system. Versions of FastPass were in use at the parks from 1999 until 2021, when they were discontinued and replaced by the current Lightning Lane system.

The FastPass system allowed park visitors to schedule a pre-set time to arrive at certain attractions. At their appointed time, FastPass holders entered a special shorter queue that takes them right to the front of the line, skipping almost all of the waiting time.

If you didn't have a FastPass, you waited in the long regular line, which might require multiple hours for popular attractions.

<img src="https://i.pinimg.com/originals/11/e1/a8/11e1a852b9a10faac95bad71c94613ac.jpg" width="50%"/>

*You're not getting your picture with Anna and Elsa unless you have a FastPass.*

From a modeling perspective, FastPass+ system is a kind of *priority queue*. There are two classes of customers:

1. FastPass holders, who have higher priority.
2. Regular non-FastPass-having plebians, who have to wait in the full queue.

Systems like FastPass+ are also called *virtual queues*, because they allow you to do your waiting virtually, while you're out in the park doing other things (and spending money), rather than by standing in line.

## Problem

The basic design challenge of a priority queueing system is deciding how many high-priority customers to admit during a block of time.

- The whole purpose of the system is to keep waiting times low for FastPass holders, so we don't want to allow a long queue of FastPass holders to build up. We should only allow as many FastPasses as we can accommodate while keeping waiting times for their holders acceptably low.

- FastPasses have higher priority, so regular customers waiting in the line keep getting interrupted by FastPass holders that get to move to the front of the line. If this happens too much, it makes waiting times in the regular queue unacceptably high and makes regular customers angry.

- At the same time, customers like the FastPass system and virtual queueing brings benefits by keeping customers in the park instead of in lines, so we should try to give out as many FastPasses as we can.

Therefore, we should seek to give out as many FastPasses as we can without degrading the quality of experience for either FastPass holders or regular waiters.

In this project, **you're going to build a simulator for a two-class priority queueing system**, which will represent the basic dynamics of FastPass+. The high-priority class will represent customers that have FastPasses and the low-priority class will be regular customers.

You'll then use your simulator to investigate how increasing the fraction of customers that have FastPasses impacts the quality of the waiting experience for both FastPass and regular customers. Your goal is to determine a good fraction that meets the needs of both groups.


## Model

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Cinderella_Castle_2013_Wade.jpg/1280px-Cinderella_Castle_2013_Wade.jpg" width="50%" />

Consider a ride that can be modeled as an **M/M/1 queue** with two classes of customers. This is fairly unrealistic assumption for a real theme park ride:

- Arrivals may be close to Poisson during some parts of the day, but are subject to bursts of arrivals around major events like opening, closing, parades, etc.
- Service times should be close to deterministic for a ride, not exponential
- Rides typically receive *bulk* arrivals as groups arrive together and serve customers in bulks

The basic M/M/1 discrete-event simulation model could be adapted to deal with all of these cases.

High-priority FastPass holders always get to go in front of low-priority non-FastPass customers, but have to wait to be served in first-come-first-served (FCFS) order. Therefore, a new FastPass holder that arrives at the ride will have to wait behind any other FastPass holders that are already in line, but no regular customers.

Regular customers have to wait behind three groups:

- Any other regular customers that are already in line.
- Any high-priority FastPass holders that are already in line.
- **Any new FastPass holders that arrive during the waiting period**.

Let's assume the following parameters are fixed and known:

- The average rate at which customers can board the ride is normalized to *μ* = 1 per minute. The average service time required to board the ride is therefore *s* = 1 minute.

- The ride runs at two utilization levels: 50% during periods of low activity and 95% during periods of high activity.

- Therefore, by the utilization law, the **total maximum arrival rate** of all customers to the ride must be normalized to *λ* = .50 riders per minute during periods of low activity and .95 riders per minute during periods of high activity.

- Customers can't be interrupted once they enter service, so a newly arriving FastPass customer can't kick a regular customer out of service.

- Service times and interarrival times are both exponentially distributed, as per the M/M/1 model.

## Design Question

What percentage of riders should we allocate as FastPasses? Does this fraction change for higher-load vs. lower-load periods?

Consider the periods of high activity, where  *λ* = .95 and *s* = 1.0.

- First, simulate the system with no FastPasses, so that all customers wait in one M/M/1 FCFS queue. You should get an average residence time of about 1 / (1 - .95) = 20 minutes.

- Now pick a fraction *f* of the .95 riders per minute to allocate as high-priority FastPass customers. Simulate the system again and record the resulting changes in the residence times for FastPass and regular customers.

- Repeat this experiment for values of *f* from 0 to .95. Use your data to choose and justify a good value of *f*.

Repeat the same experiment for the lower-load periods where *λ* = .50. Your initial residence time with no FastPasses should be about 2 minutes. Use simulation to determine a good operating level for *f*, the fraction of FastPasses. Is it the same as the high-load periods?

## Deliverable

<img src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Spaceship_Earth_2.jpg" width="50%" />

Turn in two graphs, one for the high-load periods and one for the low-load periods, showing the residence times for FastPass and regular customers as a function of *f*. Also submit your code and a **brief** write-up summarizing your results and explaining your choices for good operating values of *f* based on the data you've collected.
