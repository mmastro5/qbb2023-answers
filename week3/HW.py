#!/usr/bin/env python

import numpy as np
import sys
from fasta import readFASTA
import pandas as pd

# bringing in sequences and penalties for DNA
input_sequences = readFASTA(open(sys.argv[1]))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

DNA_penalties = pd.read_csv(sys.argv[2], delim_whitespace = True)
gap_penalty = int(sys.argv[3])



#initializing matricies
f_matrix = np.zeros((len(sequence1) + 1, len(sequence2) + 1))
trace_matrix = np.zeros((len(sequence1) + 1, len(sequence2) + 1), str)

# inital rows/columns
for i in range(len(sequence1) + 1):
	f_matrix[i,0] = gap_penalty * i 
for j in range(len(sequence2)+1):
	f_matrix[0, j] = gap_penalty * j 
for i in range(len(sequence1) + 1):
	trace_matrix[i,0] = "V"
for j in range(len(sequence2)+1):
	trace_matrix[0, j] = "H"

#populating matricies
for i in range(1, f_matrix.shape[0]): 
	for j in range(1, f_matrix.shape[1]): 
		d = d = f_matrix[i - 1, j - 1] + DNA_penalties.loc[sequence1[i-1], sequence2[j-1]]
		h = f_matrix[i, j - 1] + gap_penalty 
		v = f_matrix[i - 1, j] + gap_penalty 
		f_matrix[i,j] = max(d,h,v)

		if f_matrix[i,j] == d:
			trace_matrix[i,j] = 'D'
		elif f_matrix[i,j] == h:
			trace_matrix[i,j] = 'H'
		else:
			trace_matrix[i,j] = 'V'


#finding the optimal alignment
s1 = ""
s2 = ""
gaps_in_s1 = 0
gaps_in_s2 = 0
i = len(sequence1)
j = len(sequence2)


while i != 0 or j != 0:
	if trace_matrix[i,j] == 'D':
		s1 = sequence1[i-1] + s1
		s2 = sequence2[j-1] + s2
		i -= 1
		j -= 1
	elif trace_matrix[i,j] == 'H':
		s1 = "-" + s1
		s2 = sequence2[j-1] + s2
		i = i
		j -= 1
		gaps_in_s1 += 1
	else:
		s1 = sequence1[i-1] + s1
		s2 = "-" + s2
		i -= 1
		j = j
		gaps_in_s2 += 1


f = open('alignment.txt', "w")
f.write("Sequence 1: " + s1 + '\n' + "Sequence 2: " + s2)
f.close()

print("alignment score: ", f_matrix[f_matrix.shape[0]-1, f_matrix.shape[1]-1])
print("number of gaps in sequence 1: ", gaps_in_s1)
print("number of gaps in sequence 2: ", gaps_in_s2)






