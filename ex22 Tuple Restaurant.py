# Scenario: A restaurant stores daily ordered food items in a tuple.
# orders = ("biryani", "pongal", "burger", "biryani", "pongal")
# 1)Count how many times "biryani" was ordered.
# 2)Find the index position of "burger".
# 3)Convert the tuple into a list and add "shawarma", then convert back to tuple

orders = ("biryani", "pongal", "burger", "biryani", "pongal")

order = orders.count("biryani")
print("Biryani ordered",order)

find_burger = orders.index("burger")
print("The index of burger is",find_burger)

order_list = list(orders)

order_list.append("shawarma")
print("List:",order_list)

orders = tuple(order_list)
print("Converted back as Tuple:",orders)
