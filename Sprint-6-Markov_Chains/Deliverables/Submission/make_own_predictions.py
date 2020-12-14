import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

# Get raw text as string.
with open("dr_seuss.txt") as f:
    text = f.read()
    
# Build the Markov model
model = markovify.Text(text, state_size=2)

# Print randomly-generated sentences
for i in range(20):
    print(model.make_sentence())  # try to make sentences of no more than 60 characters
    print()