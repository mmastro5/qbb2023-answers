#!/usr/bin/env pythonmv

my_list = [5, 45, 67, 92, 134]
def mean(var_list):
	total = sum(var_list)
	amount = len(var_list)
	answer = total/amount
	return answer

print(mean(my_list))


