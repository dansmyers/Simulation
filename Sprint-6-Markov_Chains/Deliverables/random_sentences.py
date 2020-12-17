import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

with open("frost.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

"""
with open("shakespeare1.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

with open("soneets.txt") as f:
    text = f.read()
model_c = markovify.Text(text, state_size=2)
"""


# model_combo = markovify.combine([model_a, model_b, model_c], [5.0, 10.0, 3.0])

# Print five randomly-generated sentences
for i in range(5):
    for i in range(5):
        print(model_a.make_sentence())
    print ('')