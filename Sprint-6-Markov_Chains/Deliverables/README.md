# Sprint 6 Deliverables

## Make Randomized Text Great Again

Creating randomized text generators is a fun application of Markov chains. For example [this Reddit account](https://www.reddit.com/user/FloridaMan_SS/posts/), which creates random
Florida Man posts using a Markov model created from the r/FloridaMan subreddit.

The model starts by picking a random starting word, then randomly choosing the next word, in such a way that words pairs occurring more
frequently in the source text are more likely to be chosen by the generator. This process then repeats, randomly choosing the next word
based on the current word.

If you'd like, you can think of it as writing using only the autocomplete feature of your phone.

Clone this public repo:

```
git clone cms380-f18-lab-2
```

The lab instructions tell you how to use a tool named `markovify` to generate random sentences. Work through the examples it contains and 
record your five best random tweets.

## Predictive Keyboards

[Botnik](https://botnik.org/) is a group that uses predictve text to make humor products. Some of their work includes:

- [*Harry Potter and the Portrait of What Looked Like a Large Pile of Ash*](https://botnik.org/content/harry-potter.html)

- [A Bitcoin explainer](https://www.youtube.com/watch?v=tBRWJzAjkjk) trained from other Bitcoin explainers

- [This episode](https://twitter.com/botnikstudios/status/1113130983426002944) of *Tidying Up with Marie Kondo*

- ["Bored with This Desire to Get Ripped"](https://www.youtube.com/watch?v=BtybvwLJC30) trained from Morrissey lyrics and reviews of the
P90X workout DVDs

- A [makeup tutorial](https://www.youtube.com/watch?v=hSppmr_dRdQ) trained from Bob Ross episodes and YouTube makeup videos

- [Cooking for Valentine's Day](https://www.youtube.com/watch?v=ck-GZOKRBg0)

Play around with the predictive keyboard on Botnik's website. Record your best creative work.

## Make Your Own Predictions

Create your own predictive text model and curate some examples of its output. Your goal is to produce a good quality **long-form** piece of Markov-generated text and then publish it on the Internet.

Making random sentences or tweet-sized chunks is easy, so I want you to experiment with making a work that's at least one-half to one page in length.

I want you to do four things:

1. Write or find a good tool for text-generation. `markovify` and Botnik's predictive keyboards are options, but I encourage you to do a little bit of research before you commmit to a tool. If you want to experiment with writing your own code, I've included an example haiku-generation program in the repo.

2. Find a good data source and get it into a form that works with your tool.

3. Understand the tool and its parameters well enough to generate some creative high-quality outputs. **It's okay to lightly edit the random outputs as part of the creative process**.

4. Publish the results of your work on [GitHub Pages](https://pages.github.com/). This is easy to do: create a new repo to host your work, adjust some settings, and GitHub will automatically host your repo as a web page. I'm asking you to do this so you can practice creating sites via GitHub, which can be a nice low-maintenance way to build a personal site or feature your projects.

Some ideas for data sources:

- Tweets of all kinds (but Trump is too easy)
- Project Gutenberg and Wikisource for historical texts and literature
- Wikipedia articles
- Media pieces about a topic, or written by a particular writer or group of writers
- Recipes
- Poetry
- Song lyrics (you know how much I love mashups)
- Academic articles (see, for example, the [snarXiv](http://snarxiv.org/))
