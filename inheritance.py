# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 12:35:25 2017

@author: mustafa
"""

def calculate():
    scores = [100,80]
    numScores = 2
    a = float(sum(scores)/numScores) # alternatively  a = float(sum(scores)/len(scores))
    if (a>=90 and a<=100):
        return ("O")
    elif (a>=80 and a<90):
        return ("E")
    elif (a>=70 and a<80):
        return ("A")
    elif (a>=55 and a<70):
        return ("P")
    elif (a>=40 and a<55):
        return ("D")
    else:
        return ("T")
print (calculate())

# version 1 using enumerate()
def calculate1():
    scores = [60,80]
    grades = 'OEAPDT'
    
    a = sum(scores) / len(scores)
    
    conditions = [
        90 <= a <= 100, 80 <= a < 90, 70 <= a < 80, 
        55 <= a < 70, 40 <= a < 55, a < 40
    ]
    
    for i, c in enumerate(conditions):
        if c: return grades[i]
print (calculate1())

# version 2 using zip()
def calculate2():
    scores = [60,70]
    grades = 'OEAPDT'
    
    a = sum(scores) / len(scores)
    
    conditions = [
        90 <= a <= 100, 80 <= a < 90, 70 <= a < 80, 
        55 <= a < 70, 40 <= a < 55, a < 40
    ]
    
    for c, g in zip(conditions, grades):
        if c: return g
print (calculate2())

# version 3 using for loop
def calculate3(): 
    scores = [40,55]
    grades = 'OEAPDT'
    
    a = sum(scores) / len(scores)
    
    conditions = [
        90 <= a <= 100, 80 <= a < 90, 70 <= a < 80, 
        55 <= a < 70, 40 <= a < 55, a < 40
    ]
    
    for (condition, grade) in zip(conditions, grades):
        if condition is True: return grade
print (calculate3())