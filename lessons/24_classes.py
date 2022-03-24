"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""
    # Attribute definitions:
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        "Constructor definition for initializtation of attributes."
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float: 
        """Calculate price of pizza."""
        total: float = 0.0
        if self.size == "Large":
            total += 10.0
        else:
            total += 8.0
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total


a_pizza: Pizza = Pizza("Large", 3)

another_pizza: Pizza = Pizza("Small", 0)
another_pizza.extra_cheese = True

print(f"Price: ${a_pizza.price(1.05)}")
print(f"Price: ${another_pizza.price(1.05)}")