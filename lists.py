# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:57:05 2017

@author: mustafa
"""

list1 = ["a","b","c","d","e"]
list2 = ["m","n","o","p","q","m"]
list3 = ["h","i","j","k","l"]
list4 = [1,2,3,4,5]
list5 = [8,5,3,6,7,9]

#lists are mutable(can be changed) (by adding elements to the list, it is changed) and elements of a list are homogeneous(of same kind)
list1[len(list1):] = ["x"] #adding item to end of list(appending)
list1.append("z") #alternatively
print (list1)

list2[len(list2):] = "l" #extend list
list2.extend("w") #alternatively
list2.extend([1,2])
print (list2)

list3.insert(0,"y")#adding item to front of list
list3.insert(len(list3),"u")#same as appending
list3.insert(2,"v") # first parameter indicates position
print(list3)

list4.pop() #removes item at given position and return it. if no index is specified, it removes and returns the last element of the list.
print(list4.pop()) #prints the returned value
print(list4.pop(2)) #prints the returned index value
print(list4) #prints the list without the returned value

aList = [123, 'xyz', 'zara', 'abc'];

print ("A List : ", aList.pop())
print ("B List : ", aList.pop(2))

print (list2.index("p")) #returns the index(position) of the item.
print (list2.count("m")) #counts the no. of times an item appears

list4.clear() #remove all items from a list
del list1[:]#alternatively
print (list1)
print(list4) 

list5.reverse() #reverse elements of the list
print(list5)
list5.sort() # sorts(arranges) items in the list.
print(list5)

new_list = list5[:] # copying a list is most efficient using the slicing method
print(new_list)

#USING LISTS AS STACKS (STACK'S PRINCIPLE IS LAST IN FIRST OUT)(LIFO)
stack = [3,4,5]
stack.append(6)
stack[len(stack):] = [7]
#adding items to the top of the stack
print(stack)
stack.pop()
stack.pop()
#removing items to the top of the stack
print(stack)

#USING LISTS AS QUEUES (queue principle is FIRST IN FIRST OUT)(FIFO) While using append an pops at the end of a list is fast, 
#using insert and pops at the beginning of a list is slow. Hence to implement a queue use collections.deque which is fast 
#from both ends.
from collections import deque
queue = deque(["Eric","John","Tommy"])
queue.append("Michael")
queue.append("Graham")
print(queue.popleft())
print (queue)
queue.popleft()
print (queue)

#LIST COMPREHENSIONS
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares2 = list(map(lambda x:x**2, range(5))) #alternatively #lambda function is a way to create small anonymous functions, i.e. functions without a name. 
#syntax lambda argument_list: expression 
print(squares2)

squares3 = [x**2 for x in range(8)] #alternatively more concise and readable
print(squares3)

#list comprehensions consists of brackets containing an expression followed by for clause
#then zero or more for of if clauses
combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print (combs)
# equivalent to
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
print (combs)

#flatten a list using listcomp with two for
vec = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for elem in vec for num in elem]
print (flat)  

from math import pi
pie = [str(round(pi,i)) for i in range (1,6)]
print (pie)

#FUNCTIONAL PROGRAMMING TOOLS [filter(), map(), reduce()]
#syntax filter(function,sequence) if the sequence is str,unicode,tuple, the result will be of the same type. 
#otherwise it is always a list

def f(x):
    return x % 3 == 0 or x % 5 == 0
divisibility = list(filter(f,range(2,25)))  
divisibility2 = [x for x in range(2,25) if f(x)] #alternatively using list compressions
print (divisibility)
print (divisibility2)

#syntax map(function,sequence) if the sequence is str,unicode,tuple, the result will be of the same type. 
def cube(x):
    return x**3
triple = list(map(cube,range(1,11)))
print (triple)

seq = range(8)
def add(x,y):
    return x+y
addition = list(map(add,seq,seq))
print (addition)

#syntax reduce(function,sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on.
from functools import reduce
def add(x,y):
    return x+y
single = reduce(add,range(1,11))
print (single)

print(sum(range(1,11)))

#NESTED LIST COMPREHENSIONS
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
transpose = [[row[i] for row in matrix] for i in range(4)]
print (transpose)

#alternatively
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#alternatively
transposed2 = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed2.append(transposed_row)
print (transposed2)

inbuilt = list(zip(matrix))    
print (inbuilt)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print (a)
del a[2:4]
print (a)

#TUPLES AND SEQUENCES
t = 1234, 5678, 'hello' #tuple. on output it is always enclosed with parantheses 
#this is called tuple packing. The reverse is also possible x,y,z = t, but this is called sequence unpacking
print (t)
print (t[0])
u = t,(1,2,3,4,5)
print(u)
#t[0] = 3453 #tuples are immutable(can't be changed)
#Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing 
#Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

empty =() #use empty paranthesis for empty tuple
singleton = 'hello', #creating a tuple with single item. dont forget the trailing comma
print(singleton)

#SETS
#sets is an unordered collection of unique elements(no duplicates) 
#Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
#basic uses include membership testing and eliminating duplicate entries
basket = {'apple','pear','banana','orange','apple','banana','avocado'}
print (basket) #shows that duplicates have been removed
print('orange' in basket) #fast membership testing
print('mango' in basket)
#create an empty set using set() not {}, the latter creates a dictionary
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print (a)
print (b)
print (a-b) #DIFFERENCE #letters in a but not in b
print (a|b) #UNION #letters in either a or b 
print (a&b) #INTERSECTION #letters in both a and b
print (a^b) #SYMMETRIC DIFFERENCE #letters in a and b but not in both

#similar to  list comprehensions, set comprehensions are also supported
d = {x for x in 'abracadabra' if x not in 'abc'}
print (d)

#DICTIONARIES(associative arrays or associative memories in other languages)
#Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.
book = {'jack':3245, 'anthony':5678}
book['betty'] = 4098
book['kate'] = 3679
print(book)
print(list(book.keys()))
print(sorted(book.keys()))
del book['jack']
print(book)
print('kate' in book)
print('andrew' in book)

#The dict() constructor builds dictionaries directly from sequences of key-value pairs
#built = dict([('sape')])

 

  








