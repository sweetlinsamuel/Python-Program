# Scenario: Filter: From this list [10, 15, 20, 25, 30], print only the even numbers.



numbers = [10, 15, 20, 25, 30]
# even_numbers = 0

for n in numbers:
    if n % 2 == 0:
        print("even number:", n)