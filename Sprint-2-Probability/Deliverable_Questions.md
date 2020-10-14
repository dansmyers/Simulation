# Hermione Granger and the Distributions of Probability
```
## Disclaimer

This problem set is a work of fan fiction. Hermione Granger and related characters were created by J.K. Rowling. Please don't sue me.

<img src="https://64.media.tumblr.com/d85b44001002bb249c42b27e00d8dccb/tumblr_nzrkzfmjZW1s5b5tzo1_500.jpg" width="40%" />
```
## Honor Code

On my honor i have not given nor recieved nor witnessed any unauthorized assistance on this work
TJ Donahue

## List Your Team Members

Jay TJ Gonzalo

## Instructions

Answer the following questions, which cover discrete probability distributions, expected values, and conditional probabilities.

You can type your answers in this document or upload a scanned handwritten file.

## Questions

### Wizard People, Dear Reader?
```
<img src="https://64.media.tumblr.com/99413ebb9f4e29d268974d90d81da509/tumblr_ne9qzeTT7T1s5b5tzo1_500.jpg" width="40%"/>
Hermione Granger is pretty sure she’s a witch, because she read in a book that having very curly hair is a sign of latent mystical power. Also, one time an owl landed on her head. However, she didn’t receive a letter from Hogwarts on her 11th birthday.
After reading several books and pamphlets, Hermione is pretty sure that
P(She's a witch) = .75
P(Not receiving a letter | She's a witch) = .03  (because owls are actually pretty dumb)
P(Not receiving a letter | She's not a witch) = .99   
Under these assumptions, what is the probability that Hermione really is a witch even though she didn’t get a letter?
Tip: use Bayes' Rule,
             P(A) * P(B | A)
P(A | B) =  -----------------
                  P(B)
where
A = She's a witch
B = Not receiving a letter
P(B) is therefore the total probability of not receiving a letter.
P(A|B): P(A) * P(B|A) / P(B) 
```
= P(A) * P(B|A) / ( (P(B|A) * P(A)) + (P(B|~A) * P(~A)) )

= (.75 * .03) / (.03 * .75) + (.99 * .25)

= .0833


### Chocolate Frogs
```
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
30/30 + 30/29 + 30/28 + 30/27 + 30/26 + 30/25 + 30/24 + 30/23 + 30/22 + 30/21 + 30/20 + 30/19 + 30/18 + 30/17 + 
30/16 + 30/15 + 30/14 + 30/13 + 30/12 + 30/11 + 30/10 + 30/9 + 30/8 + 30/7 + 30/6 + 30/5 + 30/4 + 30/3 + 30/2 + 30/1

```
total = 0
for i in range(0, 30, 1):
  temp = 30/(30 - i) 
  total += temp; 
print(total)
```
total = 119.85

120 chocolate frogs to get all 30 cards

### Hat Problem
```
Hermione and Harry made it to Hogwarts!
Students arriving at Hogwarts are sorted into one of the four residential houses -- Gryffindor, Hufflepuff, Ravenclaw, and Slytherin -- by the magical Sorting Hat.
In theory, the Hat is supposed to examine each student's personality, consider his or her wishes, and then place the student into the most appropriate house. However, after a thousand years, the Hat has gotten pretty lazy, so it has simplified its sorting process into a two-step algorithm:
1. All evil students go into Slytherin, obviously.
2. Everybody else is just randomly sorted into one of the four houses, with a 40% probability of being put into Hufflepuff and a 20% probability of being put into each of the three other houses.
Hermione is shocked when she's sorted into Slytherin! She's never thought of herself as evil, but now that she considers it, becoming the future Dark Lady of Magical Britain does have some appeal...
If 10% of new Hogwarts students are evil, what is the probability that a randomly chosen Slytherin is evil?
Tip: the value you want is `P(Evil | Slytherin)`.
```
Given: P(Slytherin|Evil): 1; P(Hufflepuff): .4; P(Slytherin|~Evil): .2; P(evil): .1; 

-

P(Evil|Slytherin) + P(Evil) * P(Slytherin|Evil) / P(Slytherin)

= P(Evil) * P(Slytherin|Evil) / (P(Evil) * P(Slytherin|Evil) + P(Slytherin|~Evil) * P(~Evil))

P(Slytherin) = (.1) * (1) + (.2) * (.9)

= .1 + .18

= .28 students in slytherin

P(Evil|Slytherin) = (.1)(1)/.28 = .36

-

100 theoretical students, 10 are evil therefore get put into slytherin. 

of the other 90 students 20% of them get put into slytherin (90*.2 = 18). 

that makes the population of slytherin 10 evil to 18 not evil

which means P(Evil|Slytherin) = 10/28 = .36


### Dumblevator
```
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
```

P(Elevator>=13 && Going Down) = P(15)(1) + P(14)(.5) + P(13)(.5)

= (1/15)(1) + (1/15)(1/2) + (1/15)(1/2)

= (1/15)(2)

= 2/15

= .13

### Urn While You Learn
```
Hogwarts is filled with all kinds of wonderous magical objects: talking portraits, deadly moving stairs, secret passages, and the largest collection of magical urns in Western Europe.
There's an urn on the fourth floor with a strange property: every time Hermione takes a ball out, the urn randomly chooses and discards another ball!
Suppose the urn contains 10 black balls and 5 red balls. If Hermione draws two balls, what is the probability that the second ball is red?
```
P(RRR)+P(BBR)+P(BRR)+P(RBR)

= (5 * 4 * 3 / 15 * 14 * 13) + (10 * 9 * 5 / 15 * 14 * 13) + (10 * 5 * 4 / 15 * 14 * 13) + (5 * 10 * 4 / 15 * 14 * 13)

= (60/2730) + (450/2730) + 2(200/2730)

= (60 + 450 + 400) / 2730

= 910/2730 = 91/273 = .33

= 1/3

### Pólya's Urn
```
Suppose an urn contains 9 black balls and 6 red balls. On each trial, Hermione picks a ball at random from the urn, returns it to the urn, and adds in one more ball of the same color.
Suppose she carries out this procedure two times. What are the expected numbers of red and black balls in the urn?
Tip: draw a tree of possible outcomes.
```
```

