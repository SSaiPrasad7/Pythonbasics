class Account:
    def __init__(self,name):
        self.name=name
        self.amount = 1
        self.bet = 0

    def __str__(self):
        return f"\n{self.name} has balance {self.amount} dollars."

    def ask(self):
        response=False
        while response==False:
            try:
                self.amount =int(input("Enter Initial Deposit for the Game(in Dollars) :"))
                if self.amount<=0:
                    raise ValueError
                response=True
            except:
                print("Entered amount is zero or less than zero.Try again")
                response=False

    def deposit(self, bet):
        self.amount += bet

    def withdraw(self, bet):
        self.amount -= bet
