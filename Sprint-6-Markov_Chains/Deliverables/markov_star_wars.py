"""

This program implements a markov chain text generator using the scripts from Star Wars IV, V, and VI.

Jacob Buckelew
CMS380 Fall 2020

"""

import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

with open("a_new_hope.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

with open("empire_strikes_back.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

with open("return_of_the_jedi.txt") as f:
	text = f.read()
model_c = markovify.Text(text, state_size=2)

with open("art_of_war.txt") as f:
	text = f.read()
model_d = markovify.Text(text, state_size=2)

with open("sound_and_fury.txt") as f:
	text = f.read()
model_e = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b, model_c, model_d, model_e], [5.0,5.0, 5.0, 10.0, 10.0])

# Print five randomly-generated sentences
for i in range(10):
    print(model_combo.make_sentence())
    print ('')