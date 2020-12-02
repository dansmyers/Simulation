'''
Ryan King
Sprint 5 Deliverable

Run a discrete event simulation with a priority queue and a regular queue

Program will run 100 simulations of 10000 customers and f values .00 to .99 respectively. It will then
plot the average residence of priority customers, regular customers, and overall. The utilization
of the system can be changed on line 144 arg 2.

'''

from heapq import heappush, heappop
import random
import math

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def rand_exp(mu):
	
	rand = random.uniform(0, 1)
	
	number = - math.log(rand)/mu
	
	return number
	
def create_event(event_type, mu, time):
	e = (rand_exp(mu) + time, event_type)
	return e

def priority(f):
	rand = random.uniform(0, 1)
	if rand < f:
		return True
	else:
		return False


def simulate(f, arrival_rate, service_time, num_of_customers):
	
	fp_arrivals = []
	reg_arrivals = []
	
	fp_est = []
	reg_est = []
	
	fp_departures = []
	reg_departures = []
	
	num_in_fp = 0
	num_total = 0
	
	events = []
	
	time = 0
	
	heappush(events, create_event('a', arrival_rate, time))
	
	while len(events) != 0:
		
		
		event = heappop(events)
		time = event[0]
		
		if event[1] == 'a':
			
			#Arrival has f probability of having fastpass
			if priority(f):
				num_in_fp = num_in_fp + 1
				fp_arrivals.append(time)
			else:
				reg_arrivals.append(time)
			num_total = num_total + 1
				
			#If no one is in line, this person can enter service immediately and be given a deprture time
			if num_total == 1:
				heappush(events, create_event('d', service_time, time))
				if num_in_fp > 0:
					fp_est.append(time)
				else:
					reg_est.append(time)
					
			#If there is another person left in the simulation, give them an arrival time
			if num_of_customers > 0:
				heappush(events, create_event('a', arrival_rate, time))
				
				num_of_customers = num_of_customers - 1
		
		elif event[1] == 'd':
			
			#The element in service departs
			if num_in_fp > 0:
				fp_departures.append(time)
				num_in_fp = num_in_fp - 1
			else:
				reg_departures.append(time)
			num_total = num_total - 1
			
			#If anyone else is in line they enter servce, and are given a departure time
			if num_in_fp > 0:
				fp_est.append(time)
				heappush(events, create_event('d', service_time, time))
			elif num_total > 0:
				reg_est.append(time)
				heappush(events, create_event('d', service_time, time))
				
	total_res_time_fp = 0
	total_res_time_reg = 0
	#Print results to terminal
	for i in range(len(fp_arrivals)-1):
	#	print("Fastpass Customer " + str(i))
	#	print("Residence time: " + str(fp_departures[i]-fp_arrivals[i]) + "\n")
		total_res_time_fp = total_res_time_fp + (fp_departures[i]-fp_arrivals[i])
		
	for i in range(len(reg_arrivals)-1):
	#	print("Regular Customer " + str(i))
	#	print("Residence time: " + str(reg_departures[i]-reg_arrivals[i]) + "\n")
		total_res_time_reg = total_res_time_reg + (reg_departures[i]-reg_arrivals[i])
	
	if len(fp_arrivals) > 0:
		average_res_time_fp = total_res_time_fp/len(fp_arrivals)
	#	print("Average Fastpass Residence Time: " + str(average_res_time_fp))
	else:
		average_res_time_fp = 0;
	average_res_time_reg = total_res_time_reg/len(reg_arrivals)
	#print("Average Regular Residence Time: " + str(average_res_time_reg))
	
	average_res_time = (total_res_time_reg + total_res_time_fp)/(len(fp_arrivals) + len(reg_arrivals))
	#print("Average Resident Time: " + str(average_res_time))
	
	return (average_res_time, average_res_time_fp, average_res_time_reg, average_res_time_fp/average_res_time_reg)
	


res_time_averages = []
res_time_averages_fp = []
res_time_averages_reg = []
res_time_ratio = []
x_axis = []

for i in range(0, 100):
	temp = simulate(.01*i , .5, 1, 50000)
	
	res_time_averages.append(temp[0])
	res_time_averages_fp.append(temp[1])
	res_time_averages_reg.append(temp[2])
	res_time_ratio.append(temp[3])
	
	x_axis.append(i*.01)

plt.plot(x_axis, res_time_averages)
plt.legend("O")

plt.plot(x_axis, res_time_averages_fp)
plt.legend("F")

plt.plot(x_axis, res_time_averages_reg)
plt.legend("R")


plt.title('Average Residence Time for Different F values')
plt.ylabel('Avg Residence Time')
plt.xlabel('F Value')

plt.savefig('5.pdf', bbox_inches= 'tight')

for i in range(0, 100):
	print(round(i*.01, 2),  "Fastpass average: ",  round(res_time_averages_fp[i], 4), "Regular average: ", round(res_time_averages_reg[i], 4))
	






