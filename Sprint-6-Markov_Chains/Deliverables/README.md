# Sprint 6 Deliverables

<img src="https://imgs.xkcd.com/comics/twitter_bot_2x.png" width="75%" />

## Honor Code 
On my honor I have not given. recieved, nor witnessed any unauthorized assistance on this work. 

Mariah Haskell

## Description

This project will let you play around with Markov models that create randomized text outputs. We'll look at a few different techniques, then you'll be able to build your own
model.

Creating randomized text generators is a fun application of Markov chains. For example [this Reddit account](https://www.reddit.com/user/FloridaMan_SS/posts/), which creates 
random Florida Man posts using a Markov model created from the r/FloridaMan subreddit.

The model starts by picking a random starting word, then randomly choosing the next word, in such a way that words pairs occurring more
frequently in the source text are more likely to be chosen by the generator. This process then repeats, randomly choosing the next word
based on the current word.

If you'd like, you can think of it as writing using only the autocomplete feature of your phone.

In addition to the subreddit above, here are some other good examples:

- https://kingjamesprogramming.tumblr.com/

- The [snarXiv](http://snarxiv.org/) for randomized high-energy physics papers

- Lots and lots and lots of Twitter bot accounts.

Text generation is another area that has been affected by the introduction of deep-learning neural network models. The current top-of-the-pile is GPT-3, which came out in mid-2020. [It can be frighteningly good](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3).

## Make Randomized Text Great Again

Clone this public repo:

```
git clone https://github.com/rollinscs/cms380-f18-lab-2
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

For your main project, let's create some original predictive text.

I want you to do four things:

1. Write or find a good tool for text-generation. `markovify` and Botnik's predictive keyboards are options, but I encourage you to do a little bit of research before you commmit to a tool. If you want to experiment with writing your own code, I've included an example haiku-generation program in the repo.

2. Pick an interesting author. This could be a poet, fiction, or non-fiction writer. Choose someone with a unique style. If you want to choose a group of writer that are
closely related to each other, as a school or movement, then that's fine too.

3. Find a body of works by your author(s) and mash them up using the predictive text generation tool you chose in step (1). 

4. Curate your tool's output to produce interesting results. Obviously, coming up with ridiculous sentences is fun and not too hard. It's more difficult to find things that
cross the barrier from the absurd to the sublime, which is where you want to be. **It's okay to edit your randomized outputs as part of the creative process**.

What makes a good data source?

- Breaks nicely into medium-length chunks, like poems.

- Unique style or sense of phrasing. Again, poets are great for this.

- You don't have to use the entire body of works by an author. For example, picking all the works of Shakespeare might be too much, but you could work with the text of his sonnets.

- Song lyrics could be fun, but it needs to be from a writer with a large enough body of work and clear enough voice to create interesting results.
