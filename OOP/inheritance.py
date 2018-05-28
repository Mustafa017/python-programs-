#Let us try to create a little more sophisticated account type where the account holder has to maintain a pre-determined minimum balance.
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance 

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance 

class MinimumBankAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            return "Sorry, minimum balance must be maintained."
        else:
            BankAccount.withdraw(self,amount)
