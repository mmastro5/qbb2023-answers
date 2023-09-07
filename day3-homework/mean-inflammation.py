#!/usr/bin/env pythonmv

# importing and reading the file
import sys
f = sys.argv[1]
data = open(f)

patient_id = 1
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
print(inflammation_list)

#my mean function
def mean(var_list):
 	total = sum(var_list)
 	amount = len(var_list)
 	answer = total/amount
 	return answer

for key, values in inflammation_list.items():
	print(key, mean(values))




