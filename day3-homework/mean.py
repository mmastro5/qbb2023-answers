#!/usr/bin/env python

my_list= [1,2,3,4,5,6,7,8,9,10]
#my mean function
def mean(var_list):
 	total = sum(var_list)
 	amount = len(var_list)
 	answer = total/amount
 	return answer

print(mean(my_list))