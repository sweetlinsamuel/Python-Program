#4)Create a Product class with protected _price and modify it only using methods and access it in a child class.

class Product:
    def __init__(self,price):
        self._price = price

    def new_price(self, nw_price):
        self._price = nw_price
        print("new price")


class Mobile(Product):
    def display(self):
        print("Mobile Price:", self._price)

m = Mobile(25000)
m.new_price(30000)
m.display()