1        B9/15          R6/15

.       /     \         /   \

2    B10/16  R6/16   R7/16 B9/16

=    11,6    10,7     9,8   10,7
```

RR: 9b8r RB: 10b7r BR: 10b7r BB: 11b6r

-

P(RR) = 6/15 * 7/16 = .175 -> 9b8r

P(RB) = 6/15 * 9/16 = .225 -> 10b7r

P(BR) = 9/15 * 6/16 = .225 -> 10b7r

P(BB) = 9/15 * 10/16 = .375 -> 11b6r

-

P(11b6r) = .375

P(10b7r) = .225 + .225 = .45

P(9b8r) = .175

-

45% chance of pulling one black and one red resulting in 10 black and 7 red

37.5% chance of pulling two black resulting in 11 black and 6 red

17.5% chance of pulling 2 red resulting in 9 black and 8 red

-

therefore the expected number of red and black balls in the urn is 10 black and 7 red

### Arithmancy
```
The discrete uniform distribution is defined over a finite set of integer values
{a, a+1, a+2, ..., b}
each of which is equally likely to be observed.
Rolling a six-sided die is a special case of the discrete uniform distribution with `a = 1` and `b = 6`. Rolling a 20-sided die would have `a = 1` and `b = 20`.
Prove that the expected value of a discrete uniform distribution with `a = 1` and `b = n` is
        n + 1 
E[X] = -------
          2
Hint: Each of the `n` values is equally likely to be observed.
Hint-hint: There's going to be a summation. You can look up the result if you don’t remember it.
```

E[X] = E(kX + (a - k))

= k * E[X] + (a - k)

= k((N + 1)/ 2) + (a - k)

= k/2 * ((b - a + k) / (k + 1)) + a - k

= (a + b) / 2

### Birthday Attack
```
<img src="https://64.media.tumblr.com/3ee467fbfc590a59e079ddfe7f93d34d/tumblr_psp65oRMS91s5b5tzo1_500.jpg" width="40%" />
There are a total of 40 students in Hermoine's year at Hogwarts.
Birthdays are important in the Wizarding World. Sharing a birthday with another witch or wizard can create a magical bond between the two of you, leading to all sorts of ridiculous hijinks. This is why wizard twins are always crazy.
Tip: Assume that there are 365 possible birthdays (wizards can't be born on Leap Days) and that wizards are equally likely to be born on any day of the year.
Tip-Tip:
Suppose there are only two Slytherin students: Hermione and her best friend Victoria Potter, the Girl-Who-Lived.
P(Both are born on two different days) = (365 / 365) * (364 / 365)
Hermoine's birthday can be on any day, but Victoria's must occur randomly on one of the other 364 days.
What if there are three students? How about more?
```
What's the probability that no two students in Hermoine's year share the same birthday?

365/365 * 364/365 * 363/365 ... 326/365
```
total = 1
for i in range(0, 40, 1):
    temp = (365-i)/365
    total = total * temp;
print(total)
```
total = .1087...
= .11
