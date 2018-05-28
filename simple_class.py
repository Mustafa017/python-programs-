# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 08:43:57 2017

@author: mustafa
"""

class InputOutput(object):
    def __init__(self):# also (self,s="") then self.s = s
        self.s = "";
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
m = InputOutput()
m.getString()
m.printString()