""""""
# Write a Python program to calculate delivery charge based on distance.
# If distance is less than or equal to 3 km delivery charge = ₹0
# If distance is greater than 3 km and less than or equal to 7 km delivery charge = ₹30
# If distance is greater than 7 km delivery charge = ₹50
#
# Input: distance in kilometers (float)
# Output: print the delivery charge.
""""""

distance = float(input("Enter distance:"))
if distance <= 3:
    charges = 0

elif distance <= 7:
    charges = 30

else:
    charges = 50

print("Delivery charges is",charges)
