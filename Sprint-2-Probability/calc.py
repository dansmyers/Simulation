def p_dif_bday(denominator, num_s):
    
    p = 1
    for i in range (0,num_s):
        numerator = denominator - i;
        p = p * (numerator/denominator)
        
    return p
    
prob = p_dif_bday(365,40)
print(prob)