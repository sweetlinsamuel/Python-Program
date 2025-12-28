# Scenario: 1)You are given a tuple that stores seat prices of a movie theater.
# prices = (120, 150, 150, 200, 250)
# 1) Find how many times ₹150 price appears.
# 2)Find the highest seat price.
# 3)Check whether ₹300 seat price exists or not.



prices = (120, 150, 150, 200, 250)
price_times = prices.count(150)
print("No. of times 150 appeared:", price_times)

highest_price = max(prices)
print("Highest seat price:", highest_price)

check_price = False
for price in prices:
    if price == 300:
        check_price = True
        break
print("300 price seat is",check_price)
