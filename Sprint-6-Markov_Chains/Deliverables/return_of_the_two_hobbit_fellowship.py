# A program that aims to creat new original lord of the rings books
# I worked a lot with spaCy 
# And also tried to use tensorflow.
# That being said, vscode would not let me pip
# Tensorflow. And the models I created with spaCy were too unreliable
# That being said, I had a ton of fun with this project, and I have 
# Really enjoyed this semester.
# Thabk you!!

import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify
import re
import spacy

with open("Hobbit.txt", encoding="utf8") as f:
    text = f.read()
model_a = markovify.Text(text, state_size = 4)

with open("Fellowship.txt", encoding= "utf8") as f:
    text = f.read()
model_b = markovify.Text(text, state_size = 4)

with open("Towers.txt", encoding= "utf8") as f:
    text = f.read()
model_c = markovify.Text(text, state_size = 4)

with open("Return.txt", encoding= "utf8") as f:
    text = f.read()
model_d = markovify.Text(text, state_size = 4)



model_combo = markovify.combine([model_a, model_b, model_c, model_d], [25.0, 25.0, 25.0, 25.0])


print(" ")
print("    THE RETURN OF THE TWO HOBBIT FELLOWSHIP     ")
print("       |_________________              _____    ")
print("o======@______________,^^'    ___      \____.`  ")
print("       |                    ,'____\             ")
print(" ")
print ("      " + model_combo.make_sentence(tries = 100))
print (model_combo.make_sentence(tries = 100))
print (model_combo.make_sentence(tries = 100))
print (model_combo.make_sentence(tries = 100))
print (model_combo.make_sentence(tries = 100))

i = 0
while i < 50:

    sen = model_combo.make_sentence(tries = 100)
    if sen is not None:
        print(sen)

        if i % 9 == 0:
            print(" ")
            print ("      " + sen)   

    i = i + 1

print(" ")