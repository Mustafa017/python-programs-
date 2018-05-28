# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:01:29 2017

@author: mustafa
"""

def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end = '')
        a, b = b, a+b
print ()

def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
        return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
