# Final Exam Review

## Exam format

The exam will be 8-12 short answer questions, similar in format to the midterm.

## Topic list

- Fundamental queueing laws
- Using Little's Result to answer questions about system behavior
- Poisson process and the PASTA theorem
- The M/M/1 queue
- Deriving the residence time in M/M/1 using the tagged customer method
- Using the tagged customer method for variations: M/D/1, priority queues
- Discrete event simulation
- Solving discrete-time Markov chains using balance equations
- Ergodicity
- M/M/1 Markov chain
- Solving the M/M/1 CTMS using balance equations
- Markov chain variations: M/M/∞, M/M/c/c

## Specific things you should know

### Fundamental laws

- Forced flow law and Little's result
- Using Little's result to answer questions about systems

### Queueing theory
- Properties of the Poisson process
- Relationship between Poisson and exponential distributions
- State the PASTA property and use it to reason about properties of the queue at an arrival instant
- The concept of residual life
- Derivation of the M/M/1 residence time using the tagged customer method
- M/D/1 residence time derivation (from the homework)
- Implications of the M/M/1 residence time equation: Extra capacity is the price of low latencies
- Using the tagged customer equation for priority queues (you don't need to memorize these formulas, but understand the technique)

### Queueing networks

- Be able to calculate total residence time in a system with two queues in series
- Be able to calculate expected residence time for systems of parallel queues
- System of parallel queues with unbalanced split probabilities
- Comparing a parallel system to a single fast queue (question from the homework)

### Discrete-event simulation

- No questions on this topic
- No questions on heaps

### Markov chains

- The Markovian property
- Solving a DTMC using balance equations
- Requirements for ergodicity: irreducibility, aperiodicity, positive recurrence
- Be able to tell if a given chain satisfies those properties
- Given a chain and a starting state distribution, calculate the probabilities of being in each possible state at the next time step
- You **don't** need to do calculations with transition matrices, but there may be a question that asks you to relate the graph of a chain to its transition matrix.

### Markov chains and queues

- CTMCs use transition *rates*, not probabilities
- M/M/1 chain model
- Know the derivation of *π<sub>k</sub>* using the chain model
- Calculating other queue properties from *π<sub>k</sub>*
- Derivation that  *π<sub>k</sub>* is Poisson distributed in the M/M/∞ system
- Be able to write down chains for multiserver models: M/M/c/c, M/M/c

## Summary of Proofs and Derivations You Should Definitely Know

- Residence time in M/M/1 using tagged customer
- Residence time in M/D/1 using tagged customer
- Queue length probability in M/M/1 using Markov chain
- Other properties of M/M/1 derived from the Markov chain method
- Poisson distribution in M/M/{\infty}

