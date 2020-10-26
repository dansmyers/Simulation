def calculate_one_die():
    sum_prob = 0;
    highest = 7;
    p = 1/6;
    i = 1;
 
    for i in range(1,highest):
        num = pow(p,i)* pow(1-p,6-i)
        sum_prob = sum_prob + num
        
    print(sum_prob)
    
    
def calculate_two_die():
    sum_prob = 0;
    highest = 13;
    p = 1/6;
    i = 2;
    for i in range(1,highest):
        num = pow(p,i)* pow(1-p,12-i) 
        sum_prob = sum_prob + num
        
    print(sum_prob)
    
def calculate_three_die():
    sum_prob = 0;
    highest = 19;
    p = 1/6;
    i = 3;
    for i in range(1,highest):
        num = pow(p,i)* pow(1-p,18-i)  
        sum_prob = sum_prob + num
        
    print(sum_prob)
    


calculate_one_die()
calculate_two_die()
calculate_three_die()

