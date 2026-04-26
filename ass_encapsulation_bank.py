

#3)Create a Bank class with private variable __balance and access it only using methods like deposit and show_balance.


class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
        print("total amount deposited", amount)

    def show_balance(self):
        print("total balance", self.__balance)


amount = int(input("enter the amount:"))
c = Bank(5000)
c.deposit(amount)
c.show_balance()
