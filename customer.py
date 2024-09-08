class Customer:
    # List of all customer instances
    all_customers = []

    # Initialization of Customer class
    def __init__(self, name) -> None:
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) in range(1, 16):
            self._name = value
        else:
            raise ValueError("Invalid customer name")

    # Function for setting the number of orders   
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]
    
    # Function for returning a list of unique ordes for a customer
    def coffee(self):
        from order import Order
        unique_list = [order.coffee for order in Order.all_orders if order.customer == self]
        return set(unique_list)
        
    # Aggregation: Create new order
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)