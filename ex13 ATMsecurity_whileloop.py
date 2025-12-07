"""
3. ATM Security loop

Scenario 4: Retry Logic
An ATM allows only 3 wrong attempts before blocking the card.
Task:
#while loop(max 3 times)
#Ask for PIN(Correct: "1234")
#If correct --> "Welcome" & Break
# If 3 fails --> "Card Blcoked"
"""

correct_pin = "1234"
pin_attempt = 0
while pin_attempt <3:
    pin = input("Enter the PIN:")

    if pin == correct_pin:
        print("Correct PIN, Welcome")
        break

    else:
        print("Incorrect PIN, Try Again")
        pin_attempt = pin_attempt + 1


if pin != correct_pin:
        print("Multiple incorrect PIN entered, Card Blocked")

# if pin_attempt == 3:
#     print("Multiple incorrect PIN entered, Card Blocked")


