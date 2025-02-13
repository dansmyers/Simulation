# Bayesian Spam Filtering

## Overview

This project will let you explore a useful application of Bayes' Rule: **e-mail spam filtering**. Along the way, you'll get some practice working with statistical machine
learning models.

By the end of this project you will be familiar with:

- The concept of a predictive classification model
- Formulating a classification model as a conditional probability problem
- Using Bayes' Rule to derive an expression that can be used for making predictions
- How the naïve Bayesian classifier works
- How to use naïve Bayes to classify texts
- Implementing a classifier using Python's scikit-learn library

You don't have to actually write that much code to complete this project, but you will have to work through these notes and understand the mechanics of the Bayesian
classifier. Most of the difficulty comes from understanding the concepts involved.


## Spam Filtering as a Learning Problem

Suppose you want to build a system that filters unwanted e-mail or text messages ("spam") from legitimate messages (sometimes called "ham", though I hate saying that). You
could consider creating a **rule-based system**, which uses a series of conditional checks on each new message &ndash; content, grammar, sender's address, etc. &ndash; to determine
whether it should be accepted or rejected.

You would quickly run into a problem, though: coming up with a set of rules that's complex enough to identify spam messages but still reasonable to code is really hard. Such a
system would also be hard to maintain over time, because every change in spammers' behavior would require you to create and implement new sets of rules to correctly classify
the new messages.

Instead of trying to manually build a rule-based system, let's approach spam filtering as a **learning problem**. If we had a large data set of spam messages (which is not 
difficult to obtain) and a set of legitimate messages, we could **learn a model from the data** that succeeds at distinguishing between the two classes.

This formulation of spam filtering is an example of a **supervised learning problem**:

- There is a set of **classes**, which we'll denote as *C* = {*spam*, *not spam*}. Many classification problems have this type of
yes/no or true/false structure, where there are two classes of interest.

- There is a **training data set**, consisting of labeled example messages for which we know the correct classification.

- There is a **model**, which is capable of discriminating between the two classes. Our goal is to **fit** the model using the given training data, so that it makes
accurate predictions on new data that will appear in the future.

- There is usually a **testing data set**, which is used to evaluate the trained model. The testing data set consists of labeled examples with known classifications,
but isn't used in the training process. If the model is good, it should produce accurate results on the testing set. The testing set is used to ensure that the model
doesn't **overfit** the training data, which would result in a model that doesn't generalize well beyond the training examples.

## Bayesian Classification

<img src="https://imgs.xkcd.com/comics/machine_learning_2x.png" width="33%" />

### Classification as a Conditional Probability

The Bayesian approach considers classification as a **probability problem**. Suppose we're considering a message *m*. We'd like to use the **words in *m*** to determine if *m* is spam or not. 

Consider two conditional probabilities:
```
P(m is spam | words in m)
```
```
P(m is NOT spam | words in m)
```

If we could calculate these two probabilities for the message *m*, we could classify *m* based on whichever probability is highest. If our model deems it more likely that *m* is spam than not-spam, we should send *m* straight to the junk folder.

Here's the problem: **how do we calculate these two probabilities**?

To begin, let's think about the reversed conditonal probability:
```
P(words in m | spam)
```
This probability expresses the likelihood that a message picked from the universe of all spam messages contains the words in message *m*. **We can estimate this from the training data**. 

The training data contains a large number of spam messages, so we can determine this probability by looking at the words in that data set. Similarly, we can construct a model that estimates `P(words in m | not spam)` using the messages in the training data that we know are legitimate.

### Intuition

If you're not sure about this part, consider a message that contains the words "**FREE HERBAL VIAGRA**". 

I do not often receive legitimate messages on this topic, so I'd expect `P("FREE HERBAL VIAGRA" | not spam)` to be very close to zero. The other case, `P("FREE HERBAL VIAGRA" | spam)`, should be much higher.

### Bayes' Rule

**This is the perfect setup for Bayes' Rule**. We have a conditional probability of interest that's hard to calculate directly, but we can work with the reversed conditional probability.

Unleash the math!

Let *c* denote a class of interest, either *spam* or *not spam* in this example. Let *m* denote the contents of the message.

Direct application of Bayes' Rules yields:

```
             P(m | c) P (c)
P(c | m) =  ----------------
                 P(m)
```

