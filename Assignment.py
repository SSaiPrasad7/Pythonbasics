class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:{self.owner} Account balance: ${self.balance}'

    def deposit(self, dpt_amount):
        self.balance = self.balance + dpt_amount
        print('Deposit Accepted')

    def withdraw(self, amount):
        if self.balance < amount:
            print('Funds Unavailable!')
        else:
            self.balance = self.balance - amount
            print('Withdrawal Accepted')


acct1 = Account('sai', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
