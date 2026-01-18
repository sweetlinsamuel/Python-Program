# Scenario: Filter out weak passwords. Use filter() and lambda to create a new list
# containing only passwords that have more than 8 characters.
#
# Input :
# passwords = ["pass123", "secure_login_99", "admin", "python_developer", "1234"]
#
# Expected Output: ['secure_login_99', 'python_developer']


passwords = ["pass123", "secure_login_99", "admin", "python_developer", "1234"]

filter_passwords = list(filter(lambda pword: len(pword) > 8, passwords))

print("Valid Password:", filter_passwords)


