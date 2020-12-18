
# Objective: Using Markovify library, create a ultimate sherlock holmes story based on three different 
###################################################################################################
###################################################################################################
import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

# Get raw text as string.
with open("sh_scandal_bohemia.txt") as f_a:
    text_a = f_a.read()

with open ("sh_final_problem.txt") as f_b:
    text_b = f_b.read()
with open ("sherlock_holmes_Scarlet.txt") as f_c:
    text_c = f_c.read()

# Build the Markov models then create a combined model
model_a = markovify.Text(text_a, state_size=2)
model_b = markovify.Text(text_b, state_size=2)
model_c = markovify.Text(text_c, state_size=2)



model_combo = markovify.combine([model_a, model_b, model_c], [1.5, 2.5, 2.0])

sh_novel = list()


# Print randomly-generated sentences
for i in range(100):
    sh_novel.append(model_combo.make_sentence())  # try to make sentences of no more than 60 characters
    
    
for sentence in sh_novel:
    
    if (sh_novel.index(sentence) == len(sh_novel) - 1):
        
        print(sentence)
        print()
    else : 
        print(sentence, end=" ")
    
    