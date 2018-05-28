# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:39:47 2017

@author: mustafa
"""
import sys,collections
class Solution:
    def __init__(self):
        self.myStack = list()
        self.myQueue = collections.deque([])

    def pushCharacter(self,char):
        self.myStack.append(char)
       
    def popCharacter(self) :
        return self.myStack.pop() 
        
    def enqueueCharacter(self,char):
        self.myQueue.append(char)
    
    def dequeueCharacter(self):
        return self.myQueue.popleft()

s =  input() #Read input s
obj = Solution() #create Solution class object
L = len(s)

for i in range(L):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome = True
'''pop the first character from the stack and deque the first character from 
the queue then compare.'''

for i in range(L // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
'''finally print whether s is palindrome or not'''
if isPalindrome:
    print('The word, '+s+' , is a Palindrome.')
else:
     print('The word, '+s+' , is not a Palindrome.')
     
'''class Solution:
      def __init__(self):
          self.mystack = list()
          self.myqueue = list()
          return(None)

      def pushCharacter(self, char):
          self.mystack.append(char)

      def popCharacter(self):
          return(self.mystack.pop(-1))

      def enqueueCharacter(self, char):
          self.myqueue.append(char)

      def dequeueCharacter(self):
          return(self.myqueue.pop(0))'''