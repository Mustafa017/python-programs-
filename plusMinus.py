# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:46:07 2017

@author: mustafa
"""

def plusMinus(seq):
    length = len(seq)
    positive = 0
    negative = 0
    zeros = 0
    for i in range(length):
        if i >= 0:
           if i == 0:
               zeros += 1
               print(zeros/length)
           else:
               positive += 1
               print(positive/length)
        else:
            negative += 1
            print(negative/length)
        
plusMinus([-4,3,-9,0,4,1])

'''n = float(input())
lst = [int(x) for x in input().split()]
print (format(len([x for x in lst if x > 0])/n, ".6f"))
print (format(len([x for x in lst if x < 0])/n, ".6f"))
print (format(len([x for x in lst if x == 0])/n, ".6f"))'''