# Markov Chain Text Generator

## Description

In this lab, you're going to play with some tools for generating pseudorandom sentences with Markov Chains.

The main tool we'll use is a free Python library called `markovify`.

I've included a few text files in this repo for you to play with:

- `trump_tweets.txt`

- `king_james_bible.txt`

- `pride_and_prejudice.txt`

- `hamlet.txt`

- `lovecraft.txt`, *The Dunwich Horror* by H.P. Lovecraft.

- `tao.txt`, the *Tao Te Ching* by Lao-Tzu

## Setup

Install `markovify`:

```
sudo pip install markovify
```

Create a file named `markov_text_generator.py`:

```
touch markov_text_generator.py
```

Open the file and add the following code:

```
import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

# Get raw text as string.
with open("trump_tweets.txt") as f:
    text = f.read()
    
# Build the Markov model
model = markovify.Text(text, state_size=2)

# Print randomly-generated sentences
for i in range(100):
    print(model.make_sentence())  # try to make sentences of no more than 60 characters
    print()
```

Run the program and MAKE TWEETING GREAT AGAIN.

```
python markov_text_generator.py
```

Play around with the other texts. You can find more free texts on Project Gutenberg.

`state_size` controls the number of words used for each state. The default is 2, which means the model predict the next work after each
pair of words. Setting to 1 will make the text more random and 3 will make it more structured, at the risk of simply repeating sentences
verbatim. The program may hang if you run it with `state_size = 3 ` on some inputs.

## Let Our Powers Combine

When you've fully explored the possibilities of a single text, try combining two texts:

```
import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

with open("trump_tweets.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

with open("tao.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b], [1.0, 20.0])

# Print five randomly-generated sentences
for i in range(100):
    print(model_combo.make_sentence())
    print ''
```

The `combine` method joins multiple models together. The second argument is a vector of weights: increasing the weight for a smaller
corpus can make it appear more frequently in the output.

Play around with combinations.
