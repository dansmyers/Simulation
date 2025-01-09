# The Martingale

## Description

Throughout history, numerous frauds, hucksters, and morons have claimed to devise "unbeatable" betting systems that allow gamblers to somehow overcome the house edge that's built into every game of chance.

Let's get one thing straight: **there's no such thing as an "unbeatable" betting system**. In fact, all betting strategies will produce, in the long run, the exact same expected outcome, which is determined by the house edge and not by the ordering or size of individual bets.

<img src="https://cdn5.vectorstock.com/i/1000x1000/72/59/american-roulette-wheel-vector-13367259.jpg" width="25%" />

Consider roulette. A typical American roulette wheel has numbers 0 to 36, plus a special "double zero" spot. Half of the numbers 1 to 36 are colored black and the other half are colored red, with the 0 and 00 locations colored green.

The basic bet in roulette is a color bet: the player bets that that the ball will land in a red-colored spot (or a black one, the two bets are symmetric). The bet pays even money, so if you bet $10 and win, you get $10. There are 38 total pockets on the wheel, of which 18 are red, 18 are black, and two are green, so the odds of winning the red or black bet are 18/38 ~ .4736.

In the long run, if you wager a total of $X on red/black in roulette, you should expect to wind up with about .47X in the bank at the end of your adventures. It doesn't matter if you play all $X in one bet, dribble it out over $1 bets, or make bets of variable size using some system: in the end, the house edge rules all.

If betting systems can't affect your long-run winnings, are they of any interest? The answer is a qualified yes. No betting system can modify your expected overall winnings, but they can affect how your winnings are distributed over a series of play sessions.

Consider the following betting strategy, which is one of the best known. It's usually called **the Martingale**, a name that emerged in 18th Century France, probably as a reference to a region called Martigues. In the Martingale strategy, the gambler doubles the bet after every loss.

- On the first round, bet $1. If you win, keep betting $1 on the next round.

- If you lose the first round, double the bet to $2. If you win this round, you'll have recovered the $1 you lost from the first round, plus one more dollar of profit.

- If you lose the second round, double the bet again to $4. If you win this round, you will have recovered all previous losses ($1 + $2) plus one additional dollar.

- Continue the same strategy, always doubling the bet after every loss and resetting to $1 after every win.

Therefore, as long as you eventually win one round, the Martingale guarantees that you'll recover all previous losses and leave the table with at least a tiny profit. This sounds unbeatable, **and it would be if you had an infinite bankroll**. In reality, the exponential growth of the bets guarantees that you'll eventually hit a string of losses that will bankrupt you.

## Simulation

Suppose that a gambler is playing roulette, always betting on black and using the Martingale system. She begins with $255, enough to cover eight losses. She ends her gambling session when either:

- She's played 100 spins.

- The size of the bet required by the Martingale becomes too large to cover. In this case, she ends the game and takes her remaining bankroll home.

Write a simulation program to evaluate the Martingale strategy. **Use matplotlib to create a histogram of the outcomes of 1000 simulated sessions of the process described above**. Your results should show that most sessions result in a small net gain for the player, but that these are balanced by catastrophic losses where she goes near bankruptcy.

Tips:

- Try playing a few sessions before you begin coding. Make sure you understand the process before thinking about how to implement it.

- As before, use a `simulate` method that plays one complete session, then returns that amount remaining in the gambler's bankroll at the end. Collect all of your results into a list, then use matplotlib's `hist` function to create the plot.

Remember to update the bankroll after each win or loss. Wins become part of the total bankroll and can be used for future bets.
