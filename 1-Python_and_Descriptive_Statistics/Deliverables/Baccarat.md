# Baccarat

<img src="https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iyOGRok9ziCM/v1/1000x-1.jpg" width="50%" />

## Overview

> “The two cards slithered towards him across the green sea. Like an octopus under a rock, Le Chiffre watched him from the other side of the table. Bond reached out a steady right hand and drew the cards towards him. Would it be the lift of the heart which a nine brings, or an eight brings? He fanned the two cards under the curtain of his hand. The muscles of his jaw rippled as he clenched his teeth. His whole body stiffened in a reflex of self-defence. He had two queens, two red queens. They looked roguishly back at him from the shadows. They were the worst. They were nothing. Zero. Baccarat. ‘A card,’ said Bond fighting to keep hopelessness out of his voice. He felt Le Chiffre’s eyes boring into his brain.”
>
> Ian Fleming - *Casino Royale*

*Casino Royale* is the first James Bond novel, published in 1953. In it, Bond travels to a French casino with the goal of challenging and bankrupting Le Chiffre ("The Number"), 
an agent of the Soviets. Bond's game of choice, which occurs repeatedly throughout the early Ian Fleming novels, is **baccarat**.

In real-world casinos, baccarat carries an image of exclusion and luxury. It's traditionally played in special roped off areas with very 
high bets, although many casinos now offer "Mini-Bac", which uses the same rules as the high-end game, but at smaller tables on the main casino floor and with more 
reasonable bets. Despite its reputation as the province of high-rollers, baccarat is purely a game of chance: there is no strategy involved. Interestingly, it features some of 
the lowest house edges available at any casino game without resorting to special strategies like card counting in blackjack.

In this project, you'll write a Monte Carlo simulator for baccarat and estimate the expected winning probability for the two main bets.

## Rules

Almost all baccarat games available at real casinos are "punto banco" baccarat, which requires no strategic decisions on the part of the player. James Bond's preferred 
version is an older game called "chemin de fer" (French for "railway"), which did allow a player decision in certain situations. Other than its association with Bond, 
chemin de fer has died out in the real world. According to Wikipedia, more than 90% of revenue at Macau's casinos in 2014 came from punto banco baccarat.

### Hands and Card Values

The game is led by a dealer, who handles all the cards according to a fixed set of rules called the *tableau* ("table").

A round begins with the dealer dealing out two hands of two cards each, which are called the "Player" and the "Banker". The names are just traditional: all of the card handling and decision making is done by the dealer according to the tableau. Gamblers may bet for either hand to win and the two bets have different odds.

Every card has a point value:

- Number cards 2 through 9 are worth their face value.
- 10s and face cards are worth **zero points**.
- Aces are worth one point.

Here's one of the appealingly weird things about baccarat: the value of a hand is the sum of its card values **modulo 10**.

For example, if the player hand is `Jack & 5`, it has a point value of 5: the Jack counts for zero and the 5 counts for face value. If the Banker hand is `7 & 6`, it has a point value of 3, calculated as `(7 + 6) % 10`.

### The Tableau

<img src="https://www.pagat.com/images/banking/baccarat2.png" width="50%" />

Play proceeds as follows:

1. The dealer deals the two hands of two cards and announces their values using the rules above.

2. If a hand achieves an 8 or 9, it is declared a "natural" and the round ends immediately. The hand with the higher natural wins, or it's a tie if both hands have achieved equal naturals.

3. If neither hand achieves a natural, then the tableau of drawing rules is consulted, first for the player, then the banker.

4. If the player hand has a point value of 0-5, the dealer will give a third card to to the player hand. The player hand always stands on a 6 or 7.

5. The rules for the banker are more complex. If the player stood with two cards, the banker follows the same rules as the player: hit on 0-5 and stand on 6-7.  If the player did take a third card, the banker acts [according to the following tableau](https://en.wikipedia.org/wiki/Baccarat_(card_game)#Tableau_of_drawing_rules):

    - If the banker total is 2 or less, then the banker draws a card, regardless of what the player's third card is.
    - If the banker total is 3, then the banker draws a third card unless the player's third card was an 8.
    - If the banker total is 4, then the banker draws a third card if the player's third card was 2, 3, 4, 5, 6, 7.
    - If the banker total is 5, then the banker draws a third card if the player's third card was 4, 5, 6, or 7.
    - If the banker total is 6, then the banker draws a third card if the player's third card was a 6 or 7.
    - If the banker total is 7, then the banker stands.

6. After both hands have been evaluated, the dealer announces the resulting point values and declares the winner.

    - The bet for the player hand to win pays even money.
    - The bet for the banker hand to win pays 19/20 (equivalent to even money with a 5% commission).
    - If the outcome is a tie, then both the player and banker bets push, with no loss for the gambler.
    - There is also a bet for both hands to tie, but it has terrible odds.

It turns out that the player hand has a house edge of only 1.24%. The banker bet is lower at 1.06%, even after taking into account that it pays less than even money.
These numbers are comparable to playing blackjack with optimal strategy and not counting cards. The tie bet is terrible: the house edge is more than 14%.

## Simulate It!

Your goal for this project is to write a simulator that can estimate the probability of winning for the player and banker bets.

You'll need to write a `simulate` function that can execute one round of the game: dealing the cards, calculating hand values, applying the tableau rules, and then deciding
the winner. Report whether the result was a win for the player, the banker, or a tie. Run a large number of simulations, then report the fraction of wins for each hand.

Once you have the fraction of wins, you can work out the actual house edge by taking into account the payouts for each bet.

## Tips

- Take a look at [this article from the Wizard of Odds](https://wizardofodds.com/games/baccarat/basics/#toc-Rules) if you'd like to review another presentation of
the rules.

- This project is not conceptually harder than our other gambling simulations, but the rules of the game are more complex. Test your method thoroughly to make sure it's
doing what you want before you try running a long simulation.

- You have to decide how you want to handle dealing. The casino game is traditonally played with a shoe of eight decks shuffled together; the dealer reshuffles a new shoe when
the current one is almost empty. Modeling the composition of the real decks affects the probabilities, because cards that have been dealt out 
can't be used again until the decks are reshuffled. Think about the best way to represent how the cards are dealt. The easiest choice is to just generate the
cards randomly, but this will not give you the same results as a real game.
