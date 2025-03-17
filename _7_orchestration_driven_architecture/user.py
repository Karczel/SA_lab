class User:
    def __init__(self, id, money=0):
        self.id = id
        self.balance = money

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money