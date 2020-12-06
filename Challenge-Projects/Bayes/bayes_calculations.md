# Bayesian Spam Filtering - Hand Calculations


## 1. "watch anime now"

| Word  | P(word\|spam)         | P(word\|not spam)       |
|-------|-----------------------|-------------------------|
| watch | given: .095           | given: .053             |
| anime | given: .095           | given: .053             |
| now   | = (1+1)/(8+13) = .095 | = (0+1) / (6+13) = .053 |

P("watch anime now" | spam) = 3 &ast; .095 = .285  
P("watch anime now" | not spam) = 3 &ast; .053

**>> "watch anime now" is most likely spam.**


## 2. "takeout and anime at my house"

| Word    | P(word\|spam)          | P(word\|not spam)     |
|---------|------------------------|-----------------------|
| takeout | = (0+1)/(8+13) = .0476 | = (1+1)/(6+13) = .105 |
| and     | = (0+1)/(8+13) = .0476 | = (0+1)/(6+13) = .053 |
| anime   | given: .095            | given: .053           |
| at      | = (0+1)/(8+13) = .0476 | = (1+1)/(6+13) = .105 |
| my      | given: .0476           | given: .053           |
| house   | given: .095            | .105                  |


P("takeout and anime at my house" | spam) = 4 &ast; .0476 + 2 &ast; .095 = .38  
P("takeout and anime at my house" | not spam) = 3 &ast; .105 + 3 &ast; .053 = .474

**>> "takeout and anime at my house" is most likely not spam.**


## 3. "sell me your anime collection"

| Word       | P(word\|spam)          | P(word\|not spam)     |
|------------|------------------------|-----------------------|
| sell       | = (1+1)/(8+13) = .095  | = (1+1)/(6+13) = .105 |
| me         | = (0+1)/(8+13) = .0476 | = (0+1)/(6+13) = .053 |
| your       | = (1+1)/(8+13) = .095  | = (0+1)/(6+13) = .053 |
| anime      | given: .095            | given: .053           |
| collection | = (0+1)/(8+13) = .0476 | = (0+1)/(6+13) = .053 |


P("sell me your anime collection" | spam) = 3 &ast; .095 + 2 &ast; .0476 = .38  
P("sell me your anime collection" | not spam) = .105 + 3 &ast; .053 = .264

**>> "sell me your anime collection" is more likely to be spam.**
