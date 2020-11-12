import random
import math
import statistics
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    #
    # Look at the inverse CDF examples
    
    rand = random.uniform(0, 1)
    
    number = - math.log(rand)/mu
    
    return number

#--- Simulate the M/M/1 queue
#
# Inputs:
#    arrival_rate
#    avg_service_time
#    n: number of simulated customers
#
# Output: the average residence time of customer in the queue

def simulate(arrival_rate, avg_service_time, n):

    # Generate interarrival times
    # TODO: use rand_exp to generate n interarrival times with parameter arrival_rate
    interarrival_times = []
    
    for i in range(0, n):
    	interarrival_times.append(rand_exp(arrival_rate))
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    service_times = []
    
    for i in range(0, n):
    	service_times.append(rand_exp(avg_service_time))
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    
    arrival_times = []
    
    total = 0
    
    for i in range(0, n):
    	
    	total = total + interarrival_times[i]
    	arrival_times.append(total)
    	
    	# Initialize other lists
    	enter_service_times = [0] * n
    	departure_times = [0] * n
    	
    	# Setup for first arrival
    	enter_service_times[0] = arrival_times[0]
    	departure_times[0] = enter_service_times[0] + service_times[0]
    	
    # Loop over all other arrivals
    residence_times = [0]*n
    total_residence = 0
    
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        
        # TODO: calculate departure_times[i]
        departure_times[i] = enter_service_times[i] + service_times[i]
    # Calculate residence times
    # TODO: calculate list of residence times
        residence_times[i] = departure_times[i] - arrival_times[i]
        
        total_residence = total_residence + residence_times[i]
    
    # TODO: return average residence time
    average_residence = total_residence/len(residence_times)
    
    for i in range(0, n):
    	print("Person ", i, "\nArrival Time: ", arrival_times[i], "\nDeparture Time: ", departure_times[i], "\nResident Time: ", residence_times[i], "\n")
    
    return average_residence
    
averages = []

x_axis = []
for i in range(1,20):
	averages.append(simulate(i*.05, 1, 5000))
	x_axis.append(round(i*.05, 2))

for i in range(1,20):
	print("Average Residence Time for", round(i*.05, 2), ":", averages[i-1])
	

	
plt.plot(x_axis, averages)

plt.title('Average Residence Time for Different Utilizations')
plt.ylabel('Average Residence Time')
plt.xlabel('Utilization')

plt.savefig('mm1.pdf', bbox_inches= 'tight')

ci_averages = []
LDL = []
UDL = []
set_averages = []
stdev = []

for i in range(1,6):
	ci_averages.append([])
	for j in range(1, 20):
		ci_averages[i-1].append(simulate(j*.05, 1, 1000))
		
		
for j in range(0, 19):
	temp = []
	total = 0
	for i in range(0, 5):
		total = total + ci_averages[i][j]
		temp.append(ci_averages[i][j])
	set_averages.append(statistics.mean(temp));
	stdev.append(statistics.stdev(temp, set_averages[j]))
	
print(set_averages)
print(stdev)

for i in range(0, 19):
	LDL.append(set_averages[i] - 2.776 * (stdev[i] / math.sqrt(5)))
	UDL.append(set_averages[i] + 2.776 * (stdev[i] / math.sqrt(5)))
	
plt.plot(x_axis, averages)
plt.plot(x_axis, LDL)
plt.plot(x_axis, UDL)

plt.title('Average Residence Time for Different Utilizations')
plt.ylabel('Average Residence Time')
plt.xlabel('Utilization')

plt.savefig('mm1.pdf', bbox_inches= 'tight')
