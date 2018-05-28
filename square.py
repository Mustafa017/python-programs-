# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 07:07:44 2017

@author: mustafa
"""

def squares(n):
    if n < 1:
        return "Number should be greater than or equal to 1"
    else:
        s = {i:i*i for i in range(1,n+1)}
        return s
print(squares(8))

#when u use int the results appear without paranthesis
n = int(input())
l = [int(i) for i in input().split(',')]
print(l)
myList = ','.join(map(str, l))
print(myList)
print(tuple(l))

#different result. the result has paranthesis
l = [i for i in input().split(',')]
print(l)
print(tuple(l))

#difference between strip and split
my_string = "blah, lots  ,  of ,  spaces, here "
print([x for x in my_string.split(',')])
print([x.strip() for x in my_string.split(',')])#removes whitespaces
