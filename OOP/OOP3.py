class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance 

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance 

a = BankAccount()
b = BankAccount()

print(a.deposit(100))
print(a.withdraw(30))
print(b.deposit(200))
print(b.withdraw(20))