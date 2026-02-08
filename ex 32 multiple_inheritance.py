# Scenario:
# 2) Multiple Inheritance
# Create a Restaurant class with an add_menu() method and a DeliveryPartner class with a deliver_order() method.
# Create an OrderManager class that inherits both classes and uses both methods.



class Restaurant:
    def __init__(self):
        self.menu = []

    def add_menu(self, item):
        self.menu.append(item)
        print(f"{item}: Added menu")

class DeliveryPartner:
    def deliver_order(self, orderid):
        # self.menu.order.append(order)
        print(f"{orderid}: Delivered order successfully")

class OrderManager(Restaurant, DeliveryPartner):
    def order(self, item, orderid):
        if item in self.menu:
            print(f"Order {orderid} placed for '{item}'.")
            self.deliver_order(orderid)
        else:
            print(f"{item}: is unavailable in the menu")

order_manager = OrderManager()
order_manager.add_menu("Biryani")
order_manager.add_menu("Sweets")
order_manager.order("Biryani", 1)
order_manager.order("Sweets", 2)
order_manager.order("Pizza", 3)
        # self.menu.append(item)
        # print(f"{item}: Added menu")