<!--img src="https://render.githubusercontent.com/render/math?math=P(c \, | \, \textbf{m}) = \frac{P(\textbf{m} \, |  \, c) P(c)}{P(\textbf{m})}" width="20%"-->

The left-hand side is the classification probability we're interested in: the probability of observing class *c* given the contents of the message. The right side contains three terms.

- *P*(*m* | *c*), is the probability of observing message *m* if it really belongs to class *c*. This probability is also called the **likelihood**. We'll calculate this from the training data.

- *P*(*c*) is the **unconditional probability of observing class *c***, independent of any information about the message. In our problem, this is the fraction all messages that are spam or not spam. In Bayesian statistics, this is called the **prior**  probability. If you have reason to believe that one class is more likely than another, the prior probability allows you to incorporate this information into the model.  

  For example, suppose that we believe 80% of all e-mail traffic is spam and only 20% is legitimate, which is consistent with research estimates. Using these probabilities for  *P*(spam) and *P*(not spam) would make it easier to classify messages as spam and require stronger evidence to mark a message as non-spam.  

  In practice, we could use pre-existing evidence to set these values, estimate them from the training set, or assume that all classes are equally likely, which
is equivalent to assuming no prior evidence about the class distribution.

- The denominator, *P*(*m*), is the unconditional probability of observing a message with contents *m*, across the universe of all spam and non-spam messages. Notice: this does not depend on *c*! Therefore, the value of *P*(*m*) will be the **same for both classes** and **we can ignore it in our calculations**.

## Example

This is all pretty abstract, so let's look at how this plays out in a *small* example.

Suppose we have a universe of only four messages, two spam and two non-spam. Let's assume the messages have been pre-processed to remove all punctuation and case.

| Message contents           | Class label |
| -------------------------- | ----------- |
| watch free anime downloads | spam        |
| see you at the house       | not spam    |
| do you want takeout        | not spam    |
| sell your house now        | spam        |

Is the message "you want to watch anime at my house" more likely to be spam or not spam? Using the Bayesian formulation, we need to calculate two probabilities:
```
P(spam | "you want to watch anime at my house")
```
```
P(not spam | "you want to watch anime at my house")
```

Once we've performed both calculations, we'll take the larger probability to be the correct classification. From the previous model, we know that
```
P(spam | "you want to watch anime at my house") = P("you want to watch anime at my house" | spam) P(spam)
```
```
P(not spam | "you want to watch anime at my house") = P("you want to watch anime at my house" | not spam) P(not spam)
```
These formulas are the numerator of Bayes' Rule. Recall that the denominator can be ignored because it's the same for both classes.

### Prior Probabilities

Because we have an equal number of training examples in each class, we could decide that
```
P(spam) = P(not spam)
```
which means that the priors will not affect our classification decision, and can be dropped from further calculation.

If we had evidence that one class was more likely than another, we'd use the prior probabilities to incorporate that information into the model.

## The Naïve Bayes Model

To calculate the likelihoods, we're going to make a very strong simplification: **Assume that the likelihood of each individual word in a message is independent of all of the other words**.

This is a strong assumption! By assuming independence, we're choosing to ignore all word context, sentence structure, grammar, and anything else that makes some word combinations more likely than others.

If all of the words are independent, then the likelihood of the entire message is the product of the individual word likelihoods
```
P("you want to watch anime at my house" | spam) = P("you" | spam) * P("want" | spam) * P("to" | spam) * ... * P("house" | spam)
```
A Bayesian model that assumes independence of the features is called a **naïve Bayesian classifier**, because the assumption of independence is usually a huge simplification of reality. Nonetheless, naïve Bayes has been shown to be effective in many real-world problems including text classification, so it's a standard technique in the field.

### Estimating Word Likelihoods

Estimating the likelihood of individual words is easy:
```
                  Number of times word occurs in all spam messages
P(word | spam) = --------------------------------------------------
                      Count of all words in all spam messages
``` 
For example, the word "anime" occurs one time in the set of spam messages and there are a total count of eight words in the entire spam data set, so we estimate
```
P("anime" | spam) = 1 / 8 = .125
```
Based on our data set, we expect that 12.5% of all words in spam messages should be "anime".


### Smoothing

There are two other issues to consider.

First, we're doing to ignore high-frequency common words like *a*, *at*, *the*, because they don't help discriminate between the two classes. This is easy to do by preprocessing the data set before training the model.

