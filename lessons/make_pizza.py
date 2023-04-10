"""Practice implementing Pizza Class."""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("Large", 2, True)
Pauls_pizza: Pizza  = Pizza("small", 13, False)
print(my_pizza.size)
def price(pizza_order: Pizza) -> float:
    """Calculate and return cost of pizza."""
    if pizza_order.size == "Large":
        price = 6.0
