# Phase 3 Week 2 Challenge: Coffee Ordering System

This project simulates a coffee ordering system where customers can place orders for different types of coffee. It consists of three main classes: `Customer`, `Coffee`, and `Order`. Each class has its own properties and methods that help manage the interactions between customers and their coffee orders.

## Project Structure

### Classes

1. **Customer**: Represents the customers who are placing orders for coffee.
2. **Coffee**: Represents the coffee types available for ordering.
3. **Order**: Represents the orders placed by customers for a specific coffee type, including the price of the order.

---

### Class Breakdown

#### `Customer` Class

This class stores customer information and their coffee orders.

- **Attributes:**

  - `name`: Represents the name of the customer (must be a string between 1 to 15 characters long).

- **Methods:**
  - `orders()`: Returns a list of all orders placed by the customer.
  - `coffee()`: Returns a set of all unique coffee types the customer has ordered.
  - `create_order(coffee, price)`: Creates a new order for the customer, given a `Coffee` object and a price.

#### Example

```python
customer1 = Customer("Subira")
print(customer1.name)  # Outputs: Subira
```

---

#### `Coffee` Class

This class stores the details of coffee types and tracks orders related to them.

- **Attributes:**

  - `name`: The name of the coffee type (must be a string with at least 3 characters).

- **Methods:**
  - `orders()`: Returns all orders that involve this coffee type. It does so by filtering from the `Order.all_orders` list.
  - `customers()`: Returns a set of unique customers who ordered this coffee by iterating through all related orders and extracting unique customers.
  - `num_orders()`: Returns the total number of times this coffee has been ordered.
  - `average_price()`: Calculates and returns the average price of all orders for this coffee. If there are no orders, it returns 0.

#### Example

```python
coffee1 = Coffee("Mocha")
print(coffee1.name)  # Outputs: Mocha
```

In this example:

- We create a coffee type called "Mocha" by initializing a `Coffee` object.
- The name of the coffee can be accessed using the `name` property.

The methods can be called as follows:

```python
print(coffee1.num_orders())        # Get the total number of orders for "Mocha"
print(coffee1.average_price())     # Get the average price for "Mocha"
print(coffee1.customers())         # Get the unique customers who ordered "Mocha"
```

---

#### `Order` Class

This class is responsible for creating and managing individual coffee orders.

- **Attributes:**

  - `customer`: The customer placing the order. This must be an instance of the `Customer` class.
  - `coffee`: The coffee being ordered. This must be an instance of the `Coffee` class.
  - `price`: The price of the order (must be a float between 1.0 and 10.0).

- **Methods:**
  - `customer`: Getter and setter for the customer attribute. Ensures the value is an instance of the `Customer` class.
  - `coffee`: Getter and setter for the coffee attribute. Ensures the value is an instance of the `Coffee` class.
  - `price`: Getter and setter for the price attribute. Ensures the value is a float within the range of 1.0 to 10.0. Checks if the price has already been set to prevent changes after the order is created.

Each order is automatically appended to the `Order.all_orders` list when it's created.

#### Example

```python
order1 = Order(customer1, coffee1, 2.0)
print(f"{order1.customer.name} ordered {order1.coffee.name} for {order1.price}")
# Outputs: Subira ordered Mocha for 2.0
```

Here:

- A new order is created with customer1 ordering coffee1 for 2.0 units of currency.
- The properties of the order, such as the customer, coffee, and price, can be accessed and printed:

```python
print(order1.customer)  # Returns the customer object
print(order1.coffee)    # Returns the coffee object
print(order1.price)     # Returns the price of the order
```

The `Order` class ensures that:

- Only valid `Customer` and `Coffee` instances can be associated with the order.
- The price of the order is within the specified range and is set only once.

## How It Works

1. **Creating a Customer**:
   Customers are created by passing their name as a string to the `Customer` class. The name must be between 1 and 15 characters long. If the input is invalid, a `ValueError` is raised.

   ```python
   customer1 = Customer("Subira")

   ```

2. **Creating a Coffee Type:**
   Coffee types are created by passing their name as a string to the Coffee class. The name must be at least 3 characters long. If the input is invalid or if the name has already been set, a ValueError is raised.

   ```python
   coffee1 = Coffee("Mocha")
   ```

3. **Placing an Order:**
   Orders are created by instantiating the Order class with a Customer instance, a Coffee instance, and a price. The price must be a float between 1.0 and 10.0. If any of these conditions are not met, a ValueError is raised.

   ```python
   order1 = Order(customer1, coffee1, 2.0)
   ```

4. **Viewing Orders and Information:**
   You can retrieve various details about orders:

   - coffee1.orders(): Retrieves a list of all orders for that coffee.
   - coffee1.customers(): Retrieves a set of unique customers who have ordered that coffee.
   - coffee1.num_orders(): Retrieves the total number of orders for that coffee.
   - coffee1.average_price(): Retrieves the average price of orders for that coffee.

   ```python
   print(f"{coffee1.name} has been ordered {coffee1.num_orders()} times")
   print(f"Average price for {coffee1.name}: {coffee1.average_price()}")
   ```

5. **Managing Orders for Customers:**
   Customers can create new orders using the create_order method, which takes a Coffee instance and a price. This method creates an Order object and adds it to the list of orders.

   ```python
    coffee2 = Coffee("Cappuccino")
    order6 = customer1.create_order(coffee2, 3.0)
   ```

6. **Viewing Customer Orders and Coffee Types:**
   You can also view all orders placed by a customer and the unique coffee types they have ordered:

   - `customer1.orders()`: Retrieves a list of all orders placed by the customer.
   - `customer1.coffee()`: Retrieves a set of unique coffee types ordered by the customer.

   ```python
   print(f"Subira made {len(customer1.orders())} orders")
   print(f"Subira ordered {len(customer1.coffee())} unique coffees")
   ```

## Conclusion

This coffee ordering system provides a structured approach to manage coffee orders, track customer activity, and analyze order data. The object-oriented design ensures clear responsibilities and easy interaction between different components.
