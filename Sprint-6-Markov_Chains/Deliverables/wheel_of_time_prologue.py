import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

# Get raw text as string.
with open("Eye_of_the_World_Prologue.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

with open("The_Great_Hunt_Prologue.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

with open("The_Dragon_Reborn_Prologue.txt") as f:
    text = f.read()
model_c = markovify.Text(text, state_size=2)

with open("famous_quotes.txt") as f:
    text = f.read()
model_d = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b, model_c, model_d], [1.0, 1.0, 1.0, 2.0])

# Print five randomly-generated sentences
for i in range(100):
    print(model_combo.make_sentence())
    print('')