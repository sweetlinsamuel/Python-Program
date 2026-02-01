# Scenario:
#
# 1)Create a system where a user can add food items to an order. Finally, you need to calculate the total bill
# including a 5% tax.
#
#Class Name: FoodOrder
#Attributes:
# menu: A dictionary with items and prices (e.g., {"Grilled Chicken": 200, "Biryani": 300}).
# cart: An empty list to store ordered items.
# Methods:
# addItem(item):
# Check if the item exists in the menu.
# If yes, add it to the cart.
# If no, print "Item not available".
# calculateBill():
# Calculate the total price of all items in the cart.
#Add 5% tax to the total amount.
# Print the final bill.


class FoodOrder:
    def __init__(self):
        self.menu={
            "Grilled Chicken": 200,
            "Biryani": 300,
            "Sandwich": 400,
            "Sweets": 500,
        }

        self.cart=[]

    def add_item(self,item):
        if item in self.menu:
            self.cart.append(item)
            print(f"{item}added to cart")
        else:
            print("Item not available")

    def calculatebill(self):
        total = 0
        for item in self.cart:
            total += self.menu[item]

        tax = total * 0.05
        final_bill= total + tax

        print("\n------ BILL DETAILS ------")
        print("Items Ordered:")
        for item in self.cart:
            print(f"- {item}: ₹{self.menu[item]}")

        print(f"\nSubtotal: ₹{total}")
        print(f"Tax (5%): ₹{tax}")
        print(f"Total Bill: ₹{final_bill}")
        print("--------------------------")

order = FoodOrder()
order.add_item("Biryani")
order.add_item("Sweets")
order.add_item("Pizza")  # Not in menu
order.calculatebill()




