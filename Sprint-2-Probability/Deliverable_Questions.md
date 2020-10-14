# Hermione Granger and the Distributions of Probability

## Disclaimer

This problem set is a work of fan fiction. Hermione Granger and related characters were created by J.K. Rowling. Please don't sue me.

<img src="https://64.media.tumblr.com/d85b44001002bb249c42b27e00d8dccb/tumblr_nzrkzfmjZW1s5b5tzo1_500.jpg" width="40%" />

## Honor Code

“On my honor, I have not given, nor received, nor witnessed any unauthorized assistance on this work."

## List Your Team Members

Randy, Christian, Ryan, Matthew

## Instructions

Answer the following questions, which cover discrete probability distributions, expected values, and conditional probabilities.

You can type your answers in this document or upload a scanned handwritten file.

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

```
P(A) = .75         P(B|A) = .03       P(B|!A) = .99
P(!A) = 1 - .75 = .25

Using notes from class:
P(B) = P(B|A)P(A) + P(B|!A)P(!A)
     = .03 * .75  + .99 * .25
     = .0225 + .2475 = .27

Using Bayes' Rule,
P(A|B) = (.75 * .03) / .27
       = .0225 / .27 
       = .08333333
       = 8.3%
```

### Chocolate Frogs

Good news! Hermione got into Hogwarts after all!

Now she's taking her first trip to school on the magical Hogwarts Express. The snack trolley has all kinds of amazing wizard treats, including the ever-popular Chocolate Frogs. Every Chocolate Frog comes with a collectable Famous Witch or Wizard card.

Suppose that there are 30 total Famous Witch or Wizard cards in the set. Every frog is equally likely to contain any one of the cards.

What is the expected number of Chocolate Frogs Hermione would need to open to collect every Famous Witch and Wizard?

Hints:

- If Hermione buys her first frog on the Express, she's guaranteed to get a card she's never seen before.

- After that, there are 29 out of 30 unseen cards remaining. The expected number of frogs she needs to open to find one of the 29 unseen cards is 30 / 29 ~ 1.0344.

- After she has two cards, she'd expect to open 30 / 28 ~ 1.0714 cards to find a third unique card.

This problem is based on a classic called the Coupon Collector's Problem. It's related to the geometric distribution, which we'll talk about in the next sprint.

```
k = 30
Yi = number of Chocolate frogs to collect all cards
Xi = Yi+1 + Yi
Yk = Sum i = 0 to k-1 Xi
E[Xi] = k * (1/(k-i))
E[Yk] = E[Sum i = 0 to k-1 (Xi)]
      = Sum i = 0 to k-1 (E[Xi])
      
      pull the k out of the Summation
      = k Sum i = 0 to k-1 (1/(k-i))
      
      rewrite it to make it more readable
      = k Sum i = 1 to k (1/i)
      
      Sum i = 1 to k (1/i) is equal to ln k
      
      so the answer becomes
      = k ln k
```

### Hat Problem

Hermione made it to Hogwarts!

Students arriving at Hogwarts are sorted into one of the four residential houses -- Gryffindor, Hufflepuff, Ravenclaw, and Slytherin -- by the magical Sorting Hat.

In theory, the Hat is supposed to examine each student's personality, consider his or her wishes, and then place the student into the most appropriate house. However, after a thousand years, the Hat has gotten pretty lazy, so it has simplified its sorting process into a two-step algorithm:

1. All evil students go into Slytherin, obviously.

2. Everybody else is just randomly sorted into one of the four houses, with a 40% probability of being put into Hufflepuff and a 20% probability of being put into each of the three other houses.

Hermione is shocked when she's sorted into Slytherin! She's never thought of herself as evil, but now that she considers it, becoming the future Dark Lady of Magical Britain does have some appeal...

If 10% of new Hogwarts students are evil, what is the probability that a randomly chosen Slytherin is evil?

Tip: the value you want is `P(Evil | Slytherin)`.

```
P(A) = .1    P(B|A) = 1    P(B) = 1 - .1 (subtract the guys auto put in slyth) 
                                = .9 * .2 (using the 2nd step)
                                = .18 + .1 (add back in the people auto put in slyth)
                                = .28

Using Bayes' Rule:
P(A|B) = (1 * .1) / .28
       = .1 / .28
       = .357 
       about 35.7%
```

### Dumblevator

<img src="https://64.media.tumblr.com/908ee88323640428f9cbda47df177a38/tumblr_nke6rsvC3C1s5b5tzo1_500.jpg" width="40%"/>

Hogwarts is so magical that the stairs constantly rearrange themselves.  This has gotten annoying, so Headmaster Dumbledore finally magicked up an elevator to reliably transport 
students between floors and reduce, but not eliminate, the peril of leaving your room to attend classes and meals.

The school has fifteen floors. The Dumblevator continually moves between the first floor and the fifteenth floor in the order 1, 2, 3 ... 13, 14, 15, 14, 13 
... 3, 2, 1, and so forth. Any time spent stopped at a floor is negligible compared to the time moving between floors.

Hermione's last class ends at 5 PM on the thirteenth floor and she wants to go down to the first floor to reach the Great Hall for dinner. What is the probability that the Dumblevator is moving **down** when it arrives at the thirteenth floor for the first time after Hermione leaves her class?

Tips:

- This problem is based on one by Don Knuth, author of *The Art of Computer Programming*, which is famous for being one of the first comprehensive computer science texts and having a number of creative problems.

