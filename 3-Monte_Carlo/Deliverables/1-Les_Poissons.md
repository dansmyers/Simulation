# *Les Poissons*! *Les Poissons*! How I Love *les Poissons*!

<img src="https://vignette.wikia.nocookie.net/disney/images/4/4d/Tlmpe834.jpg/revision/latest?cb=20101108233151" width="40%" />

## Expected value of the Poisson Distribution

Show that the expected value of a Poisson distribution with parameter *λ* is *λ*. Use the definition of the expected value. The summation will appear to be gnarly, with a factorial in the denominator, but you can simplify it.

For this problem, you can assume the period length *t* is fixed at 1. That is, events occur at rate *λ* per unit of time.

Tip: look up definitions of the exponential function, one of which is a gnarly looking summation with a factorial in the denominator. Use that result to simplify the expected value result.


## From binomial to Poisson

Recall that the derivation of the Poisson distribution is closely related to the binomial distribution when *n* is large and *p* is small. In this problem, you're going
to show the Poisson distribution is a good approximation for the binomial under these conditions.

- Write a Python function to simulate a binomial process with *n* = 1000 and *p* = .025. To do this, perform 1000 random coin flips where each flip comes up heads with probability .025. Record the number of heads that occur, which should be 25 on average.

- Repeat the above process 1000 times and plot the fraction of times each outcome occurs &ndash; for example, the fraction of binomial trials that resulted in 0 heads, the fraction of trials that results in exactly 1 head, and so forth. You should see a peak around the expected mean of 25 successes per trial.

- On the same plot, show the Poisson pmf with *λ* = 25. You should see that the two distributions are very similar.

I recommend using two line plots in two different styles for the two distributions.
