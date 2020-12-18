"""
Script that uses Python library markovify to generate pseudorandom sentences with Markov Chains. 

This program uses text from two of Mark Mason's books: "The subtle art of not giving a f*ck" and "Everything is f*cked". It also uses text from "The alchemist" and "The little prince". I chose books that shared a common inspirational theme about living life. 

Disclaimer: I apologize for the bad words, I first came across Mark Mason in a class during my freshman year and I think that his content is very funny but also a good advice for life. 

CMS 380 - Fall 2020
Maria Morales
"""


import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

# Get raw text as string.
with open("the_alchemist.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

with open("The_little_prince.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

with open("the_subtle_art.txt") as f:
    text = f.read()
model_c = markovify.Text(text, state_size=2)

with open("Everything_Is_fucked.txt") as f:
    text = f.read()
model_d = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b, model_c, model_d], [10.0, 5.0, 15.0, 10.0])

# Print randomly-generated sentences
for i in range(100):
    print(model_combo.make_sentence())
    print(' ')