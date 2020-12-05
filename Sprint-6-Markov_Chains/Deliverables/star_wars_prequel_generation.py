import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

with open("star_wars_episode_1_script.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

with open("star_wars_episode_2_script.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

with open("star_wars_episode_3_script.txt") as f:
	text = f.read()
model_c = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b, model_c], [1.0, 20.0, 400.0])

# Print five randomly-generated sentences
for i in range(10):
    print(model_combo.make_sentence())
    print('')