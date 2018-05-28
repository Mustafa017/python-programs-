# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:44:05 2017

@author: mustafa
"""

def replicate_iter(times, data):
    if((not isinstance(times, int)) and (not isinstance(data, (int, float, complex, str)))):
            raise ValueError("Invalid arguments")
    elif(times <= 0):
            return []
    else:
            array = []
            for x in range(times):
                    array.append(data)
            return array

def replicate_recur(times, data):
    if((not isinstance(times, int)) and (not isinstance(data, (int, float, complex, str)))):
            raise ValueError("Invalid arguments")
    elif(times <= 0):
            return []
    else:
            return ([data] + replicate_recur((times - 1), data))

print(replicate_iter(3, 5))
print(replicate_recur(4, 2))

def power(a,b):
  if a == 0 & b== 0:
    return 0
  elif a>1 & b==0:
    return 1
  else:
    return eval(((str(a)+"*")*b)[:-1])
print(power(2,3))
