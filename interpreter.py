# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:05:40 2017

@author: mustafa
"""

'''fooDate='10/3/2003'
month, day, year = fooDate.split('/')
month=int(month)
day=int(day)
year=int(year)

[month, day, year] = map(int, fooDate.split('/'))
[month, day, year] = [int(x) for x in fooDate.split('/')]'''

'''digits = '1,30,5,6,7'
mylist = [int(x) for x in digits.split(',')]

#product = [x*x for x in individual if x != 0]
print(mylist)'''

s = input().strip()

def intTryParse(value):
    try:
        print (int(value))
    except ValueError:
        print ('Bad String')
intTryParse(s)