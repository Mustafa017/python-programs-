# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:24:07 2017

@author: mustafa
"""

'''n = int(input())
print(*range(1, n+1),sep='')''' # removes whitespace from result

'''N = int(input().strip())

if N % 2 == 0 and (N < 6 or N > 20):
    print ("Not "),
print ("Weird")'''
# alternative print stmnt
#print ("Not ",end="") prints in a straight line and also adds or removes whitespace print ("Weird")

## start (with positive integers)
'''print 'coup_ate_grouping'[0]  ## => 'c'
print 'coup_ate_grouping'[1]  ## => 'o'
print 'coup_ate_grouping'[2]  ## => 'u'

## start (with negative integers)
print 'coup_ate_grouping'[-1]  ## => 'g'
print 'coup_ate_grouping'[-2]  ## => 'n'
print 'coup_ate_grouping'[-3]  ## => 'i'

## start:end
print 'coup_ate_grouping'[0:4]    ## => 'coup'
print 'coup_ate_grouping'[4:8]    ## => '_ate'
print 'coup_ate_grouping'[8:12]   ## => '_gro'

## start:end
print 'coup_ate_grouping'[-4:]    ## => 'ping' (counter-intuitive)
print 'coup_ate_grouping'[-4:-1]  ## => 'pin'
print 'coup_ate_grouping'[-4:-2]  ## => 'pi'
print 'coup_ate_grouping'[-4:-3]  ## => 'p'
print 'coup_ate_grouping'[-4:-4]  ## => ''
print 'coup_ate_grouping'[0:-1]   ## => 'coup_ate_groupin'
print 'coup_ate_grouping'[0:]     ## => 'coup_ate_grouping' (counter-intuitive)

## start:end:step (or stop:end:stride)
print 'coup_ate_grouping'[-1::1]  ## => 'g'
print 'coup_ate_grouping'[-1::-1] ## => 'gnipuorg_eta_puoc'

## combinations
print 'coup_ate_grouping'[-1::-1][-4:] ## => 'puoc'
'''

'''l = [1,2,3,4,5,6,7]
for i in range(len(l)//2):
    l[i], l[-1-i] = l[-1-i], l[i]
print(l)'''

#L = [L[-i] for i in range(1, len(L) + 1)]
#print(reduce(lambda acc, x: [x] + acc, l, []))

print("hello", "world")
print("hello", "world", sep=" cruel ")#Changing sep has the expected result.
print(["hello", "world"], sep=" cruel ")#Each argument is stringified as with str().
#Passing an iterable to the print statement will stringify the iterable as one argument.

'''However, if you put the asterisk in front of your iterable
this decomposes it into separate arguments and allows for the intended use of sep.'''
print(*["hello", "world"], sep=" cruel ")
print(*range(5), sep="---")

#Using join as an alternative
'''The alternative approach for joining an iterable into a string with a given separator
 is to use the join method of a separator string.'''
print(" cruel ".join(["hello", "world"]))

#This is slightly clumsier because it requires non-string elements to be explicitly converted to strings.
print(",".join([str(i) for i in range(5)]))
