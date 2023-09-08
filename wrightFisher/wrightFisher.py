#!/usr/bin/env python

# get a starting frequency and a population size 
# 	parameters for the function

# create a function to step through each generation

# make a list to store our allele frequncies 

# while loop
# while our loop allele frequency is between 0 and 1:
# 	draw a new allele frequency for next generation
#	by drawing from the binomial distribution 
# 	convert number of successes into a frequency

# Store our allele frequency into allele frequency list




# return  a list of the allele frequeny at each time point
# number of generations of fixation is the length of your list

#exercise 1:
import numpy as np 
import matplotlib.pyplot as plt

frequency = 0.5
popsize = 1000

def wfmodel(pop, afreq):
	freq_list = []
	while afreq  < 1 and afreq > 0:
		success = np.random.binomial(2*pop, afreq)
		afreq = success / (2*pop)
		freq_list.append(afreq)
	return freq_list

# print(wfmodel(popsize, frequency))

#exercise 2: 
gen_num = []
for i in range(1000):
	my_output = wfmodel(popsize, frequency)
	gen_num.append(len(my_output))


fig, ax, ax1, ax2 = plt.subplots()

#ax.hist(gen_num)
# plt.show()

#exercise 3:

# pick 5 population sizes of at least 50
pop_sizes = [75, 500, 10000, 32500, 50000]

# for each pop size run the model 50 times
avgs = []
gen_num = []
for i in range(len(pop_sizes)):
	for outs in range(50):
		my_output = wfmodel(pop_sizes[i], frequency) # allele frequency is still 0.5
		gen_num.append(len(my_output))
	avgs.append(np.mean(gen_num))

# create a scatter polt
#	x = pop size , y = average time to fixation
ax1.scatter(pop_sizes, avgs, c = "black")
ax1.set_xlabel("Population Size")
ax1.set_ylabel("Average Generation Time to Fixation")
ax1.set_title("Multiple Population Size Model")
plt.show()

# pick 5 different allele frequencies
allele_freqs = [0.1, 0.27, 0.5, 0. 78, 0.9]


alavgs = []
gen_num2 = []
for i in range(len(allele_freqs)):
	for outs in range(10):
		my_output = wfmodel(pop_sizes[i], frequency) # allele frequency is still 0.5
		gen_num2.append(len(my_output))
	alavgs.append(np.mean(gen_num2))


fig2, ax2 = plt.subplots()
ax2.scatter(allele_freqs, alavgs, c = "black")
ax2.set_xlabel("Allele Frequencies")
ax2.set_ylabel("Average Generation Time to Fixation")
ax2.set_title("Multiple Allele Frequency Model")
plt.show()


