#random.randint -- generate random integers in a range 
import random


import matplotlib
matplotlib.use('Agg')
#needed to access in remote environment like mimir

from matplotlib import pyplot as plt
#plt is alias, we renamed and can run them as such

def simulate():
    """
    simulate one round of passe findIdx
    no inputs 
    output is true or false 
    """
    
    count = 0;
    
    for i in range(1000):
        num = random.uniform(0,1)
        if num <= .025:
            count+=1
        
    return count
    

    

def main():
    """
    call simulate a large # of times and return 
    fraction of successes
    """
    
    #make a data structure to hold 1000 outcomes
    data = []
    max_trials = 1000
    num_successes = 0
    
    for trial in range(max_trials):
        data.append(simulate())
     
    
    #create a new figure, always do before calling plotting function
    plt.figure()

    #plot the histogram onto the figure, 15 bins 
    plt.hist(data, 25)

    #Set title and axis labels
    plt.title("Histogram of coin flip # of heads")
    plt.xlabel("Number of Heads")
    plt.ylabel("count")

    #save figure to a filter
    plt.savefig("count_hist.pdf", bbox_inches='tight')

#Write some code that will call main when this program runs 

if __name__ == '__main__':
    main()