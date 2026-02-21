# Scenario: 1)Create a Login class.
# Use a private variable password.
#
# Methods:
# set_password(password)
#
# login(input_password)
#
# Rules:
# Password must be at least 6 characters
# Password should not be accessed directly
# If password is correct, print Login successful
# Else print Invalid password


class Login:
    def __init__(self):

        self.__password = []

    def set_password(self, password):
        if len(password) <=6:
            print("Password must be at least 6 characters")

        else:
            self.__password = password
            print("Password is successful")


    def login(self, enter_password):
        if self.__password is None:
            print("No password set. Please set password first.")

        elif enter_password == self.__password:
            print("Login successful")

        else:
            print("Invalid password")


user = Login()

# user.set_password("abc")
# user.set_password("secure123")
# user.login("Invalid")
# user.login("secure123")

new_password = input("Set your password: ")
user.set_password(new_password)
login_password = input("Enter password to login: ")
user.login(login_password)