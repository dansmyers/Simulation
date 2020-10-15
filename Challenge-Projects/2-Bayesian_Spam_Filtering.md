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


