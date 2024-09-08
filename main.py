# This file tests all the functions
# in the code challenge

from order import Order
from coffee import Coffee
from customer import Customer

# Create a customer
customer1 = Customer("Subira")
# customer2 = Customer("") # => Returns an error
# customer3 = Customer(2) # => Returns an error
print(f"Created customer: {customer1.name}")

# Create coffee type
coffee1 = Coffee("Mocha")
# coffee2 = Coffee(2) # => Returns an error
# coffee3 = Coffee("cf") # => Returns an error
# coffee1.name = "Mochas" # => Returns an error
print(f"Created coffee: {coffee1.name}")

# Create an order
order1 = Order(customer1, coffee1, 2.0)
# order2 = Order("This customer", coffee1, 2.0) # => Returns an error
# order3 = Order(customer1, "This coffee", 2.0) # => Returns an error
# order4 = Order(customer1, coffee1, 11.0) # => Returns an error
print(f"{order1.customer.name} ordered a {order1.coffee.name} for {order1.price}")

# Order property customer returns the customer for that order
print(f"order1 customer object: {order1.customer}")

# Order property coffee returns the coffee for that order
print(f"order1 coffee object: {order1.coffee}")

# Coffee orders() returns a list of all orders of type orders
customer4 = Customer("Angie")
order5 = Order(customer4, coffee1, 3.0)
print(f"{len(coffee1.orders())} orders for this coffee: {coffee1.orders()}")

# Coffee customers() returns a list of unique customers
print(f"{len(coffee1.customers())} customers for this coffee: {coffee1.customers()}")

# Customer create_order() creates a new order
coffee2 = Coffee("Cappucino")
order6 = customer4.create_order(coffee2, 3.0)
print(f"New order: {order6.customer.name} ordered {order6.coffee.name} for {order6.price}")

# Customer order() returns full list of orders
print(f"Angie made {len(customer4.orders())} orders: {customer4.orders()}")

# Customer coffee() returns a list of unique coffee a customer has ordered
print(f"Angie ordered {len(customer4.coffee())} unique coffees: {customer4.coffee()}")

# Coffee num_orders() returns the total number of orders for that coffee
print(f"{coffee1.name} has been ordered {coffee1.num_orders()} times")

# Coffee average_price() average price
print(f"{coffee1.name} average price: {coffee1.average_price()}")
