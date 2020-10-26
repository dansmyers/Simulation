#random.randint -- generate random integers in a range 
from random import randint
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
money = 255 



def oneRound(bet):
    global money
    won = True
    
    rand_num = randint(1,38)
    if rand_num <= 18:
        money = money + bet
    else:
        money = money - bet
        won = False
    return won


def plot(data):
    #create a new figure, always do before calling plotting function
    plt.figure()

    #plot the histogram onto the figure, 15 bins 
    plt.hist(data, 50)

    #Set title and axis labels
    plt.title("Histogram of Outcome of Martingale strategy")
    plt.xlabel("Money Left")
    plt.ylabel("count")

    #save figure to a filter
    plt.savefig("Martingale_hist.pdf", bbox_inches='tight')


def main():
    data = []
    global money
    
    for j in range(1000):
        bet = 1
        games_played = 0
        while money > bet and games_played < 100:
            outcome = oneRound(bet)
            if outcome == True:
                bet = 1
            else:
                bet = bet * 2
        
        
            games_played+=1
    
        data.append(money)
        money = 255
    plot(data)
    
    
    
if __name__ == '__main__':
    main()
  