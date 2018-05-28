# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:56:26 2017

@author: mustafa
"""

class Pet:
    no_of_legs = 0
    def sleep(self):
        print("zzz")
    def count_legs(self):
        print("Doug has %d legs" %self.no_of_legs)
doug = Pet()
doug.no_of_legs = 4
doug.count_legs()
nemo = Pet()
nemo.no_of_legs = 2
nemo.count_legs()

class Dog(Pet):
    def bark(self):
        print("Woof")
doug1 = Dog()
doug1.bark()
doug1.sleep()
        
class a:
    def abc(self):
        print ("haha")
    def test(self):
        self.abc()  
        # abc()

b = a()
b.abc() #  'haha' is printed
b.test() # 'haha' is printed

