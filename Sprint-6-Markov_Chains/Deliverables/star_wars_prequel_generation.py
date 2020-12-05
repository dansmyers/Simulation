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

with open("art_of_war.txt") as f:
	text = f.read()
model_d = markovify.Text(text, state_size=2)

with open("the_sound_and_the_fury.txt") as f:
	text = f.read()
model_e = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b, model_c, model_d, model_e], [3.0, 3.0, 3.0, 5.0, 5.0])

# Print five randomly-generated sentences
for i in range(10):
    print(model_combo.make_sentence())
    print('')