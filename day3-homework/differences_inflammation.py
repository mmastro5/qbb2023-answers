#!/usr/bin/env python

# importing and reading the file
import sys
f = sys.argv[1]
data = open(f)

# Making a patient dictionary
patient_id = 0
inflammation_list = {}
for d in data:
	numbers = d.rstrip()
	numbers = numbers.split(",")
	line_list = []
	for n in numbers:
		line_list.append(float(n))
	patient = 'Patient' + str(patient_id)
	inflammation_list[patient] = line_list
	patient_id += 1
#print(inflammation_list)

# making a function to do the differences

def difference(a,b):
	dlist = []
	for fus in range(len(a)):
		d = a[fus] - b[fus]
		dlist.append(d)
	return dlist

# using our keys to find differences
print(difference(inflammation_list['Patient1'], inflammation_list['Patient4']))


