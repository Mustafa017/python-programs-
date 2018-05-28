# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:07:58 2017

@author: mustafa
"""
def soln(A):
    total = 0
    for i in range(len(A)):
       if len(str(abs(A[i])))==2:
            total += int(A[i])
    return total
    
print(soln([1,1000,80,-91]))
print(soln([47,1900,1,90,45]))
'''def soln(A):
    result = [sum(i) for i in range(len(A)) if len(str(abs(A[i])))==2]
    print(result)
'''
