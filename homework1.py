#!/usr/bin/env python

#importing essential libraries
import numpy

#opening file
file = open("inflammation-01.csv", "r")
lines = file.readlines()



# exercise 1

#extracting patient five and making them a list
patient5 = lines[4]
patient5 = patient5.rstrip("/n")
patieint5_list = patient5.split(",")

#printing that list
print("exercise 1: ")
print(patieint5_list[0])
print(patieint5_list[9])
print(patieint5_list[-1])


# exercise 2
print("exercise 2: ")
## extracting first ten patients and making them integers
patient_list = []
patient_list_avg = []
for j in range(0,10):
	patient = lines[j]
	patient = patient.rstrip("/n")
	patient_list = patient.split(",")
	integer_list = []
	for i in patient_list:
		integer_list.append(int(i))
	patient_list_avg.append(numpy.mean(integer_list))

print(patient_list_avg)


# exercise 3
print("exercise3")

## creating each day into a list to extract max and min of each
day_list = []
day_list_max = []
day_list_min = []
for line in lines:
	day = line.rstrip()
	day_list = day.split(",")
	integer_list = []
	for i in day_list:
		integer_list.append(int(i))
	day_list_max.append(numpy.max(integer_list))
	day_list_min.append(numpy.min(integer_list))

print(day_list_min)
print(day_list_max)

# exercise 4
print("exercise 4:")

## finding the number of flare ups each patient had
patient1 = lines[0]
patient1 = patient1.rstrip("/n")
patient1_list = patient1.split(",")

patient5 = lines[4]
patient5 = patient5.rstrip("/n")
patient5_list = patient5.split(",")

#difference in total number of flare ups of the patients
difference = len(patient1_list) - len(patient5_list)


print(difference)









