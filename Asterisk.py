# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:08:51 2017

@author: mustafa
"""

'''The asterisk unpacks an iterable. '''
def exampleFunction (paramA, paramB, paramC):
    print('A:', paramA)
    print('B:', paramB)
    print('C:', paramC)

myTuple = ('foo', 'bar', 'baz')
print(myTuple)

#print(exampleFunction(myTuple)) #throws a TypeError. we need to use an asterisk to to unpack myTuple.
print(exampleFunction(myTuple[0], myTuple[1], myTuple[2]))
print(exampleFunction(*myTuple))

'''The special syntax, *args and **kwargs in function definitions is used to pass a 
variable number of arguments to a function. The single asterisk form (*args) is used 
to pass a non-keyworded, variable-length argument list, and the double asterisk form 
is used to pass a keyworded, variable-length argument list.'''

def test_var_args(farg,*args):
    print('formal args:', farg)
    for arg in args:
        print('another_arg:', arg)
test_var_args(1,'two',3)

def test_var_kwargs(farg,**kwargs):
    print('formal args:', farg)
    for key in kwargs:
        print('another keyword arg: %s: %s' %(key,kwargs[key]))
test_var_kwargs(farg=1,myarg2='two',myarg3=3)

'''Using *args and **kwargs when calling a function
This special syntax can be used, not only in function definitions, but also when calling a function.'''

def test_var_args_call(arg1,arg2,arg3):
    print('arg1:',arg1)
    print('arg2:',arg2)
    print('arg3:',arg3)
args = ('two',3)
test_var_args_call(1,*args)

def test_var_kwargs_call(arg1,arg2,arg3):
    print('arg1:',arg1)
    print('arg2:',arg2)
    print('arg3:',arg3)
kwargs = {'arg2':'two','arg3':3}
test_var_kwargs_call(1,**kwargs)