- If Hermione boards a down-moving elevator at the 13th floor, where must it have been when she arrived to wait?

- Try reasoning about a smaller number of floors and drawing a picture.
- 
```
Was confused by this by what you were mentioning in class.  "when it arrives at the thirteenth floor for the first time after Hermione leaves her class?"  Which sounds like we do not care about the time that she somehow magically catches it right at the floor when she arrives at the elevator.

Well on floor 1 and floor 15 the elevator can only go in one direction.  Every other floor it can be going in either direction.  So 15 - 2 = 13 * 2 = 26 + 2 = 28 different possible things that the elevator could be doing.  We are interested in only the time when it arrives at 13 
going down.  So if the elevator is at floor 15 or floor 14 (no matter which direction its 
going from 14 it will be going down when it first arrives at 13) so,

p = 1/28 (for floor 15) + 2/28 (for floor 14) + 1/28 (for the time it arrives at floor 13 
  going down)
p = 4/28 = 1/7 
  - so about a 14% chance when the elevator arrives at 13 it will be going down
  
  - can't the wizards just fly?
  
```


### Urn While You Learn

Hogwarts is filled with all kinds of wonderous magical objects: talking portraits, deadly moving stairs, secret passages, and the largest collection of magical urns in Western Europe.

There's an urn on the fourth floor with a strange property: every time Hermione takes a ball out, the urn randomly chooses and discards another ball!

Suppose the urn contains 10 black balls and 5 red balls. If Hermione draws two balls, what is the probability that the second ball is red?

```
Using a tree diagram
                      B:10                  R: 5
               10/15  /                        \  5/15
                   B:9    R:5                B:10        R:4
                .5/         \ .5           .5 /            \ .5
              B:8 R:5       B:9 R:4       B:9 R:4          B:10 R:3
          DC /    \ 5/13      DC/\ 4/13     DC/\ 4/13      DC / \ 3/13
          
On the left side:
10/15 * .5 * 5/13 = .1282
10/15 * .5 * 4/13 = .1026

On the right side:
5/15 * .5 * 4/13 = .0513
5/15 * .5 * 3/13 = .0385

p = .1282 + .1026 + .0513 + .0385
  = .3206
  about 32%

```

### Pólya's Urn

Suppose an urn contains 9 black balls and 6 red balls. On each trial, Hermione picks a ball at random from the urn, returns it to the urn, and adds in one more ball of the same color.

Suppose she carries out this procedure two times. What are the expected numbers of red and black balls in the urn?

Tip: draw a tree of possible outcomes.

```
Using a tree diagram
                                   B: 9 R: 6
                   9/15     /                             \    6/15
                B: 10 R: 6                                B: 9 R: 7
        10/16     /     \   6/16                      9/16 /       \  7/16
        B: 11 R: 6      B: 10 R: 7                B:10 R: 7       B: 9 R: 8

11 black balls 6 red balls = 37.5%
10 black balls 7 red balls = 22.5% * 2 = 45%
9 black balls 8 red balls = 17.5%
```

### Arithmancy

The discrete uniform distribution is defined over a finite set of integer values

```
{a, a+1, a+2, ..., b}
```

each of which is equally likely to be observed.

Rolling a six-sided die is a special case of the discrete uniform distribution with `a = 1` and `b = 6`. Rolling a 20-sided die would have `a = 1` and `b = 20`.

Prove that the expected value of a discrete uniform distribution with `a = 1` and `b = n` is

```
        n + 1 
E[X] = -------
          2
```
Hint: Each of the `n` values is equally likely to be observed.

Hint-hint: There's going to be a summation. You can look up the result if you don’t remember it.

```
E[X] = sum x (x p(x))
     = 1(1/n) + 2(1/n) + 3(1/n) + ...
     = sum k = 1 to n (k(1/n))
     = (1/n) sum k = 1 to n (k)
     = (1/n) (n(n+1))/2
     = (n+1) / 2
     
This makes sense because (n+1)/2 is also the formula to find the median.  Over
  a discrete uniform distribution this would also be the average.  The E[X] is
  sometimes written as the average value of X.

```

### Birthday Attack

<img src="https://64.media.tumblr.com/3ee467fbfc590a59e079ddfe7f93d34d/tumblr_psp65oRMS91s5b5tzo1_500.jpg" width="40%" />

There are a total of 40 students in Hermoine's year at Hogwarts.

Birthdays are important in the Wizarding World. Sharing a birthday with another witch or wizard can create a magical bond between the two of you, leading to all sorts of ridiculous hijinks. This is why wizard twins are always crazy.

What's the probability that no two students in Hermoine's year share the same birthday?

Tip: Assume that there are 365 possible birthdays (wizards can't be born on Leap Days) and that wizards are equally likely to be born on any day of the year.

Tip-Tip:

Suppose there are only two students: Hermione and her best friend Victoria Potter, the Girl-Who-Lived.

```
P(Both are born on two different days) = (365 / 365) * (364 / 365)

```

Hermoine's birthday can be on any day, but Victoria's must occur randomly on one of the other 364 days.

What if there are three students? How about more?

```

P(Both are born on two different days) = .9973 or about 99.7%

If 3 Students:
Number of pairs = (3 * 2) / 2 = 3
P(unique pair) = .9973
P(3 unique pairs) = (.9973)^3 = .9919 or about 99.19%


For 40 Students:
Number of pairs = (40 * 39) / 2 = 780
P(unique pair) = .9973
P(780 unique pairs) = (.9973)^780 = .1214 or about 12.14%

```