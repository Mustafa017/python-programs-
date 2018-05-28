# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:45:55 2017

@author: mustafa
"""
'''The str() function is meant to return representations of values which are fairly human-readable, while 
repr() is meant to generate representations which can be read by the interpreter 
rjust()  which right-justifies a string in a field of a given width by padding it with spaces on the left.'''
'''
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x**2,x**3))'''
    
'''(Note that in the first example, one space between each column 
was added by the way print() works: it always adds spaces between its arguments.)'''

'''from itertools import combinations
stuff = [-1, 0, 1]
for i in range(0, len(stuff)): 
    for subset in combinations(stuff, 2):
        print(set(subset))'''

'''from itertools import chain, combinations
def all_subsets(ss):
  return chain(*map(lambda x: combinations(ss, 2), range(0, len(ss))))

for subset in all_subsets(stuff):
  print(subset)
all_subsets([1, 0, -1])'''

'''def selfCombine( list2Combine, length ):
    listCombined = str( ['list2Combine[i' + str( i ) + ']' for i in range( length )] ).replace( "'", '' ) \
                     + 'for i0 in range(len( list2Combine ) )'
    if length > 1:
        listCombined += str( [' for i' + str( i ) + ' in range( i' + str( i - 1 ) + ', len( list2Combine ) )' for i in range( 1, length )] )\
            .replace( "', '", ' ' )\
            .replace( "['", '' )\
            .replace( "']", '' )

    listCombined = '[' + listCombined + ']'
    listCombined = eval( listCombined )

    print (listCombined)

list2Combine = [-1, 0 , 1]
listCombined = selfCombine( list2Combine, 2 )'''

'''def per(n):
    stuff = [-1,0,1]
    for i in stuff:
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        print (list(map(int,list(s))))
per(3)'''

import numpy, itertools
def possibleOutcomes(n):
    [win, lose, AwayWin] = 1, 0, -1
    subset = list(itertools.product([win, lose, AwayWin], repeat = n))
    myArray = numpy.array(subset)
    print(myArray)
possibleOutcomes(2)

'''import numpy, itertools
lst = list(itertools.product([1, 0, -1], repeat = 2))
subset = numpy.array(lst)
print(subset)'''
