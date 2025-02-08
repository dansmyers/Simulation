# Hermione Granger and the Distributions of Probability

## Disclaimer

This problem set is a work of fan fiction that I wrote when I read the entire *Harry Potter* series out loud to my kids twice during the COVID pandemic.

<img src="https://64.media.tumblr.com/d85b44001002bb249c42b27e00d8dccb/tumblr_nzrkzfmjZW1s5b5tzo1_500.jpg" width="40%" />


## Instructions

Answer the following questions, which cover discrete probability distributions, expected values, and conditional probabilities.

Type your answers in a document or upload a **clean and legible** handwritten file.

## Questions

### Wizard People, Dear Reader?

<img src="https://64.media.tumblr.com/99413ebb9f4e29d268974d90d81da509/tumblr_ne9qzeTT7T1s5b5tzo1_500.jpg" width="40%"/>

Hermione Granger is pretty sure she’s a witch, because she read in a book that having very curly hair is a sign of latent mystical power. Also, one time an owl landed on her head. However, she didn’t receive a letter from Hogwarts on her 11th birthday.

After reading several books and pamphlets, Hermione is pretty sure that
```
P(She's a witch) = .75
P(Not receiving a letter | She's a witch) = .03  (because owls are actually pretty dumb)
P(Not receiving a letter | She's not a witch) = .99   
```

Under these assumptions, what is the probability that Hermione really is a witch even though she didn’t get a letter?

Tip: use Bayes' Rule,

```
             P(A) * P(B | A)
P(A | B) =  -----------------
                  P(B)

where

A = She's a witch
B = Not receiving a letter

P(B) is therefore the total probability of not receiving a letter.
``` 

### Chocolate Frogs

Good news! Hermione got into Hogwarts after all! Now she's taking her first trip to school on the magical Hogwarts Express. The snack trolley has all kinds of amazing wizard treats, including the ever-popular Chocolate Frogs. Every Chocolate Frog comes with a collectable Famous Witch or Wizard card.

Suppose that there are 30 total Famous Witch or Wizard cards in the set. Every frog is equally likely to contain any one of the cards.

What is the expected number of Chocolate Frogs Hermione would need to open to collect every Famous Witch and Wizard?

Hints:

- If Hermione buys her first frog on the Express, she's guaranteed to get a card she's never seen before.
- After that, there are 29 out of 30 unseen cards remaining. Opening cards until she finds one of them is a geometric random variable with probability of success 29/30. The expected value of this variable is the number of cards she needs to open, on average, to find her next unseen card.
- Finding the next card is again a geometric process with a success probability of 28/30, and so forth.

This problem is based on a classic called the Coupon Collector's Problem.

Tip: Write a small program to do the calculation.

### Hat Problem

Students arriving at Hogwarts are sorted into one of the four residential houses -- Gryffindor, Hufflepuff, Ravenclaw, and Slytherin -- by the magical Sorting Hat.

In theory, the Hat is supposed to examine each student's personality, consider his or her wishes, and then place the student into the most appropriate house. However, after a thousand years, the Hat has gotten pretty lazy, so it has simplified its sorting process into a two-step algorithm:

1. All evil students go into Slytherin, obviously.
2. Everybody else is just randomly sorted into one of the four houses, with a 40% probability of being put into Hufflepuff and a 20% probability of being put into each of the three other houses.

Hermione is shocked when she's sorted into Slytherin! She's never thought of herself as evil, but now that she considers it, becoming the future Dark Lady of Magical Britain does have some appeal...

If 10% of new Hogwarts students are evil, what is the probability that a randomly chosen Slytherin is evil?

Tip: the value you want is `P(Evil | Slytherin)`.


### Magical Urn

Hogwarts is filled with all kinds of wonderous magical objects: talking portraits, deadly moving stairs, secret passages, and the largest collection of magical urns in Western Europe.

There's an urn on the fourth floor with a strange property: every time Hermione takes a ball out, the urn randomly chooses and discards another ball!

Suppose the urn contains 10 black balls and 5 red balls. If Hermione draws two balls, what is the probability that the second ball is red? What's the probability that the third draw is red?

Tip: Draw a tree showing the sequence of changes that can occur. When Hermione takes the first ball, it could be red or black, the urn then chooses another ball at random to discard, so there are four possible states the urn can be in after the first draw. You can calculate the probability of reaching each of those states, then continue to reason about the second and third possible draws.


### Pólya's Urn

Suppose an urn contains 9 black balls and 6 red balls. On each trial, Hermione picks a ball at random from the urn, returns it to the urn, and adds in one more ball of the same color.

Suppose she carries out this procedure two times. What are the expected numbers of red and black balls in the urn?

Tip: Again, draw a tree of possible outcomes.


### Birthday Attack

<img src="https://64.media.tumblr.com/3ee467fbfc590a59e079ddfe7f93d34d/tumblr_psp65oRMS91s5b5tzo1_500.jpg" width="40%" />

There are a total of 40 students in Hermoine's year at Hogwarts. What's the probability that no two students in Hermoine's year share the same birthday? Write a small program to do the calculation.

Assume that there are 365 possible birthdays (wizards can't be born on Leap Days) and that wizards are equally likely to be born on any day of the year.

Tip: Suppose there are only two students: Hermione and her best friend Harriet Potter, the Girl-Who-Lived.
```
P(Both are born on two different days) = (365 / 365) * (364 / 365)
```
Hermoine's birthday can be on any day, but Harriet's must occur randomly on one of the other 364 days.

What if there are three students? How about more?


## Binomial Problems

Use the binomial distribution to answer the following questions.

### The Newton-Pepys Problem

<img src="https://cdn.aarp.net/content/dam/aarp/food/healthy-eating/2016/2016-05/1140-peeps-nation.imgcache.rev3aa6a5a0b7d521bbef63f0e833d97a8f.web.900.513.jpg" width="300px" />

Samuel Pepys (pronounced "Peeps") was a 17th Century British naval administrator, best known for the detailed diary he kept describing his life in the 1660's. In 1693 he corresponded with Isaac Newton regarding a wager:

>Which of the following three propositions has the greatest chance of success?
>
>- Six fair dice are tossed independently and at least one six appears.
>- Twelve fair dice are tossed independently and at least two sixes appear.
>- Eighteen fair dice are tossed independently and at least three sixes appear.

What is the answer to Pepys' question? Calculate your answer exactly using a discrete probability distribution, not a simulation model.

Tip: notice that the problem is phrased as *at least* **not** *exactly*.


### Dragon Dice

Hermione has settled into a nice routine with her fellow Slytherins. During the day, she eats meals in the Great Hall, reads about famous Dark Wizards in the library, and attends her classes. During the evening she does her homework and plays wizard games with her friend Daphne Greengrass.

One of their games is called Dragon's Dice. It's a simple carnival game, also known as Chuck-a-Luck.

Hermione picks a number 1-6 and rolls three fair dice. If her number comes up *k* = 1, 2, or 3 times, she wins *k* wizard dollars. If it does not appear on any of the dice, she loses one wizard dollar.

What is Hermione's expected outcome from playing Dragon's Dice? Solve this problem analytically.


### Reliability problem (Sheldon Ross)

Consider a system with five independent components, each of which operates correctly with probability *p*. A second system has three independent components, each of which also operates correctly with probability *p*.

Each system can only function if at least half of its components function correctly on a given day. For what values of *p* is the
three component system more likely to function correctly than the five component system?
