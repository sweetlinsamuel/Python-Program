"""
Scenario: Currency
Price input is string "99.99"
Task: Convert to float & add 5.00 tax
"""

#price_str = input("Enter the price:")
price_str = "99.99"
price = float(price_str)
total_price = price + 5.00
print("The total price is ", total_price)
