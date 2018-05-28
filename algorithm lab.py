# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:31:16 2017

@author: mustafa
"""

def binary_converter(n):
  if(n == 0):
    return "0"
  elif(n < 0):
    return "Invalid input"
  elif(n > 255):
    return "Invalid input"
  else:
       ans=""
       while(n>0):
            n=n/2
            remainder=n%2
            ans += str(remainder)
            
       return ans

print(binary_converter(5))