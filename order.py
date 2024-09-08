from customer import Customer
from coffee import Coffee

class Order:
    # List of all Order instances
    all_orders = []

    # Initialization of Order class
    def __init__(self, customer, coffee, price) -> None:
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all_orders.append(self)

    # Customer Property
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Customer must be of type Customer")
        
    #Coffee property
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Coffee must be of type Coffee")

    # Price Property
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        # Checking whether the order has been instantiated
        if hasattr(self, '_price'):
            raise ValueError("The order already exists")

        # Checking whether the order price is a float and ranges between 1.0 to 10.0
        if isinstance(value, float) and 1 <= value <= 10:
            self._price = value
        else:
            raise ValueError("The order price either not a float or not within range")