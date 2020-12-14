import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

with open("trump_tweets.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

with open("forklift_operators_manual.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b], [1.0, 30.0])

# Print five randomly-generated sentences
for i in range(20):
    print(model_combo.make_sentence())
    print ('')
