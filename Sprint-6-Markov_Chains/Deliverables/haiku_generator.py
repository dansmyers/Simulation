### Generate haiku-like poems from the poetry of Kobyashi Issa

# Issa's poems are translated from Japanese, so they don't obey the
# 5-7-5 syllable structure that's often used for haiku in English.
#
# That's okay.

from random import choice

model = {}
starting_words = []
ending_words = []

f = open('kobayashi_issa_10000_haiku.txt')

# Read the file text as a string
text = f.read()

# Split into separate poems
# Poems are separated by a newline
#
# In general, split the text using some marker that makes sense
# You could use lines, periods, or other punctuation marks
poems = text.split("\n\n")

# Iterate over the poems
for poem in poems:
    
    # Split the poem into its component words
    words = poem.split()
    
    if len(words) == 0:
        continue
    
    # Keep track of the starting and ending words in each poem
    starting_words.append(words[0])
    ending_words.append(words[-1])
    
    # The is model is a dictionary
    # The keys are words from the poems
    # Each value is a list of the words that follow the key word
    for w in range(len(words) - 1):
        current_word = words[w]
        
        if current_word not in model:
            model[current_word] = []
            
        model[current_word].append(words[w + 1])

# Randomly pick a starting word
#
# Words that start multiple poems will show up multiple times in
# the list and be chosen more frequently
first_word = choice(starting_words)
haiku = [first_word]

while True:
    next_word = choice(model[haiku[-1]])
    haiku.append(next_word)
    
    if next_word not in model:
        break
    
    # Stop when the model reaches an ending word and the haiku is sufficiently long
    #
    # Play with these stopping settings to influence the style of the random poem
    if next_word in ending_words and len(haiku) > 7:
        break
    
print(haiku)

# Join the list of words into a single string
final = ' '.join(haiku)
print(final)
