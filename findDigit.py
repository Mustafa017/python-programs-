# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:09:00 2017

@author: mustafa
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = [int(i) for i in input().strip()]
    if n%arr[i] == 0:
        print(arr,end='')
                