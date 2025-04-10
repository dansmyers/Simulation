# Overview of Discrete-Event Simulation

## Strategy

Many simulations incorporate an element of **time**. As time advances, **events** happen, and the simulation program models the effects of those events. For example, in an M/M/1 queueing model, we'd probably identify two basic kinds of events:

- Arrival events that put a new customer into the queue.
- Departure events that occur when a customer finishes service and departs the queue.

There are two basic ways of dealing with time in simulation programs:

- The **continuous-time-advance** approach. Maintain a variable in the program that represents the current time within the simulation. At each step of the simulation,
advance the time value by a small increment and process any events that happened during the small window of time represented by the increment.

- The **event-advance approach**. Maintain a list of **future events**, ordered by the time in the future when the events will occur. At each step, choose the next
future event, advance simulated time to the moment of the event, and then process the event.

We're going to focus on the **event-advance** strategy. The continuous-time approach can be useful when dealing with physical systems, like circuits or fluids,
that change constantly through time, but the event-based approach is better for the kinds of discrete events we're going to be modeling.

## Implementing the Event-Advance Algorithm

The event-advance simulation method is conceptually simple. Here is a pseudocode implementation:

```
Algorithm: Discrete-event simulation (event-advance strategy)

initialize future event list

insert initial events into the future_event_list

set time = 0

while future_event_list is not empty and time < max_simulation_time:

    # Get the next event in time order
    event e = future_event_list.pop()
    
    # Advance time
    time = e.time;
    
    Process event e
    
    If processing e creates any new future events, insert them into the future_event_list
```

The  **future event list** (FEL) contains all of the events that will occur at some future time. The beginning of the program sets up the FEL and populates it with any 
initial events that establish the state of the simulation at time 0.

On each iteration, retrieve the next future event from the FEL, then advance the simulated time to the time of that event. Run the program logic to deal with the event,
which will usually involve the creation of new future events.

Unfortunately, most of the difficulty in using the discrete-event approach lies in defining the set of possible events, determining how to represent them in the program,
and then writing the logic to process each event and create new events.




## Example: Queueing Simulator

You wrote a queueing simulator in the previous sprint, which used a list-based approach. Let's think about how to re-implement a single-server simulator using the 
discrete-event strategy. This will be less efficient, but more flexible, so it can be modified to account for alternate queueing strategies.

There are two kinds of events: arrival events and departure events. We'll choose to model each event as a Python tuple with the following elements:

- The kind of event, which will be either "arrival" or "departure"
- The time at which the event will take place.

The event processing logic contains two cases, one for each type of event. Our basic strategy is to generate each departure event at the moment a customer enters service.

- If a customer arrives and finds the queue empty, it should go into service right away and generate a new future departure event. If the queue is not empty, it should join the back of the queue.

- The next arrival time is generated each time we process an arrival event.

- Use a variable called `num_in_queue` to keep track of the number of customers currently in the system. Note that we don't need to actually model the customers as individual
entities or objects: they're all statistically identical, so maintaining a count is sufficient.

- On a departure, generate the next future departure for the next waiting customer, if one is present.

Here is the pseudocode version of the program. It's a little long, but take time to look through it carefully and understand how
arrivals and departures interact in the system.

```
initialize future_event_list
generate first arrival and put it in the event list

time = 0
num_in_queue = 0

initialize empty logging lists for arrival times, enter service times, and departure times

while future_event_list is not empty and time < max_simulation_time:

    # Get the next event in time order
    event e = future_event_list.pop()
    
    # Advance time
    time = e.time
    
    ### Process events
    
    # Arrival event
    if e.type == 'arrival':
    
        log arrival time
        
        num_in_queue += 1
    
        # If queue was empty, new arrival enters service immediately
        # Generate a new future departure event
        if num_in_queue = 1:
            log enter service time
        
            s = generate_service_time()
            event future_departure = new event("departure", time + s)
            future_event_list.insert(future_departure)
            
            
        # Generate the next arrival event
        a = generate_interarrival_time()
        event next_arrival = new event("arrival", time + a)
        future_event_list.insert(next_arrival)
    
    # Departure event
    elif e.type == 'departure':
    
        log departure time
        num_in_queue -= 1
        
        # If there is a waiting customer, put it into service
        # Generate a new future departure event
        if num_in_queue > 0:
        
            log enter service time
        
            s = generate_service_time()
            event future_departure = new event("departure", time + s)
            future_event_list.insert(future_departure)
```

## Priority Queues

Let's turn attention to some implementation details.

We need a data structure to keep track of the future event list. One option is to use a basic Python list and manually insert events so
that they stay in correct time-order. The easiest way to do this is to simply step through the list linearly until we find the correct place for each new event that needs to be inserted, then perform an insert at that position. That operation would be *O*(*n*) in the worst case, which is not bad, but we can do better.

A second option is to use a **heap**, a data structure that keeps track of a set of elements and makes it easy to get the smallest (in a min-heap) or largest (in a max-heap) item from the set.

- The heap supports two operations: `push` to add a new element to the heap, and `pop` to remove the current minimum element.

- Both `push` and `pop` run in *O*(log *n*) time.

- Heaps are based on binary trees, but a common implementation strategy is to pack the tree into a regular 1-D array and avoid the overhead of implementing it as a set of nodes and links.

Take a look at this article for an overview of heaps and their ordering rules:

https://medium.com/basecs/learning-to-love-heaps-cef2b273a238

Python has a library called `heapq` that defines `heappush` and `heappop` methods that can be applied to regular lists.

- `heappush` inserts a new item in the position required by the heap ordering rules.
- `heappop` removes the current minimum element and makes any required adjustments to keep the list arranged as a heap.

```
from heapq import heappush, heappop

# Start with an empty list
h = []

# heappush inserts a new item according to heap ordering rules
heappush(h, 10)
heappush(h, 1)
heappush(h, 100)
heappush(h, 50)
heappush(h, 2)

# heappop retrieves items in sorted order
print(heappop(h))  # Prints 1
print(heappop(h))  # Prints 2
print(heappop(h))  # Prints 10

# etc.
```

Take a look at `discrete_event_queue.py` for a more detailed example of how these methods work.

## Replication

Simulations are, of course, **random**. Therefore, when you run a simulation, there's always going to be **error** between the outputs
observed from the simulator and the real, true underlying parameter value that you're trying to estimate. It's fair to say that **minimizing random error** is a major component of simulation study and research.

There are three ways to handle random variation in simulation results:

1. Run your simulation for a long time. The more data you collect (for example, the more customers you observe at a queueing system), the more accurate measurements calculated from those simulated observations will become.

2. Run multiple independent simulations and average their individual estimates together. The result should be a combined estimate that 
is more accurate than any individual run.

3. Run multiple independent replications and average them, as in (2), but also calculate a **confidence interval** for the mean.

The `main` method of `discrete_event_queue.py` uses the second approach:

```
def main():
    
    """ Simulate for different utilization levels """
    
    for u in range(50, 100, 5):
        
        # Run 20 trials at each utilization level and use the average of the simulated
        # values as the estimate of the residence time
        
        sim_residence_times = []
        
        for trial in range(20):
            sim_residence_times.append(simulate(u / 100.0))
        
        sim_r_avg = sum(sim_residence_times) / len(sim_residence_times)
        
        print('%d\t%f' % (u, sim_r_avg))
```
