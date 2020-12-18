import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

with open("ec.txt") as f:
    text = f.read()
model_a = markovify.NewlineText(text, state_size=1)

with open("cs.txt") as f:
    text = f.read()
model_b = markovify.NewlineText(text, state_size=1)

model_combo = markovify.combine([model_a, model_b], [1.0, 25.0])

# Print five randomly-generated sentences
for i in range(100):
    print(model_combo.make_sentence())
    print()