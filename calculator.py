# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:23:12 2017

@author: mustafa
"""

class Calculator:
    def power(self,n,p):
        if n < 0 or p<0:
            raise Exception('n and p should not be negative')
        else:
            return n**p
myCalculator = Calculator()
T = int(input()) 
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans = myCalculator.power(n,p)
        print (ans)
    except Exception as e:
        print (e)