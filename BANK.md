```.py
class account():

    def __init__(self,  firstname, lastname, contact, age, initialBalance=0):
        # constractor of the class. Template
        self.Balance = initialBalance
        self.Firstname = firstname
        self.Lastname = lastname
        self.Contact = contact
        self.age = age = 100

    def checkbalance(self):
        print(f'the {self.Firstname} has a balance of {self.Balance}')

    def deposite(self, money):
        # here enter the code for a deposite
        self.Balance += money

    def withdraw(self, money):
        # check if tyhe user has a balance first
        if money > self.Balance:
            print("Balance is insufficient")
            return None
        self.Balance -= money


customer = account('Alex', 'Chin', 'alex.chin.jp', '8',1000)
customer2 = account('Kelven', 'Hasan', 'Kelven.Hasan.jp', '80',1580)
```
