"""
Example spam filtering model using a naive Bayesian classifier.

The spam.csv dataset is from Kaggle.
"""

#--- Imports
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np
import pandas as pd


#--- Load spam.csv as a Pandas dataframe
df = pd.read_csv('spam.csv', header = 0, encoding='latin1')
print(df)


#--- Split into training and testing sets, 70-30 ratio
#
# df['message'] is the column of text message contents
# df['label'] is the column of labels for each message, either 'spam' or 'ham'
#
# X_train is the set of training messages
# y_train is the set of correct labels for the training messages
# X_test is the set of testing messages
# y_test is the set of correct labels for the testing messages

X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size = 0.30)

    
#--- Build a Pipeline that implements the classifier
#
# 1. CountVectorizer turns input text into counts of words
# 2. MultinomialNB is the multinomial naive Bayes classifier
    
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', MultinomialNB()),
])


#--- Fit the model to the training data
#
# TODO: add one line to fit text_clf using X_train and y_train as the inputs
text_clf.fit(X_train,y_train)
    
#--- Use the trained model to predict classes on the test set       
#
# TODO: complete the right-hand side to use text_clf to predict the labels for X_test

predicted = text_clf.predict(X_test)


#--- Testing accuracy
print(np.mean(predicted == y_test))


#--- Print more detailed assessment of the model's performance
print(metrics.classification_report(y_test, predicted,
    target_names=['spam', 'ham']))
