# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:27:07 2017

@author: mustafa
"""

def insertionSort(alist):
    for index in range(1,len(alist)):
        current_value = alist[index]
        position = index
        
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = current_value
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print (alist)