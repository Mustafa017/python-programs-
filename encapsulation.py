# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:53:36 2017

@author: mustafa
"""

class Encapsulation:
    def __init__(self,a,b,c):
        self.public = a
        self._protected = b
        self.__private = c
        
#USE COMMANDLINE
'''from encapsulation import Encapsulation
x = Encapsulation(11,13,17)
x.public
x._protected
x._protected = 23
x._protected * value is changed
x.__private *AttributeError: 'Encapsulation' object has no attribute '__private' 
*cant be accessed from outside'''
