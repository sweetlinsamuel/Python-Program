# 2)Create a StudentProfile class.
# Use a private variable email.
#
# Methods:
# set_email(email)
# get_email()
#
# Rules:
#
# Email must contain @
# Email should not be accessed directly
# If email is invalid, print Invalid email

class StudentProfile:
    def __init__(self):
        self.__email = []

    def set_email(self, new_email):
        if '@' in new_email:
            self.__email = new_email
            print("email address entered successfully")

        else:
            print("email address entered is not valid")

    def get_email(self):
        if self.__email is None:
            return "no email set"
        # print("email address entered is not valid")
        return self.__email

student = StudentProfile()
email_input = input("Enter your email:")
student.set_email(email_input)
print("Stored Email:", student.get_email())

