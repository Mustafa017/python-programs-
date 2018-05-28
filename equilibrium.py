# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:04:45 2017

@author: mustafa
"""

def equilibriums(A):               # line 1
    result = []                    # line 2
    difference = sum(A)            # line 3

    for p in range(len(A)):        # line 4

        difference -= 2*A[p]       # line 5

        if -A[p] == sum_of_tail:   # line 6
            result.append(p)       # line 7

    return result        
    
def equi(v):
    left_side = 0       
    right_side = sum(v)

    for i in range(len(v)):
        right_side -= v[i]
        if left_side == right_side:
            return i   
        left_side += v[i]
    return -1 
    
def equi(A):
    result = []
    x=1
    i=1
    r=sum(A)
    for e in A:
        i-=1
        r-=2*e
        if -e==r:
            result.append(-i)
    return result
    
print(equi([-1,3,-4,5,1,-6,2,1]))
#print(equilibriums([1,2,3,0,1,0,0,0,0,1,6]))  
print(equi([-1,3,-4,5,1,-6,2,1]))
