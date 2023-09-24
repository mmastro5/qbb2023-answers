#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#_______________________________________________#
#												#
#    			Exercise 1 						#
# _____________________________________________ #

def simulation_coverage(coverage, genome_len, read_len, figname):

	#Creating the simulation
	coverage_arr = np.zeros(genome_len)
	num_reads = int(coverage * genome_len / read_len)

	low = 0 
	high = genome_len - read_len
	start_position = np.random.randint(low = low, high = high + 1, size = num_reads) # high value is exclusive

	for start in start_position:
		coverage_arr[start: start + read_len] += 1

	#looking at the coverage of the genome (answer 1.3)
	x = np.arange(0, max(coverage_arr)+1)

	sim_zcov = genome_len - np.count_nonzero(coverage_arr)
	sim_zcov_percent = 100 * sim_zcov / genome_len
	print(f'In the simlation there are {sim_zcov} with 0 coverage')
	print(f'This is {sim_zcov_percent}% of the genome')

	#creating curve overlays for the graph
	#Get Poisson distribution
	y_poisson = stats.poisson.pmf(x, mu = coverage) * genome_len
	#Get Normal distribution
	y_normal = stats.norm.pdf(x, loc = coverage, scale = np.sqrt(coverage)) * genome_len

	#Plot the simulation in a histogram w/ curve overlays
	fig, ax = plt.subplots()
	ax.hist(coverage_arr, bins=x, label = 'Simulation', color = "pink")
	ax.plot(x, y_poisson, label = "Poisson", color = "black")
	ax.plot(x, y_normal, label = "Normal")
	ax.legend()
	ax.set_xlabel('Coverage')
	ax.set_ylabel('Frequency (bp)')
	fig.tight_layout()
	fig.show()
	fig.savefig(figname)

#Run three conditions
simulation_coverage(3, 1_000_000, 100, 'ex1_3x_cov.png')
simulation_coverage(10, 1_000_000, 100, 'ex1_10x_cov.png')
simulation_coverage(30, 1_000_000, 100, 'ex1_30x_cov.png')


#_______________________________________________#
#												#
#    			Exercise 2						#
# _____________________________________________ #



reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

graph = set()

k = 3

for x in reads:
  for i in range(len(x) - k):
    kmer1 = x[i: i+k]
    kmer2 = x[i+1: i+1+k]
    graph.add(f'{kmer1} -> {kmer2}')

print(graph)

# creating dot 
f = open("edges.txt", "w")
f.write("digraph {")
for edge in graph:
   f.write(edge + "\n")
f.write('}')














