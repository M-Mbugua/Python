class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: £{self.balance}"

    def deposit(self, amount):

        self.balance += amount

        print(f"Deposit Accepted. \n{amount} has been added to {self.owner}'s account. \nNew balance is {self.balance}")

    def withdrawal(self, amount):

        if amount > self.balance:
            self.balance -= amount
            print("Sorry, funds are unavailable")

        else:
            print(f"Withdrawal Accepted. \n{amount} has been withdrawn from {self.owner}'s account. \nNew balance is {self.balance}")
