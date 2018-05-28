# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:44:05 2017

@author: mustafa
"""

def manipulate_data(data):
    if isinstance(data, list):
      return [len([n for n in data if isinstance(n, int) and n >= 0]), sum(n for n in data if isinstance(n, int) and n < 0)]
    else:
      return 'Only lists allowed'
      
print(manipulate_data([1,2,-3,-4,-5]))