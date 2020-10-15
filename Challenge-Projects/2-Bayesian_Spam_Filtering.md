# Challenge Project &ndash; Bayesian Spam Filtering

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

## Spam Filtering as a Learning Problem

Suppose you want to build a system that filters unwanted e-mail or text messages ("spam") from legitimate messages (sometimes called "ham", though I hate saying that). You
could consider creating a **rule-based system**, which uses a series of conditional checks on each new message &ndash; content, grammar, sender's address, etc. &ndash; to determine
whether it should be accepted or rejected.

You would quickly run into a problem, though: coming up with a set of rules that's complex enough to identify spam messages but still reasonable to code is really hard. Such a
system would also be hard to maintain over time, because every change in spammers' behavior would require you to create and implement new sets of rules to correctly classify
the new messages.

Instead of trying to manually build a rule-based system, let's approach spam filtering as a **learning problem**. If we had a large data set of spam messages (which is not 
difficult to obtain) and a set of legitimate messages, we could **learn a model from the data** that succeeds at distinguishing between the two classes. Given a new 
message, our model should be able to predict, with high accuracy, whether that message is more likely to be spam or legitimate.

This formulation of spam filtering is an example of a **supervised learning problem**:

- There is a set of **classes**, which we'll denote as *C*. Here, the set of classes is *C* = {*spam*, *not spam*}. Many classification problems have this type of
yes/no or true/false structure, where there are two classes of interest, but it's possible to create models that differentiate between more than two classes.

- There is a **training data set**, consisting of labeled example messages for which we know the correct classification.

- There is a **model**, which is capable of discriminating between the two classes. Our goal is to **fit** the model using the given training data, so that it makes
accurate predictions on new data that will appear in the future. 

  Most machine learning models are like abstract and general pieces of applied statistics and linear algebra; 
every model can be used to solve many different types of classification tasks, although some models may be better suited for some problems that others. Examples
of popular machine learning models include the naïve Bayesian classifier, which we'll discuss in more detail below, deep learning neural networks, decision trees, and
support vector machines.

- There is usually a **testing data set**, which is used to evaluate the trained model. The testing data set consists of labeled examples with known classifications,
but isn't used in the training process. If the model is good, it should produce accurate results on the testing set. The testing set is used to ensure that the model
doesn't **overfit** the training data, which would result in a model that doesn't generalize well beyond the training examples.

## Bayesian Classification

Very good. We've now committed to learning a model using a training data set that can discriminate between spam and non-spam messages.

The Bayesian approach considers classification as a **probability problem**. Suppose we're considering a message *m*. We'd like to use the **words in *m*** as our **features**
to determine if *m* is spam or not. We could, potenially, expand our list of features to include things other than just the contents of the message, but we won't worry about 
that in these examples.

Intuitively, there are some words that are likely to occur in spam message but not in legitimate messages. I'll let you think about what some of those words are.

Consider two conditional probabilities:

```
P(m is spam | words in m)
```

```
P(m is NOT spam | words in m)
```

If we could calculate these two probabilities for the message *m*, we could classify *m* based on whichever probability is highest. For example, if our model deems it more 
likely that *m* is spam than not-spam, we should send *m* straight to the junk folder.

Here's the problem: **how do we calculate these two probabilities**?

To begin, let's think about the reversed conditonal probability:

```
P(words in m | spam)
```

This probability expresses the likelihood that a message picked from the universe of all spam messages contains the words we observed in message *m*. **We can estimate
this from the training data**. The training data contains a large number of example spam messages, so we can look at the words they contain and build a model that
estimates how likely a given message is if it's really spam.

Similarly, we can construct a model that estimates `P(words in m | not spam)` using the messages in the training data that we know are legitimate.

**This is the perfect setup for Bayes' Rule**. We have a conditional probability of interest that's hard to calculate directly, but we can reason about the reversed conditional
probability.

Unleash the math!

<img src="https://render.githubusercontent.com/render/math?math=P(c \, | \textbf{m}) = \frac{P(\textbf{m}  |  c) P(c)}{P(\textbf{m})}" width="20%">





