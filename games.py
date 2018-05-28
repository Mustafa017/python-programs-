# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:44:11 2017

@author: mustafa
"""

import numpy, itertools
def possibleOutcomes(n):
    [win, lose, AwayWin] = 1, 0, -1
    subset = list(itertools.product([win, lose, AwayWin], repeat = n))
    myArray = numpy.array(subset)
    print(myArray)
    
possibleOutcomes(2)