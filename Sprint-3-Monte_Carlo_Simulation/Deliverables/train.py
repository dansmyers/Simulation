#random.randint -- generate random integers in a range 
from random import randint

nums = []

def simulate(num):
    found = False
    
    #See if our number seat number is not taken 
    #If it is open, take it and remove from avaliable list
    for j in range(len(nums) - 1):
        if nums[j] == num:
            nums.remove(num)
            found = True
    #If it is taken, take another random seat and remove from
    #available list
    if found == False:
        rand_num = randint(0,len(nums) - 1)
        nums.pop(rand_num)




def sims():
    max_trials = 1000
    count_hundred = 0
    
    for trials in range(max_trials):
    
        for i in range(1,101):
            nums.append(i)
        
        #have passenger 1 take a random seat
        nums.pop(randint(0,99))
    
        #simulate first 99 passengers, then see what number is left
        for k in range(1,99):
            simulate(k)
        if nums[0] == 100:
            count_hundred+=1
        
        #remove last number so we can repopulate nums
        nums.pop(0)
    return count_hundred

def main():
    data =[]
    for i in range(100):
       data.append(sims())
    
    prob_dist = sum(data)/len(data) *.001
    
    print("Probability = ", prob_dist)
    
    
#Write some code that will call main when this program runs 

if __name__ == '__main__':
    main()