# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:42:21 2017

@author: mustafa
"""

'''def soln(N):
    for i in range(1,N+1):
        if i%105 == 0:
            print("FuzzBuzzWoof")
        elif i%35 == 0:
            print("BuzzWoof")
        elif i%21 == 0:
            print("FuzzWoof")
        elif i%15 == 0:
            print("FuzzBuzz")
        elif i%7 == 0:
            print("Woof")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fuzz")
        else:
            print(i)
soln(24)  '''

def soln(n):
    if n%15 == 0:
        return "FizzBuzz"
    elif n%5 == 0:
        return "Buzz"
    elif n%3 == 0:
        return "Fizz"
    else:
        return n
print(soln(25))

a = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        a.append(i)
print(a, sep=',')#prints values in a new line
