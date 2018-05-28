# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 14:10:00 2017

@author: mustafa
"""

'''def bubble_sort():
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]'''

'''mylist = [12, 5, 13, 8, 9, 65]

def bubble(badList):
    length = len(badList) - 1
    unsorted = True

    while unsorted:
        for element in range(0,length):
            unsorted = False
            if badList[element] > badList[element + 1]:
                hold = badList[element + 1]
                badList[element + 1] = badList[element]
                badList[element] = hold
                print (badList)
            else:
                unsorted = True

print (bubble(mylist))'''


'''To explain why your script isn't working right now, I'll rename the variable 
unsorted to sorted.

At first, your list isn't yet sorted. Of course, we set sorted to False.

As soon as we start the while loop, we assume that the list is already sorted. 
The idea is this: as soon as we find two elements that are not in the right order, 
we set sorted back to False. sorted will remain True only if there were no elements 
in the wrong order.

There are also minor little issues that would help the code be more efficient or readable.

In the for loop, you use the variable element. Technically, element is not an 
element; it's a number representing a list index. Also, it's quite long. 
In these cases, just use a temporary variable name, like i for "index".
for i in range(0, length):
    
The range command can also take just one argument (named stop). In that case, you 
get a list of all the integers from 0 to that argument.
for i in range(length):
    
The Python Style Guide recommends that variables be named in lowercase with 
underscores. This is a very minor nitpick for a little script like this; 
it's more to get you accustomed to what Python code most often resembles.
def bubble(bad_list):
    
To swap the values of two variables, write them as a tuple assignment.
The right hand side gets evaluated as a tuple (say, (badList[i+1], badList[i]) 
is (3, 5)) and then gets assigned to the two variables on the left hand side 
((badList[i], badList[i+1])).
bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
'''
'''my_list = [12, 5, 13, 8, 9, 65]
def bubble(bad_list):
    count = 0
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
                count += 1
                print(count)
bubble(my_list)
print (my_list)'''

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count = 0
length = len(a) - 1
sorted = False

while not sorted:
    sorted = True
    for i in range(length):
        if a[i] > a[i+1]:
            sorted = False
            a[i],a[i+1] = a[i+1],a[i]
            count += 1
print("Array is sorted in",count,"swaps" )            
print("First Element:",a[0] )
print("First Element:",a[-1] )

'''n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count = 0
for i in range(n):
    j=0
    while j<n-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            count+=1
        j+=1
print ('Array is sorted in %d swaps.'%count)
print ('First Element: %d'%a[0])
print ('Last Element: %d'%a[-1])'''

def bubblesort(alist):
    for passnum in range(len(alist) - 1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist = [54,26,93,17,77,31,44,55,20]
bubblesort(alist)
print (alist)
