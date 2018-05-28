# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 09:22:52 2017

@author: mustafa
"""

def find_max_min(n):
    for i in range(len(n)):
        if not isinstance(n,list):
            raise ValueError("Input should be a list")
        else:
            result = []
            if n[i] == n[i+1]:
                return [n[i]]*len(n)
            else:
                smallest = min(n)
                largest = max(n)
                result.extend([smallest, largest])
                return result
print(find_max_min([3,3,3,3]))
 
def find_max_min(n):
    for i in range(len(n)):
        if not isinstance(n,list):
            raise ValueError("Input should be a list")
        else:
            result = []
            smallest = min(n)
            largest = max(n)

            if smallest == largest:
                result.append(n[i])
                return result
            else:
                result.extend([smallest, largest])
                return result
print(find_max_min([3,3,3,3]))


print(list(reversed([2, 4, 6, 8, 10])))

