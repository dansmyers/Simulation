def calc_ev():
    p = 1/6 
    q = 1 - p
    highest = 3
    total_prob = 0
    i = 1
    for i in range(1, highest + 1):
        first = pow(p,i)
        second = pow(q, 3-i)
        num = first*second
        print(num)
        total_prob = total_prob + num
    return total_prob
    


prob = calc_ev()
number = 7
p_picked = 1/6
ev = 0
for x in range(1,number):
    ev = ev + p_picked*x*prob