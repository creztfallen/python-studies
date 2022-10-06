from customer import Customer
class Account():
    def __init__(self, balance, customer, limit):
        self.balance = balance
        self.limit = limit
        self.customer = customer

    def deposit(self, money):
        if self.balance + money <= self.limit: 
            self.balance += money
        else:
            print("Error: You don't have any more limit.")    
        
    def withdraw(self, money):
        if money > self.balance:
            print("Error: You don't have enough money.")
        else:
                self.balance -= money    
            