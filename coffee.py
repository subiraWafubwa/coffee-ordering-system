class Coffee:
    # Initialization of Coffee class
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Checking whether the name has already been set
        if hasattr(self, '_name'):
            raise ValueError("This coffee name already exists")

        # Checking whether the coffee name is a string and has more than 3 letters
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("The coffee name is either not a string or not within range")
        
    # Function to return all orders
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]
    
    # Function to return all unique customers
    def customers(self):
        unique_customers = {order.customer for order in self.orders()}
        return set(unique_customers)
    
    # Function that returns the number of times a coffee has been ordered
    def num_orders(self):
        return len(self.orders())
    
    # Function to calculate the average price based on existing coffee
    def average_price(self):
        all_orders = self.orders()

        if not all_orders:
            return 0
        
        total_price = sum(order.price for order in all_orders)
        return total_price/ len(all_orders)
