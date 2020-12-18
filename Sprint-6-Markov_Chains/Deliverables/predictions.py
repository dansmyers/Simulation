#!/usr/bin/python3

"""
noah olmstead harvey
predictions
18122020
this script is a markov chain tolkien song generator/text-predictor
"""

####  IMPORTS  #################################################################################################################

import markovify

####  FUNCTIONS  ###############################################################################################################

def endLine(model):                                             #  outputs a string with an ending char
    lastLine = model.make_sentence(tries=100)
    while(lastLine[-1] not in "!."):
        lastLine = model.make_sentence(tries=100)
    return(lastLine)

def makeChorus(model):                                          #  outputs a four-line chorus for repeat
    chorus = model.make_sentence(tries=100)
    chorus += ('\n' + model.make_sentence(tries=100))
    chorus += ('\n' + model.make_sentence(tries=100))
    chorus += ('\n' + endLine(model))
    return(chorus)

####  MAIN  ####################################################################################################################

with open("lotrPoems.txt",'r') as f:                            #  open lotr poems
    lotrData = f.read()
f.close()

with open("hobbitPoems.txt", 'r') as f:                         #  open hobbit poems      
    hobbitData = f.read()
f.close()

lotr = markovify.NewlineText(lotrData, state_size = 2)          #  create a model using the lotr poems
hobbit = markovify.NewlineText(hobbitData, state_size = 2)      #  create a model using the hobbit poems
both = markovify.combine([hobbit, lotr], [2.0, 1.0])            #  combine the models - weight the smaller hobbit model higher

song = "\n\n"                                                   #  initialize a string for the generated song
chorus = makeChorus(lotr)                                       #  generate a chorus
for i in range(4):                                              #  generate the verses
    song += both.make_sentence(tries=100)
    for ii in range(7):
        if(ii == 6):                                            #  end the verse with a '.' or '!'
            song += endLine(both)
        else:
            song += ('\n' + both.make_sentence(tries=100))
    if(i == 3):
        song +=("\n\n")                                         #  end the song without repeating the chorus
    else:
        song += ("\n\n" + chorus + "\n\n")
print(song)                                                     #  display the song
