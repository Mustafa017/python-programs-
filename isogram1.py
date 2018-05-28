# -*- coding: utf-8 -*-
"""
Created on Mon May 22 10:29:36 2017

@author: mustafa
"""

def isogram(string):
    iso = [i for i in string if string.count(i) == 1]
    return iso
print (isogram("mustafa"))
            
string = "banana"
print(list(enumerate(string)))
lst = list(string)
print(lst.index('a'))

d = [x for x,y in enumerate(string) if y == 'a']
print(d)

a = [x for x,y in enumerate(string) if y == 'n']
print(a)

def is_isogram(word):
    '''This function tests for isogram'''
    word_set = set(word)

    if word.strip() == "":
        return (word, False)

    elif len(word) == len(word_set):
        return (word, True)

    elif type(word)!= str :
        raise TypeError

    else:
        return (word, False)
print (is_isogram("mustafa"))