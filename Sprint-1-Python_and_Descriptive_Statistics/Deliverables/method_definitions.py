"""
Calculate and return the mean of input list x
"""
def calc_mean(x):
    number_of_values = len(x)
    values_sum = 0
    
    for num in x:
        values_sum += num
    
    mean = values_sum / number_of_values
    
    return  mean
"""
Calculate and return the median of input list x 
"""    
def calc_median(x):
    number_of_values = len(x)
    sorted_list = sorted(x)
    middle = (number_of_values - 1) // 2
    
    if number_of_values % 2 == 1:
        return sorted_list[middle]
    else:
        return (sorted_list[middle] + sorted_list[middle + 1]) / 2

"""
Calculate and return the variance of input list x 
"""        
def calc_variance(x):
    number_of_values  = len(x)
    mean = calc_mean(x)
    value_sum = 0
    
    for num in x:
        value_sum += pow((num - mean), 2)
        
    return value_sum/number_of_values
    
"""
Calculate and return the standard deviation of input list x 
"""
def calc_standard_deviation(x):
    variance = calc_variance(x)
    
    return math.sqrt(variance)