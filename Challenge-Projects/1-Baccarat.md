# Challenge Project &ndash; Baccarat

<img src="https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iyOGRok9ziCM/v1/1000x-1.jpg" width="50%" />

## Overview

> “The two cards slithered towards him across the green sea. Like an octopus under a rock, Le Chiffre watched him from the other side of the table. Bond reached out a steady right hand and drew the cards towards him. Would it be the lift of the heart which a nine brings, or an eight brings? He fanned the two cards under the curtain of his hand. The muscles of his jaw rippled as he clenched his teeth. His whole body stiffened in a reflex of self-defence. He had two queens, two red queens. They looked roguishly back at him from the shadows. They were the worst. They were nothing. Zero. Baccarat. ‘A card,’ said Bond fighting to keep hopelessness out of his voice. He felt Le Chiffre’s eyes boring into his brain.”
>
> - Ian Fleming - *Casino Royale*

*Casino Royale* is the first James Bond novel, published in 1953. In it, Bond travels to a French casino with the goal of challenging and bankrupting Le Chiffre ("The Number"), 
an agent of the Soviets. Bond's game of choice, which occurs repeatedly throughout the early Ian Fleming novels, is **baccarat**.

In real-world casinos, baccarat carries an image of exclusion and luxury. It's traditionally played in special roped off areas with very 
high minimum bets, although many casinos now offer "Mini-Bac", which uses the same rules as the high-end game, but at smaller tables on the main casino floor and with more 
reasonable bets.

Despite its reputation as the province of high-rollers, baccarat is purely a game of chance: there is no strategy involved. Interestingly, it features some of the lowest house 
edges available at any casino game without resorting to special strategies like card counting in blackjack.

In this project, you'll write a Monte Carlo simulator for baccarat and calculate the player's expected winning probability for the two main bets.

## Rules

Almost all baccarat games available at real casinos "punto banco" baccarat, which requires no strategic decisions on the part of the player. James Bond's preferred version is an
older game called "chemin de fer" (French for "railway"), which did allow a player decision in certain situations. Other than its association with Bond, chemin de fer has
died out in the real world. According to Wikipedia, more than 90% of revenue at Macau's casinos in 2014 came from punto banco baccarat.

### Hands and Card Values

The game is led by a dealer, who handles all the cards according to a fixed set of rules called the *tableau* ("table").

A round begins with the dealer dealing out two hands of two cards each, which are called the "Player" and the "Banker". The names are traditional: all of the card handling
and decision making is done by the dealer, and the "Player" hand is not managed or associated with any of the gamblers placing wagers. 
Gamblers may make one of two basic bets: for the "Player" hand to win, or for the "Banker" hand to win.

Every card has a point value:

- Number cards 2 through 9 are worth their face value.
- 10s and face cards are worth **zero points**.
- Aces are worth one point.
- The value of a hand is the sum of its card values **modulo 10**.

For example,

If the player hand is `Jack & 5`, it has a point value of 5: the Jack counts for zero and the 5 counts for face value. If the Banker hand is `7 & 6`, it has a point value
of 3: calculated as `(7 + 6) % 10`.

### The Tableau

Play proceeds as follows:

1. The dealer deals the two hands of two cards and announces their values using the rules above.

2. If a hand achieves an 8 or 9, it is declared a "natural" and the round ends immediately. The hand with the natural wins, or it's a tie if both hands have achieved naturals.

3. If neither hand achieves a natural, then the tableau of drawing rules is consulted, first for the player, then the banker.

4. If the player hand has a point value of 0-5, the dealer will give a third card to to the player hand. The player hand stands on a 6 or 7.

5. The rules for the banker are more complex. If the player stood with two cards, the banker follows the same rules as the player: hit on 0-5 and stand on 6-7.  
  If the player did take a third card, the banker acts according to the following tableau:

  - If the banker total is 2 or less, then the banker draws a card, regardless of what the player's third card is.
  - If the banker total is 3, then the banker draws a third card unless the player's third card was an 8.
  - If the banker total is 4, then the banker draws a third card if the player's third card was 2, 3, 4, 5, 6, 7.
  - If the banker total is 5, then the banker draws a third card if the player's third card was 4, 5, 6, or 7.
  - If the banker total is 6, then the banker draws a third card if the player's third card was a 6 or 7.
  - If the banker total is 7, then the banker stands.