The second issue is more complicated. What about words that don't appear in one of the data sets?

For example, "anime" does not appear in the non-spam data set, but we don't want to conclude that `P("anime" | non-spam) = 0`, because that would imply it's impossible for me to receive a non-spam message about anime.

A typical solution to this problem is to assume that every word has some small constant probability of occurring, even if it was never observed in the training data set. Modify the word likelihood formula to be

```
                                  Number of times word occurs in all spam messages + 1
P(word | spam) = ---------------------------------------------------------------------------------------
                      Count of all words in all spam messages + Number of unique words in all messages

```

The numerator is now guaranteed to be at least 1, even a word does not appear in any messages. To compensate for this change, the denominator has been increased to include the number of unique words in all messages (the **vocabulary** of the training set). Our training set contains 12 unique words after dropping "at", "the", and "do".

Under these new assumptions, we can calculate
```
                      1 + 1
P("anime" | spam) =  -------- ~ .10
                      8 + 12
```
The corresponding non-spam probability is
```
                           0 + 1
P("anime" | not spam) =  -------- ~ .055
                           6 + 12
```
The fancy name for this adjustment is **Laplace smoothing**.

### Results

Here is the table of likelihoods for the important words in "you want to watch anime at my house" calculated using the Laplace smoothing strategy.


| word | P(word \| spam)  | P(word \| not spam) |
|------| ----------------- | ------------------- |
| you | .05 | .166 |
| want | .05 | .111 |
| watch | .10 | .055 |
| anime | .10 | .055 |
| my | .05 | .055 |
| house | .10 | .111 |

For example, "you" appears two times in the non-spam messages and zero times in the spam messages. It's probabilities are therefore:
```
P("you" | non-spam) = (2 + 1) / (6 + 12) ~ .166
```
```
P("you" | spam) = (0 + 1) / (8 + 12) ~ .05
```
Also observe that "my" doesn't appear in either the spam or non-spam group of training examples, but we can still calculate non-zero probabilities for it because
of smoothing.

### The probabilities

The final step is to calculate the likelihood of the entire message "you want to watch anime at my house".
```
P("you want to watch anime at my house" | spam) = P("you" | spam) * P("want" | spam) * ... * P("house" | spam)

                                                = .05 * .05 * .10 * .10 * .05 * .10
                                              
                                                = 1.25e-7
```

The corresponding probability for the non-spam case is
```
P("you want to watch anime at my house" | not spam) = .166 * .111 * .055 * .055 * .055 * .111
                                           
                                                    = 3.4e-7

```

Based on these results, we conclude that "you want to watch anime at my house" is **most likely not spam** because the non-spam case yields the higher value.

Note that we can't truly interpret the output of these calculations as probabilities, due to the changes we've made to the original Bayes formulation, like dropping the denominator. The results are still **proportional** to the true probabilities, which is what allows us to conclude that the not spam case is more likely.

## Practice Problems

### Calculations

Using the training data set given above and the naïve Bayesian classifer technique, determine whether the following messages are more likely to be spam or not spam.

1. "watch anime now"

2. "takeout and anime at my house"

3. "sell me your anime collection"

### Code

Now generate a Bayesian learning model to classify the entries in `spam.csv`. Use the `naive_bayes` model of the `scikit-learn` library.

Some guidelines:

- Split the data set so that 70% of entries are used for training and the other 30% for testing
- Print the accuracy on the test set, and also output a more detailed report using `metrics.classification_report`
- Once you have the report, explain the meaning of the terms *precision* and *recall*. What information do they give you about the model's performance and how are they different from the basic accuracy measurement and from each other?

How are you going to do this? **Use an AI model** to help you generate and interpret the required code.

I recommend starting with a chat model of your choice and having a discussion about what you need. Ask it to guide you through developing the Bayesian model and talk about what features the program needs to have. Once you've worked out the details, prompt it to generate code. This should be pretty easy.


## Summary

All of the challenge in this project is in working through the details of the naïve Bayes model. You should be able to complete the calculations and scikit-learn example
without difficulty if you understand the model.

This example is just scratching the surface of machine learning in general and statistical learning in particular. If you're interested in learning more, I recommend starting with [this video](https://www.youtube.com/watch?v=aircAruvnKk&vl=en) on neural networks and the handwritten digit classification problem.
