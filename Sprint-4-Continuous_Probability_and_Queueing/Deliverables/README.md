Honor Code Statment "On my honor I have not given nor recieved not witnessed any unauthorized assistance on this work."

I have worked on this project with Jacob and Maria.

# Sprint 4 &ndash; Deliverables

## Yet More Lightbulbs

Lightbulbs are the urns of the exponential distribution.

I have two brand-new lightbulbs, each rated for an average lifetime of 2000 hours. What is the probability that both bulbs survive
for more than 3000 hours?

Assume that the bulbs are independent.

The answer is about .04978.

## The Non-Persistence of Memory

<img src="https://uploads5.wikiart.org/images/salvador-dali/the-disintegration-of-the-persistence-of-memory.jpg!Large.jpg" width="50%" />
                                                                                                                                  
*The Disintegration of the Persistence of Memory*, Salvador Dali    

Suppose I've got some of the same type lightbulbs as in the previous problem, but that these have already been in operation for a while. The first bulb has already run for 1000 hours and the second has already run for 2500 hours. What is the probability that both bulbs have a lifetime of more than 3000 hours?

Tip: use the memoryless property to reason about the future behavior of the exponential lifetime.

The answer is about .2231.

## Check My Math

I measured a system with one disk for a long period of time and collected the following data:

- Average service time for a disk access = 5 ms
- Average number of disk accesses per job = 2
- Average number of jobs in the system at any moment = 120
- Average residence time of a job in the system = 1 second

Did I make a mistake?

Tip: use Little's Law to derive the system throughput, then check the utilization at the disk using the Utilization Law.

Answer: Yes, I did. The number you're looking for is 1.2.


## Unbalanced Server Loads

There are two servers, A and B, in a system that receives arrivals at rate λ. Suppose that A receives 60% of
the arrivals and B receives 40%, and that A runs at a utilization of 80% and B at a utilization of 60%.

B can process one request in an average of 250 µs. Calculate the average service time at server A.

Tip: Start by calculating the throughput at server B using the Utilization Law.

The answer should be about 222 µs.


## The M/M/1 Queue

The M/M/1 queue is the classical, canonical queueing model. By itself, it isn't always the best model for real systems, but understanding it is the key to unlocking every other result in queueing theory.

The style of describing queues with letters and numbers is referred to as *Kendall's notation*. Each of the three items refers to a property of the system:

- The first letter describes the distribution of interarrival times. Here, *M* stands for *Markovian*, which Kendall used to mean that the time between arrivals is **exponentially distributed**.

- The second letter describes the distribution of service times. Again, the *M* means that service times in the queue are **exponentially distributed**.

- The *1* is the number of servers. The M/M/1 queue is a *single-server* queue.

Different queueing systems can be described using Kendall's notation:

- M/D/1 is a queue with exponential interarrival times, deterministic service times, and one server.

- M/M/*c* is a queue with exponential interarrival and service times and *c* servers. We'll talk about how to model multi-server systems later in the class.

Suppose you want to **simulate** the behavior of the M/M/1 queue. The basic strategy is to use four lists:

1. The list of customer arrival times, sorted in increasing order. The time between arrivals will be exponentially distrbuted with a parameter that we'll call `arrival_rate`.
2. A list of customer service times.
3. A list of the time each customer entered service.
4. A list of customer departure times.

A customer enters service immediately if the queue is empty at its arrival time. If the queue is not empty, it has to wait for the previous customer to depart. Therefore,

```
enter_service_time[i] = max(arrival_times[i], departure_times[i - 1])
```

If `arrival_times[i] > departure_times[i - 1]`, then customer `i - 1` must have departed before customer `i` arrives, so the queue is empty at the arrival instant.

Calculating the departure times is easy:

```
departure_times[i] = enter_service_times[i] + service_times[i]
```

The residence time is then the difference between departure and arrival.

```
residence_times[i] = departure_times[i] - arrival_times[i]
```

Practice this algorithm by filling in the table below, then calculate the average residence time.

```
arrival_time   service_time   enter_service_time   departure_time   residence_time
------------   ------------   ------------------   --------------   --------------
     1              3                 1                  4                3             
     3              2                 4                  6                3
     5              4
     7              1
     8              1            
    13              2                     
    14              1     
    17              3    
```


## Simulating M/M/1

Write a Python program that implements the single-server queue simulation algorithm. Use the pseudocode below as a starting point for your program. I've given you some `TODO` notes where you need to fill in code.

```
#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    #
    # Look at the inverse CDF examples

#--- Simulate the M/M/1 queue
#
# Inputs:
#    arrival_rate
#    avg_service_time
#    n: number of simulated customers
#
# Output: the average residence time of customer in the queue

def simulate(arrival_rate, avg_service_time, n):

    # Generate interarrival times
    # TODO: use rand_exp to generate n interarrival times with parameter arrival_rate
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    
    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        
        # TODO: calculate departure_times[i]
        
    # Calculate residence times
    # TODO: calculate list of residence times
    
    # TODO: return average residence time
```

Write a `main` method that calls `simulate` for increasing values of `arrival_rate`.

- Keep `avg_service_time = 1.0` in all trials.
- Let `n = 5000` for all trials.
- Let `arrival_rate = .05, .10, .15, ..., .95` and record the average residence times that result in each case.

From the Utilization Law,

```
utilization = arrival_rate * avg_service_time
```

Therefore, increasing the arrival rate while keeping the service time fixed has the effect of increasing the utilization.

**Make a plot (using matplotlib) with utilization on the x-axis and simulated average residence time on the y-axis**. You should see a graph that stays mostly flat up to about 75% utilization then rises steeply.

Your results should show that

```
      avg_service_time
R ~ --------------------
      1 - utilization
```

At 50% utilization, the residence time should be about 2.0; at 80% utilization, it should be about 5; and at 95% utilization it should be about 20.

We'll see how to derive this formula in a future sprint.


## Confidence Intervals

Modify your simulator to run multiple replications of your M/M/1 simulation and construct confidence intervals for the average residence time estimate. As in the previous problem, you'll test arrival rates from .05 to .95.

1. Run five replications for each utilization value. Let `n = 1000` for all trials.

2. Calculate the average of the five replications as your best estimate of the true mean residence time for that utilization level. Call this number `Y_bar`

3. Calculate the standard deviation of the five residence time estimates. Call this value `s`.

4. Calculate the upper and lower 95% confidence limits for your simulated estimates. For a t-distribution with four degrees of freedom, the critical value is 2.776 and the relevant formulas are:

```
UCL = Y_bar + 2.776 * s / sqrt(5)

LCL = Y_bar - 2.776 * s / sqrt(5)
```

5. Create one plot showing the average residence time estimates and the upper and lower confidence levels.
