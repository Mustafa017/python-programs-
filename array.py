# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:30:30 2017

@author: mustafa
"""
#output is a reversed comma separated list
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print (arr[::-1])

#output is reversed space separated integers
for i in range(n//2):
    temp = arr[i]
    arr[i] = arr[-1-i]
    arr[-1-i] = temp
    
result = ""
for i in arr:
    result = result + str(i) + " "

print(result)