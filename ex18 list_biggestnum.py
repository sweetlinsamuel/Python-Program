#Scenario: Find the biggest number in [88, 24, 99, 15] using a loop (don't use max())



numbers = [88, 24, 99, 15]
biggest_number = numbers[0]

for n in numbers:
    if n > biggest_number:
        print("biggest number:", n)

