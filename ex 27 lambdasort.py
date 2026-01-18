# Scenario: 1)I have a list of products (dictionaries). Write a Python program to sort
# this list based on the price (Low to High) using the sorted() function and a lambda function.
#
# Input :
# products = [
#     {"name": "Laptop", "price": 50000},
#     {"name": "Mobile", "price": 15000},
#     {"name": "Headphones", "price": 2000},
#     {"name": "Monitor", "price": 12000}
# ]
#
#
# Expected Output: The list should be ordered: Headphones -> Monitor -> Mobile -> Laptop.

# -----------------------------------------------------------------------------------------------


products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile", "price": 15000},
    {"name": "Headphones", "price": 2000},
    {"name": "Monitor", "price": 12000}
]


sorted_products = sorted(products, key=lambda product: product["price"])


for product in sorted_products:
    print(product["name"], product["price"])