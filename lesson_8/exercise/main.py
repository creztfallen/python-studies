from account import Account
from customer import Customer

customer = Customer("Mateus", 11111111111, 24)
# print(customer)

acc = Account(2000, customer, 10000)
print(acc.customer.name, acc.balance)



