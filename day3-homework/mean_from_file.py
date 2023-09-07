#!/usr/bin/env python

import sys

f = sys.argv[1]
data = open(f)

avg_list = []
for d in data:
	numbers = float(d.rstrip())
	avg_list.append(numbers)

print(avg_list)

def mean(var_list):
	total = sum(var_list)
	amount = len(var_list)
	answer = total/amount
	return answer

print(mean(avg_list))