# 3)Hierarchical Inheritance
# Create a User class with a login() method.
# Create Customer and Seller classes that inherit the User class.
# Add a buy_product() method in Customer and an add_product() method in Seller.


class User:
    def login(self):
        print("login successful")

class Customer(User):
    def buy_product(self):
        print("bought product successful")

class Seller(User):
    def add_product(self):
        print("added product to cart")


Customer = Customer()
Customer.login()
Customer.buy_product()


seller = Seller()
seller.login()
seller.add_product()


