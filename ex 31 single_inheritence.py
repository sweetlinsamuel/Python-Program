# Scenario: Single Inheritance
# Create a User class with a login() method.
# Create a Customer class that inherits the User class and adds a place_order() method.

class User:
    def login(self):
        print("logged in successfully")

class Customer(User):
    def order(self):
        print("ordered book successfully")

obj = Customer()
obj.login()
obj.order()
