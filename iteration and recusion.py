# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:28:32 2017

@author: mustafa
"""
class BankAccount:
    def withdraw(self):
        pass
    
    def deposit(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance=1500):
        self.balance = balance

    def deposit(self, amount):
        if (amount <= 0):
            return "Invalid deposit amount"
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if(self.balance <= 1500):
            return "Cannot withdraw beyond the minimum account balance"
        elif(self.balance - amount > 1500):
            self.balance -= amount
            return self.balance
        elif(amount > self.balance):
            return "Cannot withdraw beyond the current account balance"
        elif(amount < 0):
            return "Invalid withdraw amount"

class CurrentAccount(BankAccount):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if (amount <= 0):
            return "Invalid deposit amount"
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if (amount <= 0):
            return "Invalid withdraw amount"
        elif (amount >= self.balance):
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount
            return self.balance
        